from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM
from comum import matriz, metas, indicadores, aceite, nas, fig_raias, fig_crono, fig_interf

COD = "3.2.2.2"

ELEMENTOS = [
    ACAO("Ação 3.2.2.2 – Trabalho técnico-social"),

    ITEM("1. Contextualização"),
    P("O trabalho técnico-social caracteriza as famílias e as condições de saneamento de cada comunidade, define o "
      "público a ser atendido e valida socialmente as soluções técnicas. Compreende também a mobilização da população, "
      "a educação sanitária e ambiental, a capacitação das lideranças locais e o estímulo à gestão participativa dos "
      "serviços, de modo que cada comunidade disponha de grupo organizado para a gestão dos sistemas (IAT, 2026a; "
      "IAT, 2026b)."),
    P("A ausência de participação das famílias está associada à subutilização e ao abandono de sistemas de saneamento "
      "rural. O Programa Nacional de Saneamento Rural estabelece a educação e a participação social como um dos três "
      "eixos indissociáveis do saneamento rural, ao lado da gestão dos serviços e da tecnologia (BRASIL, 2019). Há, "
      "ainda, o risco de exclusão de famílias vulneráveis, de áreas remotas ou de comunidades tradicionais quando o "
      "levantamento se apoia apenas em cadastros preexistentes."),
    P("A ação produz as informações das quais dependem as demais. O diagnóstico subsidia a definição da captação e o "
      "projeto dos sistemas de abastecimento, identifica a situação do esgotamento sanitário em cada domicílio e reúne "
      "as adesões que dão origem às associações de saneamento rural."),
    PL("Inclui:", "a mobilização dos municípios, das comunidades, das associações e dos proprietários; a busca ativa e "
       "o cadastro domiciliar; o diagnóstico coletivo e domiciliar das formas de abastecimento e de esgotamento "
       "sanitário; os critérios de enquadramento e os termos de adesão das famílias; a educação sanitária e ambiental; "
       "a capacitação das lideranças; o acompanhamento social das obras; e o relatório final."),
    PL("Não inclui:", "os projetos e as obras dos sistemas nem a capacitação técnica dos operadores na pré-operação, a "
       "cargo do executor das obras de abastecimento. As duas ações atuam de forma complementar: o executor capacita os "
       "operadores, e o trabalho técnico-social trata do uso adequado e da manutenção junto às famílias."),
    COM("Definir o item de custo da capacitação em operação e manutenção. A planilha a inclui no trabalho "
        "técnico-social; a nota técnica e o MOP de março a preveem na implantação dos sistemas."),
    PL("Valor previsto:", "R$ 6,47 milhões (empréstimo BIRD: R$ 6,47 milhões; contrapartida: R$ 0,00 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    ITEM("2. Área de atuação"),
    P("A ação abrange as 83 comunidades da seleção preliminar dos sistemas de abastecimento de água, com 5.810 "
      "domicílios e cerca de 16,3 mil pessoas, que constituem também a base do esgotamento sanitário nas comunidades "
      "({fig:mapa}). O diagnóstico confirma ou corrige a seleção preliminar: comunidades sem adesão suficiente ou sem "
      "viabilidade técnica podem ser substituídas por outras que atendam aos mesmos critérios. Em cada comunidade, as "
      "famílias atendidas são definidas por critérios sociais, territoriais e técnicos, aplicados na Etapa 5."),

    ITEM("3. Arranjo institucional e partes interessadas"),
    P("O IAT, por meio da DISAR, contrata a empresa, fiscaliza o contrato e valida os produtos, com a participação da "
      "SEAB, que atua junto às comunidades rurais e apoia a mobilização. A empresa contratada executa o trabalho de "
      "campo, e as prefeituras apoiam a articulação local, a divulgação e a cessão de espaços para as reuniões. A UGP "
      "acompanha a execução."),
    BUL("**Coexecutora:** SEAB, na mobilização e na validação dos produtos;",
        "**Intervenientes:** prefeituras; associações de moradores e lideranças locais; empresa contratada;",
        "**Público envolvido:** famílias e proprietários das comunidades selecionadas."),
    P("Os beneficiários diretos são as famílias das 83 comunidades, cerca de 16,3 mil pessoas, e as lideranças "
      "capacitadas. Os beneficiários indiretos são os municípios, que passam a dispor de cadastro atualizado do "
      "saneamento rural, aplicável a outras políticas públicas."),

    ITEM("4. Processo de execução operacional"),
    P("A ação compreende sete etapas, da contratação da empresa ao relatório final ({fig:raias-3222}). A empresa "
      "contratada executa o trabalho de campo, e as famílias formalizam a adesão na Etapa 5. Os produtos das etapas "
      "subsidiam os modelos de gestão, os projetos dos sistemas de abastecimento e o esgotamento sanitário nas "
      "comunidades."),
    fig_raias(COD),

    ETAPA("4.1 Etapa 1: Contratação da empresa"),
    PL("Atividades:", "elaboração do Termo de Referência, com escopo, produtos, prazos e perfil da equipe; publicação "
       "do edital; seleção da empresa; assinatura do contrato e emissão da ordem de serviço."),
    PL("Entradas:", "Termos de Cooperação assinados com os municípios; lista preliminar de comunidades."),
    PL("Responsáveis:", "IAT (executa e aprova); UGP e Banco Mundial (consultados, quando houver revisão prévia)."),
    PL("Produto:", "contrato assinado e ordem de serviço."),

    ETAPA("4.2 Etapa 2: Mobilização e sensibilização"),
    PL("Atividades:", "reuniões com as prefeituras, as associações e as lideranças; reuniões comunitárias, com "
       "linguagem acessível, para apresentação do Programa, estímulo à participação e reconhecimento do território; "
       "divulgação do Mecanismo de Queixas e Reclamações."),
    PL("Entradas:", "contrato; agenda pactuada com as prefeituras."),
    PL("Responsáveis:", "empresa contratada (executa); SEAB e prefeituras (consultadas); IAT (aprova)."),
    PL("Produto:", "plano de mobilização executado, com atas e listas de presença."),

    ETAPA("4.3 Etapa 3: Busca ativa e cadastro domiciliar"),
    PL("Atividades:", "visita a todos os domicílios da comunidade, inclusive em áreas remotas, sem dependência "
       "exclusiva de cadastros prévios; inventário social; cadastro domiciliar georreferenciado. O tratamento dos dados "
       "pessoais observa a Lei Geral de Proteção de Dados Pessoais (LGPD) e restringe-se às finalidades da ação "
       "(BRASIL, 2018)."),
    PL("Entradas:", "lista de comunidades; bases do Censo 2022 e do Cadastro Nacional de Endereços para Fins "
       "Estatísticos (CNEFE)."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova); SEAB (consultada)."),
    PL("Produto:", "cadastro domiciliar georreferenciado."),

    ETAPA("4.4 Etapa 4: Diagnóstico coletivo e domiciliar"),
    PL("Atividades:", "diagnóstico das formas atuais de abastecimento e de esgotamento sanitário, da demanda de água, "
       "da infraestrutura necessária e da viabilidade dos sistemas; levantamento das condições de cada domicílio para a "
       "solução de esgotamento sanitário; validação social das tecnologias propostas."),
    PL("Entradas:", "cadastro domiciliar."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova); SEAB (consultada)."),
    PL("Produto:", "diagnóstico por comunidade e por domicílio."),

    ETAPA("4.5 Etapa 5: Enquadramento e adesão das famílias"),
    PL("Atividades:", "aplicação dos critérios sociais, territoriais e técnicos de definição das famílias atendidas; "
       "assinatura do termo de adesão, com o compromisso de uso e manutenção adequados."),
    PL("Entradas:", "diagnóstico; critérios de enquadramento aprovados pelo IAT."),
    PL("Responsáveis:", "empresa contratada e famílias (executam); IAT (aprova)."),
    PL("Produto:", "lista de famílias enquadradas e termos de adesão assinados."),

    ETAPA("4.6 Etapa 6: Educação sanitária e ambiental e acompanhamento"),
    PL("Atividades:", "oficinas de educação sanitária e ambiental; capacitação das lideranças locais; apoio à "
       "organização comunitária e à constituição da associação; acompanhamento social das obras e da entrega dos "
       "sistemas."),
    PL("Entradas:", "termos de adesão; cronograma das obras de abastecimento."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova); prefeituras e SEAB (consultadas)."),
    PL("Produto:", "lideranças capacitadas, com listas de presença e certificados, e relatórios de acompanhamento."),

    ETAPA("4.7 Etapa 7: Relatório final"),
    PL("Atividades:", "consolidação dos resultados; elaboração do relatório final; registro da conclusão da etapa no "
       "Termo de Cooperação."),
    PL("Entradas:", "produtos das Etapas 2 a 6."),
    PL("Responsáveis:", "empresa contratada (executa); SEAB (consultada na validação); IAT (aprova)."),
    COM("A nota técnica prevê a validação conjunta do relatório final. Na matriz, a SEAB figura como C (consultada "
        "antes da aprovação), porque o Guia de Identidade Visual admite um único A por etapa; confirmar."),
    PL("Produto:", "relatório final aprovado."),

    ETAPA("4.8 Modalidade de execução"),
    P("O item de custo é o trabalho técnico e social: 36 profissionais-mês a R$ 179.835,30, no total de R$ 6,47 "
      "milhões, com recursos do empréstimo do BIRD. A execução ocorre mediante licitação de serviços, conforme o "
      "Caderno AQ, e o número de lotes é definido no Plano de Aquisições."),

    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3222} apresenta o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("IAT", ["R, A", "A", "A", "A", "A", "A", "A"], "A"),
        ("SEAB", ["–", "C", "C", "C", "C", "C", "C"], "C"),
        ("Empresa contratada", ["–", "R", "R", "R", "R", "R", "R"], "R"),
        ("Prefeituras", ["I", "C", "I", "I", "I", "C", "I"], "I"),
        ("Famílias e associações", ["–", "C", "C", "C", "R", "C", "I"], "I"),
        ("UGP", ["C", "I", "I", "I", "I", "I", "I"], "I"),
        ("Banco Mundial", ["C", "–", "–", "–", "–", "–", "–"], "–"),
    ], "cadastro, diagnóstico e termos de adesão das 83 comunidades"),

    ITEM("6. Metas, indicadores e comprovação"),
    P("A meta física é expressa em profissionais-mês e concentra-se entre 2027 e 2030 ({qua:metas-3222}), pois o "
      "diagnóstico deve estar concluído antes dos projetos e das obras."),
    metas(COD, [("Trabalho técnico e social", "prof.-mês", {1: 6, 2: 12, 3: 12, 4: 6})],
          nota_extra="Prof.-mês = profissionais-mês."),
    P("O {qua:ind-3222} reúne os indicadores de andamento da ação, apurados por comunidade."),
    indicadores(COD, [
        ["Comunidades com diagnóstico aprovado", "comunidades", "0", "83", "Por lote; IAT"],
        ["Domicílios cadastrados", "domicílios", "0", "5.810", "Por lote; cadastro domiciliar"],
        ["Famílias com termo de adesão assinado", "famílias", "0", "a definir no diagnóstico", "Por lote; IAT"],
        ["Lideranças e moradores capacitados", "pessoas", "0", "a definir no plano de trabalho", "Semestral; listas de presença"],
    ]),
    COM("Definir as metas de famílias aderidas e de pessoas capacitadas no plano de trabalho da empresa contratada."),
    P("Os critérios de aceite e as evidências constam do {qua:aceite-3222}. O relatório final, aprovado pelo IAT após "
      "consulta à SEAB, constitui a evidência de conclusão de cada lote e registra a conclusão da etapa no Termo de "
      "Cooperação."),
    aceite(COD, [
        ["Plano de trabalho", "Metodologia, cronograma e equipe compatíveis com o Termo de Referência",
         "Plano aprovado", "IAT"],
        ["Cadastro domiciliar", "Todos os domicílios da comunidade visitados e georreferenciados; dados tratados "
         "conforme a LGPD", "Base do cadastro; relatório de campo", "IAT"],
        ["Diagnóstico", "Condições de abastecimento e de esgotamento sanitário descritas por comunidade e por domicílio",
         "Relatório de diagnóstico", "IAT"],
        ["Termos de adesão", "Assinados pelas famílias enquadradas", "Termos assinados", "IAT"],
        ["Capacitação", "Conteúdo do plano de educação sanitária e ambiental cumprido",
         "Listas de presença e certificados", "IAT"],
        ["Relatório final", "Consolida os produtos e é aprovado", "Relatório final; registro no Termo de Cooperação",
         "IAT, após consulta à SEAB"],
    ]),

    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("A ação não envolve obras. Os riscos concentram-se na exclusão de famílias, na consulta inadequada a comunidades "
      "tradicionais, nas condições de trabalho da equipe de campo e no tratamento dos dados pessoais do cadastro. O "
      "{qua:nas-3222} indica as NAS aplicáveis e as medidas; as NAS 3, 4, 5, 6 e 8 não se aplicam à ação."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Risco de exclusão de famílias vulneráveis ou de áreas remotas",
         "Busca ativa em todos os domicílios; aplicação rigorosa dos critérios de vulnerabilidade social (MGAS)"],
        ["NAS 2 – Condições de trabalho", "Equipe de campo da empresa contratada",
         "Cláusulas trabalhistas e de segurança nos deslocamentos; Procedimentos de Gestão de Mão de Obra"],
        ["NAS 7 – Povos indígenas e comunidades tradicionais", "Comunidades tradicionais nas áreas selecionadas",
         "Consulta culturalmente adequada, com participação das lideranças (MGAS e PEPI)"],
        ["NAS 10 – Engajamento das partes interessadas", "Toda a ação, por constituir o principal canal de diálogo "
         "com as famílias", "Reuniões com linguagem acessível; registro das consultas; divulgação e acompanhamento do "
         "Mecanismo de Queixas e Reclamações (PEPI e MQR)"],
    ], nota="Nota: o cadastro domiciliar observa a Lei Geral de Proteção de Dados Pessoais (BRASIL, 2018)."),

    ITEM("8. Cronograma"),
    P("A contratação ocorre em 2027; a mobilização, o cadastro e o diagnóstico, de 2027 a 2029; o enquadramento e as "
      "adesões, em 2028 e 2029; a educação sanitária e ambiental e o acompanhamento, de 2028 a 2030; e o relatório "
      "final, em 2030 ({fig:crono-3222})."),
    fig_crono(COD),
    COM("O trabalho técnico-social encerra-se em 2030, e as obras de abastecimento e de esgotamento sanitário "
        "prosseguem até 2033. Avaliar se o acompanhamento social das obras de 2031 a 2033 requer recursos adicionais ou "
        "se será realizado pela equipe do IAT e pelas unidades regionais."),

    ITEM("9. Interfaces e dependências"),
    P("A ação recebe dos modelos de gestão os municípios aderidos e os Termos de Cooperação e, da implantação dos "
      "sistemas de abastecimento, o cronograma das obras. Fornece o cadastro e as adesões que dão origem às "
      "associações, o diagnóstico que subsidia os projetos de abastecimento e a relação de domicílios sem esgotamento "
      "sanitário adequado ({fig:interf-3222})."),
    fig_interf(COD),

    ITEM("10. Documentos complementares"),
    BUL("Termo de Referência do trabalho técnico-social (a elaborar);",
        "Termo de Cooperação entre o IAT e cada município;",
        "Plano de Engajamento das Partes Interessadas (PEPI) e Mecanismo de Queixas e Reclamações, no Caderno AS;",
        "Lei nº 13.709/2018 (Lei Geral de Proteção de Dados Pessoais);",
        "Programa Nacional de Saneamento Rural (BRASIL, 2019);",
        "Caderno AQ."),
]
