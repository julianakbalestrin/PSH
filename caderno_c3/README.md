# Caderno C3 · Atividade 3.2.2 (Word)

Atividade 3.2.2 – *Implantar e reabilitar sistemas coletivos de abastecimento de água no
meio rural e as soluções de saneamento associadas* (antigo Subcomponente 3.2.b),
preenchida no modelo do Caderno do Componente 3 do MOP (v0.4).

```
MOP_PSH-PR_C3_Componente_3_v0.4_Atividade_3.2.2.docx   caderno com a Atividade 3.2.2 preenchida
previa_Atividade_3.2.2.pdf                            prévia em PDF só da Atividade 3.2.2
modelo/                                               modelo original do caderno (v0.4)
fonte/                                                textos, dados, fluxogramas (TikZ) e montador
```

## Ao abrir no Word

Aceite a atualização dos campos (ou selecione tudo e tecle F9). Assim a numeração das
figuras e dos quadros, as referências cruzadas, o sumário e as listas de figuras, quadros
e tabelas ficam corretos. As pendências estão como comentários (autor “IAT – pendências da
Atividade 3.2.2”).

## Regenerar

```bash
cd fonte
python3 figmanuais.py            # escreve os fluxogramas desenhados à mão (fig/f-*.tex)
python3 gerafig.py gerar         # escreve as figuras padronizadas (fig/g-*.tex)
python3 gerafig.py compilar      # compila em PNG (png/) — precisa de LaTeX com TikZ
pdftoppm -r 180 -jpeg -jpegopt quality=88 -singlefile ../../figuras/mapa-saneamento-rural.pdf png/f-mapa
python3 monta.py ../modelo/MOP_PSH-PR_C3_Componente_3_v0.4.docx ../MOP_PSH-PR_C3_Componente_3_v0.4_Atividade_3.2.2.docx
```

O tamanho do mapa (16 cm de largura) deve constar em `png/tamanhos.json`
(`"f-mapa": [16.0, 11.313]`).
