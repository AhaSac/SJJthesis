# 课程论文

当前题目为《高精度数值模拟及其在泵设计中的应用》。约三千字中文摘要与正文已经写入 `main.tex` 和 `chapters/content.tex`，17篇2017—2024年代表性论文已纳入 `references.bib`，其中3篇以中文发表。原有姓名和学号已经保留，课程名称和教师仍待填写。

建议先读以下文件：

- [综述正文](chapters/content.tex) 与 [编译后的PDF](out/main.pdf)。
- [文献阅读索引](research/文献阅读索引.md)：按阅读顺序说明每篇文献的用途，附原文链接。
- [Origin四套图表方案](origin/README_Origin图表制作指南.md)：图1、4有真实公开数据，图2、3需要补充自己的仿真数据。
- [检索与写作说明](research/检索与写作说明.md)：检索范围、验证边界、字数口径和资料说明。

Origin完成图1、4后，将矢量PDF分别命名为 `fig01_grid.pdf`、`fig04_redesign.pdf` 放入 `figures/`，即可在下次编译时自动插入并生成图注。正文未预填不存在的实验曲线或图像。

本项目已读取工作区 `zjuthesis.tex`、`zjuthesis.cls` 和 `config/format/general/` 中的字体、标题、页面设置，沿用其 CTeX 中文排版方式，改用适合课程论文的 `ctexart` 结构。原模板设置仍保留在上级目录；本项目可以单独编译。

## 字体与格式

| 内容 | 配置 |
| --- | --- |
| 大标题（论文总标题） | 宋体三号，16 bp，居中，不额外加粗 |
| 小标题（各级正文标题、摘要标题、参考文献标题） | 宋体四号，14 bp，左对齐，不额外加粗 |
| 正文、摘要、作者信息、图表说明、参考文献正文 | 宋体小四号，12 bp |
| 西文与数字 | 沿用原模板的 Times New Roman，字号随所在段落 |
| 纸张与页边距 | A4，四边均为 2.5 厘米 |
| 正文段落 | 首行缩进两字，1.5 倍基准行距，段间不额外留空 |
| 页码 | 底部居中，单面连续排版 |
| 编译 | XeLaTeX，由 latexmk 自动管理重复编译及参考文献 |

这里将“大标题”解释为论文总标题，“小标题”解释为正文各级标题。页边距、行距、编号等是尚未指定时采用的初始设置，均集中在 `coursepaper.cls` 中，可后续调整。数学公式使用标准数学字体。

## 在 VS Code 中写作

1. 打开本目录中的 `课程论文.code-workspace`，或用 VS Code 的“打开文件夹”打开整个 `20261020` 目录，使项目自带的编译设置生效。
2. 安装推荐扩展 **LaTeX Workshop**（James Yu）。项目已经配置扩展，但配置文件不会代替扩展安装。
3. 修改 `main.tex` 中的题目、姓名、学号、课程、教师及日期。
4. 在 `chapters/content.tex` 中替换各节占位内容，插图放到 `figures/`。
5. 保存 `.tex` 文件即可自动编译，也可按 `Ctrl+Alt+B`。命令面板执行 **LaTeX Workshop: View LaTeX PDF file** 可打开预览。

生成的 PDF 为 `out/main.pdf`。在上级模板文件夹中直接编辑时，应打开本项目的独立工作区，以应用本目录的 VS Code 设置。

## 参考文献

已经启用 `biblatex`、Biber 和 GB/T 7714—2015 顺序编码格式。正文使用 `\cite{文献标识}`，参考文献中的DOI及原文网址可以点击。新增条目后运行 `python research/verify_references.py` 可检查引用键、未引用条目及DOI字段；原文事实核验仍以出版社/期刊页面和全文为依据。

## 终端编译

在本目录运行：

```powershell
latexmk -xelatex -outdir=out main.tex
```

若终端受 `C.UTF-8` 环境变量影响而出现 Perl locale 提示，可在当前 PowerShell 会话先设置：

```powershell
$env:LC_ALL = 'C'
$env:LANG = 'C'
latexmk -xelatex -outdir=out main.tex
```

项目的 VS Code 编译工具已设置上述环境变量。
