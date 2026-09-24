# PSH-PR · MOP em formato metodológico (LaTeX)

Modelo de estrutura para reescrever as atividades do IAT no Manual Operativo do
Projeto (MOP) do PSH-PR como o capítulo de metodologia de uma dissertação.
O piloto é o **Subcomponente 3.2.b**, item B.3.2.2 do MOP de 17/03/2026:
implantação e reabilitação de sistemas coletivos de abastecimento de água e
esgotamento sanitário no meio rural.

## Compilar

```bash
latexmk -pdf main.tex
```

Pacotes necessários (TeX Live): `abntex2`, `tabularx`, `pdflscape`, `enumitem`,
`tikz`, `pgfgantt`, `todonotes`. No Overleaf, compila direto.

## Organização

```
main.tex                        documento principal (classe abnTeX2)
config/preambulo.tex            pacotes, cores e ambiente "quadro" (ABNT)
config/comandos.tex             \pendencia, \atividade, ficha-síntese, estilos TikZ
capitulos/apresentacao.tex      explicação do modelo e correspondência com o MOP
capitulos/subcomponente-3-2-b/  o capítulo, um arquivo por seção ou atividade
  01-contexto-objetivos.tex     justificativa, objetivos e metas
  02-area-criterios.tex         área de abrangência e critérios de seleção
  03-delineamento.tex           premissas, fluxograma e arranjo institucional
  04-1 ... 04-6                 uma atividade por arquivo (3.2.2.1 a 3.2.2.6)
  05-salvaguardas.tex           riscos e medidas (MGAS, PEPI, PGR, MRF, MQR)
  06-monitoramento.tex          indicadores, metas e fluxo de validação
  07-cronograma.tex             diagrama de Gantt
figuras/                        fluxogramas e cronograma em TikZ
modelos/modelo-atividade.tex    esqueleto em branco para novas atividades
apendices/pendencias.tex        lista automática das pendências
referencias.bib                 referências (ABNT)
```

## Estrutura padrão de cada atividade

1. Objetivo e fundamentação
2. Ficha-síntese (quadro com 12 campos fixos)
3. Procedimentos, organizados em fases
4. Etapas, produtos e evidências (quadro em paisagem)
5. Interfaces

Para outra atividade ou subcomponente, copie `modelos/modelo-atividade.tex`.

## Pendências

As inconsistências encontradas no MOP durante a reestruturação estão marcadas
no texto com `\pendencia{...}` (caixas laranja) e listadas no Apêndice A. Para
gerar a versão final sem elas, troque `\mostrarpendenciastrue` por
`\mostrarpendenciasfalse` em `main.tex`.
