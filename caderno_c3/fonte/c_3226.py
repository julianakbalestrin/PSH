from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM, TAB
from comum import matriz, metas, indicadores, aceite, nas, fig_ipo, fig_crono, fig_interf

COD = "3.2.2.6"

MANANCIAIS = [
    ["Rio Marumbi", "Qualitativo", "128", "120", "94"],
    ["Rio Pirapó", "Qualitativo", "2.750", "1.925", "70"],
    ["Ribeirão Floresta", "Qualitativo", "17", "17", "100"],
    ["Rio Palmital", "Qualitativo", "20", "16", "80"],
    ["Ribeirão Paracatu", "Qualitativo", "17", "17", "100"],
    ["Ribeirão Guarazinho", "Qualitativo", "22", "22", "100"],
    ["Rio Água Grande", "Qualitativo", "91", "53", "58"],
    ["Ribeirão Água na Campina", "Qualitativo", "37", "37", "100"],
    ["Ribeirão do Noitimbo", "Quali-quantitativo", "29", "29", "100"],
    ["Total", "", "3.111", "2.236", "72"],
]

ELEMENTOS = [
    ACAO("Ação 3.2.2.6 – Esgotamento sanitário em propriedades de mananciais (área do IDR-Paraná)"),

    ITEM("1. Contextualização"),
    P("A ação instala soluções individuais de esgotamento sanitário em 2.300 domicílios rurais situados em mananciais "
      "de abastecimento público da área prioritária do PSH-PR, em propriedades atendidas pelo IDR-Paraná, entre 2029 e "
      "2033. Além de atender domicílios sem solução, a ação substitui sistemas considerados inadequados para a "
      "disposição do esgoto (IAT, 2026a)."),
    P("O esgoto sem tratamento lançado no solo e nos rios de um manancial chega à água que abastece as cidades, com "
      "matéria orgânica, nutrientes e microrganismos patogênicos. Nos nove mananciais selecionados, 2.236 domicílios "
      "permanentes ocupados têm destinação inadequada do esgoto, segundo os dados do Censo 2022 e do CNEFE "
      "(IAT, 2026a)."),
    P("A ação reduz a carga poluidora nos mananciais e complementa o Subcomponente 3.1, de gestão de riscos nas bacias "
      "de abastecimento público, e o Subcomponente 2.3, em que o IDR-Paraná trabalha as práticas agropecuárias nas "
      "mesmas propriedades. Contribui também para o indicador de pessoas atendidas com, pelo menos, esgotamento "
      "sanitário, com cerca de 6,4 mil pessoas."),
    PL("Inclui:", "a indicação dos domicílios pelo IDR-Paraná; a contratação das soluções e das obras; o projeto "
       "sanitário de cada propriedade; a instalação conforme a ABNT NBR 17076:2024; a verificação técnica; a orientação "
       "do proprietário; e a medição, a comprovação e o pagamento, com validação conjunta do IAT e do IDR-Paraná."),
    PL("Não inclui:", "a elaboração dos Planos Integrados de Propriedade (PIP), feita no Subcomponente 2.3, nem redes "
       "coletoras ou obras dentro das moradias."),
    PL("Valor previsto:", "R$ 18,40 milhões (empréstimo BIRD: R$ 18,40 milhões; contrapartida: R$ 0,00 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    ITEM("2. Área de atuação"),
    P("A área é definida por critérios sucessivos ({fig:selecao-mananciais}): as microbacias prioritárias do PSH-PR; "
      "os mananciais de abastecimento público selecionados por critérios de qualidade e quantidade da água; os "
      "domicílios rurais permanentes ocupados; a falta de destinação adequada do esgoto, segundo o Censo 2022; e a "
      "existência de diagnóstico da microbacia e de adesão da propriedade ao PSH-PR e às ações do IDR-Paraná "
      "(IAT, 2026a)."),
    FIG("selecao-mananciais", "f-selecao-mananciais", "Critérios de seleção dos domicílios em mananciais",
        "Fonte: IAT (2026), com base em IAT (2026a).",
        alt="Funil com os cinco critérios de seleção dos domicílios em mananciais, que resulta em 2.236 domicílios e "
            "na meta de 2.300."),
    P("A aplicação desses critérios resultou em 2.236 domicílios com esgoto inadequado em nove mananciais, dos quais "
      "1.925 no manancial do Rio Pirapó ({tab:mananciais}). Para dimensionar a ação, o número foi arredondado para "
      "2.300 domicílios, margem que absorve as incertezas das bases de dados, as variações cadastrais e as demandas "
      "futuras."),
    TAB("mananciais", "Tabela", "Domicílios com esgoto inadequado nos mananciais da Ação 3.2.2.6",
        ["Manancial", "Critério", "Domicílios permanentes", "Esgoto inadequado", "%"],
        MANANCIAIS, [2900, 1900, 1700, 1700, 871], "llrrr",
        "Fonte: Adaptado de IAT (2026a), com dados do Censo Demográfico 2022 agregados por setor censitário e do CNEFE "
        "(IBGE, 2024).",
        nota="Nota: domicílios particulares permanentes ocupados. Para o dimensionamento, adotaram-se 2.300 domicílios.",
        negrito_ultima=True),
    COM("Na tabela da nota técnica, o Rio Marumbi aparece com 90%, mas 120 de 128 domicílios correspondem a 94%. "
        "Conferir."),
    COM("O Acordo de Empréstimo, item (j)(vii), pede a identificação das áreas rurais da Parte 3.2. Incluir o mapa dos "
        "nove mananciais, com as microbacias e os municípios."),

    ITEM("3. Arranjo institucional e partes interessadas"),
    P("O IAT, por meio da DISAR, contrata a empresa, fiscaliza a instalação e faz o pagamento. O IDR-Paraná indica os "
      "domicílios a partir dos PIP, apoia a mobilização dos proprietários e valida os resultados junto com o IAT. A "
      "empresa contratada elabora o projeto de cada propriedade e executa a instalação; o proprietário autoriza, "
      "acompanha e confirma a execução. A supervisora da Ação 3.2.2.7 apoia a fiscalização, e a UGP acompanha a "
      "execução."),
    BUL("**Coexecutor:** IDR-Paraná, na indicação dos domicílios, na mobilização e na validação;",
        "**Intervenientes:** empresa contratada; supervisora (Ação 3.2.2.7);",
        "**Público envolvido:** proprietários e moradores das propriedades rurais dos mananciais."),
    P("Os beneficiários diretos são os moradores dos 2.300 domicílios, cerca de 6,4 mil pessoas. Os beneficiários "
      "indiretos são as populações abastecidas pelos mananciais, que recebem água bruta de melhor qualidade."),

    ITEM("4. Processo de execução operacional"),
    P("A ação segue o mesmo procedimento de instalação, verificação, medição e pagamento da Ação 3.2.2.5 "
      "({fig:instalacao} e {fig:medicao}). As diferenças estão na origem da demanda, no território e na validação "
      "({qua:diferencas}): os domicílios são indicados pelos PIP do IDR-Paraná, e não pelo trabalho técnico-social; o "
      "território é o dos mananciais de abastecimento público; e a validação é compartilhada entre o IAT e o "
      "IDR-Paraná ({fig:ipo-3226})."),
    TAB("diferencas", "Quadro", "Diferenças entre as ações de esgotamento sanitário",
        ["Aspecto", "Ação 3.2.2.5 – comunidades", "Ação 3.2.2.6 – mananciais"],
        [["Origem da demanda", "Diagnóstico do trabalho técnico-social (Ação 3.2.2.2)",
          "Planos Integrados de Propriedade do IDR-Paraná (Subcomponente 2.3)"],
         ["Território", "Comunidades atendidas com água (Ação 3.2.2.3)", "Nove mananciais da área prioritária do PSH-PR"],
         ["Base do levantamento", "Censo 2022 e CNEFE: 70% dos 5.810 domicílios sem esgotamento adequado",
          "Censo 2022 e CNEFE: 2.236 domicílios, arredondados para 2.300"],
         ["Meta", "4.067 domicílios", "2.300 domicílios"],
         ["Prazo", "2028 a 2033", "2029 a 2033"],
         ["Validação", "IAT", "IAT e IDR-Paraná"]],
        [2200, 3435, 3436], "lll", "Fonte: IAT (2026), com base em IAT (2026a) e PARANÁ (2026)."),
    fig_ipo(COD),

    ETAPA("4.1 Etapa 1: Indicação dos domicílios pelo IDR-Paraná"),
    PL("Atividades:", "o IDR-Paraná indica, a partir dos PIP e do diagnóstico das microbacias, os domicílios sem "
       "destinação adequada do esgoto; o proprietário confirma a adesão e autoriza a intervenção."),
    PL("Entradas:", "PIP (Subcomponente 2.3); diagnóstico das microbacias; critérios do item 2."),
    PL("Responsáveis:", "IDR-Paraná (executa); IAT (aprova a lista); proprietários (consultados)."),
    PL("Produto:", "lista de domicílios por manancial."),
    COM("Confirmar o cronograma dos PIP no Subcomponente 2.3, que condiciona o início das instalações em 2029."),

    ETAPA("4.2 Etapa 2: Contratação das soluções e das obras"),
    PL("Atividades:", "Termo de Referência das soluções descentralizadas e das obras civis; edital; licitação; "
       "contratação. A contratação pode ser feita no mesmo processo da Ação 3.2.2.5, em lotes próprios."),
    PL("Entradas:", "lista de domicílios; especificações conforme a ABNT NBR 17076:2024."),
    PL("Responsáveis:", "IAT (executa e aprova); IDR-Paraná (consultado); UGP e Banco Mundial (consultados, quando "
       "houver revisão prévia)."),
    PL("Produto:", "contrato assinado."),

    ETAPA("4.3 Etapa 3: Projeto sanitário da propriedade"),
    PL("Atividades:", "a empresa elabora o projeto de cada propriedade, considerando o terreno, o número de moradores, "
       "a infiltração do solo e a solução de tratamento adequada, inclusive o manejo do lodo."),
    PL("Entradas:", "contrato; dados do PIP."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova); IDR-Paraná e proprietário (consultados)."),
    PL("Produto:", "projeto aprovado."),

    ETAPA("4.4 Etapa 4: Instalação e verificação técnica"),
    PL("Atividades:", "obras civis e instalação dos dispositivos; verificação do funcionamento, da estanqueidade e da "
       "garantia; correções, quando necessárias, conforme a {fig:instalacao}."),
    PL("Entradas:", "projeto aprovado; autorização do proprietário."),
    PL("Responsáveis:", "empresa contratada (executa); supervisora (acompanha); IAT (aprova)."),
    PL("Produto:", "sistema verificado e validado."),

    ETAPA("4.5 Etapa 5: Orientação do proprietário"),
    PL("Atividades:", "orientação sobre o funcionamento, o uso adequado, a manutenção preventiva e a limpeza periódica, "
       "durante a instalação, com apoio dos técnicos do IDR-Paraná que atendem a propriedade."),
    PL("Entradas:", "sistema em instalação; material de orientação."),
    PL("Responsáveis:", "empresa contratada (executa); IDR-Paraná (consultado); IAT (aprova o material)."),
    PL("Produto:", "proprietário orientado."),

    ETAPA("4.6 Etapa 6: Medição, comprovação e pagamento"),
    PL("Atividades:", "relatórios de medição e evidências; assinatura do proprietário; auditoria documental e "
       "verificação *in loco*; relatório de medição final; amostragem *in loco*; ordenação das despesas e pagamento, "
       "conforme a {fig:medicao}. A validação técnica é feita em conjunto pelo IAT e pelo IDR-Paraná."),
    PL("Entradas:", "sistemas validados; assinaturas dos proprietários."),
    PL("Responsáveis:", "empresa contratada (executa); IDR-Paraná (valida em conjunto); IAT (aprova e paga)."),
    PL("Produto:", "relatório técnico aprovado pelo IAT e pelo IDR-Paraná e comprovante de pagamento, por lote."),

    ETAPA("4.7 Etapa 7: Finalização"),
    PL("Atividades:", "encerramento de cada lote e do contrato; registro das propriedades atendidas, para a assistência "
       "técnica do IDR-Paraná."),
    PL("Entradas:", "relatórios aprovados e pagamentos realizados."),
    PL("Responsáveis:", "IAT (executa); UGP (valida)."),
    PL("Produto:", "lote encerrado."),

    ETAPA("4.8 Modalidade de execução"),
    P("O item de custo é o sistema individual de tratamento de efluentes: 2.300 domicílios a R$ 8.000,00, total de "
      "R$ 18,40 milhões, financiados pelo empréstimo do BIRD. A execução é por licitação de obras, com o projeto e a "
      "instalação no mesmo contrato, conforme o Caderno de Aquisições. O agrupamento com a Ação 3.2.2.5 em um mesmo "
      "processo, em lotes distintos, será definido no Plano de Aquisições."),

    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3226} indica o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("IAT", ["A", "R, A", "A", "A", "A", "A", "R"], "A"),
        ("IDR-Paraná", ["R", "C", "C", "I", "C", "R", "I"], "R"),
        ("Empresa contratada", ["–", "–", "R", "R", "R", "R", "I"], "R"),
        ("Supervisora (Ação 3.2.2.7)", ["–", "–", "–", "R", "–", "C", "–"], "–"),
        ("Proprietários", ["C", "–", "C", "I", "R", "R", "I"], "I"),
        ("UGP", ["I", "C", "I", "I", "I", "I", "A"], "I"),
        ("Banco Mundial", ["–", "C", "–", "–", "–", "–", "–"], "–"),
    ], "domicílios dos mananciais com solução individual instalada e aprovada"),

    ITEM("6. Metas, indicadores e comprovação"),
    P("A meta é de 460 domicílios por ano, de 2029 a 2033 ({qua:metas-3226})."),
    metas(COD, [("Sistema individual de tratamento de efluentes", "domicílios", {3: 460, 4: 460, 5: 460, 6: 460, 7: 460})]),
    P("Os indicadores estão no {qua:ind-3226}; o de pessoas atendidas é calculado como na Ação 3.2.2.5."),
    indicadores(COD, [
        ["Domicílios de mananciais com solução individual instalada e aprovada", "domicílios", "0", "2.300", "Por lote; IAT e IDR-Paraná"],
        ["Pessoas atendidas com, pelo menos, esgotamento sanitário (parcela do indicador do Componente 3)",
         "pessoas", "0", "6.440", "Anual; IAT, com desagregação por sexo e jovens"],
        ["Mananciais com instalações concluídas", "mananciais", "0", "9", "Anual; IAT"],
    ]),
    P("Os critérios de aceite são os mesmos da Ação 3.2.2.5, com validação conjunta do IAT e do IDR-Paraná "
      "({qua:aceite-3226})."),
    aceite(COD, [
        ["Lista de domicílios", "Domicílios dos mananciais sem destinação adequada, com adesão do proprietário",
         "Lista do IDR-Paraná com os PIP de origem", "IAT"],
        ["Projeto sanitário", "Solução adequada à propriedade, conforme a ABNT NBR 17076:2024", "Projeto aprovado", "IAT"],
        ["Sistema instalado", "Execução conforme o projeto; teste de estanqueidade aprovado",
         "Relatório de medição; laudo de verificação; registro fotográfico", "IAT e IDR-Paraná"],
        ["Execução confirmada", "Proprietário confirma as melhorias", "Assinatura do proprietário", "IAT"],
        ["Lote aprovado", "Auditoria documental, verificação *in loco* e amostragem aprovadas",
         "Relatório técnico aprovado; comprovante de pagamento", "IAT e IDR-Paraná"],
    ]),

    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("Os riscos são os mesmos da Ação 3.2.2.5, com atenção maior à proteção da água, porque as instalações ficam em "
      "mananciais de abastecimento público ({qua:nas-3226})."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Instalação em propriedades de mananciais", "Dimensionamento conforme a "
         "ABNT NBR 17076:2024; distância segura de nascentes e cursos d'água; verificação técnica (MGAS)"],
        ["NAS 2 – Condições de trabalho", "Trabalhadores das empresas contratadas", "Uso de EPI; treinamento de "
         "segurança; Procedimentos de Gestão de Mão de Obra"],
        ["NAS 3 – Eficiência de recursos e prevenção da poluição", "Contaminação do solo e da água do manancial; lodo",
         "Testes de estanqueidade; orientação sobre o lodo; Plano de Gerenciamento de Resíduos Sólidos"],
        ["NAS 4 – Saúde e segurança da comunidade", "Valas abertas nas propriedades", "Sinalização, isolamento e "
         "proteção das valas"],
        ["NAS 10 – Engajamento das partes interessadas", "Proprietários rurais", "Autorização prévia; apoio dos "
         "técnicos do IDR-Paraná; Mecanismo de Queixas e Reclamações (PEPI e MQR)"],
    ], nota="Nota: a NAS 5 não se aplica, porque não há aquisição de terras; a NAS 6 é verificada na triagem das "
            "propriedades em áreas de preservação."),

    ITEM("8. Cronograma"),
    P("O IDR-Paraná indica os domicílios a partir de 2028, a contratação ocorre em 2029 e as instalações seguem de 2029 "
      "a 2033, com 460 domicílios por ano ({fig:crono-3226})."),
    fig_crono(COD),

    ITEM("9. Interfaces e dependências"),
    P("A ação depende dos PIP e do diagnóstico das microbacias elaborados pelo IDR-Paraná no Subcomponente 2.3 e da "
      "supervisão das instalações (Ação 3.2.2.7). Entrega ao Subcomponente 3.1 a redução da carga de esgoto nos "
      "mananciais, à UGP as pessoas atendidas para o indicador do Componente 3 e ao IDR-Paraná o registro das "
      "propriedades atendidas ({fig:interf-3226})."),
    fig_interf(COD),

    ITEM("10. Documentos complementares"),
    BUL("ABNT NBR 17076:2024 (ABNT, 2024);",
        "Planos Integrados de Propriedade do IDR-Paraná (Subcomponente 2.3);",
        "Protocolo de validação conjunta IAT–IDR-Paraná (a elaborar);",
        "Termo de Referência e edital das soluções e das obras (a elaborar);",
        "Caderno de Aquisições e Caderno Ambiental e Social do MOP."),
]
