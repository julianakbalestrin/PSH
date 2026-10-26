"""Construtor de fluxogramas em raias, no padrão do Guia de Identidade Visual do MOP
(seção 5.2): uma raia por ator, na ordem em que entram no processo; leitura da esquerda
para a direita; os 8 símbolos de fig/estilo.tex.

As figuras de visão geral (item 4 das ações) têm ainda uma faixa de entradas no topo e
uma de saídas na base; cada documento leva o número da etapa que o usa ou o produz.
"""

LARG = 15.8        # largura total da figura (cm), menor que a largura útil de 16 cm
ROT = 2.35         # coluna dos rótulos das raias
PASSO = 2.25       # distância entre colunas
CAIXA = 1.9        # largura das caixas de atividade


def tex(s):
    s = s.replace("\\", r"\textbackslash{}")
    for a, b in [("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_")]:
        s = s.replace(a, b)
    return s


def col(i):
    """Centro da coluna i (1 a 6) do corpo da figura."""
    return round(ROT + 0.15 + CAIXA / 2 + (i - 1) * PASSO, 3)


class Raias:
    def __init__(self, raias, entradas=None, saidas=None, h_banda=1.5):
        """raias: lista de (chave, rótulo, altura em cm).
        entradas/saídas: lista de (texto, [etapas])."""
        self.faixas = []
        y = 0.0
        if entradas:
            self.faixas.append(dict(chave="ENT", rotulo="Entradas", y0=y, y1=y - h_banda, banda=True))
            y -= h_banda
        for chave, rotulo, h in raias:
            self.faixas.append(dict(chave=chave, rotulo=rotulo, y0=y, y1=y - h, banda=False))
            y -= h
        if saidas:
            self.faixas.append(dict(chave="SAI", rotulo="Saídas", y0=y, y1=y - h_banda, banda=True))
            y -= h_banda
        self.base = y
        self.entradas, self.saidas = entradas or [], saidas or []
        self.nos, self.setas = [], []

    # ------------------------------------------------------------------ geometria
    def faixa(self, chave):
        for f in self.faixas:
            if f["chave"] == chave:
                return f
        raise KeyError(chave)

    def y(self, chave, dy=0.0):
        f = self.faixa(chave)
        return round((f["y0"] + f["y1"]) / 2 + dy, 3)

    def topo(self, chave, d=0.0):
        return round(self.faixa(chave)["y0"] - d, 3)

    # ------------------------------------------------------------------ elementos
    def no(self, nome, estilo, raia, x, texto, num=None, dy=0.0):
        self.nos.append(rf"  \node[{estilo}] ({nome}) at ({x},{self.y(raia, dy)}) {{{texto}}};")
        if num is not None:
            self.nos.append(rf"  \etapa{{{nome}}}{{{num}}}")

    def ativ(self, nome, raia, c, texto, num=None, dy=0.0, w=None):
        larg = w or CAIXA
        self.no(nome, f"atividade={larg - 0.18:.2f}cm", raia, col(c) if isinstance(c, int) else c,
                tex(texto), num, dy)

    def seta(self, caminho):
        self.setas.append(rf"  \draw[conector] {caminho};")

    def rot(self, onde, texto, ancora="south west"):
        self.setas.append(rf"  \node[rotulo, anchor={ancora}, align=center] at {onde} {{{texto}}};")

    def bruto(self, s):
        self.setas.append(s)

    # ------------------------------------------------------------------ saída
    def _documentos(self, itens, chave, prefixo):
        if not itens:
            return []
        n = len(itens)
        x0, x1 = ROT + 0.2, LARG - 0.2
        gap = 0.3
        w = min(3.2, (x1 - x0 - gap * (n - 1)) / n)
        tot = n * w + (n - 1) * gap
        ini = x0 + (x1 - x0 - tot) / 2
        yc = self.y(chave, -0.05)
        out = []
        for k, (texto, etapas) in enumerate(itens):
            xc = ini + w / 2 + k * (w + gap)
            nome = f"{prefixo}{k + 1}"
            out.append(rf"  \node[documento={w - 0.2:.2f}cm] ({nome}) at ({xc:.3f},{yc}) {{{tex(texto)}}};")
            for j, e in enumerate(etapas):
                out.append(rf"  \node[numero] at ($({nome}.north west)+({-0.04 + j * 0.44:.2f},0.04)$) {{{e}}};")
        return out

    def tikz(self):
        L = [r"\begin{tikzpicture}[x=1cm, y=1cm]"]
        # fundos e rótulos das faixas (rótulos em cinza 10%, Arial 9 negrito)
        for f in self.faixas:
            L.append(rf"  \fill[cinza10] (0,{f['y0']}) rectangle ({ROT},{f['y1']});")
            if f["banda"]:
                L.append(rf"  \fill[cinza5] ({ROT},{f['y0']}) rectangle ({LARG},{f['y1']});")
            yc = (f["y0"] + f["y1"]) / 2
            L.append(rf"  \node[raiarotulo, text width={ROT - 0.25}cm] at ({ROT / 2},{yc:.3f}) {{{tex(f['rotulo'])}}};")
        # fios: horizontais em Cinza 20, moldura e separação dos rótulos
        for f in self.faixas[1:]:
            L.append(rf"  \draw[cinza20, line width=0.6pt] (0,{f['y0']}) -- ({LARG},{f['y0']});")
        L.append(rf"  \draw[cinza20, line width=0.6pt] (0,0) rectangle ({LARG},{self.base});")
        L.append(rf"  \draw[cinza20, line width=0.6pt] ({ROT},0) -- ({ROT},{self.base});")
        # bandas de entradas e saídas
        L += self._documentos(self.entradas, "ENT", "ent")
        L += self._documentos(self.saidas, "SAI", "sai")
        L += self.nos
        L += self.setas
        L.append(r"\end{tikzpicture}")
        return "\n".join(L)

    def documento_tex(self):
        return ("\\documentclass[border=2pt]{standalone}\n\\input{estilo}\n\\begin{document}\n"
                + self.tikz() + "\n\\end{document}\n")
