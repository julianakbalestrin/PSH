from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM
from comum import matriz, metas, indicadores, aceite, nas, fig_raias, fig_crono, fig_interf

COD = "3.2.2.3"

ELEMENTOS = [
    ACAO("Ação 3.2.2.3 – Implantação e reabilitação dos sistemas coletivos de abastecimento de água"),

    ITEM("1. Contextualização"),
    P("A ação implanta ou reabilita 83 sistemas coletivos de abastecimento de água em comunidades rurais, com "
      "captação por poço tubular profundo, tratamento por cloração, reservatório, rede de distribuição e ligações "
      "domiciliares com hidrômetro. Os sistemas atendem 5.810 domicílios, cerca de 16,3 mil pessoas, entre 2028 e 2033 "
      "(PARANÁ, 2026; IAT, 2026a)."),
    P("No meio rural do Paraná, 99,59% dos domicílios têm água canalizada, segundo o Censo 2022, mas só 16,92% do "
      "abastecimento vem de sistemas coletivos com tratamento completo (IAT, 2026a). Predominam nascentes e poços rasos "
      "escavados (cacimbas), em grande parte contaminados por agrotóxicos, metais e coliformes e sujeitos à perda de "
      "vazão nas estiagens, que atingem o campo paranaense todos os anos. A água contaminada está ligada a doenças de "
      "veiculação hídrica, como diarreia, hepatite e esquistossomose."),
    P("Por isso, a ação capta água subterrânea por poço tubular profundo. A água do aquífero é filtrada naturalmente "
      "ao percolar o solo, sofre menos com a variação do clima e, na maioria dos casos, precisa apenas de cloração "
      "simples. A captação também custa menos, fica pronta em menos tempo e tem menor impacto ambiental do que uma "
      "fonte superficial, que exige barragem, adutora e estação de tratamento (IAT, 2026a)."),
    P("A {fig:esquema-saa} mostra os componentes de um sistema típico."),
    FIG("esquema-saa", "f-esquema-saa", "Componentes de um sistema coletivo de abastecimento de água rural",
        "Fonte: IAT (2026). Esquema ilustrativo, sem escala.",
        alt="Esquema em corte com poço tubular profundo, casa química, reservatório elevado, rede de distribuição e "
            "casas com hidrômetro."),
    P("A ação se apoia na experiência do Programa Água no Campo, em que o IAT perfura poços e implanta sistemas "
      "coletivos em comunidades fora da cobertura das companhias de saneamento. Desde 2019, o programa perfurou 801 "
      "poços, com investimento aproximado de R$ 12,3 milhões e cerca de 250 mil pessoas beneficiadas; só no primeiro "
      "semestre de 2025, foram 39 poços em 21 municípios, para 1.253 famílias (IAT, 2026a). Os resultados esperados vão "
      "além do acesso à água: menos doenças de veiculação hídrica e gastos públicos com saúde, mais conforto e "
      "bem-estar, estímulo à permanência das famílias no campo e fortalecimento da vida comunitária."),
    P("A ação é a principal entrega do IAT para o indicador do Componente 3 de pessoas atendidas com água gerida de "
      "forma segura: cerca de 16,3 mil das 59.780 pessoas previstas. As demais vêm do Programa Sanepar Rural "
      "(Ação 3.2.2.4)."),
    PL("Inclui:", "estudos preliminares e regularização das áreas; locação, perfuração, testes de vazão, análises "
       "físico-químicas e bacteriológicas e outorga dos poços; projetos básico e executivo; licenciamento; obras da casa "
       "química, do reservatório, da parte eletromecânica, da rede e das ligações com hidrômetro; reabilitação de "
       "sistemas existentes operados por associações; pré-operação, testes e capacitação dos operadores; e entrega à "
       "entidade gestora."),
    PL("Não inclui:", "a supervisão independente das obras (Ação 3.2.2.7), o modelo de gestão (Ação 3.2.2.1), o "
       "trabalho técnico-social (Ação 3.2.2.2), o esgotamento sanitário (Ação 3.2.2.5) e os sistemas do Programa "
       "Sanepar Rural (Ação 3.2.2.4)."),
    PL("Valor previsto:", "R$ 107,90 milhões (empréstimo BIRD: R$ 107,90 milhões; contrapartida: R$ 0,00 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    ITEM("2. Área de atuação"),
    P("A ação abrange todo o Estado, nas Microrregiões de Água e Esgoto, mas atende apenas as comunidades que passam "
      "pelos critérios de seleção ({fig:selecao-comunidades}). O primeiro critério é o adensamento: comunidade ou "
      "conjunto de comunidades com 70 ou mais domicílios ocupados, número que torna viável o modelo de gestão."),
    P("O segundo é o desempenho do município no Índice Ipardes de Desempenho Municipal (IPDM), que varia de 0 a 1 e "
      "classifica os municípios em quatro estratos: baixo (de 0 a menos de 0,4), médio baixo (de 0,4 a menos de 0,6), "
      "médio (de 0,6 a menos de 0,8) e alto (de 0,8 a 1,0). A ação trabalha apenas com municípios de médio baixo e de "
      "médio desempenho."),
    P("Também contam os pedidos que os municípios já encaminharam ao IAT para perfuração de poços e a existência de "
      "associações de moradores que operam sistemas e precisam de complementação ou melhorias. Por fim, a comunidade "
      "só segue para a implantação se nada impedir a perfuração: aquífero sem água suficiente, solo ou rochas que "
      "impossibilitem a obra, falhas geológicas que possam contaminar a água ou interromper o fluxo, contaminantes que "
      "comprometam a potabilidade ou restrições legais e ambientais (IAT, 2026a)."),
    FIG("selecao-comunidades", "f-selecao-comunidades", "Critérios de seleção das comunidades atendidas com água",
        "Fonte: IAT (2026), com base em IAT (2026a).",
        alt="Funil com os cinco critérios de seleção das comunidades, que resulta na seleção preliminar de 83 "
            "comunidades e 5.810 domicílios."),
    COM("Explicar por que os municípios de baixo e de alto desempenho no IPDM ficam de fora. O Banco Mundial costuma "
        "perguntar pela exclusão de municípios mais vulneráveis."),
    P("A aplicação preliminar dos critérios indicou 83 comunidades, com 5.810 domicílios: a conta considera a média de "
      "70 domicílios por comunidade e 2,8 habitantes por domicílio, do Censo 2022. As áreas com maior concentração de "
      "domicílios rurais e os municípios consorciados ao CISPAR estão no mapa da {fig:mapa}. A lista final é confirmada "
      "pelo trabalho técnico-social (Ação 3.2.2.2) e pela viabilidade do poço (Etapa 2)."),
    COM("O Acordo de Empréstimo, item (j)(vii), pede a identificação das áreas rurais da Parte 3.2. Anexar a lista das "
        "83 comunidades selecionadas, com município e coordenadas, ou o mapa com a sua localização."),

    ITEM("3. Arranjo institucional e partes interessadas"),
    P("A ação é coordenada pelo IAT, por meio da DISAR, que planeja, contrata, fiscaliza e recebe os sistemas. Dentro do "
      "próprio IAT, a Diretoria de Licenciamento e Outorga emite a outorga de direito de uso da água e as licenças "
      "ambientais. As prefeituras apoiam a regularização das áreas e a articulação local, a entidade gestora definida "
      "na Ação 3.2.2.1 recebe e opera cada sistema, e a UGP acompanha a execução e consolida o reporte ao Banco "
      "Mundial."),
    BUL("**Coexecutor:** IDR-Paraná, na implementação local junto às comunidades;",
        "**Intervenientes:** prefeituras; entidades gestoras; empresas contratadas para projetos e obras; laboratórios "
        "contratados para as análises de potabilidade; empresa supervisora (Ação 3.2.2.7);",
        "**Público envolvido:** proprietários das áreas do poço, do reservatório e da rede; moradores das comunidades."),
    COM("O MOP de março atribui ao IDR-Paraná corresponsabilidade pelo abastecimento, e a nota técnica o inclui na "
        "implementação local, mas nenhum dos dois detalha o papel do instituto nesta ação. Detalhar."),
    P("Os beneficiários diretos são os moradores dos 5.810 domicílios ligados aos sistemas, cerca de 16,3 mil pessoas, "
      "selecionados pelos critérios do item 2. Os beneficiários indiretos são os municípios, que reduzem gastos com "
      "saúde, e os moradores das áreas próximas, que deixam de depender de fontes contaminadas."),

    ITEM("4. Processo de execução operacional"),
    P("A implantação de cada sistema segue seis etapas, cada uma na raia de quem a executa ({fig:raias-3223}). Duas "
      "premissas valem para todas: as comunidades atendidas são confirmadas pelo trabalho técnico-social, e o modelo de "
      "gestão é pactuado antes das obras. A saída de cada sistema é o Termo de Recebimento Definitivo (TRD), emitido "
      "pelo IAT depois do aceite da entidade gestora."),
    fig_raias(COD),

    ETAPA("4.1 Etapa 1: Estudos preliminares e regularização das áreas"),
    PL("Atividades:", "estudos de viabilidade técnica, social e ambiental; levantamento de campo geológico e "
       "hidrogeológico; verificação da titularidade e da situação fundiária das áreas do poço, do reservatório e das "
       "demais estruturas; formalização da doação, da cessão ou da servidão das áreas, com anuência do proprietário; "
       "anteprojeto e investigação social. A {fig:captacao} mostra a sequência das Etapas 1 a 3."),
    FIG("captacao", "f-captacao", "Captação subterrânea, projeto e licenciamento (Etapas 1 a 3)",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias para a DISAR, a área de licenças e outorga do IAT, o laboratório e a empresa "
            "contratada, com a decisão sobre a viabilidade do poço."),
    PL("Entradas:", "diagnóstico da comunidade (Ação 3.2.2.2); entidade gestora pactuada (Ação 3.2.2.1); Termo de "
       "Cooperação."),
    PL("Responsáveis:", "IAT (executa e aprova); prefeituras (executam a regularização das áreas públicas); "
       "proprietários (consultados)."),
    PL("Produto:", "áreas regularizadas e anteprojeto aprovado."),

    ETAPA("4.2 Etapa 2: Perfuração e outorga do poço"),
    PL("Atividades:", "locação do poço e projeto construtivo; anuência prévia de perfuração; perfuração, segundo as "
       "normas técnicas de projeto e construção de poços; teste de vazão; análises físico-químicas e bacteriológicas da "
       "água; outorga de direito de uso. Se a vazão ou a qualidade forem insuficientes, o IAT faz nova locação ou "
       "substitui a comunidade por outra que atenda aos critérios. O IAT tem equipes próprias de perfuração, com "
       "equipamentos e equipe técnica para mais de 150 poços por ano (IAT, 2026a)."),
    PL("Entradas:", "áreas regularizadas; estudo hidrogeológico."),
    PL("Responsáveis:", "equipe de perfuração do IAT ou empresa contratada (executa); laboratório contratado "
       "(análises); IAT (aprova e emite a outorga)."),
    PL("Produto:", "poço perfurado, testado e outorgado."),
    COM("A nota técnica prevê que os poços sejam perfurados pelas equipes do IAT; o MOP de março previa a contratação "
        "integrada do poço. Definir quem perfura."),

    ETAPA("4.3 Etapa 3: Contratação integrada, projetos e licenças"),
    PL("Atividades:", "contratação integrada, em que a mesma empresa elabora os projetos executivos e executa as obras; "
       "projetos básico e executivo da casa química, do reservatório, da parte eletromecânica, da rede e das ligações; "
       "aprovação dos projetos pelo IAT; estudos ambientais e sociais e obtenção das licenças. A obra só começa com a "
       "outorga e as licenças obtidas."),
    PL("Entradas:", "poço outorgado; vazão e qualidade da água; anteprojeto."),
    PL("Responsáveis:", "IAT (contrata, aprova os projetos e emite as licenças); empresa contratada (elabora os "
       "projetos); Banco Mundial (consultado, quando houver revisão prévia)."),
    PL("Produto:", "projetos aprovados e licenças emitidas."),
    COM("O MOP define “contratação integrada” como aquela em que o contratado elabora o projeto executivo e executa a "
        "obra, o que corresponde à contratação semi-integrada da Lei nº 14.133/2021 (art. 6º, XXXIII). Definir o regime "
        "e verificar a compatibilidade com o Regulamento de Aquisições do Banco Mundial."),

    ETAPA("4.4 Etapa 4: Execução das obras"),
    PL("Atividades:", "a obra é acompanhada em três níveis ({fig:obras}): o executor constrói conforme o projeto e "
       "instala um hidrômetro em cada ligação domiciliar; a supervisora (Ação 3.2.2.7) acompanha a execução e registra o "
       "andamento em relatórios mensais; e a fiscalização do IAT verifica a conformidade com o projeto e as normas. "
       "Havendo não conformidade, o executor corrige e a obra é verificada de novo. Estando tudo conforme, o IAT emite o "
       "atesto de recebimento, com os laudos de vistoria e o projeto *as built*."),
    FIG("obras", "f-obras", "Execução, supervisão e fiscalização das obras, por responsável",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias para a fiscalização do IAT, a empresa executora e a supervisora, com a decisão de "
            "conformidade e a correção das não conformidades."),
    PL("Entradas:", "projetos aprovados; outorga e licenças; ordem de serviço."),
    PL("Responsáveis:", "empresa contratada (executa); supervisora (acompanha); IAT (fiscaliza e aprova); prefeituras "
       "(consultadas)."),
    PL("Produto:", "sistema implantado, com atesto de recebimento, laudos de vistoria e projeto *as built*."),
    COM("No MOP de março, a quantidade de hidrômetros está como “XXX”. Pela meta de domicílios, são 5.810 hidrômetros, "
        "um por ligação. Confirmar."),

    ETAPA("4.5 Etapa 5: Pré-operação, capacitação e entrega"),
    PL("Atividades:", "pré-operação e testes de funcionamento; capacitação dos operadores locais, conforme o Plano de "
       "Operação e Manutenção; reunião técnica de entrega com a comunidade e a entidade gestora; aceite da entidade "
       "gestora; emissão do TRD ({fig:entrega})."),
    FIG("entrega", "f-entrega", "Transferência, operação e encerramento dos sistemas de abastecimento",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias para a empresa executora, o IAT e a entidade gestora, da pré-operação ao registro dos "
            "dados de operação no SIGARH e no GeoPR."),
    PL("Entradas:", "sistema implantado; entidade gestora constituída (Ação 3.2.2.1)."),
    PL("Responsáveis:", "empresa contratada (pré-operação e capacitação); entidade gestora (aceita o sistema); IAT "
       "(aprova e emite o TRD)."),
    PL("Produto:", "Termo de Recebimento Definitivo e operadores capacitados."),

    ETAPA("4.6 Etapa 6: Acompanhamento pós-implantação e encerramento"),
    PL("Atividades:", "suporte técnico pós-implantação; avaliação semestral de desempenho; acompanhamento da qualidade "
       "da água distribuída, conforme o padrão de potabilidade (BRASIL, 2021); registro dos dados no SIGARH e no "
       "GeoPR; relatório final e prestação de contas."),
    PL("Entradas:", "TRD; dados de operação informados pela entidade gestora."),
    PL("Responsáveis:", "IAT (executa); entidade gestora (informa os dados de operação); UGP (valida o relatório final)."),
    PL("Produto:", "relatórios semestrais de desempenho e relatório final."),

    ETAPA("4.7 Modalidade de execução"),
    P("O item de custo é o de sistemas coletivos de abastecimento de água: 83 sistemas a R$ 1,3 milhão, total de "
      "R$ 107,90 milhões, financiados pelo empréstimo do BIRD. Os projetos executivos e as obras são contratados por "
      "licitação, em contratação integrada, conforme o Caderno AQ; os ensaios laboratoriais de potabilidade também são "
      "licitados."),
    P("Os estudos preliminares, a regularização das áreas e a outorga são de execução direta do IAT. A perfuração pode "
      "ser feita diretamente pelas equipes do IAT ou incluída na contratação das obras."),
    COM("A nota técnica estima R$ 1,4 milhão por sistema; a planilha de custos (R$ 1,3 milhão) prevalece."),

    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3223} indica o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("IAT", ["R, A", "R, A", "A", "A", "A", "R"], "R, A"),
        ("Prefeituras", ["R", "I", "C", "C", "C", "I"], "I"),
        ("Empresas contratadas", ["–", "R", "R", "R", "R", "–"], "–"),
        ("Supervisora (Ação 3.2.2.7)", ["–", "–", "–", "R", "C", "–"], "–"),
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
    P("Os indicadores estão no {qua:ind-3223}. O indicador de pessoas atendidas com água gerida de forma segura conta o "
      "número acumulado de domicílios ligados aos sistemas, multiplicado por 2,8, com desagregação por sexo e para "
      "jovens de 15 a 24 anos. A água é considerada gerida de forma segura quando a fonte é melhorada, está no "
      "domicílio, fica disponível pelo menos 12 horas por dia e é livre de contaminação fecal e química prioritária."),
    indicadores(COD, [
        ["Sistemas implantados com Termo de Recebimento Definitivo", "sistemas", "0", "83", "Semestral; IAT"],
        ["Domicílios atendidos com sistema coletivo de água", "domicílios", "0", "5.810", "Anual; IAT e entidades gestoras"],
        ["Pessoas atendidas com água gerida de forma segura (parcela do indicador do Componente 3)",
         "pessoas", "0", "16.268", "Anual; IAT, com desagregação por sexo e jovens"],
        ["Análises de entrega conformes ao padrão de potabilidade", "% das análises", "–", "100", "Na entrega e semestral; laudos laboratoriais"],
    ]),
    P("Os critérios de aceite e as evidências de cada produto estão no {qua:aceite-3223}. A evidência de conclusão de "
      "cada sistema é o TRD; no encerramento, o relatório final é validado pela UGP e apresentado ao Banco Mundial."),
    aceite(COD, [
        ["Áreas regularizadas", "Titularidade comprovada; doação, cessão ou servidão formalizada",
         "Matrícula ou termo de cessão; anuência do proprietário", "IAT"],
        ["Poço perfurado", "Construído conforme o projeto construtivo e as normas técnicas",
         "Relatório de perfuração; laudo de vistoria; atesto de recebimento", "IAT"],
        ["Vazão e qualidade", "Vazão compatível com a demanda e água dentro do padrão de potabilidade",
         "Teste de vazão; laudos físico-químicos e bacteriológicos", "IAT"],
        ["Outorga", "Outorga de direito de uso emitida", "Ato de outorga", "IAT"],
        ["Projetos e licenças", "Projetos básico e executivo aprovados; licenças emitidas",
         "Parecer de aprovação; licenças", "IAT"],
        ["Sistema implantado", "Obra conforme projeto e normas; um hidrômetro por ligação",
         "Relatórios de supervisão e de fiscalização; laudos; *as built*", "IAT"],
        ["Operadores capacitados", "Capacitação conforme o Plano de Operação e Manutenção",
         "Listas de presença e certificados", "IAT"],
        ["Sistema entregue", "Testes aprovados, aceite da entidade gestora e abastecimento de pelo menos 12 horas por dia",
         "Termo de aceite; Termo de Recebimento Definitivo", "IAT"],
    ]),

    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("A ação tem obras de pequeno porte, dispersas pelo Estado. Os principais riscos são a contaminação do aquífero, os "
      "impactos temporários das obras (ruído, poeira, resíduos e erosão local), acidentes de trabalho, conflitos pela "
      "posse das áreas e pelo uso da água e a exclusão de famílias vulneráveis. O {qua:nas-3223} indica as NAS "
      "aplicáveis e as medidas."),
    P("A NAS 9 não se aplica ao Programa, e as medidas detalhadas estão no Caderno AS."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Obras de captação, reservação e distribuição em cada comunidade",
         "Triagem socioambiental de cada sistema; licenciamento; plano ambiental e social da obra (MGAS)"],
        ["NAS 2 – Condições de trabalho", "Equipes de perfuração e de obras",
         "Uso de EPI; treinamento de segurança; código de conduta (Procedimentos de Gestão de Mão de Obra)"],
        ["NAS 3 – Eficiência de recursos e prevenção da poluição", "Uso da água subterrânea; risco de contaminação do "
         "aquífero; resíduos e fluidos de perfuração", "Outorga e hidrometração; normas técnicas de perfuração e "
         "proteção sanitária do poço; Plano de Gerenciamento de Resíduos Sólidos"],
        ["NAS 4 – Saúde e segurança da comunidade", "Valas abertas, trânsito de máquinas e qualidade da água "
         "distribuída", "Sinalização e isolamento das valas; controle de horários e de poeira; análises de potabilidade "
         "na entrega e na operação"],
        ["NAS 5 – Aquisição de terras", "Áreas para poço, reservatório e rede", "Verificação documental da titularidade; "
         "doação, cessão ou servidão com anuência; sem reassentamento involuntário (Marco de Política de Reassentamento)"],
        ["NAS 6 – Biodiversidade", "Escolha das áreas das estruturas", "Triagem para evitar supressão de vegetação nativa "
         "e áreas de preservação permanente"],
        ["NAS 7 – Povos indígenas e comunidades tradicionais", "Comunidades tradicionais nas áreas selecionadas",
         "Consulta culturalmente adequada (MGAS e PEPI)"],
        ["NAS 8 – Patrimônio cultural", "Escavações para poço, reservatório e rede", "Procedimento de achados fortuitos"],
        ["NAS 10 – Engajamento das partes interessadas", "Moradores e proprietários afetados pelas obras",
         "Reuniões comunitárias; divulgação do Mecanismo de Queixas e Reclamações; resposta às queixas (PEPI e MQR)"],
    ]),

    ITEM("8. Cronograma"),
    P("Os estudos preliminares começam em 2027, de execução direta pelo IAT. A perfuração, os projetos e as licenças "
      "ocorrem de 2028 a 2032, e as obras e as entregas, de 2028 a 2033, no ritmo da planilha: 5 sistemas em 2028, 10 "
      "em 2029, 20 em 2030 e em 2031, 18 em 2032 e 10 em 2033 ({fig:crono-3223}). O acompanhamento pós-implantação "
      "começa com os primeiros sistemas entregues e segue até o encerramento."),
    fig_crono(COD),

    ITEM("9. Interfaces e dependências"),
    P("A ação depende da entidade gestora pactuada (Ação 3.2.2.1), do diagnóstico das comunidades (Ação 3.2.2.2), da "
      "supervisão das obras (Ação 3.2.2.7) e dos instrumentos de recursos hídricos do Subcomponente 1.1, como a outorga, "
      "o SIGARH e os dados de águas subterrâneas. Entrega as comunidades com água, que recebem o esgotamento sanitário "
      "(Ação 3.2.2.5), os sistemas prontos para a entrega à entidade gestora e o número de pessoas atendidas para o "
      "indicador do Componente 3 ({fig:interf-3223})."),
    fig_interf(COD),

    ITEM("10. Documentos complementares"),
    BUL("Termo de Referência e edital da contratação integrada de projetos e obras (a elaborar);",
        "Plano de Operação e Manutenção dos sistemas (a elaborar);",
        "Portaria GM/MS nº 888/2021, que altera o Anexo XX da Portaria de Consolidação GM/MS nº 5/2017 (padrão de "
        "potabilidade da água para consumo humano);",
        "ABNT NBR 12212:2017 e NBR 12244:2006 (projeto e construção de poço tubular) e demais normas ABNT de projeto de "
        "sistemas de abastecimento de água;",
        "Lei nº 9.433/1997 e Lei Estadual nº 12.726/1999 (outorga de direito de uso de recursos hídricos) e normas de "
        "licenciamento ambiental do IAT;",
        "Caderno AQ e Caderno AS;",
        "Notas técnicas de origem (IAT, 2026a; IAT, 2026b)."),
]
