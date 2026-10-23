from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM
from comum import matriz, metas, indicadores, aceite, nas, fig_ipo, fig_crono, fig_interf

COD = "3.2.2.2"

ELEMENTOS = [
    ACAO("Ação 3.2.2.2 – Trabalho técnico-social"),

    ITEM("1. Contextualização"),
    P("O trabalho técnico-social conhece as famílias e as condições de saneamento de cada comunidade, define quem será "
      "atendido e valida socialmente as soluções técnicas. Também mobiliza a população, promove a educação sanitária e "
      "ambiental, capacita as lideranças locais e incentiva a gestão participativa dos serviços, para que cada "
      "comunidade tenha um grupo de pessoas preparado para manter os sistemas (IAT, 2026a; IAT, 2026b)."),
    P("Sem a participação das famílias, os sistemas rurais costumam ser subutilizados ou abandonados. O Programa "
      "Nacional de Saneamento Rural trata a educação e a participação social como um dos três eixos indissociáveis do "
      "saneamento rural, ao lado da gestão dos serviços e da tecnologia (BRASIL, 2019). Há também o risco de deixar de "
      "fora famílias vulneráveis, de áreas remotas ou de comunidades tradicionais, quando o levantamento depende apenas "
      "de cadastros existentes."),
    P("A ação produz a informação de que as demais dependem. O diagnóstico orienta a captação e o projeto do sistema de "
      "água (Ação 3.2.2.3), indica domicílio a domicílio a situação do esgoto (Ação 3.2.2.5) e reúne as adesões que "
      "formam as associações (Ação 3.2.2.1)."),
    PL("Inclui:", "a mobilização dos municípios, das comunidades, das associações e dos proprietários; a busca ativa e "
       "o cadastro domiciliar; o diagnóstico coletivo e domiciliar das formas de abastecimento e de esgotamento; os "
       "critérios de enquadramento e os termos de adesão das famílias; a educação sanitária e ambiental; a capacitação "
       "das lideranças; o acompanhamento social das obras; e o relatório final."),
    PL("Não inclui:", "os projetos e as obras dos sistemas nem o treinamento técnico dos operadores na pré-operação, "
       "feito pelo executor da obra (Ação 3.2.2.3). As duas ações trabalham juntas na capacitação: o executor treina os "
       "operadores, e o trabalho técnico-social trata do uso correto e da manutenção com as famílias."),
    COM("Definir em qual item de custo fica a capacitação em operação e manutenção. A planilha a inclui no trabalho "
        "técnico-social; a nota técnica e o MOP de março a preveem na implantação dos sistemas."),
    PL("Valor previsto:", "R$ 6,47 milhões (empréstimo BIRD: R$ 6,47 milhões; contrapartida: R$ 0,00 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    ITEM("2. Área de atuação"),
    P("A ação atua nas 83 comunidades da seleção preliminar da Ação 3.2.2.3, com 5.810 domicílios, cerca de 16,3 mil "
      "pessoas, que são também a base da Ação 3.2.2.5 (ver o mapa da {fig:mapa}). O diagnóstico confirma ou corrige a "
      "seleção preliminar: comunidades sem adesão suficiente ou sem viabilidade técnica podem ser substituídas por "
      "outras que atendam aos mesmos critérios. Dentro de cada comunidade, as famílias atendidas são definidas por "
      "critérios sociais, territoriais e técnicos, aplicados na Etapa 5."),

    ITEM("3. Arranjo institucional e partes interessadas"),
    P("O IAT, por meio da DISAR, contrata a empresa, fiscaliza o contrato e valida os produtos em conjunto com o "
      "IDR-Paraná, que conhece as comunidades rurais e apoia a mobilização. A empresa contratada executa o trabalho de "
      "campo, e as prefeituras apoiam a articulação local, a divulgação e a cessão de espaços para as reuniões. A UGP "
      "acompanha a execução."),
    BUL("**Coexecutor:** IDR-Paraná, na mobilização e na validação dos produtos;",
        "**Intervenientes:** prefeituras; associações de moradores e lideranças locais; empresa contratada;",
        "**Público envolvido:** famílias e proprietários das comunidades selecionadas."),
    P("Os beneficiários diretos são as famílias das 83 comunidades, cerca de 16,3 mil pessoas, e as lideranças "
      "capacitadas. Os beneficiários indiretos são os municípios, que passam a contar com um cadastro atualizado do "
      "saneamento rural, útil a outras políticas públicas."),

    ITEM("4. Processo de execução operacional"),
    P("O trabalho começa com a contratação da empresa e termina com o relatório final, que dá baixa na etapa "
      "correspondente do Termo de Cooperação ({fig:ipo-3222}). A sequência detalhada, com os produtos de cada etapa e "
      "as ações que usam os resultados, está na {fig:tts}."),
    fig_ipo(COD),
    FIG("tts", "f-tts", "Sequência, produtos e usos do trabalho técnico-social",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma vertical com as etapas do trabalho técnico-social, os produtos de cada etapa e as ações que "
            "usam o diagnóstico."),

    ETAPA("4.1 Etapa 1: Contratação da empresa"),
    PL("Atividades:", "elaboração do Termo de Referência, com escopo, produtos, prazos e perfil da equipe; edital; "
       "seleção da empresa; assinatura do contrato e ordem de serviço."),
    PL("Entradas:", "Termos de Cooperação assinados (Ação 3.2.2.1); lista preliminar de comunidades."),
    PL("Responsáveis:", "IAT (executa e aprova); UGP e Banco Mundial (consultados, quando houver revisão prévia)."),
    PL("Produto:", "contrato assinado e ordem de serviço."),

    ETAPA("4.2 Etapa 2: Mobilização e sensibilização"),
    PL("Atividades:", "reuniões com as prefeituras, as associações e as lideranças; reuniões comunitárias em "
       "linguagem simples para apresentar o Programa, estimular a participação e conhecer o território; divulgação do "
       "canal de queixas e reclamações."),
    PL("Entradas:", "contrato; agenda pactuada com as prefeituras."),
    PL("Responsáveis:", "empresa contratada (executa); IDR-Paraná e prefeituras (consultados); IAT (aprova)."),
    PL("Produto:", "plano de mobilização executado, com atas e listas de presença."),

    ETAPA("4.3 Etapa 3: Busca ativa e cadastro domiciliar"),
    PL("Atividades:", "visita a todos os domicílios da comunidade, inclusive em áreas remotas, sem depender só de "
       "cadastros prévios; inventário social; cadastro domiciliar georreferenciado. Os dados pessoais são tratados "
       "conforme a Lei Geral de Proteção de Dados Pessoais, apenas para as finalidades da ação (BRASIL, 2018)."),
    PL("Entradas:", "lista de comunidades; bases do Censo 2022 e do CNEFE."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova); IDR-Paraná (consultado)."),
    PL("Produto:", "cadastro domiciliar georreferenciado."),

    ETAPA("4.4 Etapa 4: Diagnóstico coletivo e domiciliar"),
    PL("Atividades:", "diagnóstico das formas atuais de abastecimento e de esgotamento, da demanda de água, da "
       "infraestrutura necessária e da viabilidade dos sistemas; levantamento das condições de cada domicílio para a "
       "solução de esgoto; validação social das tecnologias propostas."),
    PL("Entradas:", "cadastro domiciliar."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova); IDR-Paraná (consultado)."),
    PL("Produto:", "diagnóstico por comunidade e por domicílio."),

    ETAPA("4.5 Etapa 5: Enquadramento e adesão das famílias"),
    PL("Atividades:", "aplicação dos critérios sociais, territoriais e técnicos que definem as famílias atendidas; "
       "assinatura do termo de adesão, com o compromisso de uso e manutenção adequados."),
    PL("Entradas:", "diagnóstico; critérios de enquadramento aprovados pelo IAT."),
    PL("Responsáveis:", "empresa contratada e famílias (executam); IAT (aprova)."),
    PL("Produto:", "lista de famílias enquadradas e termos de adesão assinados."),

    ETAPA("4.6 Etapa 6: Educação sanitária e ambiental e acompanhamento"),
    PL("Atividades:", "oficinas de educação sanitária e ambiental; capacitação das lideranças locais; apoio à "
       "organização comunitária e à constituição da associação; acompanhamento social das obras e da entrega dos "
       "sistemas."),
    PL("Entradas:", "termos de adesão; cronograma das obras (Ação 3.2.2.3)."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova); prefeituras e IDR-Paraná (consultados)."),
    PL("Produto:", "lideranças capacitadas, com listas de presença e certificados, e relatórios de acompanhamento."),

    ETAPA("4.7 Etapa 7: Relatório final"),
    PL("Atividades:", "consolidação dos resultados; relatório final; baixa da etapa no Termo de Cooperação."),
    PL("Entradas:", "produtos das Etapas 2 a 6."),
    PL("Responsáveis:", "empresa contratada (executa); IAT e IDR-Paraná (validam; a aprovação final é do IAT)."),
    PL("Produto:", "relatório final aprovado."),

    ETAPA("4.8 Modalidade de execução"),
    P("O item de custo é o trabalho técnico e social: 36 profissionais-mês a R$ 179.835,30, total de R$ 6,47 milhões, "
      "financiados pelo empréstimo do BIRD. A execução é por licitação de serviços, conforme o Caderno de Aquisições. "
      "O número de lotes será definido no Plano de Aquisições."),

    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3222} indica o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("IAT", ["R, A", "A", "A", "A", "A", "A", "A"], "A"),
        ("IDR-Paraná", ["–", "C", "C", "C", "C", "C", "R"], "C"),
        ("Empresa contratada", ["–", "R", "R", "R", "R", "R", "R"], "R"),
        ("Prefeituras", ["I", "C", "I", "I", "I", "C", "I"], "I"),
        ("Famílias e associações", ["–", "C", "C", "C", "R", "C", "I"], "I"),
        ("UGP", ["C", "I", "I", "I", "I", "I", "I"], "I"),
        ("Banco Mundial", ["C", "–", "–", "–", "–", "–", "–"], "–"),
    ], "cadastro, diagnóstico e termos de adesão das 83 comunidades"),

    ITEM("6. Metas, indicadores e comprovação"),
    P("A meta física é medida em profissionais-mês e se concentra entre 2027 e 2030 ({qua:metas-3222}), porque o "
      "diagnóstico precisa estar pronto antes dos projetos e das obras."),
    metas(COD, [("Trabalho técnico e social", "prof.-mês", {1: 6, 2: 12, 3: 12, 4: 6})],
          nota_extra="Prof.-mês = profissionais-mês."),
    P("O {qua:ind-3222} reúne os indicadores que acompanham o andamento da ação, comunidade a comunidade."),
    indicadores(COD, [
        ["Comunidades com diagnóstico aprovado", "comunidades", "0", "83", "Por lote; IAT"],
        ["Domicílios cadastrados", "domicílios", "0", "5.810", "Por lote; cadastro domiciliar"],
        ["Famílias com termo de adesão assinado", "famílias", "0", "a definir no diagnóstico", "Por lote; IAT"],
        ["Lideranças e moradores capacitados", "pessoas", "0", "a definir no plano de trabalho", "Semestral; listas de presença"],
    ]),
    COM("Definir as metas de famílias aderidas e de pessoas capacitadas no plano de trabalho da empresa contratada."),
    P("Os critérios de aceite e as evidências estão no {qua:aceite-3222}. O relatório final, validado pelo IAT e pelo "
      "IDR-Paraná, é a evidência de conclusão de cada lote e dá baixa no Termo de Cooperação."),
    aceite(COD, [
        ["Plano de trabalho", "Metodologia, cronograma e equipe compatíveis com o Termo de Referência",
         "Plano aprovado", "IAT"],
        ["Cadastro domiciliar", "Todos os domicílios da comunidade visitados e georreferenciados; dados tratados "
         "conforme a LGPD", "Base do cadastro; relatório de campo", "IAT"],
        ["Diagnóstico", "Condições de abastecimento e de esgoto descritas por comunidade e por domicílio",
         "Relatório de diagnóstico", "IAT"],
        ["Termos de adesão", "Assinados pelas famílias enquadradas", "Termos assinados", "IAT"],
        ["Capacitação", "Conteúdo do plano de educação sanitária e ambiental cumprido",
         "Listas de presença e certificados", "IAT"],
        ["Relatório final", "Consolida os produtos e é aprovado", "Relatório final; baixa no Termo de Cooperação",
         "IAT e IDR-Paraná"],
    ]),

    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("A ação não tem obras. Os riscos estão na exclusão de famílias, na consulta inadequada a comunidades "
      "tradicionais, nas condições de trabalho da equipe de campo e no tratamento dos dados pessoais do cadastro. O "
      "{qua:nas-3222} indica as NAS aplicáveis e as medidas; as NAS 3, 4, 5, 6 e 8 não se aplicam à ação."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Risco de excluir famílias vulneráveis ou de áreas remotas",
         "Busca ativa em todos os domicílios; aplicação rigorosa dos critérios de vulnerabilidade social (MGAS)"],
        ["NAS 2 – Condições de trabalho", "Equipe de campo da empresa contratada",
         "Cláusulas trabalhistas e de segurança nos deslocamentos; Procedimentos de Gestão de Mão de Obra"],
        ["NAS 7 – Povos indígenas e comunidades tradicionais", "Comunidades tradicionais nas áreas selecionadas",
         "Consulta culturalmente adequada, com participação das lideranças (MGAS e PEPI)"],
        ["NAS 10 – Engajamento das partes interessadas", "Toda a ação: é o principal canal de diálogo com as famílias",
         "Reuniões em linguagem simples; registro das consultas; divulgação e acompanhamento do Mecanismo de Queixas "
         "e Reclamações (PEPI e MQR)"],
    ], nota="Nota: o cadastro domiciliar segue a Lei Geral de Proteção de Dados Pessoais (BRASIL, 2018)."),

    ITEM("8. Cronograma"),
    P("A contratação ocorre em 2027; a mobilização, o cadastro e o diagnóstico, de 2027 a 2029; o enquadramento e as "
      "adesões, em 2028 e 2029; a educação sanitária e ambiental e o acompanhamento, de 2028 a 2030; e o relatório "
      "final, em 2030 ({fig:crono-3222})."),
    fig_crono(COD),
    COM("O trabalho técnico-social termina em 2030, mas as obras de água e de esgoto seguem até 2033. Avaliar se o "
        "acompanhamento social das obras de 2031 a 2033 precisa de recursos adicionais ou será feito pela equipe do IAT "
        "e pelas unidades regionais."),

    ITEM("9. Interfaces e dependências"),
    P("A ação recebe da Ação 3.2.2.1 os municípios aderidos e os Termos de Cooperação, e da Ação 3.2.2.3 o cronograma "
      "das obras. Entrega o cadastro e as adesões que formam as associações, o diagnóstico que orienta os projetos de "
      "água e a lista de domicílios sem esgotamento adequado para a Ação 3.2.2.5 ({fig:interf-3222})."),
    fig_interf(COD),

    ITEM("10. Documentos complementares"),
    BUL("Termo de Referência do trabalho técnico-social (a elaborar);",
        "Termo de Cooperação entre o IAT e cada município;",
        "Plano de Engajamento das Partes Interessadas (PEPI) e Mecanismo de Queixas e Reclamações, no Caderno Ambiental "
        "e Social do MOP;",
        "Lei nº 13.709/2018 (Lei Geral de Proteção de Dados Pessoais);",
        "Programa Nacional de Saneamento Rural (BRASIL, 2019);",
        "Caderno de Aquisições do MOP."),
]
