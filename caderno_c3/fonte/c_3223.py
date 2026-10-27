from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM
from comum import matriz, metas, indicadores, aceite, nas, fig_raias, fig_crono, fig_interf

COD = "3.2.2.3"

ELEMENTOS = [
    ACAO("Ação 3.2.2.3 – Implantação e reabilitação dos sistemas coletivos de abastecimento de água"),

    ITEM("1. Contextualização"),
    P("A ação implanta ou reabilita 83 sistemas coletivos de abastecimento de água em comunidades rurais, com captação "
      "subterrânea por poço tubular profundo, desinfecção por cloração, reservação, rede de distribuição e ligações "
      "domiciliares com hidrômetro. Os sistemas atendem 5.810 domicílios, cerca de 16,3 mil pessoas, entre 2028 e 2033 "
      "(PARANÁ, 2026; IAT, 2026a)."),
    P("No meio rural do Paraná, 99,59% dos domicílios dispõem de água canalizada, segundo o Censo 2022, mas apenas "
      "16,92% do abastecimento provém de sistemas coletivos com tratamento completo (IAT, 2026a). Predominam nascentes "
      "e poços rasos escavados (cacimbas), em grande parte contaminados por agrotóxicos, metais e coliformes e sujeitos "
      "à redução de vazão nas estiagens recorrentes no Estado. O consumo de água contaminada está associado a doenças "
      "de veiculação hídrica, como diarreia, hepatite e esquistossomose."),
    P("Por essas razões, a ação adota a captação de água subterrânea por poço tubular profundo. A água subterrânea "
      "apresenta, em geral, melhor qualidade microbiológica e menor sensibilidade à variabilidade climática, o que, na "
      "maior parte dos casos, restringe o tratamento à desinfecção por cloração. A captação subterrânea tem também "
      "menor custo, menor prazo de implantação e menor impacto ambiental que a captação superficial, que requer "
      "barragem, adutora e estação de tratamento (IAT, 2026a)."),
    P("A {fig:esquema-saa} apresenta os componentes de um sistema típico."),
    FIG("esquema-saa", "f-esquema-saa", "Componentes de um sistema coletivo de abastecimento de água rural",
        "Fonte: IAT (2026). Esquema ilustrativo, sem escala.",
        alt="Esquema em corte com poço tubular profundo, casa de química, reservatório elevado, rede de distribuição "
            "e domicílios com hidrômetro."),
    P("A ação apoia-se na experiência do Programa Água no Campo, no qual o IAT perfura poços e implanta sistemas "
      "coletivos em comunidades não atendidas pelas companhias de saneamento. Desde 2019, o programa perfurou 801 "
      "poços, com investimento aproximado de R$ 12,3 milhões e cerca de 250 mil pessoas beneficiadas; no primeiro "
      "semestre de 2025, foram 39 poços em 21 municípios, para 1.253 famílias (IAT, 2026a). Os resultados esperados "
      "incluem a redução das doenças de veiculação hídrica e dos gastos públicos com saúde, a melhoria das condições de "
      "vida, o estímulo à permanência das famílias no campo e o fortalecimento da organização comunitária."),
    P("A ação constitui a principal contribuição do IAT ao indicador de pessoas atendidas com água gerida de forma "
      "segura: cerca de 16,3 mil das 59.780 pessoas previstas. As demais decorrem do Programa Sanepar Rural."),
    PL("Inclui:", "estudos preliminares e regularização das áreas; locação, perfuração, teste de vazão, análises "
       "físico-químicas e bacteriológicas e outorga dos poços; projetos básico e executivo; licenciamento ambiental; "
       "obras da casa de química, do reservatório, das instalações eletromecânicas, da rede e das ligações com "
       "hidrômetro; reabilitação de sistemas existentes operados por associações; pré-operação, testes e capacitação "
       "dos operadores; e entrega à entidade gestora."),
    PL("Não inclui:", "a supervisão independente das obras, o modelo de gestão, o trabalho técnico-social, o "
       "esgotamento sanitário e os sistemas do Programa Sanepar Rural, objeto de ações próprias."),
    PL("Valor previsto:", "R$ 107,90 milhões (empréstimo BIRD: R$ 107,90 milhões; contrapartida: R$ 0,00 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    ITEM("2. Área de atuação"),
    P("A ação abrange todo o Estado, nas Microrregiões de Água e Esgoto, e restringe-se às comunidades que atendem aos "
      "critérios de seleção ({fig:selecao-comunidades}). O primeiro critério é o adensamento: comunidade ou conjunto de "
      "comunidades com 70 ou mais domicílios ocupados, número mínimo que viabiliza o modelo de gestão."),
    P("O segundo critério é o desempenho do município no IPDM, que varia de 0 a 1 e classifica os municípios em quatro "
      "estratos: baixo (0 a menos de 0,4), médio baixo (0,4 a menos de 0,6), médio (0,6 a menos de 0,8) e alto (0,8 a "
      "1,0). A ação restringe-se aos municípios de médio baixo e de médio desempenho."),
    P("Consideram-se, ainda, as solicitações de perfuração de poços já encaminhadas pelos municípios ao IAT e a "
      "existência de associações de moradores que operam sistemas com necessidade de complementação ou melhoria. Por "
      "fim, a comunidade somente prossegue para a implantação na ausência de impedimentos à perfuração: disponibilidade "
      "hídrica insuficiente no aquífero, condições geológicas que inviabilizem a obra, falhas geológicas com risco de "
      "contaminação ou de interrupção do fluxo, contaminantes que comprometam a potabilidade ou restrições legais e "
      "ambientais (IAT, 2026a)."),
    FIG("selecao-comunidades", "f-selecao-comunidades", "Critérios de seleção das comunidades atendidas com água",
        "Fonte: IAT (2026), com base em IAT (2026a).",
        alt="Funil com os cinco critérios de seleção das comunidades, que resulta na seleção preliminar de 83 "
            "comunidades e 5.810 domicílios."),
    COM("Justificar a exclusão dos municípios de baixo e de alto desempenho no IPDM. O Banco Mundial costuma questionar "
        "a exclusão de municípios mais vulneráveis."),
    P("A aplicação preliminar dos critérios indicou 83 comunidades, com 5.810 domicílios, considerada a média de 70 "
      "domicílios por comunidade e de 2,8 habitantes por domicílio (Censo 2022). As áreas de maior concentração de "
      "domicílios rurais e os municípios consorciados ao CISPAR constam da {fig:mapa}. A lista final é confirmada pelo "
      "trabalho técnico-social e pela viabilidade do poço (Etapa 2)."),
    COM("O Acordo de Empréstimo, item (j)(vii) das definições, exige a identificação das áreas rurais da Parte 3.2. "
        "Anexar a lista das 83 comunidades selecionadas, com município e coordenadas, ou o mapa com a respectiva "
        "localização."),

    ITEM("3. Arranjo institucional e partes interessadas"),
    P("A ação é coordenada pelo IAT, por meio da DISAR, responsável pelo planejamento, pela contratação, pela "
      "fiscalização e pelo recebimento dos sistemas. No próprio IAT, a Diretoria de Licenciamento e Outorga emite a "
      "outorga de direito de uso de recursos hídricos e as licenças ambientais. As prefeituras apoiam a regularização "
      "das áreas e a articulação local, a entidade gestora recebe e opera cada sistema, e a UGP acompanha a execução e "
      "consolida o reporte ao Banco Mundial."),
    BUL("**Coexecutora:** SEAB, na implementação local junto às comunidades;",
        "**Intervenientes:** prefeituras; entidades gestoras; empresas contratadas para projetos e obras; laboratórios "
        "contratados para as análises de potabilidade; empresa supervisora das obras;",
        "**Público envolvido:** proprietários das áreas do poço, do reservatório e da rede; moradores das comunidades."),
    COM("O MOP de março e a nota técnica preveem a participação da instituição parceira da área rural na implementação "
        "local, sem detalhar o seu papel nesta ação. Detalhar a atuação da SEAB."),
    P("Os beneficiários diretos são os moradores dos 5.810 domicílios ligados aos sistemas, cerca de 16,3 mil pessoas, "
      "selecionados pelos critérios do item 2. Os beneficiários indiretos são os municípios, com a redução de gastos "
      "com saúde, e a população do entorno, que deixa de depender de fontes contaminadas."),

    ITEM("4. Processo de execução operacional"),
    P("A implantação de cada sistema compreende seis etapas ({fig:raias-3223}). Duas premissas aplicam-se a todas: as "
      "comunidades atendidas são confirmadas pelo trabalho técnico-social, e o modelo de gestão é pactuado antes das "
      "obras. O produto final de cada sistema é o Termo de Recebimento Definitivo (TRD), emitido pelo IAT após o aceite "
      "da entidade gestora."),
    fig_raias(COD),

    ETAPA("4.1 Etapa 1: Estudos preliminares e regularização das áreas"),
    PL("Atividades:", "estudos de viabilidade técnica, social e ambiental; levantamento de campo geológico e "
       "hidrogeológico; verificação da titularidade e da situação fundiária das áreas do poço, do reservatório e das "
       "demais estruturas; formalização da doação, da cessão ou da servidão das áreas, com anuência do proprietário; "
       "anteprojeto e investigação social. A {fig:captacao} apresenta a sequência das Etapas 1 a 3."),
    FIG("captacao", "f-captacao", "Captação subterrânea, projeto e licenciamento (Etapas 1 a 3)",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias da DISAR, da área de licenciamento e outorga do IAT, do laboratório e da empresa "
            "contratada, com a decisão sobre a viabilidade do poço."),
    PL("Entradas:", "diagnóstico da comunidade (trabalho técnico-social); entidade gestora pactuada; Termo de "
       "Cooperação."),
    PL("Responsáveis:", "IAT (executa e aprova); prefeituras (executam a regularização das áreas públicas); "
       "proprietários (consultados)."),
    PL("Produto:", "áreas regularizadas e anteprojeto aprovado."),

    ETAPA("4.2 Etapa 2: Perfuração e outorga do poço"),
    PL("Atividades:", "locação do poço e projeto construtivo; anuência prévia de perfuração; perfuração conforme as "
       "normas técnicas de projeto e construção de poços; teste de vazão; análises físico-químicas e bacteriológicas da "
       "água; outorga de direito de uso. Em caso de vazão ou qualidade insuficientes, o IAT procede a nova locação ou "
       "substitui a comunidade por outra que atenda aos critérios. O IAT dispõe de equipes próprias de perfuração, com "
       "equipamentos e equipe técnica para mais de 150 poços por ano (IAT, 2026a)."),
    PL("Entradas:", "áreas regularizadas; estudo hidrogeológico."),
    PL("Responsáveis:", "equipe de perfuração do IAT ou empresa contratada (executa); laboratório contratado "
       "(análises); IAT (aprova e emite a outorga)."),
    PL("Produto:", "poço perfurado, testado e outorgado."),
    COM("A nota técnica prevê a perfuração dos poços pelas equipes do IAT; o MOP de março previa a contratação "
        "integrada do poço. Definir o responsável pela perfuração."),

    ETAPA("4.3 Etapa 3: Contratação integrada, projetos e licenças"),
    PL("Atividades:", "contratação integrada, na qual a mesma empresa elabora os projetos executivos e executa as "
       "obras; projetos básico e executivo da casa de química, do reservatório, das instalações eletromecânicas, da rede "
       "e das ligações; aprovação dos projetos pelo IAT; estudos ambientais e sociais e obtenção das licenças. As obras "
       "iniciam-se somente após a emissão da outorga e das licenças."),
    PL("Entradas:", "poço outorgado; vazão e qualidade da água; anteprojeto."),
    PL("Responsáveis:", "IAT (contrata, aprova os projetos e emite as licenças); empresa contratada (elabora os "
       "projetos); Banco Mundial (consultado, quando houver revisão prévia)."),
    PL("Produto:", "projetos aprovados e licenças emitidas."),
    COM("O MOP define “contratação integrada” como aquela em que o contratado elabora o projeto executivo e executa a "
        "obra, o que corresponde à contratação semi-integrada da Lei nº 14.133/2021 (art. 6º, XXXIII). Definir o regime "
        "e verificar a compatibilidade com o Regulamento de Aquisições do Banco Mundial."),

    ETAPA("4.4 Etapa 4: Execução das obras"),
    PL("Atividades:", "a obra é acompanhada em três níveis ({fig:obras}): o executor constrói conforme o projeto e "
       "instala hidrômetro em cada ligação domiciliar; a supervisora acompanha a execução e registra o andamento em "
       "relatórios mensais; e a fiscalização do IAT verifica a conformidade com o projeto e as normas. Constatada não "
       "conformidade, o executor procede à correção, e a obra é submetida a nova verificação. Atestada a conformidade, "
       "o IAT emite o atesto de recebimento, acompanhado dos laudos de vistoria e do projeto *as built*."),
    FIG("obras", "f-obras", "Execução, supervisão e fiscalização das obras, por responsável",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias da fiscalização do IAT, da empresa executora e da supervisora, com a decisão de "
            "conformidade e a correção das não conformidades."),
    PL("Entradas:", "projetos aprovados; outorga e licenças; ordem de serviço."),
    PL("Responsáveis:", "empresa contratada (executa); supervisora (acompanha); IAT (fiscaliza e aprova); prefeituras "
       "(consultadas)."),
    PL("Produto:", "sistema implantado, com atesto de recebimento, laudos de vistoria e projeto *as built*."),
    COM("No MOP de março, a quantidade de hidrômetros consta como “XXX”. Pela meta de domicílios, são 5.810 "
        "hidrômetros, um por ligação; confirmar."),

    ETAPA("4.5 Etapa 5: Pré-operação, capacitação e entrega"),
    PL("Atividades:", "pré-operação e testes de funcionamento; capacitação dos operadores locais, conforme o Plano de "
       "Operação e Manutenção; reunião técnica de entrega com a comunidade e a entidade gestora; aceite da entidade "
       "gestora; emissão do TRD ({fig:entrega})."),
    FIG("entrega", "f-entrega", "Transferência, operação e encerramento dos sistemas de abastecimento",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias da empresa executora, do IAT e da entidade gestora, da pré-operação ao registro dos "
            "dados de operação no SIGARH e no GeoPR."),
    PL("Entradas:", "sistema implantado; entidade gestora constituída."),
    PL("Responsáveis:", "empresa contratada (pré-operação e capacitação); entidade gestora (aceita o sistema); IAT "
       "(aprova e emite o TRD)."),
    PL("Produto:", "Termo de Recebimento Definitivo e operadores capacitados."),

    ETAPA("4.6 Etapa 6: Acompanhamento pós-implantação e encerramento"),
    PL("Atividades:", "suporte técnico pós-implantação; avaliação semestral de desempenho; acompanhamento da qualidade "
       "da água distribuída, conforme o padrão de potabilidade (BRASIL, 2021); registro dos dados no SIGARH e no "
       "GeoPR; relatório final e prestação de contas."),
    PL("Entradas:", "TRD; dados de operação informados pela entidade gestora."),
    PL("Responsáveis:", "IAT (executa); entidade gestora (informa os dados de operação); UGP (valida o relatório "
       "final)."),
    PL("Produto:", "relatórios semestrais de desempenho e relatório final."),

    ETAPA("4.7 Modalidade de execução"),
    P("O item de custo é o de sistemas coletivos de abastecimento de água: 83 sistemas a R$ 1,3 milhão, no total de "
      "R$ 107,90 milhões, com recursos do empréstimo do BIRD. Os projetos executivos e as obras são contratados "
      "mediante licitação, em regime de contratação integrada, conforme o Caderno AQ; os ensaios laboratoriais de "
      "potabilidade também são licitados."),
    P("Os estudos preliminares, a regularização das áreas e a outorga são executados diretamente pelo IAT. A "
      "perfuração pode ser executada pelas equipes do IAT ou incluída na contratação das obras."),
    COM("A nota técnica estima R$ 1,4 milhão por sistema; prevalece o valor da planilha de custos (R$ 1,3 milhão)."),

    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3223} apresenta o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("IAT", ["R, A", "R, A", "A", "A", "A", "R"], "R, A"),
        ("Prefeituras", ["R", "I", "C", "C", "C", "I"], "I"),
        ("Empresas contratadas", ["–", "R", "R", "R", "R", "–"], "–"),
        ("Supervisora", ["–", "–", "–", "R", "C", "–"], "–"),
        ("Entidade gestora", ["C", "I", "C", "I", "R", "R"], "R"),
        ("UGP", ["I", "I", "I", "I", "I", "A"], "I"),
        ("Banco Mundial", ["–", "–", "C", "–", "–", "I"], "I"),
    ], "sistemas em operação, com Termo de Recebimento Definitivo"),

    ITEM("6. Metas, indicadores e comprovação"),
    P("O {qua:metas-3223} distribui os 83 sistemas ao longo do Programa, com os domicílios ligados e as pessoas "
      "atendidas em cada ano."),
    metas(COD, [
        ("Sistemas coletivos de abastecimento de água", "sistemas", {2: 5, 3: 10, 4: 20, 5: 20, 6: 18, 7: 10}),
        ("Domicílios ligados", "domicílios", {2: 350, 3: 700, 4: 1400, 5: 1400, 6: 1260, 7: 700}),
        ("Pessoas atendidas", "pessoas", {2: 980, 3: 1960, 4: 3920, 5: 3920, 6: 3528, 7: 1960}),
    ], nota_extra="Domicílios: 70 por sistema; pessoas: 2,8 por domicílio (Censo 2022)."),
    P("Os indicadores constam do {qua:ind-3223}. O indicador de pessoas atendidas com água gerida de forma segura "
      "corresponde ao número acumulado de domicílios ligados aos sistemas multiplicado por 2,8, com desagregação por "
      "sexo e para jovens de 15 a 24 anos. Considera-se gerida de forma segura a água proveniente de fonte melhorada, "
      "disponível no domicílio por pelo menos 12 horas diárias e isenta de contaminação fecal e de contaminação química "
      "prioritária."),
    indicadores(COD, [
        ["Sistemas implantados com Termo de Recebimento Definitivo", "sistemas", "0", "83", "Semestral; IAT"],
        ["Domicílios atendidos com sistema coletivo de abastecimento", "domicílios", "0", "5.810", "Anual; IAT e entidades gestoras"],
        ["Pessoas atendidas com água gerida de forma segura (parcela do indicador do componente)",
         "pessoas", "0", "16.268", "Anual; IAT, com desagregação por sexo e jovens"],
        ["Análises de entrega conformes ao padrão de potabilidade", "% das análises", "–", "100", "Na entrega e semestral; laudos laboratoriais"],
    ]),
    P("Os critérios de aceite e as evidências de cada produto constam do {qua:aceite-3223}. A evidência de conclusão "
      "de cada sistema é o TRD; no encerramento, o relatório final é validado pela UGP e apresentado ao Banco Mundial."),
    aceite(COD, [
        ["Áreas regularizadas", "Titularidade comprovada; doação, cessão ou servidão formalizada",
         "Matrícula ou termo de cessão; anuência do proprietário", "IAT"],
        ["Poço perfurado", "Construído conforme o projeto construtivo e as normas técnicas",
         "Relatório de perfuração; laudo de vistoria; atesto de recebimento", "IAT"],
        ["Vazão e qualidade", "Vazão compatível com a demanda e água conforme o padrão de potabilidade",
         "Teste de vazão; laudos físico-químicos e bacteriológicos", "IAT"],
        ["Outorga", "Outorga de direito de uso emitida", "Ato de outorga", "IAT"],
        ["Projetos e licenças", "Projetos básico e executivo aprovados; licenças emitidas",
         "Parecer de aprovação; licenças", "IAT"],
        ["Sistema implantado", "Obra conforme o projeto e as normas; um hidrômetro por ligação",
         "Relatórios de supervisão e de fiscalização; laudos; *as built*", "IAT"],
        ["Operadores capacitados", "Capacitação conforme o Plano de Operação e Manutenção",
         "Listas de presença e certificados", "IAT"],
        ["Sistema entregue", "Testes aprovados, aceite da entidade gestora e abastecimento por pelo menos 12 horas "
         "diárias", "Termo de aceite; Termo de Recebimento Definitivo", "IAT"],
    ]),

    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("A ação envolve obras de pequeno porte, dispersas no território estadual. Os principais riscos são a contaminação "
      "do aquífero, os impactos temporários das obras (ruído, poeira, resíduos e erosão localizada), os acidentes de "
      "trabalho, os conflitos relativos à posse das áreas e ao uso da água e a exclusão de famílias vulneráveis. O "
      "{qua:nas-3223} indica as NAS aplicáveis e as respectivas medidas."),
    P("A NAS 9 não se aplica ao Programa, e as medidas detalhadas constam do Caderno AS."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Obras de captação, reservação e distribuição em cada comunidade",
         "Triagem socioambiental de cada sistema; licenciamento; plano ambiental e social da obra (MGAS)"],
        ["NAS 2 – Condições de trabalho", "Equipes de perfuração e de obras",
         "Uso de equipamento de proteção individual (EPI); treinamento de segurança; código de conduta "
         "(Procedimentos de Gestão de Mão de Obra)"],
        ["NAS 3 – Eficiência de recursos e prevenção da poluição", "Uso da água subterrânea; risco de contaminação do "
         "aquífero; resíduos e fluidos de perfuração", "Outorga e hidrometração; normas técnicas de perfuração e "
         "proteção sanitária do poço; Plano de Gerenciamento de Resíduos Sólidos"],
        ["NAS 4 – Saúde e segurança da comunidade", "Valas abertas, trânsito de máquinas e qualidade da água "
         "distribuída", "Sinalização e isolamento das valas; controle de horários e de emissão de poeira; análises de "
         "potabilidade na entrega e na operação"],
        ["NAS 5 – Aquisição de terras", "Áreas para poço, reservatório e rede", "Verificação documental da "
         "titularidade; doação, cessão ou servidão com anuência; ausência de reassentamento involuntário (Marco de "
         "Política de Reassentamento)"],
        ["NAS 6 – Biodiversidade", "Definição das áreas das estruturas", "Triagem para evitar supressão de vegetação "
         "nativa e intervenção em áreas de preservação permanente"],
        ["NAS 7 – Povos indígenas e comunidades tradicionais", "Comunidades tradicionais nas áreas selecionadas",
         "Consulta culturalmente adequada (MGAS e PEPI)"],
        ["NAS 8 – Patrimônio cultural", "Escavações para poço, reservatório e rede", "Procedimento de achados fortuitos"],
        ["NAS 10 – Engajamento das partes interessadas", "Moradores e proprietários afetados pelas obras",
         "Reuniões comunitárias; divulgação do Mecanismo de Queixas e Reclamações; resposta às queixas (PEPI e MQR)"],
    ]),

    ITEM("8. Cronograma"),
    P("Os estudos preliminares iniciam-se em 2027, com execução direta pelo IAT. A perfuração, os projetos e as "
      "licenças ocorrem de 2028 a 2032, e as obras e as entregas, de 2028 a 2033, conforme a planilha de custos: 5 "
      "sistemas em 2028, 10 em 2029, 20 em 2030 e em 2031, 18 em 2032 e 10 em 2033 ({fig:crono-3223}). O "
      "acompanhamento pós-implantação inicia-se com os primeiros sistemas entregues e estende-se até o encerramento."),
    fig_crono(COD),

    ITEM("9. Interfaces e dependências"),
    P("A ação depende da entidade gestora pactuada, do diagnóstico das comunidades, da supervisão das obras e dos "
      "instrumentos de gestão de recursos hídricos do Programa, como a outorga, o SIGARH e os dados de águas "
      "subterrâneas. Fornece ao esgotamento sanitário as comunidades atendidas com água, aos modelos de gestão os "
      "sistemas concluídos para entrega e à UGP o número de pessoas atendidas para o indicador do componente "
      "({fig:interf-3223})."),
    fig_interf(COD),

    ITEM("10. Documentos complementares"),
    BUL("Termo de Referência e edital da contratação integrada de projetos e obras (a elaborar);",
        "Plano de Operação e Manutenção dos sistemas (a elaborar);",
        "Portaria GM/MS nº 888/2021, que altera o Anexo XX da Portaria de Consolidação GM/MS nº 5/2017 (padrão de "
        "potabilidade da água para consumo humano);",
        "Normas da Associação Brasileira de Normas Técnicas (ABNT) NBR 12212:2017 e NBR 12244:2006 (projeto e "
        "construção de poço tubular) e demais normas ABNT de projeto de sistemas de abastecimento de água;",
        "Lei nº 9.433/1997 e Lei Estadual nº 12.726/1999 (outorga de direito de uso de recursos hídricos) e normas de "
        "licenciamento ambiental do IAT;",
        "Caderno AQ e Caderno AS;",
        "Notas técnicas de origem (IAT, 2026a; IAT, 2026b)."),
]
