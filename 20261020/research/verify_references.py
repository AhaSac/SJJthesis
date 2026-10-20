"""Audit citation keys locally; optionally archive Crossref metadata for DOI checks.

Run from the project folder: python research/verify_references.py [--online]
Crossref coverage is incomplete for some Chinese journals; an API miss does not
invalidate an article verified on its journal website.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import csv
import json
import re
from urllib.request import Request, urlopen
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--online', action='store_true')
args = parser.parse_args()
PROJECT = ROOT / 'sjj22627171'
bib = (PROJECT / 'reference.bib').read_text(encoding='utf-8')
entries = []
for part in re.split(r'(?m)^@\w+\{', bib)[1:]:
    key = part.split(',', 1)[0].strip()
    fields = dict(re.findall(r'(?m)^\s*(\w+)\s*=\s*\{(.*)\}\s*,?\s*$', part))
    # Several scalar fields can share a line in a valid BibTeX entry.
    fields.update(dict(re.findall(r'\b(year|volume|number|pages)\s*=\s*\{([^{}]*)\}', part)))
    entries.append({'key': key, **fields})
text = (PROJECT / 'sjj22627171.tex').read_text(encoding='utf-8')
text = re.sub(r'(?m)^\s*%.*$', '', text)
cited = set(k.strip() for group in re.findall(r'\\cite\w*\{([^}]+)\}', text)
            for k in group.split(','))
keys = [e['key'] for e in entries]
missing = sorted(cited - set(keys))
unused = sorted(set(keys) - cited)
duplicates = sorted(k for k in set(keys) if keys.count(k) > 1)
audit = {'entries': len(entries), 'cited': len(cited), 'missing': missing,
         'unused': unused, 'duplicate_keys': duplicates,
         'missing_doi': [e['key'] for e in entries if not e.get('doi')],
         'years': sorted(set(e.get('year', '') for e in entries))}
(ROOT / 'research' / 'citation_audit.json').write_text(
    json.dumps(audit, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(audit, ensure_ascii=False))
if missing or unused or duplicates or audit['missing_doi']:
    raise SystemExit('Citation integrity check failed; review the keys above.')

if args.online:
    def fetch(entry):
        result = {'key': entry['key'], 'doi': entry['doi'],
                  'local_title': entry.get('title'), 'local_year': entry.get('year')}
        uri = 'https://api.crossref.org/works/' + quote(entry['doi'], safe='/')
        try:
            req = Request(uri, headers={'User-Agent': 'CoursePaperReferenceAudit/1.0'})
            with urlopen(req, timeout=30) as response:
                metadata = json.load(response)['message']
            result.update(status='metadata_received', metadata=metadata)
        except Exception as exc:
            result.update(status='manual_journal_check_required', error=str(exc))
        return result

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, entries))
    (ROOT / 'research' / 'crossref_metadata.json').write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    with (ROOT / 'research' / 'doi_metadata_check.csv').open(
            'w', newline='', encoding='utf-8-sig') as stream:
        writer = csv.writer(stream)
        writer.writerow(['BibKey', 'DOI', 'Status', 'RegisteredTitle',
                         'RegisteredYear', 'RegisteredAuthors', 'OriginalURL'])
        for result in results:
            meta = result.get('metadata', {})
            date = meta.get('published', meta.get('issued', {}))
            years = date.get('date-parts', [['']])
            names = '; '.join(' '.join([a.get('given', ''), a.get('family', '')]).strip()
                              for a in meta.get('author', []))
            writer.writerow([result['key'], result['doi'], result['status'],
                             '; '.join(meta.get('title', [])), years[0][0],
                             names, 'https://doi.org/' + result['doi']])
    print('Metadata received:', sum(r['status'] == 'metadata_received' for r in results),
          '/', len(results))
