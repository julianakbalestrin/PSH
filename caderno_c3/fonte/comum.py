"""Construtores dos quadros padronizados das ações (matriz, metas, indicadores...)."""
from mop import TAB, FIG
from dados import ACOES

FONTE_PLANILHA = "Fonte: Planilha PSH_CUSTO_Consolidada, versão v2408 (PARANÁ, 2026)."
NOTA_ANOS = "Nota: Ano 1 = 2027 e Ano 7 = 2033."


def c(cod):
    return cod.replace(".", "")


def n(v):
    return f"{v:,}".replace(",", ".")


def matriz(cod, partes, produto_final):
    """partes: lista de (parte, [papéis por etapa], papel no produto final)."""
    ne = len(ACOES[cod]["etapas"])
    cab = ["Parte"] + [f"E{i}" for i in range(1, ne + 1)] + ["Produto final"]
    col = 800
    larg = [2300] + [col] * ne + [9071 - 2300 - col * ne]
    linhas = [[p] + papeis + [prod] for p, papeis, prod in partes]
    for ln in linhas:
        assert len(ln) == ne + 2, (cod, ln)
    return TAB(f"raci-{c(cod)}", "Quadro", f"Matriz de responsabilidades da Ação {cod}",
               cab, linhas, larg, "l" + "c" * (ne + 1),
               "Fonte: IAT (2026).",
               nota=(f"Nota: E1 a E{ne} são as Etapas 1 a {ne} do item 4. R = executa; A = aprova ou valida o "
                     "produto (um por etapa); C = é consultado antes; I = é informado depois. "
                     f"Produto final: {produto_final}."),
               margem=60)


def metas(cod, linhas, nota_extra=""):
    """linhas: lista de (produto, unidade, {ano: valor})."""
    cab = ["Produto", "Unidade"] + [f"Ano {a}" for a in range(1, 8)] + ["Total"]
    larg = [1900, 1150] + [720] * 7 + [981]
    corpo = []
    for prod, un, val in linhas:
        tot = sum(val.values())
        corpo.append([prod, un] + [n(val[a]) if a in val else "–" for a in range(1, 8)] + [n(tot)])
    nota = NOTA_ANOS + (" " + nota_extra if nota_extra else "")
    return TAB(f"metas-{c(cod)}", "Quadro", f"Metas anuais da Ação {cod}", cab, corpo, larg,
               "ll" + "r" * 8, FONTE_PLANILHA, nota=nota, margem=60)


def indicadores(cod, linhas, fonte="Fonte: IAT (2026)."):
    cab = ["Indicador", "Unidade", "Linha de base (2025)", "Meta", "Frequência e fonte dos dados"]
    larg = [2871, 1250, 1000, 1450, 2500]
    return TAB(f"ind-{c(cod)}", "Quadro", f"Indicadores da Ação {cod}", cab, linhas, larg,
               "llrrl", fonte, margem=60)


def aceite(cod, linhas, fonte="Fonte: IAT (2026)."):
    cab = ["Produto", "Critério de aceite", "Evidência de comprovação", "Quem valida"]
    larg = [1950, 3071, 2650, 1400]
    return TAB(f"aceite-{c(cod)}", "Quadro", f"Critérios de aceite e evidências da Ação {cod}",
               cab, linhas, larg, "llll", fonte)


def nas(cod, linhas, nota=None):
    cab = ["NAS", "Como se aplica à ação", "Medidas e instrumentos"]
    larg = [1700, 3371, 4000]
    return TAB(f"nas-{c(cod)}", "Quadro", f"Aplicação das Normas Ambientais e Sociais à Ação {cod}",
               cab, linhas, larg, "lll",
               "Fonte: IAT (2026), com base nos instrumentos do Caderno Ambiental e Social do MOP.",
               nota=nota)


def fig_ipo(cod):
    return FIG(f"ipo-{c(cod)}", f"g-ipo-{c(cod)}",
               f"Entradas, etapas e saídas da Ação {cod}", "Fonte: IAT (2026).",
               alt=f"Fluxograma com as entradas, as etapas, os produtos de cada etapa e as saídas da Ação {cod}.")


def fig_crono(cod, fonte=None):
    return FIG(f"crono-{c(cod)}", f"g-crono-{c(cod)}",
               f"Cronograma das etapas e das entregas da Ação {cod}",
               fonte or "Fonte: IAT (2026), com quantidades da planilha PSH_CUSTO_Consolidada (PARANÁ, 2026).",
               alt=f"Cronograma anual de 2027 a 2033 com as etapas e as quantidades a entregar da Ação {cod}.")


def fig_interf(cod):
    return FIG(f"interf-{c(cod)}", f"g-interf-{c(cod)}",
               f"Interfaces e dependências da Ação {cod}", "Fonte: IAT (2026).",
               alt=f"Diagrama do que a Ação {cod} recebe de outras ações e do que entrega a elas.")
