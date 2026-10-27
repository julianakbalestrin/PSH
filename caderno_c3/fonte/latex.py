"""Gera a versão LaTeX (Overleaf) da Atividade 3.2.2 a partir das mesmas fontes do caderno Word.

Uso: python3 latex.py <modelo.docx> <pasta de saída> [<arquivo .zip>]

O modelo .docx fornece a lista de siglas do caderno. A pasta de saída recebe:
  main.tex             preâmbulo abnTeX2, elementos pré-textuais e pós-textuais
  conteudo/*.tex       apresentação da atividade e um arquivo por ação, referências e glossário
  figuras/*.pdf|jpg    figuras em PDF vetorial (compiladas de fig/*.tex) e o mapa em JPG
  figuras/tikz/        fontes TikZ editáveis das figuras (compilam isoladas, com estilo.tex)
Antes, rode gerafig.py compilar e mapa.py (as figuras saem de build/ e png/).
"""
import os
import re
import shutil
import sys
import zipfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from mop import TAMANHOS, LARG_TEXTO  # noqa: E402
import monta  # noqa: E402
import c_atividade, c_3221, c_3222, c_3223, c_3224, c_3225, c_3226, c_3227  # noqa: E402

PARTES = [("atividade", c_atividade), ("acao-3-2-2-1", c_3221), ("acao-3-2-2-2", c_3222),
          ("acao-3-2-2-3", c_3223), ("acao-3-2-2-4", c_3224), ("acao-3-2-2-5", c_3225),
          ("acao-3-2-2-6", c_3226), ("acao-3-2-2-7", c_3227)]
BUILD = os.path.join(AQUI, "build")
PNG = os.path.join(AQUI, "png")
FIGTEX = os.path.join(AQUI, "fig")
TIPO_REF = {"fig": "Figura", "qua": "Quadro", "tab": "Tabela"}


# ------------------------------------------------------------------ texto
def escapa(s):
    s = s.replace("\\", "\\textbackslash{}")
    for a, b in [("&", "\\&"), ("%", "\\%"), ("$", "\\$"), ("#", "\\#"), ("_", "\\_"),
                 ("{", "\\{"), ("}", "\\}"), ("~", "\\textasciitilde{}"), ("^", "\\textasciicircum{}")]:
        s = s.replace(a, b)
    # espaços não separáveis: R$ 6,90 · nº 13.019 · Figura 3
    return s.replace("R\\$ ", "R\\$~").replace("US\\$ ", "US\\$~").replace("nº ", "nº~")


def tex(texto):
    """Converte a marcação dos textos (negrito, itálico, referências, selos RACI, URLs) em LaTeX."""
    partes = re.split(r"(\*\*|\*|\{(?:fig|qua|tab):[\w\-]+\}|\[\[[RACI]\]\]|https?://[^\s]+)", str(texto))
    out, b, i = [], False, False
    for p in partes:
        if p == "**":
            out.append("}" if b else "\\textbf{")
            b = not b
        elif p == "*":
            out.append("}" if i else "\\textit{")
            i = not i
        elif re.fullmatch(r"\{(?:fig|qua|tab):[\w\-]+\}", p):
            tipo, chave = p[1:-1].split(":", 1)
            out.append(f"{TIPO_REF[tipo]}~\\ref{{{chave}}}")
        elif re.fullmatch(r"\[\[[RACI]\]\]", p):
            out.append(f"\\raci{{{p[2]}}}")
        elif p.startswith("http"):
            fim = ""
            while p and p[-1] in ".,;)":
                fim = p[-1] + fim
                p = p[:-1]
            out.append(f"\\url{{{p}}}{escapa(fim)}")
        else:
            out.append(escapa(p))
    assert not b and not i, texto
    return "".join(out)


def sem_prefixo(s, prefixo):
    return s[len(prefixo):].strip() if s.startswith(prefixo) else s


# ------------------------------------------------------------------ elementos
def figura(d):
    nome = d["arquivo"]
    ext = "jpg" if os.path.exists(os.path.join(PNG, nome + ".jpg")) else "pdf"
    larg = min(d.get("largura") or TAMANHOS[nome][0], 16.0)
    return "\n".join([
        "\\begin{figure}[H]",
        "  \\centering",
        f"  \\caption{{{tex(d['titulo'])}}}\\label{{{d['chave']}}}",
        f"  \\includegraphics[width={larg:.2f}cm]{{figuras/{nome}.{ext}}}",
        f"  \\fonteMOP{{{tex(d['fonte'])}}}",
        f"  % Texto alternativo: {d['alt']}",
        "\\end{figure}", ""])


def coluna(alinh, frac):
    cmd = {"l": "\\raggedright", "c": "\\centering", "r": "\\raggedleft"}[alinh]
    return f">{{{cmd}\\arraybackslash}}p{{\\dimexpr {frac:.4f}\\linewidth-2\\tabcolsep\\relax}}"


def quadro(d):
    amb = "quadro" if d["tipo"] == "Quadro" else "table"
    spec = "".join(coluna(a, w / LARG_TEXTO) for a, w in zip(d["alinh"], d["larguras"]))
    cab = []
    for k, c in enumerate(d["cab"]):
        centro = "\\centering\\arraybackslash " if d["alinh"][k] == "r" else ""
        cab.append(f"{centro}\\textcolor{{white}}{{\\textbf{{{tex(c)}}}}}")
    L = [f"\\begin{{{amb}}}[H]",
         f"  \\caption{{{tex(d['titulo'])}}}\\label{{{d['chave']}}}",
         f"  \\footnotesize\\renewcommand{{\\arraystretch}}{{1.25}}\\setlength{{\\tabcolsep}}{{{d['margem'] / 20:g}pt}}",
         f"  \\begin{{tabular}}{{{spec}}}",
         "    \\rowcolor{azulEscuro}" + " & ".join(cab) + " \\\\"]
    n = len(d["linhas"])
    for r, ln in enumerate(d["linhas"]):
        ultima = r == n - 1
        neg = d["negrito_ultima"] and ultima
        cor = "\\rowcolor{petroleo12}" if neg else ("\\rowcolor{cinza5}" if r % 2 == 1 else "")
        cel = [f"\\textbf{{{tex(c)}}}" if neg and c else tex(c) for c in ln]
        regra = ("\\noalign{\\global\\arrayrulewidth=1pt}\\arrayrulecolor{azulEscuro}\\hline"
                 "\\noalign{\\global\\arrayrulewidth=0.4pt}" if ultima else "\\arrayrulecolor{cinza20}\\hline")
        L.append(f"    {cor}" + " & ".join(cel) + f" \\\\ {regra}")
    L.append("  \\end{tabular}")
    L.append(f"  \\fonteMOP{{{tex(d['fonte'])}}}")
    if d.get("nota"):
        L.append(f"  \\notaMOP{{{tex(d['nota'])}}}")
    L.append(f"\\end{{{amb}}}")
    return "\n".join(L) + "\n"


def titulo(cmd, nivel_toc, texto):
    t = tex(texto)
    linhas = ["\\phantomsection", f"\\{cmd}*{{{t}}}"]
    if nivel_toc:
        linhas.insert(1, f"\\addcontentsline{{toc}}{{{nivel_toc}}}{{{t}}}")
    return "\n".join(linhas) + "\n"


def converte(elementos):
    out = []
    for el in elementos:
        tipo, d = el[0], el[1]
        if tipo == "H2":
            out.append(f"\\atividade{{{tex(d)}}}\n")
        elif tipo == "ACAO":
            out.append(f"\\acao{{{tex(d)}}}\n")
        elif tipo == "ITEM":
            out.append(titulo("subsection", "subsection", d))
        elif tipo == "ETAPA":
            out.append(titulo("subsubsection", None, d))
        elif tipo == "P":
            out.append(tex(d) + "\n")
        elif tipo == "BUL":
            out.append("\\begin{itemize}\n" + "".join(f"  \\item {tex(i)}\n" for i in d) + "\\end{itemize}\n")
        elif tipo == "COM":
            out.append(f"\\pendencia{{{tex(d)}}}\n")
        elif tipo == "FIG":
            out.append(figura(d))
        elif tipo == "TAB":
            out.append(quadro(d))
        else:
            raise ValueError(tipo)
    return "\n".join(out)


# ------------------------------------------------------------------ siglas, referências e glossário
def siglas_do_modelo(modelo):
    """Linhas da tabela 'Lista de siglas' do modelo Word (sigla, significado)."""
    with zipfile.ZipFile(modelo) as z:
        doc = z.read("word/document.xml").decode("utf-8")
    j = doc.index(">Lista de siglas</w:t>")
    t0 = doc.index("<w:tbl>", j)
    t1 = doc.index("</w:tbl>", t0)
    res = {}
    for ln in re.findall(r"<w:tr>.*?</w:tr>", doc[t0:t1], re.S)[1:]:
        cel = ["".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", c)) for c in re.findall(r"<w:tc>.*?</w:tc>", ln, re.S)]
        if len(cel) == 2 and cel[0].strip():
            res[cel[0].strip()] = cel[1].strip()
    return res


def lista_siglas(modelo, texto_todo):
    dic = siglas_do_modelo(modelo)
    for s, v in monta.SIGLAS_NOVAS.items():
        dic.setdefault(s, v)
    usadas = {s: v for s, v in dic.items() if re.search(r"(?<![\w-])" + re.escape(s) + r"(?![\w-])", texto_todo)}
    linhas = [f"  \\item[{escapa(s)}] {tex(v)}" for s, v in sorted(usadas.items(), key=lambda kv: kv[0].lower())]
    return "\\begin{siglas}\n" + "\n".join(linhas) + "\n\\end{siglas}\n"


def referencias():
    L = ["\\chapter*{Referências}", "\\addcontentsline{toc}{chapter}{Referências}",
         "\\begin{SingleSpacing}\\raggedright"]
    for r in monta.REFERENCIAS:
        L.append(f"\\noindent {tex(r)}\\par\\medskip")
    L.append("\\end{SingleSpacing}")
    return "\n".join(L) + "\n"


def glossario():
    L = ["\\chapter*{Glossário complementar}", "\\addcontentsline{toc}{chapter}{Glossário complementar}",
         "Os termos abaixo complementam o glossário geral do MOP.", ""]
    for t, d in monta.GLOSSARIO:
        L.append(f"\\noindent\\textbf{{{tex(t)}:}} {tex(d)}\\par\\smallskip")
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ main.tex
PREAMBULO = r"""% =====================================================================
%  MOP PSH-PR -- Caderno do Componente 3
%  Atividade 3.2.2 -- Implantar e reabilitar sistemas coletivos de abastecimento
%  de água no meio rural e as soluções de saneamento associadas
%
%  Versão LaTeX gerada a partir das mesmas fontes do caderno Word
%  (caderno_c3/fonte/latex.py). Compilar com pdfLaTeX (padrão do Overleaf).
%  Figuras: figuras/*.pdf (as fontes TikZ estão em figuras/tikz/).
% =====================================================================
\documentclass[12pt, oneside, a4paper, english, brazil]{abntex2}

% Mostrar (true) ou ocultar (false) as caixas de pendência no PDF.
\newif\ifmostrarpendencias
\mostrarpendenciastrue

% =====================================================================
%  PACOTES
% =====================================================================
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[scaled=0.92]{helvet}          % Arial (Guia de Identidade Visual, seção 2.1)
\renewcommand{\familydefault}{\sfdefault}
\usepackage{microtype}
\usepackage[table]{xcolor}
\usepackage{graphicx}
\usepackage{array}
\usepackage{enumitem}
\usepackage{xurl}                          % quebra URLs longas nas referências
\urlstyle{same}
\setlist{itemsep=2pt, parsep=0pt, topsep=2pt, leftmargin=*}
\setlength{\marginparwidth}{2cm}
\ifmostrarpendencias
  \usepackage[colorinlistoftodos, textsize=footnotesize, figwidth=\linewidth]{todonotes}
\else
  \usepackage[disable]{todonotes}
\fi

% =====================================================================
%  CORES (Guia de Identidade Visual do MOP)
% =====================================================================
\definecolor{azulEscuro}{HTML}{0B3A5A}
\definecolor{azul}{HTML}{0A73BA}
\definecolor{verde}{HTML}{029749}
\definecolor{cinza60}{HTML}{666666}
\definecolor{cinza20}{HTML}{CCCCCC}
\definecolor{cinza10}{HTML}{E6E6E6}
\definecolor{cinza5}{HTML}{F2F2F2}
\definecolor{verde20}{HTML}{CCEADB}
\definecolor{amarelo30}{HTML}{FDF9C8}
\definecolor{petroleo}{HTML}{00747A}      % cor do Caderno C3
\definecolor{petroleo12}{HTML}{E0EEEF}

% =====================================================================
%  CONFIGURAÇÕES
% =====================================================================
\makeatletter
\hypersetup{
  pdftitle={MOP PSH-PR -- Atividade 3.2.2}, pdfauthor={Instituto Água e Terra},
  colorlinks=true, linkcolor=azulEscuro, citecolor=azulEscuro,
  filecolor=azulEscuro, urlcolor=azulEscuro, bookmarksdepth=4
}
\makeatother

% Títulos: os números já fazem parte do texto (Ação 3.2.2.1, 1. Contextualização, 4.1 Etapa 1)
\renewcommand{\ABNTEXchapterfont}{\bfseries\color{petroleo}}
\renewcommand{\ABNTEXchapterfontsize}{\large}
\renewcommand{\ABNTEXsectionfont}{\bfseries\color{petroleo}}
\renewcommand{\ABNTEXsectionfontsize}{\normalsize}
\renewcommand{\ABNTEXsubsectionfont}{\bfseries\color{azulEscuro}}
\renewcommand{\ABNTEXsubsectionfontsize}{\normalsize}
\renewcommand{\ABNTEXsubsubsectionfont}{\bfseries\itshape}
\renewcommand{\ABNTEXsubsubsectionfontsize}{\normalsize}
\settocdepth{subsection}

% Texto: Arial 12, espaçamento 1,5, justificado, parágrafos sem recuo (como no Word)
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\setlength{\emergencystretch}{3em}

% Legendas acima (Arial 10, negrito, à esquerda); fonte e nota abaixo (Arial 10, Cinza 60)
\captionnamefont{\small\bfseries}
\captiontitlefont{\small\bfseries}
\AtBeginDocument{\captionstyle[\raggedright]{\raggedright}}   % depois da configuração do abnTeX2
\newcommand{\fonteMOP}[1]{\par\vspace{2pt}{\SingleSpacing\raggedright\footnotesize\color{cinza60}#1\par}}
\newcommand{\notaMOP}[1]{\par\vspace{1pt}{\SingleSpacing\raggedright\footnotesize\color{cinza60}#1\par}}

% Quadros: conteúdo textual vai em "quadro"; dados, em "tabela"
\newcommand{\quadroname}{Quadro}
\newcommand{\listofquadrosname}{Lista de quadros}
\newfloat[chapter]{quadro}{loq}{\quadroname}
\newlistof{listofquadros}{loq}{\listofquadrosname}
\newlistentry{quadro}{loq}{0}
\counterwithout{quadro}{chapter}
\renewcommand{\cftquadroname}{\quadroname\space}
\renewcommand*{\cftquadroaftersnum}{\hfill--\hfill}
\setfloatlocations{quadro}{htbp}
\counterwithout{figure}{chapter}
\counterwithout{table}{chapter}
% [H] = exatamente aqui. O pacote float precisa vir DEPOIS do \newfloat do quadro
\usepackage{float}

% =====================================================================
%  COMANDOS
% =====================================================================
% \pendencia{texto}: caixa de pendência no texto; todas são listadas ao final
\newcommand{\pendencia}[1]{%
  \todo[inline, color=amarelo30, bordercolor=azulEscuro, caption={#1}]{\textbf{Pendência:} #1}}

% Título da atividade (Título 2 do modelo Word): nova página, à esquerda, na cor do caderno
\newcommand{\atividade}[1]{%
  \clearpage\phantomsection\addcontentsline{toc}{chapter}{#1}%
  \markboth{MOP PSH-PR -- Caderno do Componente 3}{MOP PSH-PR -- Caderno do Componente 3}%
  {\raggedright\large\bfseries\color{petroleo}#1\par}\vspace{8pt}}

% Título da ação: nova página, cor do caderno e fio de 1,5 pt abaixo (Guia, seção 6)
\newcommand{\acao}[1]{%
  \clearpage\phantomsection\addcontentsline{toc}{section}{#1}%
  \section*{#1}\vspace{-0.9\baselineskip}%
  {\color{petroleo}\hrule height 1.5pt}\vspace{0.6\baselineskip}}

% Matriz RACI: letras em selos nas cores fixas do Guia (seção 5.3)
\newcommand{\selo}[3]{{\setlength{\fboxsep}{1.4pt}\colorbox{#1}{\textcolor{#2}{\textbf{#3}}}}}
\newcommand{\raciR}{\selo{azul}{white}{R}}
\newcommand{\raciA}{\selo{azulEscuro}{white}{A}}
\newcommand{\raciC}{\selo{verde20}{black}{C}}
\newcommand{\raciI}{\selo{cinza10}{black}{I}}
\newcommand{\raci}[1]{\csname raci#1\endcsname}

% =====================================================================
%  DADOS DO DOCUMENTO
% =====================================================================
\titulo{Manual Operativo do Programa de Segurança Hídrica do Paraná (PSH-PR)}
\autor{Instituto Água e Terra -- IAT}
\local{Curitiba}
\data{2026}
\instituicao{Governo do Estado do Paraná\par Instituto Água e Terra}
\tipotrabalho{Manual Operativo}
\preambulo{Caderno do Componente 3 -- Atividade 3.2.2: Implantar e reabilitar sistemas
coletivos de abastecimento de água no meio rural e as soluções de saneamento associadas.}

\begin{document}
\selectlanguage{brazil}
\frenchspacing

% =====================================================================
%  ELEMENTOS PRÉ-TEXTUAIS
% =====================================================================
\pretextual
\imprimirfolhaderosto

\pdfbookmark[0]{\listfigurename}{lof}
\listoffigures*
\cleardoublepage

\pdfbookmark[0]{\listofquadrosname}{loq}
\listofquadros*
\cleardoublepage

\pdfbookmark[0]{\listtablename}{lot}
\listoftables*
\cleardoublepage

"""

FINAL = r"""
\pdfbookmark[0]{\contentsname}{toc}
\tableofcontents*
\cleardoublepage

% =====================================================================
%  ELEMENTOS TEXTUAIS
% =====================================================================
\textual

\input{conteudo/atividade}
\input{conteudo/acao-3-2-2-1}
\input{conteudo/acao-3-2-2-2}
\input{conteudo/acao-3-2-2-3}
\input{conteudo/acao-3-2-2-4}
\input{conteudo/acao-3-2-2-5}
\input{conteudo/acao-3-2-2-6}
\input{conteudo/acao-3-2-2-7}

% =====================================================================
%  ELEMENTOS PÓS-TEXTUAIS
% =====================================================================
\postextual
\input{conteudo/referencias}
\input{conteudo/glossario}

\ifmostrarpendencias
  \chapter*{Lista de pendências}
  \addcontentsline{toc}{chapter}{Lista de pendências}
  \makeatletter\@starttoc{tdo}\makeatother
\fi

\end{document}
"""

LEIAME = """Versão LaTeX da Atividade 3.2.2 (MOP PSH-PR, Caderno do Componente 3)

Overleaf: New Project > Upload Project > escolha este .zip. O documento principal é main.tex
e compila com pdfLaTeX (padrão). Para ocultar as caixas de pendência, troque
\\mostrarpendenciastrue por \\mostrarpendenciasfalse no início de main.tex.

conteudo/   apresentação da atividade, um arquivo por ação, referências e glossário
figuras/    figuras em PDF (vetorial) e o mapa em JPG
figuras/tikz/  fontes TikZ das figuras; cada arquivo compila sozinho (usa estilo.tex)

O texto é o mesmo do caderno Word (MOP_PSH-PR_C3_Componente_3_v0.4_Atividade_3.2.2.docx).
Os comentários do Word aparecem aqui como caixas de pendência.
"""


def main(modelo, saida, arq_zip=None):
    os.makedirs(os.path.join(saida, "conteudo"), exist_ok=True)
    os.makedirs(os.path.join(saida, "figuras", "tikz"), exist_ok=True)
    textos = {}
    for nome, mod in PARTES:
        textos[nome] = converte(mod.ELEMENTOS)
    textos["referencias"] = referencias()
    textos["glossario"] = glossario()
    for nome, corpo in textos.items():
        with open(os.path.join(saida, "conteudo", nome + ".tex"), "w", encoding="utf-8") as f:
            f.write(corpo)
    todo = " ".join(textos.values())
    with open(os.path.join(saida, "main.tex"), "w", encoding="utf-8") as f:
        f.write(PREAMBULO + lista_siglas(modelo, todo) + FINAL)
    with open(os.path.join(saida, "LEIAME.txt"), "w", encoding="utf-8") as f:
        f.write(LEIAME)

    # figuras usadas: PDF vetorial (ou o mapa em JPG) e a fonte TikZ
    usadas = sorted(set(re.findall(r"\\includegraphics\[[^]]*\]\{figuras/([\w\-]+)\.(?:pdf|jpg)\}", todo)))
    for nome in usadas:
        jpg = os.path.join(PNG, nome + ".jpg")
        if os.path.exists(jpg):
            shutil.copy(jpg, os.path.join(saida, "figuras", nome + ".jpg"))
            continue
        shutil.copy(os.path.join(BUILD, nome + ".pdf"), os.path.join(saida, "figuras", nome + ".pdf"))
        shutil.copy(os.path.join(FIGTEX, nome + ".tex"), os.path.join(saida, "figuras", "tikz", nome + ".tex"))
    shutil.copy(os.path.join(FIGTEX, "estilo.tex"), os.path.join(saida, "figuras", "tikz", "estilo.tex"))
    print(f"LaTeX: {saida} | {len(PARTES)} partes, {len(usadas)} figuras")

    if arq_zip:
        if os.path.exists(arq_zip):
            os.remove(arq_zip)
        with zipfile.ZipFile(arq_zip, "w", zipfile.ZIP_DEFLATED) as z:
            for raiz, _, arqs in os.walk(saida):
                for a in sorted(arqs):
                    if a.endswith((".aux", ".log", ".out", ".toc", ".lof", ".lot", ".loq", ".tdo", ".pdf")) \
                            and raiz == saida:
                        continue
                    p = os.path.join(raiz, a)
                    z.write(p, os.path.relpath(p, saida))
        print("zip:", arq_zip)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
