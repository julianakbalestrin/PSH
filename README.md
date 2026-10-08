# PSH-PR · MOP do Subcomponente 3.2.b (LaTeX)

Modelo de estrutura para as ações do IAT no Manual Operativo do Projeto (MOP)
do PSH-PR. O piloto é o **Subcomponente 3.2.b**: implantação e reabilitação de
sistemas coletivos de abastecimento de água e esgotamento sanitário no meio
rural. Prazos, metas e custos seguem a **planilha de custos do PSH-PR**.

## Arquivos

```
main.tex                     documento completo: preâmbulo, texto, figuras,
                             apêndices e referências (gravadas em
                             referencias.bib durante a compilação)
figuras/mapa-saneamento-rural.pdf  mapa do item 1.3 (único arquivo externo)
modelos/modelo-acao.tex      esqueleto em branco dos 13 tópicos, para outras ações
```

## Compilar

```bash
latexmk -pdf main.tex
```

No Overleaf: envie `main.tex` e a pasta `figuras/` (ou o .zip do projeto),
com compilador pdfLaTeX.

## Estrutura (13 tópicos)

1.1 Mapa mental · 1.2 Critérios de seleção · 1.3 Mapa · 1.4 Responsabilidades
das instituições · 1.5 Visão geral da implementação · 1.6 Modelo de gestão
(1.6.1 Trabalho técnico-social) · 1.7 Abastecimento de água · 1.8 Esgotamento
sanitário · 1.9 Conexão com outros subcomponentes · 1.10 Gestão ambiental e
social · 1.11 Controle de qualidade · 1.12 Matriz de custos · 1.13 Cronograma.

Cada figura e quadro fica dentro do item que o cita: há um `\FloatBarrier`
antes de cada seção e subseção.

## Mapa

O item 1.3 usa o mapa inicial elaborado pelo IAT e pelo IDR-Paraná (11/11/2025):
áreas prioritárias, associações de municípios, CISPAR e concentração de
domicílios rurais. Para trocá-lo, substitua `figuras/mapa-saneamento-rural.pdf`.

## Pendências

As inconsistências do MOP aparecem em caixas laranja e no Apêndice A. Para a
versão final, troque `\mostrarpendenciastrue` por `\mostrarpendenciasfalse`
no início de `main.tex`.
