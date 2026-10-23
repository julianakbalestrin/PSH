"""Gera as figuras padronizadas (entradas-processo-saídas, cronogramas e interfaces)
das ações da Atividade 3.2.2 e compila todas as figuras em PNG.

Uso:  python3 gerafig.py gerar      -> escreve fig/g-*.tex
      python3 gerafig.py compilar   -> compila fig/*.tex em build/ e gera png/
"""
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from dados import ACOES, CUSTOS, ano_civil  # noqa: E402

FIG = os.path.join(AQUI, "fig")
BUILD = os.path.join(AQUI, "build")
PNG = os.path.join(AQUI, "png")

CAB = r"""\documentclass[11pt,border=4pt]{standalone}
\input{estilo}
\begin{document}
"""
FIM = r"""
\end{document}
"""


def tex(s):
    s = s.replace("\\", r"\textbackslash{}")
    for a, b in [("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_")]:
        s = s.replace(a, b)
    s = s.replace("≥", r"$\geq$").replace("≤", r"$\leq$")
    return s


def num(v):
    """Inteiro com separador de milhar brasileiro."""
    return f"{v:,}".replace(",", ".")


def dec(v):
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# ---------------------------------------------------------------- entradas, processo e saídas
def ipo(cod, a):
    etapas = a["etapas"]
    linhas = [CAB, r"\begin{tikzpicture}"]
    linhas.append(r"""
  \tikzset{
    item/.style={draw=#1, fill=white, rounded corners=1.5pt, align=left, text width=3.0cm,
      inner sep=3pt, font=\scriptsize, minimum height=0.75cm},
    passo/.style={etapa=4.15cm, minimum height=0.92cm, align=left},
    chip/.style={produto=2.5cm, minimum height=0.72cm}
  }
  \node[cab=3.1cm, fill=cBlue, anchor=north west] (hE) at (0,0) {Entradas};
  \node[cab=7.25cm, fill=cNavy, anchor=north west] (hP) at (3.85,0) {Etapas e produtos de cada etapa};
  \node[cab=3.1cm, fill=cTeal, anchor=north west] (hS) at (12.2,0) {Saídas};
""")
    # etapas
    for i, e in enumerate(etapas, 1):
        pos = r"anchor=north west] (e1) at (3.95,-0.85)" if i == 1 else f"below=0.3cm of e{i-1}] (e{i})"
        linhas.append(rf"  \node[passo, {pos} {{\textbf{{Etapa {i}}}\\ {tex(e['nome'])}}};")
        linhas.append(rf"  \node[chip, anchor=west] (p{i}) at ($(e{i}.east)+(0.32,0)$) {{{tex(e['produto'])}}};")
        linhas.append(rf"  \draw[setaleve, densely dotted] (e{i}.east) -- (p{i}.west);")
        if i > 1:
            linhas.append(rf"  \draw[seta] (e{i-1}.south) -- (e{i}.north);")
    n = len(etapas)
    linhas.append(rf"  \coordinate (fundo) at ($(e{n}.south)+(0,-0.3)$);")
    # entradas
    for i, t in enumerate(a["entradas"], 1):
        pos = r"anchor=north west] (i1) at (0.075,-0.85)" if i == 1 else f"below=0.22cm of i{i-1}] (i{i})"
        linhas.append(rf"  \node[item=cBlue!70, {pos} {{{tex(t)}}};")
    for i, t in enumerate(a["saidas"], 1):
        pos = r"anchor=north west] (o1) at (12.275,-0.85)" if i == 1 else f"below=0.22cm of o{i-1}] (o{i})"
        linhas.append(rf"  \node[item=cTeal!80, {pos} {{{tex(t)}}};")
    linhas.append(r"""
  \begin{scope}[on background layer]
    \fill[cBlueBg] (hE.south west) rectangle (hE.east |- fundo);
    \fill[cGrayBg] (hP.south west) rectangle (hP.east |- fundo);
    \fill[cTealBg] (hS.south west) rectangle (hS.east |- fundo);
  \end{scope}
  \coordinate (meio) at ($(hP.south)!0.5!(hP.south |- fundo)$);
  \draw[-{Triangle[length=2.6mm,width=4.2mm]}, line width=2.2pt, draw=cBlue!70]
    (hE.east |- meio) ++(0.06,0) -- ++(0.44,0);
  \draw[-{Triangle[length=2.6mm,width=4.2mm]}, line width=2.2pt, draw=cTeal]
    (hP.east |- meio) ++(0.06,0) -- ++(0.44,0);
\end{tikzpicture}""")
    linhas.append(FIM)
    return "\n".join(linhas)


# ---------------------------------------------------------------- cronograma (Gantt)
def faixas(anos):
    anos = sorted(anos)
    blocos, ini, ant = [], None, None
    for x in anos:
        if ini is None:
            ini = ant = x
        elif x == ant + 1:
            ant = x
        else:
            blocos.append((ini, ant))
            ini = ant = x
    if ini is not None:
        blocos.append((ini, ant))
    return blocos


def gantt(linhas_etapas, entregas, rotulo_col="Etapa", cor_barra=None, numeros=True,
          total_fmt=num, larg_rot=4.95):
    Lw, Cw, Tw, Rh, Hh = larg_rot, 1.33, 1.2, 0.8, 0.95
    x0 = Lw
    xt = x0 + 7 * Cw
    xf = xt + Tw
    n = len(linhas_etapas)
    m = len(entregas)
    L = [CAB, r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    # cabeçalho
    L.append(rf"  \fill[cNavy] (0,0) rectangle ({xf},{-Hh});")
    L.append(rf"  \node[font=\scriptsize\bfseries, text=white, anchor=west] at (0.1,{-Hh/2}) {{{rotulo_col}}};")
    for a in range(1, 8):
        xc = x0 + (a - 0.5) * Cw
        L.append(rf"  \node[font=\scriptsize\bfseries, text=white, align=center] at ({xc},{-Hh/2}) {{Ano {a}\\ {ano_civil(a)}}};")
    L.append(rf"  \node[font=\scriptsize\bfseries, text=white] at ({xt + Tw/2},{-Hh/2}) {{Total}};")
    # linhas de etapas
    for i, linha in enumerate(linhas_etapas):
        rot, anos, rotulos, cor = linha[:4]
        tot_linha = linha[4] if len(linha) > 4 else None
        y1 = -Hh - i * Rh
        y2 = y1 - Rh
        ym = (y1 + y2) / 2
        if i % 2 == 1:
            L.append(rf"  \fill[cGrayBg] (0,{y1}) rectangle ({xf},{y2});")
        L.append(rf"  \node[anchor=west, align=left, text width={Lw-0.25}cm, font=\scriptsize] at (0.1,{ym}) {{{tex(rot)}}};")
        c = cor or cor_barra or "cTeal"
        for (a, b) in faixas(anos):
            xa = x0 + (a - 1) * Cw + 0.07
            xb = x0 + b * Cw - 0.07
            L.append(rf"  \fill[{c}, rounded corners=1.5pt] ({xa},{ym-0.2}) rectangle ({xb},{ym+0.2});")
        for a, t in (rotulos or {}).items():
            xc = x0 + (a - 0.5) * Cw
            L.append(rf"  \node[font=\tiny\bfseries, text=white] at ({xc},{ym}) {{{tex(t)}}};")
        if tot_linha:
            L.append(rf"  \node[font=\scriptsize] at ({xt + Tw/2},{ym}) {{{tot_linha}}};")
        L.append(rf"  \draw[cGrayLine, line width=0.3pt] (0,{y2}) -- ({xf},{y2});")
    # linhas de entregas
    yb = -Hh - n * Rh
    for j, (rot, valores) in enumerate(entregas):
        y1 = yb - j * Rh
        y2 = y1 - Rh
        ym = (y1 + y2) / 2
        L.append(rf"  \fill[cTealBg] (0,{y1}) rectangle ({xf},{y2});")
        L.append(rf"  \node[anchor=west, align=left, text width={Lw-0.25}cm, font=\scriptsize\bfseries, text=cNavy] at (0.1,{ym}) {{{tex(rot)}}};")
        tot = 0
        for a in range(1, 8):
            v = valores.get(a)
            if v is None:
                continue
            tot += v
            xc = x0 + (a - 0.5) * Cw
            txt = total_fmt(v) if numeros else str(v)
            L.append(rf"  \node[font=\scriptsize\bfseries, text=cNavy] at ({xc},{ym}) {{{txt}}};")
        L.append(rf"  \node[font=\scriptsize\bfseries, text=cNavy] at ({xt + Tw/2},{ym}) {{{total_fmt(tot)}}};")
        L.append(rf"  \draw[cGrayLine, line width=0.3pt] (0,{y2}) -- ({xf},{y2});")
    yfim = yb - m * Rh
    for a in range(0, 8):
        x = x0 + a * Cw
        L.append(rf"  \draw[cGrayLine, line width=0.3pt] ({x},{-Hh}) -- ({x},{yfim});")
    L.append(rf"  \draw[cGrayLine, line width=0.3pt] ({xt},{-Hh}) -- ({xt},{yfim});")
    L.append(rf"  \draw[cNavy, line width=0.9pt] (0,{yfim}) -- ({xf},{yfim});")
    L.append(r"\end{tikzpicture}")
    L.append(FIM)
    return "\n".join(L)


def gantt_acao(cod, a):
    linhas = []
    for i, e in enumerate(a["etapas"], 1):
        linhas.append((f"{i}. {e['nome']}", e["anos"], e.get("rotulos"), None))
    return gantt(linhas, a["entregas"])


def gantt_atividade():
    cores = {"3.2.2.4": "cBlue", "3.2.2.7": "cNavy"}
    linhas = []
    for cod, a in ACOES.items():
        custos = CUSTOS[cod]
        rot = {k: dec(v) for k, v in custos.items()}
        linhas.append((f"{cod} {a['curto']}", list(custos.keys()), rot, cores.get(cod, "cTeal"),
                       dec(sum(custos.values()))))
    tot = {}
    for cod in ACOES:
        for k, v in CUSTOS[cod].items():
            tot[k] = tot.get(k, 0) + v
    return gantt(linhas, [("Total da atividade (R$ milhões)", tot)], rotulo_col="Ação",
                 total_fmt=dec, larg_rot=4.95)


# ---------------------------------------------------------------- interfaces
def interfaces(cod, a):
    L = [CAB, r"\begin{tikzpicture}"]
    L.append(r"""
  \tikzset{
    rec/.style={draw=cBlue!70, fill=cBlueBg, rounded corners=1.5pt, align=left,
      text width=4.9cm, inner sep=3.5pt, font=\scriptsize, minimum height=0.95cm},
    ent/.style={draw=cTeal!80, fill=cTealBg, rounded corners=1.5pt, align=left,
      text width=4.9cm, inner sep=3.5pt, font=\scriptsize, minimum height=0.95cm}
  }
  \node[cab=4.9cm, fill=cBlue, anchor=north west] (hR) at (0,0) {Recebe de};
  \node[cab=4.9cm, fill=cTeal, anchor=north west] (hE) at (10.45,0) {Entrega a};
""")
    for i, (o, t) in enumerate(a["recebe"], 1):
        pos = r"below=0.3cm of hR.south west, anchor=north west] (r1)" if i == 1 else f"below=0.22cm of r{i-1}] (r{i})"
        L.append(rf"  \node[rec, {pos} {{\textbf{{{tex(o)}}}\\ {tex(t)}}};")
    for i, (o, t) in enumerate(a["entrega"], 1):
        pos = r"below=0.3cm of hE.south west, anchor=north west] (s1)" if i == 1 else f"below=0.22cm of s{i-1}] (s{i})"
        L.append(rf"  \node[ent, {pos} {{\textbf{{{tex(o)}}}\\ {tex(t)}}};")
    nr, ns = len(a["recebe"]), len(a["entrega"])
    L.append(rf"""
  \path let \p1=(r1.north), \p2=(r{nr}.south), \p3=(s1.north), \p4=(s{ns}.south) in
    coordinate (cc) at (7.95, {{(max(\y1,\y3)+min(\y2,\y4))/2}});
  \node[marco=3.0cm, minimum height=1.6cm, font=\small\bfseries] (A) at (cc) {{Ação {cod}\\[2pt]
    \normalfont\scriptsize {tex(a['curto'])}}};""")
    for i in range(1, nr + 1):
        L.append(rf"  \draw[seta, draw=cBlue] (r{i}.east) -- (A.west);")
    for i in range(1, ns + 1):
        L.append(rf"  \draw[seta, draw=cTeal] (A.east) -- (s{i}.west);")
    L.append(r"\end{tikzpicture}")
    L.append(FIM)
    return "\n".join(L)


def gerar():
    os.makedirs(FIG, exist_ok=True)
    for cod, a in ACOES.items():
        c = cod.replace(".", "")
        for nome, fun in [("ipo", ipo), ("crono", gantt_acao), ("interf", interfaces)]:
            with open(os.path.join(FIG, f"g-{nome}-{c}.tex"), "w", encoding="utf-8") as f:
                f.write(fun(cod, a))
    with open(os.path.join(FIG, "g-crono-atividade.tex"), "w", encoding="utf-8") as f:
        f.write(gantt_atividade())
    print("figuras geradas")


def compilar(filtro=None):
    os.makedirs(BUILD, exist_ok=True)
    os.makedirs(PNG, exist_ok=True)
    tamanhos = {}
    arq_tam = os.path.join(PNG, "tamanhos.json")
    if os.path.exists(arq_tam):
        tamanhos = json.load(open(arq_tam))
    erros = []
    for f in sorted(os.listdir(FIG)):
        if not f.endswith(".tex") or f in ("estilo.tex", "teste.tex"):
            continue
        if filtro and not re.search(filtro, f):
            continue
        nome = f[:-4]
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                            "-output-directory", BUILD, f], cwd=FIG,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        pdf = os.path.join(BUILD, nome + ".pdf")
        if r.returncode != 0 or not os.path.exists(pdf):
            erros.append(nome)
            log = r.stdout.decode("latin-1")
            m = re.findall(r"^!.*$", log, re.M)
            print("ERRO", nome, m[:3])
            continue
        info = subprocess.run(["pdfinfo", pdf], stdout=subprocess.PIPE).stdout.decode()
        w, h = map(float, re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info).groups())
        wcm, hcm = w / 72 * 2.54, h / 72 * 2.54
        subprocess.run(["pdftoppm", "-png", "-r", "300", "-singlefile", pdf,
                        os.path.join(PNG, nome)], check=True)
        tamanhos[nome] = [round(wcm, 3), round(hcm, 3)]
        aviso = "  <-- LARGO" if wcm > 16.0 else ""
        print(f"{nome}: {wcm:.2f} x {hcm:.2f} cm{aviso}")
    json.dump(tamanhos, open(arq_tam, "w"), indent=1)
    if erros:
        print("com erro:", erros)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "gerar"
    if cmd == "gerar":
        gerar()
    elif cmd == "compilar":
        compilar(sys.argv[2] if len(sys.argv) > 2 else None)
