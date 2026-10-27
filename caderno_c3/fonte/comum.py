"""Construtores dos quadros padronizados das ações (matriz, metas, indicadores...).

As legendas citam a ação pelo nome (campos "de" e "a" de dados.ACOES), sem a numeração.
"""
from mop import TAB, FIG
from dados import ACOES

FONTE_PLANILHA = "Fonte: Planilha PSH_CUSTO_Consolidada, versão v2408 (PARANÁ, 2026)."
NOTA_ANOS = "Nota: Ano 1 = 2027 e Ano 7 = 2033."


def c(cod):
    return cod.replace(".", "")


def n(v):
    return f"{v:,}".replace(",", ".")


def selos(papel):
    """'R, A' -> '[[R]] [[A]]' (letras em selos coloridos); '–' fica como está."""
    letras = [x.strip() for x in papel.split(",")]
    if all(x in "RACI" and len(x) == 1 for x in letras):
        return " ".join(f"[[{x}]]" for x in letras)
    return papel


def matriz(cod, partes, produto_final):
    """partes: lista de (parte, [papéis por etapa], papel no produto final).
    Confere a regra do Guia: exatamente um A por etapa."""
    ne = len(ACOES[cod]["etapas"])
    for k in range(ne):
        n_a = sum("A" in p[1][k] for p in partes)
        assert n_a == 1, (cod, f"E{k + 1}", n_a)
    cab = ["Parte"] + [f"E{i}" for i in range(1, ne + 1)] + ["Produto final"]
    col = 800
    larg = [2300] + [col] * ne + [9071 - 2300 - col * ne]
    linhas = [[p] + [selos(x) for x in papeis] + [selos(prod)] for p, papeis, prod in partes]
    for ln in linhas:
        assert len(ln) == ne + 2, (cod, ln)
    return TAB(f"raci-{c(cod)}", "Quadro", f"Matriz de responsabilidades {ACOES[cod]['de']}",
               cab, linhas, larg, "l" + "c" * (ne + 1),
               "Fonte: IAT (2026).",
               nota=(f"Nota: E1 a E{ne} correspondem às Etapas 1 a {ne} do item 4. [[R]] executa (pode haver mais "
                     "de um); [[A]] aprova ou valida o produto (um por etapa); [[C]] é consultado previamente; [[I]] é "
                     f"informado posteriormente. Produto final: {produto_final}."),
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
    return TAB(f"metas-{c(cod)}", "Quadro", f"Metas anuais {ACOES[cod]['de']}", cab, corpo, larg,
               "ll" + "r" * 8, FONTE_PLANILHA, nota=nota, margem=60)


def indicadores(cod, linhas, fonte="Fonte: IAT (2026)."):
    cab = ["Indicador", "Unidade", "Linha de base (2025)", "Meta", "Frequência e fonte dos dados"]
    larg = [2871, 1250, 1000, 1450, 2500]
    return TAB(f"ind-{c(cod)}", "Quadro", f"Indicadores {ACOES[cod]['de']}", cab, linhas, larg,
               "llrrl", fonte, margem=60)


def aceite(cod, linhas, fonte="Fonte: IAT (2026)."):
    cab = ["Produto", "Critério de aceite", "Evidência de comprovação", "Responsável pela validação"]
    larg = [1950, 3071, 2650, 1400]
    return TAB(f"aceite-{c(cod)}", "Quadro", f"Critérios de aceite e evidências {ACOES[cod]['de']}",
               cab, linhas, larg, "llll", fonte)


def nas(cod, linhas, nota=None):
    cab = ["NAS", "Aplicação à ação", "Medidas e instrumentos"]
    larg = [1700, 3371, 4000]
    return TAB(f"nas-{c(cod)}", "Quadro", f"Aplicação das Normas Ambientais e Sociais {ACOES[cod]['a']}",
               cab, linhas, larg, "lll",
               "Fonte: IAT (2026), com base nos instrumentos do Caderno AS.",
               nota=nota)


def fig_raias(cod):
    de = ACOES[cod]["de"]
    return FIG(f"raias-{c(cod)}", f"g-raias-{c(cod)}",
               f"Fluxograma {de}: entradas, etapas por responsável e saídas", "Fonte: IAT (2026).",
               alt=(f"Fluxograma em raias {de}, com uma raia por instituição, as etapas numeradas na raia do "
                    "executor, as entradas no topo e as saídas na base."))


def fig_crono(cod, fonte=None):
    de = ACOES[cod]["de"]
    return FIG(f"crono-{c(cod)}", f"g-crono-{c(cod)}",
               f"Cronograma das etapas e das entregas {de}",
               fonte or "Fonte: IAT (2026), com quantidades da planilha PSH_CUSTO_Consolidada (PARANÁ, 2026).",
               alt=f"Cronograma anual de 2027 a 2033 com as etapas e as quantidades a entregar {de}.")


def fig_interf(cod):
    de = ACOES[cod]["de"]
    return FIG(f"interf-{c(cod)}", f"g-interf-{c(cod)}",
               f"Interfaces e dependências {de}", "Fonte: IAT (2026).",
               alt=f"Diagrama das interfaces {de}: insumos recebidos de outras partes do Programa e produtos "
                   "entregues a elas.")
