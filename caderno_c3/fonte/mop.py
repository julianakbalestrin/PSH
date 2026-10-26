"""Biblioteca para montar a Atividade 3.2.2 no modelo Word do Caderno C3.

Elementos de conteúdo (listas de tuplas) e geração de WordprocessingML com os
estilos do modelo: Heading2, TituloAcao, ItemAcao, EtapaAcao, Legenda, Fonte,
TextoQuadro, CabQuadro e Normal.

Marcação nos textos:
  **negrito**   *itálico*   {fig:chave} {qua:chave} {tab:chave} (referência cruzada)
"""
import json
import os
import re
from xml.sax.saxutils import escape

AQUI = os.path.dirname(os.path.abspath(__file__))
PNG = os.path.join(AQUI, "png")
_ARQ_TAM = os.path.join(PNG, "tamanhos.json")   # gerado por gerafig.py compilar
TAMANHOS = json.load(open(_ARQ_TAM)) if os.path.exists(_ARQ_TAM) else {}

LARG_TEXTO = 9071          # largura útil em twips (16,0 cm)
EMU_CM = 360000
NUM_BULLET = 2             # numId criado em numbering.xml (abstractNum 2, "•")


# ------------------------------------------------------------------ construtores
def H2(t): return ("H2", t)
def ACAO(t): return ("ACAO", t)
def ITEM(t): return ("ITEM", t)
def ETAPA(t): return ("ETAPA", t)
def P(t): return ("P", t)
def PL(rotulo, t): return ("P", f"**{rotulo}** {t}")
def BUL(*itens): return ("BUL", list(itens))
def COM(t): return ("COM", t)
def FIG(chave, arquivo, titulo, fonte, alt=None, largura=None):
    return ("FIG", dict(chave=chave, arquivo=arquivo, titulo=titulo, fonte=fonte,
                        alt=alt or titulo, largura=largura))
def TAB(chave, tipo, titulo, cab, linhas, larguras, alinh, fonte, nota=None,
        negrito_ultima=False, fonte_cab=None, margem=100):
    """tipo: 'Quadro' ou 'Tabela'. larguras em twips (somam 9071).
    alinh: string com 'l', 'c' ou 'r' por coluna."""
    assert abs(sum(larguras) - LARG_TEXTO) <= 2, (chave, sum(larguras))
    assert len(cab) == len(larguras) == len(alinh), chave
    for ln in linhas:
        assert len(ln) == len(cab), (chave, ln)
    return ("TAB", dict(chave=chave, tipo=tipo, titulo=titulo, cab=cab, linhas=linhas,
                        larguras=larguras, alinh=alinh, fonte=fonte, nota=nota,
                        negrito_ultima=negrito_ultima, margem=margem))
def RAW(xml): return ("RAW", xml)


# ------------------------------------------------------------------ utilidades XML
def x(t):
    return escape(t, {'"': "&quot;"})


def run(texto, b=False, i=False, extra_rpr=""):
    if texto == "":
        return ""
    rpr = ""
    if b:
        rpr += "<w:b/><w:bCs/>"
    if i:
        rpr += "<w:i/><w:iCs/>"
    rpr += extra_rpr
    rpr = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
    return f'<w:r>{rpr}<w:t xml:space="preserve">{x(texto)}</w:t></w:r>'


# Letras da matriz RACI com cor fixa (Guia de Identidade Visual, seção 5.3):
# R Azul, A Azul-escuro (texto branco); C Verde 20%, I cinza 10% (texto preto).
CORES_RACI = {"R": ("0A73BA", "FFFFFF"), "A": ("0B3A5A", "FFFFFF"),
              "C": ("CCEADB", "000000"), "I": ("E6E6E6", "000000")}


def selo_raci(letra):
    fundo, cor = CORES_RACI[letra]
    # a borda da mesma cor dá a folga em volta da letra (selo)
    return (f'<w:r><w:rPr><w:b/><w:bCs/><w:color w:val="{cor}"/>'
            f'<w:bdr w:val="single" w:sz="16" w:space="0" w:color="{fundo}"/>'
            f'<w:shd w:val="clear" w:color="auto" w:fill="{fundo}"/></w:rPr>'
            f'<w:t xml:space="preserve">{letra}</w:t></w:r>')


class Montador:
    def __init__(self, autor_coment="IAT – pendências da Atividade 3.2.2"):
        self.bm_id = 7000
        self.docpr_id = 500
        self.rid = 700
        self.coment_id = 0
        self.comentarios = []          # (id, texto)
        self.midias = []               # (rId, origem, destino)
        self.legendas = {}             # chave -> dict(tipo, bm, titulo)
        self.autor = autor_coment
        self.saida = []
        self.ultimo_par = None         # índice em self.saida do último parágrafo que aceita comentário

    # -------------------------------------------------------------- texto com marcação
    def runs(self, texto, base_b=False, base_i=False):
        """Converte marcação em runs; referências viram campos REF e [[R]] vira o selo RACI."""
        partes = re.split(r"(\*\*|\*|\{(?:fig|qua|tab):[\w\-]+\}|\[\[[RACI]\]\])", texto)
        b, i = base_b, base_i
        out = []
        for p in partes:
            if p == "**":
                b = not b
            elif p == "*":
                i = not i
            elif p.startswith("{") and p.endswith("}") and ":" in p:
                chave = p[1:-1].split(":", 1)[1]
                out.append(self.campo_ref(chave, b, i))
            elif p.startswith("[[") and p.endswith("]]"):
                out.append(selo_raci(p[2]))
            else:
                out.append(run(p, b, i))
        return "".join(out)

    def campo_ref(self, chave, b=False, i=False):
        rpr = ("<w:b/><w:bCs/>" if b else "") + ("<w:i/><w:iCs/>" if i else "")
        rpr = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
        return (f'<w:r>{rpr}<w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
                f'<w:r>{rpr}<w:instrText xml:space="preserve"> REF @@BM:{chave}@@ \\h </w:instrText></w:r>'
                f'<w:r>{rpr}<w:fldChar w:fldCharType="separate"/></w:r>'
                f'<w:r>{rpr}<w:t xml:space="preserve">@@REFTXT:{chave}@@</w:t></w:r>'
                f'<w:r>{rpr}<w:fldChar w:fldCharType="end"/></w:r>')

    def par(self, estilo, conteudo_xml, ppr_extra="", comentavel=True):
        ppr = ""
        if estilo and estilo != "Normal":
            ppr += f'<w:pStyle w:val="{estilo}"/>'
        ppr += ppr_extra
        ppr = f"<w:pPr>{ppr}</w:pPr>" if ppr else ""
        self.saida.append(f"<w:p>{ppr}@@CS@@{conteudo_xml}@@CE@@</w:p>")
        if comentavel:
            self.ultimo_par = len(self.saida) - 1

    def comentar(self, texto):
        assert self.ultimo_par is not None, texto
        k = self.coment_id
        self.coment_id += 1
        self.comentarios.append((k, texto))
        p = self.saida[self.ultimo_par]
        # vários comentários no mesmo parágrafo: encadeia
        p = p.replace("@@CS@@", f'@@CS@@<w:commentRangeStart w:id="{k}"/>', 1)
        p = p.replace("@@CE@@", f'<w:commentRangeEnd w:id="{k}"/><w:r><w:commentReference w:id="{k}"/></w:r>@@CE@@', 1)
        self.saida[self.ultimo_par] = p

    # -------------------------------------------------------------- legendas
    def novo_bm(self, chave, tipo, titulo):
        assert chave not in self.legendas, chave
        self.bm_id += 1
        nome = "_Ref32" + str(self.bm_id).zfill(7)
        self.legendas[chave] = dict(tipo=tipo, bm=nome, id=self.bm_id, titulo=titulo)
        return self.legendas[chave]

    def legenda(self, chave, tipo, titulo):
        lg = self.novo_bm(chave, tipo, titulo)
        xml = (f'<w:bookmarkStart w:id="{lg["id"]}" w:name="{lg["bm"]}"/>'
               + run(f"{tipo} ")
               + '<w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
               + f'<w:r><w:instrText xml:space="preserve"> SEQ {tipo} \\* ARABIC </w:instrText></w:r>'
               + '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
               + f'<w:r><w:t>@@SEQ:{chave}@@</w:t></w:r>'
               + '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
               + f'<w:bookmarkEnd w:id="{lg["id"]}"/>'
               + run(f" – {titulo}"))
        self.par("Legenda", xml)

    # -------------------------------------------------------------- figuras
    def figura(self, d):
        nome = d["arquivo"]
        ext = "jpg" if os.path.exists(os.path.join(PNG, nome + ".jpg")) else "png"
        orig = os.path.join(PNG, f"{nome}.{ext}")
        assert os.path.exists(orig), orig
        wcm, hcm = TAMANHOS[nome]
        larg = d.get("largura") or wcm
        larg = min(larg, 16.0)
        alt = larg * hcm / wcm
        cx, cy = int(larg * EMU_CM), int(alt * EMU_CM)
        self.rid += 1
        rid = f"rId{self.rid}"
        destino = f"media/c3_{nome}.{ext}"
        self.midias.append((rid, orig, destino))
        self.docpr_id += 1
        did = self.docpr_id
        self.legenda(d["chave"], "Figura", d["titulo"])
        desenho = (
            f'<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
            f'<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
            f'<wp:docPr id="{did}" name="Figura {did}" descr="{x(d["alt"])}"/>'
            f'<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
            f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
            f'<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:nvPicPr><pic:cNvPr id="{did}" name="c3_{nome}.{ext}" descr="{x(d["alt"])}"/><pic:cNvPicPr/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
            f'</a:graphicData></a:graphic></wp:inline></w:drawing></w:r>')
        self.par("Normal", desenho,
                 '<w:keepNext/><w:spacing w:before="60" w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>',
                 comentavel=False)
        self.par("Fonte", self.runs(d["fonte"]), comentavel=False)

    # -------------------------------------------------------------- tabelas
    def celula(self, texto, larg, alinh, cab=False, fundo="FFFFFF", borda_inf="CCCCCC",
               borda_inf_sz=4, negrito=False, margem=100):
        if cab:
            bord = ('<w:top w:val="none" w:color="FFFFFF" w:sz="0"/><w:left w:val="none" w:color="FFFFFF" w:sz="0"/>'
                    '<w:bottom w:val="single" w:color="CCCCCC" w:sz="4"/><w:right w:val="none" w:color="FFFFFF" w:sz="0"/>')
            fundo = "0B3A5A"
        else:
            bord = (f'<w:top w:val="single" w:color="CCCCCC" w:sz="4"/><w:left w:val="none" w:color="FFFFFF" w:sz="0"/>'
                    f'<w:bottom w:val="single" w:color="{borda_inf}" w:sz="{borda_inf_sz}"/><w:right w:val="none" w:color="FFFFFF" w:sz="0"/>')
        tcpr = (f'<w:tcPr><w:tcW w:type="dxa" w:w="{larg}"/><w:tcBorders>{bord}</w:tcBorders>'
                f'<w:shd w:fill="{fundo}" w:color="auto" w:val="clear"/>'
                f'<w:tcMar><w:top w:type="dxa" w:w="40"/><w:left w:type="dxa" w:w="{margem}"/>'
                f'<w:bottom w:type="dxa" w:w="40"/><w:right w:type="dxa" w:w="{margem}"/></w:tcMar>'
                '<w:vAlign w:val="center"/></w:tcPr>' if cab else
                f'<w:tcPr><w:tcW w:type="dxa" w:w="{larg}"/><w:tcBorders>{bord}</w:tcBorders>'
                f'<w:shd w:fill="{fundo}" w:color="auto" w:val="clear"/>'
                f'<w:tcMar><w:top w:type="dxa" w:w="40"/><w:left w:type="dxa" w:w="{margem}"/>'
                f'<w:bottom w:type="dxa" w:w="40"/><w:right w:type="dxa" w:w="{margem}"/></w:tcMar></w:tcPr>')
        jc = {"l": "left", "c": "center", "r": "right"}[alinh]
        estilo = "CabQuadro" if cab else "TextoQuadro"
        pars = []
        for linha in str(texto).split("\n"):
            bullet = linha.startswith("• ")
            ppr = f'<w:pStyle w:val="{estilo}"/>'
            if bullet:
                ppr += '<w:ind w:left="170" w:hanging="170"/>'
            ppr += f'<w:jc w:val="{jc}"/>'
            pars.append(f"<w:p><w:pPr>{ppr}</w:pPr>{self.runs(linha, base_b=negrito)}</w:p>")
        return f"<w:tc>{tcpr}{''.join(pars)}</w:tc>"

    def tabela(self, d):
        self.legenda(d["chave"], d["tipo"], d["titulo"])
        cap_idx = self.ultimo_par
        larg = d["larguras"]
        al = d["alinh"]
        grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in larg)
        tblpr = ('<w:tblPr><w:tblW w:type="dxa" w:w="9071"/><w:tblBorders>'
                 '<w:top w:val="single" w:color="auto" w:sz="4"/><w:left w:val="single" w:color="auto" w:sz="4"/>'
                 '<w:bottom w:val="single" w:color="auto" w:sz="4"/><w:right w:val="single" w:color="auto" w:sz="4"/>'
                 '<w:insideH w:val="single" w:color="auto" w:sz="4"/><w:insideV w:val="single" w:color="auto" w:sz="4"/>'
                 '</w:tblBorders><w:tblLayout w:type="fixed"/></w:tblPr>')
        linhas = []
        cab_al = "".join("c" if a == "c" or a == "r" else "l" for a in al)
        linhas.append("<w:tr><w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>" +
                      "".join(self.celula(c, larg[k], cab_al[k], cab=True, margem=d["margem"])
                              for k, c in enumerate(d["cab"])) +
                      "</w:tr>")
        n = len(d["linhas"])
        for r, ln in enumerate(d["linhas"]):
            fundo = "FFFFFF" if r % 2 == 0 else "F2F2F2"
            ultima = r == n - 1
            neg = d["negrito_ultima"] and ultima
            bi, bs = ("0B3A5A", 8) if ultima else ("CCCCCC", 4)
            if neg:
                fundo = "E3F1F2"
            linhas.append("<w:tr><w:trPr><w:cantSplit/></w:trPr>" +
                          "".join(self.celula(c, larg[k], al[k], fundo=fundo, borda_inf=bi,
                                              borda_inf_sz=bs, negrito=neg, margem=d["margem"])
                                  for k, c in enumerate(ln)) + "</w:tr>")
        self.saida.append(f"<w:tbl>{tblpr}<w:tblGrid>{grid}</w:tblGrid>{''.join(linhas)}</w:tbl>")
        self.par("Fonte", self.runs(d["fonte"]), '<w:keepNext/>' if d.get("nota") else "", comentavel=False)
        if d.get("nota"):
            self.par("Fonte", self.runs(d["nota"]), '<w:spacing w:before="0" w:after="240"/>', comentavel=False)
        self.ultimo_par = cap_idx

    # -------------------------------------------------------------- elementos
    def processar(self, elementos):
        for el in elementos:
            tipo = el[0]
            if tipo == "H2":
                self.par("Heading2", self.runs(el[1]))
            elif tipo == "ACAO":
                self.par("TituloAcao", self.runs(el[1]))
            elif tipo == "ITEM":
                self.par("ItemAcao", self.runs(el[1]))
            elif tipo == "ETAPA":
                self.par("EtapaAcao", self.runs(el[1]))
            elif tipo == "P":
                self.par("Normal", self.runs(el[1]))
            elif tipo == "BUL":
                for item in el[1]:
                    self.par("ListParagraph", self.runs(item),
                             f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="{NUM_BULLET}"/></w:numPr>'
                             '<w:spacing w:before="0" w:after="60"/>')
            elif tipo == "COM":
                self.comentar(el[1])
            elif tipo == "FIG":
                self.figura(el[1])
            elif tipo == "TAB":
                self.tabela(el[1])
            elif tipo == "RAW":
                self.saida.append(el[1])
            else:
                raise ValueError(tipo)

    def xml(self):
        return "".join(self.saida).replace("@@CS@@", "").replace("@@CE@@", "")

    def comentarios_xml(self, data="2026-10-23T00:00:00Z"):
        out = []
        for k, t in self.comentarios:
            pars = "".join(f'<w:p>{run(linha)}</w:p>' for linha in t.split("\n"))
            out.append(f'<w:comment w:id="{k}" w:author="{x(self.autor)}" w:date="{data}" w:initials="IAT">{pars}</w:comment>')
        return "".join(out)
