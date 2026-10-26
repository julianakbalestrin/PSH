# Caderno C3 · Atividade 3.2.2 (Word)

Atividade 3.2.2 – *Implantar e reabilitar sistemas coletivos de abastecimento de água no
meio rural e as soluções de saneamento associadas* (antigo Subcomponente 3.2.b),
preenchida no modelo do Caderno do Componente 3 do MOP (v0.4), conforme o Guia de
Identidade Visual do MOP e as Orientações para elaboração dos cadernos de componente.

```
MOP_PSH-PR_C3_Componente_3_v0.4_Atividade_3.2.2.docx           caderno com a Atividade 3.2.2 preenchida
previa_Atividade_3.2.2.pdf                                     prévia em PDF da atividade, das referências e do glossário
PSH_Controle_Referencias_Normativas_MOP_Atividade_3.2.2.xlsx   normas citadas na atividade e cada citação
modelo/                                                        modelo original do caderno (v0.4)
fonte/                                                         textos, dados, figuras (TikZ) e montador
```

## Ao abrir no Word

Aceite a atualização dos campos (ou selecione tudo e tecle F9). Assim a numeração das
figuras e dos quadros, as referências cruzadas, o sumário e as listas de figuras, quadros
e tabelas ficam corretos. As pendências estão como comentários (autor “IAT – pendências da
Atividade 3.2.2”).

## Padrão aplicado

- Fluxogramas em raias, uma por instituição, com os 8 símbolos do Guia (seção 5): visão
  geral de cada ação no item 4, com entradas no topo, etapas numeradas na raia de quem as
  executa e saídas na base; processos detalhados (adesão, captação, obras, entrega,
  instalação, medição e supervisão) no mesmo padrão.
- Cronogramas como linha do tempo: barras em Azul, marco de cada etapa em losango Azul e
  marco principal em Verde. Interfaces como organograma, com a ação em Azul-escuro.
- Matriz RACI com as letras nas cores fixas (R Azul, A Azul-escuro, C Verde 20%, I cinza
  10%) e exatamente um A por etapa (o montador confere).
- Texto com até 3 frases por parágrafo; remissões aos cadernos transversais pelo código
  (Caderno AQ, Caderno AS); normas citadas por remissão e registradas na planilha.
- Mapa sem os logos das instituições (figuras e mapas não levam logos).

## Regenerar

Precisa de Python 3 com Pillow e openpyxl, LaTeX com TikZ (pacotes `texlive-latex-base`,
`texlive-latex-recommended`, `texlive-latex-extra`, `texlive-pictures` e
`texlive-fonts-recommended`) e Poppler (`pdftoppm`).

```bash
cd fonte
python3 figmanuais.py            # escreve os fluxogramas, diagramas e esquemas (fig/f-*.tex)
python3 gerafig.py gerar         # escreve raias, cronogramas e interfaces das ações (fig/g-*.tex)
python3 gerafig.py compilar      # compila em PNG (png/) e registra os tamanhos
python3 mapa.py ../../figuras/mapa-saneamento-rural.pdf   # mapa sem logos (png/f-mapa.jpg)
python3 monta.py ../modelo/MOP_PSH-PR_C3_Componente_3_v0.4.docx ../MOP_PSH-PR_C3_Componente_3_v0.4_Atividade_3.2.2.docx

# planilha de referências normativas, a partir do modelo PSH_Controle_Referencias_Normativas_MOP.xlsx
cd referencias
python3 preenche.py <modelo>.xlsx ../../PSH_Controle_Referencias_Normativas_MOP_Atividade_3.2.2.xlsx
```

`referencias/ocorrencias.py` localiza nos textos (incluindo quadros, figuras e comentários)
cada citação de norma; `preenche.py` cadastra as normas e as citações na planilha.
