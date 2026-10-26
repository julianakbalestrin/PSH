"""Gera png/f-mapa.jpg a partir do mapa A3 em PDF, sem os logos institucionais
(Guia de Identidade Visual do MOP, seção 2.6: figuras e mapas não levam logos).

Uso: python3 mapa.py ../../figuras/mapa-saneamento-rural.pdf
"""
import json
import os
import subprocess
import sys

from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__))
PNG = os.path.join(AQUI, "png")
LOGOS = (2272, 916, 2926, 1075)   # faixa dos logos dentro do quadro da legenda (imagem a 180 dpi)


def main(pdf):
    os.makedirs(PNG, exist_ok=True)
    saida = os.path.join(PNG, "f-mapa")
    subprocess.run(["pdftoppm", "-r", "180", "-jpeg", "-jpegopt", "quality=92", "-singlefile", pdf, saida],
                   check=True)
    im = Image.open(saida + ".jpg").convert("RGB")
    assert im.size == (2977, 2105), im.size
    ImageDraw.Draw(im).rectangle(LOGOS, fill=(255, 255, 255))
    im.save(saida + ".jpg", quality=92, subsampling=0)
    arq = os.path.join(PNG, "tamanhos.json")
    tam = json.load(open(arq)) if os.path.exists(arq) else {}
    tam["f-mapa"] = [16.0, round(16.0 * im.size[1] / im.size[0], 3)]
    json.dump(tam, open(arq, "w"), indent=1)
    print("mapa sem logos:", saida + ".jpg")


if __name__ == "__main__":
    main(sys.argv[1])
