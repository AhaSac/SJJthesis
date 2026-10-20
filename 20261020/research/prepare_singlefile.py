"""One-time migration to a self-contained course-paper source package."""
from pathlib import Path
import json
import re
import shutil

BASE = Path(__file__).resolve().parents[1]
paper = BASE / 'sjj22627171'
paper.mkdir(exist_ok=True)
target = paper / 'sjj22627171.tex'
if target.exists():
    raise SystemExit('Refusing to overwrite an existing single-file paper.')

style = (BASE / 'coursepaper.cls').read_text(encoding='utf-8')
style = re.sub(r'\A.*?\\LoadClass(\[[^\]]*\])\{ctexart\}',
               lambda m: r'\documentclass' + m.group(1) + '{ctexart}',
               style, count=1, flags=re.S)
style = style.replace(r'\RequirePackage', r'\usepackage')
style = style.replace(r'\addbibresource{references.bib}', r'\addbibresource{reference.bib}')
style = style.replace(r'\graphicspath{{figures/}}', r'\graphicspath{{./}}')

def remove_metadata(text):
    return '\n'.join(line for line in text.splitlines()
                     if not re.match(r'\s*%\s*!TEX\b', line))

main = remove_metadata((BASE / 'main.tex').read_text(encoding='utf-8'))
body = remove_metadata((BASE / 'chapters/content.tex').read_text(encoding='utf-8'))
body = body.replace('% Origin图件放入figures/后由chapters/figures.tex自动插入。', '')
figures = remove_metadata((BASE / 'chapters/figures.tex').read_text(encoding='utf-8'))
figures = figures.replace('figures/', '')
main = main.replace(r'\documentclass{coursepaper}', style)
main = main.replace(r'\input{chapters/content}', body)
main = main.replace(r'\input{chapters/figures}', figures)
header = ('% !TEX root = sjj22627171.tex\n'
          "% 编译：latexmk -norc -xelatex '-outdir=../build/sjj22627171' sjj22627171.tex\n"
          '% 请使用包含Biber的完整编译流程；不要添加仅运行xelatex的program注释。\n'
          '% 字体、格式、摘要和正文均在本文件；文献库为同目录reference.bib。\n')
target.write_text(header + main.lstrip() + '\n', encoding='utf-8')
shutil.copy2(BASE / 'references.bib', paper / 'reference.bib')
for filename in ['fig01_grid.pdf', 'fig04_redesign.pdf']:
    src = BASE / 'figures' / filename
    if src.exists():
        shutil.copy2(src, paper / filename)

# Keep editor settings outside the source-only package.
def editor_settings(output):
    return {
        'files.encoding': 'utf8',
        'editor.wordWrap': 'on',
        'latex-workshop.latex.outDir': output,
        'latex-workshop.latex.autoBuild.run': 'onSave',
        'latex-workshop.latex.recipe.default': 'first',
        'latex-workshop.view.pdf.viewer': 'tab',
        'latex-workshop.latex.recipes': [
            {'name': 'XeLaTeX + Biber (latexmk)', 'tools': ['paper-latexmk']}],
        'latex-workshop.latex.tools': [{
            'name': 'paper-latexmk', 'command': 'latexmk',
            'args': ['-norc', '-cd', '-xelatex', '-synctex=1',
                     '-interaction=nonstopmode', '-file-line-error',
                     '-halt-on-error', '-outdir=%OUTDIR%', '%DOC%'],
            'env': {'LC_ALL': 'C', 'LANG': 'C'}}]
    }

workspace = {'folders': [{'path': 'sjj22627171'}],
             'settings': editor_settings('%DIR%/../build/%DOCFILE%'),
             'extensions': {'recommendations': ['James-Yu.latex-workshop']}}
(BASE / 'sjj22627171.code-workspace').write_text(
    json.dumps(workspace, ensure_ascii=False, indent=4) + '\n', encoding='utf-8')

# Support both the current repository window and a window opened at 20261020.
for root in [BASE, BASE.parent]:
    settings_file = root / '.vscode/settings.json'
    old = json.loads(settings_file.read_text(encoding='utf-8')) if settings_file.exists() else {}
    old.update(editor_settings((BASE / 'build').as_posix() + '/%DOCFILE%'))
    settings_file.parent.mkdir(exist_ok=True)
    settings_file.write_text(json.dumps(old, ensure_ascii=False, indent=4) + '\n', encoding='utf-8')

print('Created:', target)
print('Package files:', ', '.join(p.name for p in paper.iterdir()))
