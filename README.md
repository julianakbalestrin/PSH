# PSH-PR · MOP em formato metodológico (LaTeX)

Modelo de estrutura para reescrever as ações do IAT no Manual Operativo do
Projeto (MOP) do PSH-PR como o capítulo de metodologia de uma dissertação:
texto corrido, na ordem em que a implementação acontece, apoiado por
fluxogramas. O piloto é o **Subcomponente 3.2.b**, item B.3.2.2 do MOP de
17/03/2026: implantação e reabilitação de sistemas coletivos de abastecimento
de água e esgotamento sanitário no meio rural.

## Compilar

```bash
latexmk -pdf main.tex
```

Pacotes necessários (TeX Live): `abntex2`, `tabularx`, `pdflscape`, `enumitem`,
`tikz`, `pgfgantt`, `adjustbox`, `todonotes`. No Overleaf, compila direto.

## Estrutura do capítulo (13 tópicos)

1. Mapa mental
2. Critérios de seleção
3. Mapa das áreas de intervenção
4. Responsabilidades das instituições (roteiro por ação e matriz E/A/V)
5. Visão geral da implementação
6. Modelo de gestão e trabalho técnico-social
7. Implementação do abastecimento de água
8. Implementação do esgotamento sanitário
9. Conexão com outros subcomponentes do MOP
10. Gestão ambiental e social (sem citar as NAS)
11. Controle de qualidade (registro, evidências, sustentabilidade)
12. Matriz de custos
13. Cronograma (anual, com metas físicas)

Apêndice A: pendências. Apêndice B: quadros de etapas do MOP. Anexo A:
cronograma mensal de 2026 e 2027 (POA).

## Mapa

O mapa (`figuras/mapa-3-2-b.pdf`) é gerado por `mapa/gerar_mapa.py` a partir
da malha municipal do IBGE (`mapa/pr_municipios.geojson`) e da planilha
`mapa/municipios_selecionados.csv` (código IBGE, município, frente). Para
atualizar, preencha o CSV e rode:

```bash
pip install matplotlib
python3 mapa/gerar_mapa.py
```

## Organização dos arquivos

```
main.tex                          documento principal (classe abnTeX2)
config/preambulo.tex              pacotes, cores e ambiente "quadro" (ABNT)
config/comandos.tex               \pendencia, \fluxograma, \atividade, estilos TikZ
capitulos/apresentacao.tex        explicação do modelo e correspondência com o MOP
capitulos/subcomponente-3-2-b/    o capítulo, um arquivo por tópico (01 a 13)
figuras/                          fluxogramas e cronogramas em TikZ
modelos/modelo-acao.tex           esqueleto em branco dos 13 tópicos
mapa/                             malha municipal, seleção (CSV) e script do mapa
apendices/                        pendências e quadros de etapas
anexos/cronograma-poa.tex         cronograma 2026–2027 (POA)
referencias.bib                   referências (ABNT)
```

## Tipos de fluxograma

| Tipo | Quando usar | Exemplo |
|---|---|---|
| Sequência | ordem das etapas | `figuras/fluxograma-captacao-projeto.tex` |
| Raias | quem faz o quê, com várias instituições | `figuras/fluxograma-obras.tex` |
| Linha do tempo | fases com prazos e produtos | `figuras/fluxograma-modelo-gestao.tex` |
| Zigue-zague por fases | visão do começo ao fim | `figuras/fluxograma-abastecimento.tex` |

Os fluxogramas são inseridos com `\fluxograma{arquivo}`, que reduz a figura
apenas quando ela é mais larga que o texto.

## Pendências

As inconsistências encontradas no MOP e no POA estão marcadas no texto com
`\pendencia{...}` (caixas laranja) e listadas no Apêndice A. Para gerar a
versão final sem elas, troque `\mostrarpendenciastrue` por
`\mostrarpendenciasfalse` em `main.tex`.
