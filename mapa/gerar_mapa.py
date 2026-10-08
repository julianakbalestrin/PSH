"""Gera o mapa de localização do Subcomponente 3.2.b (figuras/mapa-3-2-b.pdf).

Uso:
    python3 mapa/gerar_mapa.py

Entradas:
    mapa/pr_municipios.geojson        malha municipal do Paraná (IBGE, 399 municípios)
    mapa/municipios_selecionados.csv  municípios selecionados, uma linha por município:
        codigo_ibge,municipio,frente
        4106902,Curitiba,comunidades
    Valores aceitos em "frente":
        comunidades     abastecimento de água + esgotamento nas comunidades (IAT)
        mananciais_idr  esgotamento descentralizado na área do IDR-Paraná
        sanepar_rural   Programa Sanepar Rural
    Um município com mais de uma frente pode aparecer em mais de uma linha;
    no mapa prevalece a primeira frente da lista acima.

Enquanto o CSV estiver vazio, o mapa mostra só a base municipal e a legenda.
Requer: matplotlib.
"""
import csv
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Polygon

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
MALHA = os.path.join(AQUI, "pr_municipios.geojson")
SELECAO = os.path.join(AQUI, "municipios_selecionados.csv")
SAIDA = os.path.join(RAIZ, "figuras", "mapa-3-2-b.pdf")

FRENTES = [  # ordem de prioridade, cor, rótulo
    ("comunidades", "#2E75B6", "Frente comunidades: abastecimento e esgotamento (IAT)"),
    ("mananciais_idr", "#70AD47", "Frente mananciais: esgotamento (IAT e IDR-Paraná)"),
    ("sanepar_rural", "#FFC000", "Programa Sanepar Rural"),
]
COR_BASE = "#F2F2F2"


def ler_selecao():
    frente_por_mun = {}
    if not os.path.exists(SELECAO):
        return frente_por_mun
    prioridade = {f: i for i, (f, _, _) in enumerate(FRENTES)}
    with open(SELECAO, encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            cod = (linha.get("codigo_ibge") or "").strip()
            frente = (linha.get("frente") or "").strip()
            if not cod or frente not in prioridade:
                continue
            atual = frente_por_mun.get(cod)
            if atual is None or prioridade[frente] < prioridade[atual]:
                frente_por_mun[cod] = frente
    return frente_por_mun


def main():
    with open(MALHA, encoding="utf-8") as f:
        malha = json.load(f)
    selecao = ler_selecao()
    cores = {f: c for f, c, _ in FRENTES}

    fig, ax = plt.subplots(figsize=(8.2, 5.6))
    for feat in malha["features"]:
        cod = str(feat["properties"]["id"])
        geom = feat["geometry"]
        aneis = [geom["coordinates"][0]] if geom["type"] == "Polygon" else [p[0] for p in geom["coordinates"]]
        cor = cores.get(selecao.get(cod), COR_BASE)
        for anel in aneis:
            ax.add_patch(Polygon(anel, closed=True, facecolor=cor, edgecolor="#9E9E9E", linewidth=0.25))

    ax.autoscale_view()
    ax.set_aspect(1 / 0.9)  # correção aproximada de aspecto na latitude do Paraná
    ax.set_xlabel("Longitude", fontsize=7)
    ax.set_ylabel("Latitude", fontsize=7)
    ax.tick_params(labelsize=6)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)

    # seta do norte
    ax.annotate("N", xy=(0.95, 0.93), xytext=(0.95, 0.80), xycoords="axes fraction",
                ha="center", fontsize=9, fontweight="bold",
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.2))

    itens = [Patch(facecolor=c, edgecolor="#9E9E9E", label=r) for _, c, r in FRENTES]
    itens.append(Patch(facecolor=COR_BASE, edgecolor="#9E9E9E", label="Demais municípios"))
    ax.legend(handles=itens, loc="lower left", fontsize=6.5, frameon=True, framealpha=0.95)

    if not selecao:
        ax.text(0.5, 0.5, "Seleção dos municípios em andamento\n(POA: mapa previsto para dez/2026)",
                transform=ax.transAxes, ha="center", va="center", fontsize=9,
                color="#7F7F7F", style="italic",
                bbox=dict(boxstyle="round", facecolor="white", edgecolor="#BFBFBF"))

    fig.tight_layout()
    fig.savefig(SAIDA)
    print("Mapa salvo em", SAIDA, "-", len(selecao), "municípios destacados")


if __name__ == "__main__":
    main()
