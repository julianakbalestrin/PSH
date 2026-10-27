# Caderno C3 · Atividade 3.2.2 (Word e LaTeX)

Atividade 3.2.2 – *Implantar e reabilitar sistemas coletivos de abastecimento de água no
meio rural e as soluções de saneamento associadas* (antigo Subcomponente 3.2.b),
preenchida no modelo do Caderno do Componente 3 do MOP (v0.4), conforme o Guia de
Identidade Visual do MOP e as Orientações para elaboração dos cadernos de componente.

```
MOP_PSH-PR_C3_Componente_3_v0.4_Atividade_3.2.2.docx           caderno com a Atividade 3.2.2 preenchida
previa_Atividade_3.2.2.pdf                                     prévia em PDF da atividade, das referências e do glossário
PSH_Controle_Referencias_Normativas_MOP_Atividade_3.2.2.xlsx   normas citadas na atividade e cada citação
Atividade_3.2.2_overleaf.zip                                   versão LaTeX para o Overleaf (mesmo texto do Word)
overleaf/                                                      o mesmo projeto LaTeX, descompactado
modelo/                                                        modelo original do caderno (v0.4)
fonte/                                                         textos, dados, figuras (TikZ) e geradores
```

## Ao abrir no Word

Aceite a atualização dos campos (ou selecione tudo e tecle F9). Assim a numeração das
figuras e dos quadros, as referências cruzadas, o sumário e as listas de figuras, quadros
e tabelas ficam corretos. As pendências estão como comentários (autor “IAT – pendências da
Atividade 3.2.2”). A troca de nome da ação de mananciais (“área da SEAB”) está registrada
com controle de alterações no quadro de atividades e ações do Subcomponente 3.2.

## No Overleaf

New Project › Upload Project › `Atividade_3.2.2_overleaf.zip`. O documento principal é
`main.tex` (classe abnTeX2, compilador pdfLaTeX). As pendências do Word aparecem como caixas
`\pendencia{...}`; para ocultá-las, troque `\mostrarpendenciastrue` por
`\mostrarpendenciasfalse`. As figuras estão em PDF vetorial em `figuras/` e as fontes TikZ,
em `figuras/tikz/`.

## Padrão aplicado

- Redação técnica (Guia, seção 6.1): sujeito explícito, verbo no presente, termos do
  glossário e até 3 frases por parágrafo. As outras ações são citadas pelo nome; a numeração
  aparece só nos títulos e na lista de ações do modelo.
- Fluxogramas em raias, uma por instituição, com os 8 símbolos do Guia (seção 5): visão
  geral de cada ação no item 4, com entradas no topo, etapas numeradas na raia de quem as
  executa e saídas na base; processos detalhados no mesmo padrão.
- Cronogramas como linha do tempo, com marco principal em Verde; interfaces como
  organograma, com a ação em Azul-escuro.
- Matriz RACI com as letras nas cores fixas e exatamente um A por etapa (o montador confere).
- Remissões aos cadernos transversais pelo código (Caderno AQ, Caderno AS); normas citadas
  por remissão e registradas na planilha.
- Mapa sem os logos das instituições (figuras e mapas não levam logos).

## Regenerar

Precisa de Python 3 com Pillow e openpyxl, LaTeX com TikZ (pacotes `texlive-latex-base`,
`texlive-latex-recommended`, `texlive-latex-extra`, `texlive-pictures` e
`texlive-fonts-recommended`; para compilar a versão LaTeX localmente, também
`texlive-publishers` e `texlive-lang-portuguese`) e Poppler (`pdftoppm`).

```bash
cd fonte
python3 figmanuais.py            # escreve os fluxogramas, diagramas e esquemas (fig/f-*.tex)
python3 gerafig.py gerar         # escreve raias, cronogramas e interfaces das ações (fig/g-*.tex)
python3 gerafig.py compilar      # compila em PDF (build/) e PNG (png/) e registra os tamanhos
python3 mapa.py ../../figuras/mapa-saneamento-rural.pdf   # mapa sem logos (png/f-mapa.jpg)
python3 monta.py ../modelo/MOP_PSH-PR_C3_Componente_3_v0.4.docx ../MOP_PSH-PR_C3_Componente_3_v0.4_Atividade_3.2.2.docx
python3 latex.py ../modelo/MOP_PSH-PR_C3_Componente_3_v0.4.docx ../overleaf ../Atividade_3.2.2_overleaf.zip

# planilha de referências normativas, a partir do modelo PSH_Controle_Referencias_Normativas_MOP.xlsx
cd referencias
python3 preenche.py <modelo>.xlsx ../../PSH_Controle_Referencias_Normativas_MOP_Atividade_3.2.2.xlsx
```

`referencias/ocorrencias.py` localiza nos textos (incluindo quadros, figuras e comentários)
cada citação de norma; `preenche.py` cadastra as normas e as citações na planilha.
