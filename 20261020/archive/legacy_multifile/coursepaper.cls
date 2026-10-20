\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{coursepaper}[2026/10/20 Chinese course paper]

% 根据工作区 zjuthesis 的 CTeX 结构改编；课程论文使用 article 结构。
% 所有字体、标题和页面设置集中在本文件。
\LoadClass[UTF8,a4paper,zihao=-4,fontset=none,oneside]{ctexart}

\RequirePackage{iftex}
\RequireXeTeX
\RequirePackage{geometry}
\RequirePackage{amsmath,amssymb}
\RequirePackage{graphicx}
\RequirePackage{booktabs}
\RequirePackage{caption}
\RequirePackage[backend=biber,style=gb7714-2015,sorting=none,doi=true,url=true]{biblatex}
\RequirePackage[hidelinks,unicode]{hyperref}

% 中文统一使用 Windows 宋体，标题不额外加粗。
% 保留原模板的西文 Times New Roman；数学公式使用标准数学字体。
\setmainfont{Times New Roman}
\setsansfont{Times New Roman}
\setCJKmainfont{SimSun}
\setCJKsansfont{SimSun}
\setCJKmonofont{SimSun}
\setCJKfamilyfont{zhsong}{SimSun}
\providecommand{\songti}{\CJKfamily{zhsong}}
\renewcommand{\familydefault}{\rmdefault}

\geometry{a4paper,margin=2.5cm}
\linespread{1.5}
\setlength{\parindent}{2\ccwd}
\setlength{\parskip}{0pt}
\pagestyle{plain}
\setcounter{secnumdepth}{3}
\graphicspath{{figures/}}
\addbibresource{references.bib}

% 大标题：论文总标题宋体三号（16 bp）。
\makeatletter
\renewcommand{\maketitle}{%
  \begingroup
    \centering
    {\normalfont\songti\zihao{3}\@title\par}
    \vspace{0.8\baselineskip}
    {\normalfont\songti\zihao{-4}\@author\par}
    \vspace{0.25\baselineskip}
    {\normalfont\songti\zihao{-4}\@date\par}
    \vspace{0.8\baselineskip}
  \endgroup
}
\makeatother

% 小标题：正文一级、二级、三级标题均为宋体四号（14 bp）。
\ctexset{
  section = {
    format = \normalfont\songti\zihao{4}\raggedright,
    number = \arabic{section},
    aftername = \quad,
    beforeskip = 12bp,
    afterskip = 6bp,
    afterindent = true
  },
  subsection = {
    format = \normalfont\songti\zihao{4}\raggedright,
    number = \arabic{section}.\arabic{subsection},
    aftername = \quad,
    beforeskip = 10bp,
    afterskip = 4bp,
    afterindent = true
  },
  subsubsection = {
    format = \normalfont\songti\zihao{4}\raggedright,
    number = \arabic{section}.\arabic{subsection}.\arabic{subsubsection},
    aftername = \quad,
    beforeskip = 8bp,
    afterskip = 4bp,
    afterindent = true
  }
}

% 摘要、图表说明和参考文献正文也统一为宋体小四号（12 bp）。
\renewenvironment{abstract}
  {\section*{摘要}\normalfont\songti\zihao{-4}}
  {\par}
\DeclareCaptionFont{coursebody}{\normalfont\songti\zihao{-4}}
\captionsetup{font=coursebody,labelfont=normalfont,labelsep=quad}
\renewcommand{\bibfont}{\normalfont\songti\zihao{-4}}
\defbibheading{bibliography}[参考文献]{\section*{#1}}
\AtBeginDocument{\normalfont\songti\zihao{-4}}
