"""Gera as figuras padronizadas da Atividade 3.2.2 (fluxogramas em raias de visão geral,
cronogramas e interfaces) no padrão do Guia de Identidade Visual do MOP e compila todas as
figuras em PNG.

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
from fluxos import FLUXOS  # noqa: E402
from raias import tex  # noqa: E402

FIG = os.path.join(AQUI, "fig")
BUILD = os.path.join(AQUI, "build")
PNG = os.path.join(AQUI, "png")

CAB = "\\documentclass[border=2pt]{standalone}\n\\input{estilo}\n\\begin{document}\n"
FIM = "\n\\end{document}\n"


def num(v):
    """Inteiro com separador de milhar brasileiro."""
    return f"{v:,}".replace(",", ".")


def dec(v):
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


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


def gantt(linhas_etapas, entregas, rotulo_col="Etapa", total_fmt=num, larg_rot=4.95, marcos=True):
    """linhas_etapas: (rótulo, anos, rótulos por ano, total da linha).
    Linha do tempo do Guia: barras em Azul; cada barra termina num marco (losango Azul) e a
    última etapa, no marco principal (losango Verde)."""
    Lw, Cw, Tw, Rh, Hh = larg_rot, 1.33, 1.2, 0.8, 0.95
    x0 = Lw
    xt = x0 + 7 * Cw
    xf = xt + Tw
    n = len(linhas_etapas)
    m = len(entregas)
    L = [CAB, r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    # cabeçalho em Azul-escuro, texto branco
    L.append(rf"  \fill[azulEscuro] (0,0) rectangle ({xf},{-Hh});")
    L.append(rf"  \node[font=\fonte{{8.5}}{{10}}\bfseries, text=white, anchor=west] at (0.1,{-Hh/2}) {{{rotulo_col}}};")
    for a in range(1, 8):
        xc = x0 + (a - 0.5) * Cw
        L.append(rf"  \node[font=\fonte{{8.5}}{{10}}\bfseries, text=white, align=center] at ({xc},{-Hh/2}) {{Ano {a}\\ {ano_civil(a)}}};")
    L.append(rf"  \node[font=\fonte{{8.5}}{{10}}\bfseries, text=white] at ({xt + Tw/2},{-Hh/2}) {{Total}};")
    # etapas: zebrado cinza 5%, barras em Azul, marcos em losango
    for i, linha in enumerate(linhas_etapas):
        rot, anos, rotulos = linha[:3]
        tot_linha = linha[3] if len(linha) > 3 else None
        y1 = -Hh - i * Rh
        y2 = y1 - Rh
        ym = (y1 + y2) / 2
        if i % 2 == 1:
            L.append(rf"  \fill[cinza5] (0,{y1}) rectangle ({xf},{y2});")
        L.append(rf"  \node[anchor=west, align=left, text width={Lw-0.25}cm] at (0.1,{ym}) {{{tex(rot)}}};")
        blocos = faixas(anos)
        for (a, b) in blocos:
            xa = x0 + (a - 1) * Cw + 0.07
            xb = x0 + b * Cw - (0.2 if marcos else 0.07)
            L.append(rf"  \fill[azul, rounded corners=1.5pt] ({xa},{ym-0.17}) rectangle ({xb},{ym+0.17});")
        if marcos and blocos:
            xb = x0 + blocos[-1][1] * Cw - 0.2
            estilo = "marcoprincipal" if i == n - 1 else "marco"
            L.append(rf"  \node[{estilo}] at ({xb},{ym}) {{}};")
        for a, t in (rotulos or {}).items():
            xc = x0 + (a - 0.5) * Cw
            L.append(rf"  \node[font=\fonte{{7}}{{8}}\bfseries, text=white] at ({xc - (0.07 if marcos else 0)},{ym}) {{{tex(t)}}};")
        if tot_linha:
            L.append(rf"  \node at ({xt + Tw/2},{ym}) {{{tot_linha}}};")
        L.append(rf"  \draw[cinza20, line width=0.5pt] (0,{y2}) -- ({xf},{y2});")
    # entregas: fundo Azul 12%, números em preto
    yb = -Hh - n * Rh
    for j, (rot, valores) in enumerate(entregas):
        y1 = yb - j * Rh
        y2 = y1 - Rh
        ym = (y1 + y2) / 2
        L.append(rf"  \fill[azul12] (0,{y1}) rectangle ({xf},{y2});")
        L.append(rf"  \node[anchor=west, align=left, text width={Lw-0.25}cm, font=\fonte{{8}}{{9.4}}\bfseries] at (0.1,{ym}) {{{tex(rot)}}};")
        tot = 0
        for a in range(1, 8):
            v = valores.get(a)
            if v is None:
                continue
            tot += v
            xc = x0 + (a - 0.5) * Cw
            L.append(rf"  \node[font=\fonte{{8}}{{9.4}}\bfseries] at ({xc},{ym}) {{{total_fmt(v)}}};")
        L.append(rf"  \node[font=\fonte{{8}}{{9.4}}\bfseries] at ({xt + Tw/2},{ym}) {{{total_fmt(tot)}}};")
        L.append(rf"  \draw[cinza20, line width=0.5pt] (0,{y2}) -- ({xf},{y2});")
    yfim = yb - m * Rh
    for a in range(0, 8):
        x = x0 + a * Cw
        L.append(rf"  \draw[cinza20, line width=0.5pt] ({x},{-Hh}) -- ({x},{yfim});")
    L.append(rf"  \draw[cinza20, line width=0.5pt] ({xt},{-Hh}) -- ({xt},{yfim});")
    L.append(rf"  \draw[azulEscuro, line width=1pt] (0,{yfim}) -- ({xf},{yfim});")
    if marcos:
        yl = yfim - 0.38
        L.append(rf"  \fill[azul, rounded corners=1.5pt] (0.1,{yl-0.15}) rectangle (0.75,{yl+0.15});")
        L.append(rf"  \node[anchor=west] at (0.82,{yl}) {{período da etapa}};")
        L.append(rf"  \node[marco] at (3.55,{yl}) {{}};")
        L.append(rf"  \node[anchor=west] at (3.75,{yl}) {{marco: produto da etapa entregue}};")
        L.append(rf"  \node[marcoprincipal] at (8.55,{yl}) {{}};")
        L.append(rf"  \node[anchor=west] at (8.75,{yl}) {{marco principal: produto final da ação}};")
    L.append(r"\end{tikzpicture}")
    L.append(FIM)
    return "\n".join(L)


def gantt_acao(cod, a):
    linhas = []
    for i, e in enumerate(a["etapas"], 1):
        linhas.append((f"{i}. {e['nome']}", e["anos"], e.get("rotulos")))
    return gantt(linhas, a["entregas"])


def gantt_atividade():
    linhas = []
    for cod, a in ACOES.items():
        custos = CUSTOS[cod]
        rot = {k: dec(v) for k, v in custos.items()}
        nome = a["curto"] + (" (contrapartida)" if cod == "3.2.2.4" else "")
        linhas.append((f"{cod} {nome}", list(custos.keys()), rot, dec(sum(custos.values()))))
    tot = {}
    for cod in ACOES:
        for k, v in CUSTOS[cod].items():
            tot[k] = tot.get(k, 0) + v
    return gantt(linhas, [("Total da atividade (R$ milhões)", tot)], rotulo_col="Ação",
                 total_fmt=dec, larg_rot=4.95, marcos=False)


# ---------------------------------------------------------------- interfaces
def interfaces(cod, a):
    """Organograma de interfaces: a ação em destaque Azul-escuro; as demais partes em caixas
    brancas com borda Cinza 60; conectores em ângulo reto."""
    wl, wc, gap = 5.1, 2.9, 0.95
    xl, xc, xr = 0, wl + gap, wl + gap + wc + gap
    L = [CAB, r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    L.append(rf"  \node[titulocol={wl}cm, anchor=north west] (hR) at ({xl},0) {{Recebe de}};")
    L.append(rf"  \node[titulocol={wl}cm, anchor=north west] (hE) at ({xr},0) {{Entrega a}};")
    L.append(rf"  \draw[cinza20, line width=0.6pt] ({xl},-0.5) -- ({xl + wl},-0.5);")
    L.append(rf"  \draw[cinza20, line width=0.6pt] ({xr},-0.5) -- ({xr + wl},-0.5);")
    for i, (o, t) in enumerate(a["recebe"], 1):
        pos = rf"anchor=north west] (r1) at ({xl},-0.72)" if i == 1 else f"below=0.25cm of r{i-1}] (r{i})"
        L.append(rf"  \node[caixa={wl - 0.21:.2f}cm, minimum height=0.95cm, {pos} {{\textbf{{{tex(o)}}}\\ {tex(t)}}};")
    for i, (o, t) in enumerate(a["entrega"], 1):
        pos = rf"anchor=north west] (s1) at ({xr},-0.72)" if i == 1 else f"below=0.25cm of s{i-1}] (s{i})"
        L.append(rf"  \node[caixa={wl - 0.21:.2f}cm, minimum height=0.95cm, {pos} {{\textbf{{{tex(o)}}}\\ {tex(t)}}};")
    nr, ns = len(a["recebe"]), len(a["entrega"])
    L.append(rf"""
  \path let \p1=(r1.north), \p2=(r{nr}.south), \p3=(s1.north), \p4=(s{ns}.south) in
    coordinate (cc) at ({xc + wc/2}, {{(max(\y1,\y3)+min(\y2,\y4))/2}});
  \node[destaque={wc - 0.21:.2f}cm, minimum height=1.6cm] (A) at (cc) {{Ação {cod}\\[3pt]
    \fonte{{8}}{{9.4}}\mdseries {tex(a['curto'])}}};""")
    xbl = xl + wl + gap / 2
    xbr = xr - gap / 2
    for i in range(1, nr + 1):
        L.append(rf"  \draw[cinza60, line width=1pt] (r{i}.east) -- ({xbl},0 |- r{i}.east);")
    L.append(rf"  \draw[cinza60, line width=1pt] ({xbl},0 |- r1.east) -- ({xbl},0 |- r{nr}.east);")
    L.append(rf"  \draw[conector] ({xbl},0 |- A.west) -- (A.west);")
    L.append(rf"  \draw[cinza60, line width=1pt] (A.east) -- ({xbr},0 |- A.east);")
    L.append(rf"  \draw[cinza60, line width=1pt] ({xbr},0 |- s1.west) -- ({xbr},0 |- s{ns}.west);")
    for i in range(1, ns + 1):
        L.append(rf"  \draw[conector] ({xbr},0 |- s{i}.west) -- (s{i}.west);")
    L.append(r"\end{tikzpicture}")
    L.append(FIM)
    return "\n".join(L)


def gerar():
    os.makedirs(FIG, exist_ok=True)
    for cod, a in ACOES.items():
        c = cod.replace(".", "")
        with open(os.path.join(FIG, f"g-raias-{c}.tex"), "w", encoding="utf-8") as f:
            f.write(FLUXOS[cod]().documento_tex())
        for nome, fun in [("crono", gantt_acao), ("interf", interfaces)]:
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
        log = open(os.path.join(BUILD, nome + ".log"), encoding="latin-1").read()
        cheios = len(re.findall(r"^Overfull \\hbox", log, re.M))
        info = subprocess.run(["pdfinfo", pdf], stdout=subprocess.PIPE).stdout.decode()
        w, h = map(float, re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info).groups())
        wcm, hcm = w / 72 * 2.54, h / 72 * 2.54
        subprocess.run(["pdftoppm", "-png", "-r", "300", "-singlefile", pdf,
                        os.path.join(PNG, nome)], check=True)
        tamanhos[nome] = [round(wcm, 3), round(hcm, 3)]
        aviso = "  <-- LARGO" if wcm > 16.0 else ""
        aviso += f"  <-- {cheios} overfull" if cheios else ""
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
