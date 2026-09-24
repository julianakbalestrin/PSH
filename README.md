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

## Estrutura do capítulo

1. Contextualização e objetivos
2. Área de abrangência e critérios de seleção
3. Arranjo institucional e visão geral da implementação
4. **Implementação do abastecimento de água, do começo ao fim**: adesão,
   modelo de gestão, trabalho técnico-social, captação e projeto, obras,
   entrega e Programa Sanepar Rural
5. **Implementação do esgotamento sanitário, do começo ao fim**:
   identificação dos domicílios, contratação, instalação e verificação,
   medição e pagamento e frente do IDR-Paraná
6. Salvaguardas ambientais e sociais
7. Monitoramento, avaliação e indicadores
8. Cronograma de execução

Apêndice A: pendências encontradas no MOP. Apêndice B: quadros detalhados
de etapas (Quadros 28 e 29 do MOP). **Anexo A: cronograma mensal de 2026 e
2027**, tirado do POA 2026–2027 (aba "Componente 3", linhas 15 a 29).

## Organização dos arquivos

```
main.tex                          documento principal (classe abnTeX2)
config/preambulo.tex              pacotes, cores e ambiente "quadro" (ABNT)
config/comandos.tex               \pendencia, \fluxograma, \atividade, estilos TikZ
capitulos/apresentacao.tex        explicação do modelo e correspondência com o MOP
capitulos/subcomponente-3-2-b/    o capítulo, um arquivo por seção (01 a 08)
figuras/                          fluxogramas e cronogramas em TikZ
modelos/modelo-secao.tex          esqueleto em branco de uma seção de implementação
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
