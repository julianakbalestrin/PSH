from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM
from comum import matriz, metas, indicadores, aceite, nas, fig_raias, fig_crono, fig_interf

COD = "3.2.2.7"

ELEMENTOS = [
    ACAO("Ação 3.2.2.7 – Supervisão e gerenciamento das obras"),

    ITEM("1. Contextualização"),
    P("A ação contrata empresa de supervisão e gerenciamento para o acompanhamento independente das obras de "
      "abastecimento de água e de esgotamento sanitário da atividade, em apoio à fiscalização do IAT, com registro do "
      "andamento, da qualidade e da conformidade ambiental e social das obras (IAT, 2026a)."),
    P("As obras da atividade são numerosas e dispersas no território estadual: 83 sistemas coletivos de abastecimento "
      "de água e 6.367 instalações domiciliares de esgotamento sanitário. A equipe de fiscalização do IAT não tem "
      "capacidade para acompanhar simultaneamente todas as frentes, e a ausência de acompanhamento contínuo eleva os "
      "riscos de atraso, de não conformidade e de pagamento sem comprovação suficiente."),
    P("A supervisão confere qualidade e rastreabilidade às obras: os relatórios e as medições verificadas pela "
      "supervisora subsidiam os critérios de aceite, os pagamentos e a emissão do Termo de Recebimento Definitivo nas "
      "ações de abastecimento de água e de esgotamento sanitário."),
    PL("Inclui:", "o plano de supervisão; o acompanhamento de campo; o controle de qualidade dos materiais e dos "
       "serviços; a verificação das medições; o controle de prazos e custos; a verificação da conformidade ambiental, "
       "social e de saúde e segurança do trabalho; os relatórios mensais; e o apoio ao recebimento das obras."),
    PL("Não inclui:", "a fiscalização dos contratos, que permanece atribuição do IAT, nem os projetos e as obras."),
    PL("Valor previsto:", "R$ 10,79 milhões (empréstimo BIRD: R$ 10,79 milhões; contrapartida: R$ 0,00 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    ITEM("2. Área de atuação"),
    P("A supervisão abrange todas as frentes de obra da atividade: as 83 comunidades atendidas com abastecimento de "
      "água e esgotamento sanitário ({fig:mapa}) e as propriedades dos nove mananciais selecionados "
      "({tab:mananciais})."),

    ITEM("3. Arranjo institucional e partes interessadas"),
    P("O IAT, por meio da DISAR, contrata a supervisora, designa a fiscalização de cada contrato de obra e aprova os "
      "relatórios. A supervisora acompanha as obras e reporta ao IAT, e os executores das obras corrigem as não "
      "conformidades apontadas. A UGP recebe as informações de progresso físico e de conformidade ambiental e social, e "
      "o Banco Mundial manifesta-se sobre o Termo de Referência e a seleção, quando houver revisão prévia."),
    BUL("**Intervenientes:** empresa supervisora; empresas executoras das obras; prefeituras, informadas do andamento;",
        "**Público envolvido:** moradores das comunidades e proprietários das áreas com obras."),
    P("Os beneficiários diretos são o IAT, que amplia a capacidade de acompanhamento das obras, e as comunidades, que "
      "recebem obras de melhor qualidade. Os beneficiários indiretos são os usuários dos sistemas e o Programa, com a "
      "redução dos riscos de execução."),

    ITEM("4. Processo de execução operacional"),
    P("A ação compreende cinco etapas, da contratação ao relatório final ({fig:raias-3227}). Durante as obras, a "
      "supervisão opera em ciclo mensal ({fig:ciclo-supervisao}): visitas de campo e controle de qualidade, correção "
      "das não conformidades pelo executor, verificação das medições, relatório mensal aprovado pelo IAT e "
      "consolidação do progresso pela UGP."),
    fig_raias(COD),
    FIG("ciclo-supervisao", "f-ciclo-supervisao", "Ciclo mensal de supervisão das obras",
        "Fonte: IAT (2026).",
        alt="Fluxograma em raias do ciclo mensal de supervisão, com a correção das não conformidades, a aprovação do "
            "relatório pelo IAT, a consolidação pela UGP e a repetição mensal até a conclusão das obras."),

    ETAPA("4.1 Etapa 1: Contratação da supervisora"),
    PL("Atividades:", "elaboração do Termo de Referência, com escopo, equipe e produtos; seleção da consultoria pelo "
       "método definido no Plano de Aquisições; assinatura do contrato e emissão da ordem de serviço."),
    PL("Entradas:", "cronogramas previstos das obras; Termo de Referência."),
    PL("Responsáveis:", "IAT (executa e aprova); UGP e Banco Mundial (consultados)."),
    PL("Produto:", "contrato assinado."),

    ETAPA("4.2 Etapa 2: Mobilização e plano de supervisão"),
    PL("Atividades:", "mobilização da equipe; elaboração do plano de supervisão, com procedimentos de medição, de "
       "controle de qualidade e de registro das não conformidades; implantação do sistema de registro e de relatórios."),
    PL("Entradas:", "contrato; projetos aprovados; contratos das obras."),
    PL("Responsáveis:", "supervisora (executa); IAT (aprova)."),
    PL("Produto:", "plano de supervisão aprovado."),

    ETAPA("4.3 Etapa 3: Acompanhamento das obras"),
    PL("Atividades:", "visitas de campo; controle de qualidade dos materiais e dos serviços; verificação dos requisitos "
       "ambientais, sociais e de saúde e segurança do trabalho; registro das não conformidades e acompanhamento da "
       "correção."),
    PL("Entradas:", "plano de supervisão; obras em execução."),
    PL("Responsáveis:", "supervisora (executa); executores das obras (corrigem); IAT (aprova)."),
    PL("Produto:", "registros de campo e de não conformidades."),

    ETAPA("4.4 Etapa 4: Medições e relatórios"),
    PL("Atividades:", "verificação das medições dos executores; controle de prazos e custos; relatórios mensais ao IAT, "
       "com as informações de progresso destinadas à UGP."),
    PL("Entradas:", "registros de campo; medições dos executores."),
    PL("Responsáveis:", "supervisora (executa); IAT (aprova); UGP (informada)."),
    PL("Produto:", "relatórios mensais aprovados."),

    ETAPA("4.5 Etapa 5: Recebimento das obras e encerramento"),
    PL("Atividades:", "apoio ao recebimento provisório e definitivo das obras; conferência dos projetos *as built*; "
       "relatório final de supervisão."),
    PL("Entradas:", "obras concluídas; relatórios mensais."),
    PL("Responsáveis:", "supervisora (executa); IAT (aprova)."),
    PL("Produto:", "relatório final de supervisão."),

    ETAPA("4.6 Modalidade de execução"),
    P("O item de custo é a supervisão e o gerenciamento de obras: 36 profissionais-mês a R$ 299.722,20, no total de "
      "R$ 10,79 milhões, com recursos do empréstimo do BIRD. A execução ocorre mediante licitação de serviços de "
      "consultoria, conforme o Caderno AQ."),
    COM("A supervisão está prevista de 2029 a 2032, e as obras de abastecimento estendem-se de 2028 a 2033. Avaliar a "
        "supervisão das obras de 2028 e de 2033 e confirmar se o escopo inclui as instalações de esgotamento "
        "sanitário."),

    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3227} apresenta o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("IAT", ["R, A", "A", "A", "A", "A"], "A"),
        ("Supervisora", ["–", "R", "R", "R", "R"], "R"),
        ("Executores das obras", ["–", "C", "R", "C", "C"], "I"),
        ("Prefeituras", ["–", "I", "I", "–", "I"], "I"),
        ("UGP", ["C", "I", "I", "I", "I"], "I"),
        ("Banco Mundial", ["C", "–", "–", "–", "–"], "–"),
    ], "obras supervisionadas, com relatórios aprovados"),

    ITEM("6. Metas, indicadores e comprovação"),
    P("A meta física é expressa em profissionais-mês, de 2029 a 2032 ({qua:metas-3227})."),
    metas(COD, [("Supervisão e gerenciamento de obras", "prof.-mês", {3: 6, 4: 12, 5: 12, 6: 6})],
          nota_extra="Prof.-mês = profissionais-mês."),
    P("Os indicadores constam do {qua:ind-3227}, e os critérios de aceite, do {qua:aceite-3227}."),
    indicadores(COD, [
        ["Relatórios de supervisão aprovados", "relatórios", "0", "1 por mês de supervisão", "Mensal; IAT"],
        ["Sistemas de abastecimento supervisionados com Termo de Recebimento Definitivo", "sistemas", "0", "83",
         "Semestral; IAT"],
        ["Não conformidades corrigidas no prazo", "% das registradas", "–", "100", "Mensal; relatórios de supervisão"],
    ]),
    COM("Definir no Termo de Referência o número de relatórios e a distribuição dos 36 profissionais-mês entre as "
        "frentes de obra."),
    aceite(COD, [
        ["Plano de supervisão", "Procedimentos de medição, qualidade e registro definidos", "Plano aprovado", "IAT"],
        ["Relatório mensal", "Andamento, medições, não conformidades e conformidade ambiental e social de cada frente",
         "Relatório aprovado", "IAT"],
        ["Medições verificadas", "Quantidades conferidas em campo", "Boletins de medição atestados", "IAT"],
        ["Relatório final", "Consolida a supervisão e o recebimento das obras", "Relatório final aprovado", "IAT"],
    ]),

    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("A supervisora constitui instrumento de cumprimento das NAS nas obras, mediante verificação em campo dos "
      "requisitos ambientais, sociais e de saúde e segurança aplicáveis às ações de abastecimento de água e de "
      "esgotamento sanitário ({qua:nas-3227}). As demais NAS são tratadas nas respectivas ações."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Acompanhamento dos planos ambientais e sociais das obras",
         "Verificação e registro em cada relatório mensal (MGAS)"],
        ["NAS 2 – Condições de trabalho", "Trabalhadores das obras e da própria supervisora", "Verificação de EPI, "
         "treinamentos e registros de incidentes (Procedimentos de Gestão de Mão de Obra)"],
        ["NAS 4 – Saúde e segurança da comunidade", "Sinalização e isolamento das obras nas comunidades",
         "Inspeção de campo e exigência de correção imediata"],
        ["NAS 10 – Engajamento das partes interessadas", "Queixas relacionadas às obras", "Registro e encaminhamento ao "
         "Mecanismo de Queixas e Reclamações (MQR)"],
    ]),

    ITEM("8. Cronograma"),
    P("A contratação ocorre em 2028, a mobilização em 2029 e a supervisão de 2029 a 2032, com 6 profissionais-mês em "
      "2029, 12 em 2030 e em 2031 e 6 em 2032 ({fig:crono-3227})."),
    fig_crono(COD),

    ITEM("9. Interfaces e dependências"),
    P("A ação depende dos contratos, dos projetos e dos cronogramas das obras de abastecimento de água e de "
      "esgotamento sanitário. Fornece ao IAT os relatórios que fundamentam as medições, os pagamentos e o recebimento "
      "das obras, aos executores as não conformidades a corrigir e à UGP as informações de progresso físico e de "
      "conformidade ({fig:interf-3227})."),
    fig_interf(COD),

    ITEM("10. Documentos complementares"),
    BUL("Termo de Referência da supervisão e do gerenciamento das obras (a elaborar);",
        "Regulamento de Aquisições do Banco Mundial para mutuários de Financiamento de Projetos de Investimento e "
        "Caderno AQ;",
        "Caderno AS;",
        "Normas técnicas aplicáveis às obras (ABNT) e projetos aprovados de cada sistema."),
]
