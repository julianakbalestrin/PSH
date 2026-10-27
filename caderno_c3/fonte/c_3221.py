from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM, TAB
from comum import matriz, metas, indicadores, aceite, nas, fig_raias, fig_crono, fig_interf

COD = "3.2.2.1"

ELEMENTOS = [
    ACAO("Ação 3.2.2.1 – Implantação dos modelos de gestão"),

    # ------------------------------------------------------------ 1
    ITEM("1. Contextualização"),
    P("A ação estrutura os modelos de gestão responsáveis pela operação e pela manutenção dos sistemas de "
      "abastecimento de água e das soluções de esgotamento sanitário implantados na atividade. Os objetivos são: "
      "definir, com as prefeituras e as comunidades, o arranjo de gestão de cada sistema; constituir ou regularizar as "
      "associações de saneamento rural; instituir a tarifa; e estruturar três unidades regionais de apoio técnico às "
      "entidades gestoras (IAT, 2026a; IAT, 2026b)."),
    P("O Paraná não dispõe de política estadual de saneamento rural que estabeleça modelo de gestão para esses "
      "serviços. As iniciativas existentes são descentralizadas, concentram-se no abastecimento de água e são "
      "executadas pela Sanepar, por serviços municipais, por arranjos entre o Estado e os municípios e, em parte dos "
      "casos, pelas próprias comunidades (IAT, 2026a)."),
    P("A autogestão comunitária, predominante no meio rural, apresenta deficiências de capacidade técnica, financeira "
      "e institucional e carece de apoio do poder público, o que compromete a regularidade e a qualidade da prestação. "
      "A dispersão das comunidades e a limitação de pessoal e de recursos dos municípios agravam esse quadro "
      "(BRASIL, 2019; IAT, 2026a)."),
    P("A ação responde pela sustentabilidade dos investimentos da atividade. Sem entidade gestora habilitada a operar o "
      "sistema, cobrar a tarifa e executar a manutenção, os poços, as redes e as soluções de esgotamento sanitário "
      "tendem à deterioração em poucos anos; por esse motivo, o modelo de gestão é pactuado antes das obras e "
      "acompanha cada sistema até a entrega. A contribuição da ação é medida pelo indicador de associações de "
      "saneamento rural com modelo de gestão adotado."),
    PL("Inclui:", "a definição e o enquadramento jurídico do modelo; a pactuação com os municípios, formalizada em "
       "Termo de Cooperação; a constituição ou a regularização das associações e a adesão das famílias; a elaboração "
       "de estatutos, manuais e cartilhas; a instituição da tarifa, com tarifa social; a estruturação das três unidades "
       "regionais de apoio (equipe técnica, sede, veículo, geração de energia fotovoltaica e custeio de operação e "
       "manutenção); e o acompanhamento das entidades gestoras até o encerramento."),
    PL("Não inclui:", "as obras dos sistemas de abastecimento de água e das soluções de esgotamento sanitário, o "
       "trabalho técnico-social com as famílias e a formulação da política estadual de saneamento rural, objeto de "
       "atividade própria do subcomponente."),
    PL("Valor previsto:", "R$ 6,90 milhões (empréstimo BIRD: R$ 6,90 milhões; contrapartida: R$ 0,00 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    # ------------------------------------------------------------ 2
    ITEM("2. Área de atuação"),
    P("A ação abrange as comunidades atendidas pelos sistemas coletivos de abastecimento de água do IAT, selecionadas "
      "pelos seguintes critérios: 70 ou mais domicílios ocupados; município classificado como de médio baixo ou de "
      "médio desempenho no Índice Ipardes de Desempenho Municipal (IPDM); e prioridade para demandas já encaminhadas "
      "ao IAT e para associações que já operam sistemas. A seleção preliminar indicou 83 comunidades, com 5.810 "
      "domicílios, sendo o número mínimo de domicílios o requisito de viabilidade da gestão (IAT, 2026a). Os modelos "
      "de gestão aplicam-se também às associações constituídas no Programa Sanepar Rural."),
    P("A {fig:mapa} apresenta o mapa inicial das áreas potenciais de atuação: 2.571 aglomerados de domicílios rurais "
      "situados a menos de 350 m entre si, classificados em nove faixas de número de domicílios, com os limites das "
      "associações de municípios e os 112 municípios consorciados ao Consórcio Intermunicipal de Saneamento do Paraná "
      "(CISPAR). A presença do consórcio indica as regiões com base institucional para o arranjo intermunicipal, e as "
      "maiores concentrações de domicílios (Região Metropolitana de Curitiba, Centro-Sul e Sudeste do Estado) indicam "
      "as localizações candidatas às unidades regionais de apoio. A localização das três unidades é definida após a "
      "seleção final das comunidades."),
    FIG("mapa", "f-mapa",
        "Áreas prioritárias, associações de municípios, CISPAR e concentração de domicílios rurais",
        "Fonte: IAT e IDR-Paraná (2025). Hidrografia: IAT (2020) e GeoPR (2025); limites político-administrativos: GeoPR (2025).",
        alt="Mapa do Paraná com as áreas prioritárias do PSH-PR, as associações de municípios, os municípios do CISPAR "
            "e os aglomerados de domicílios rurais."),
    COM("O Acordo de Empréstimo, item (j)(vii) das definições, exige a identificação das áreas rurais da Parte 3.2 no "
        "MOP. O mapa representa o potencial de atuação, e não as 83 comunidades selecionadas; incluir a lista ou o mapa "
        "das comunidades e a localização das três unidades regionais."),
    COM("Os logos institucionais foram removidos do mapa, conforme o Guia de Identidade Visual (seção 2.6). Na versão "
        "final, refazer o mapa sobre a base cartográfica oficial (IAT/ITCG), com as áreas do Programa na cor do "
        "Caderno C3 e 40% de transparência (seção 5.4)."),

    # ------------------------------------------------------------ 3
    ITEM("3. Arranjo institucional e partes interessadas"),
    P("A ação é coordenada pelo IAT, por meio da Diretoria de Saneamento Ambiental e Recursos Hídricos (DISAR), "
      "responsável pela definição do modelo, pela pactuação com os municípios e pela constituição e pelo "
      "acompanhamento das entidades gestoras. A Secretaria de Estado das Cidades (SECID) valida o modelo de gestão e a "
      "tarifa. A UGP acompanha a execução e consolida o reporte ao Banco Mundial."),
    COM("Indicar a gerência do IAT responsável pela ação (instituição, diretoria e gerência)."),
    P("As partes interessadas são:"),
    BUL("**Coexecutores:** a Secretaria de Estado da Agricultura e do Abastecimento (SEAB), na mobilização social e "
        "na articulação local, e a Sanepar, nas associações constituídas no Programa Sanepar Rural;",
        "**Intervenientes:** a SECID, que valida o modelo e a tarifa; as prefeituras, que participam da governança, "
        "celebram o Termo de Cooperação, aprovam a lei autorizativa, quando exigida, e apoiam as associações; os "
        "consórcios públicos intermunicipais, como o CISPAR, na hipótese de arranjo consorciado; e as empresas "
        "contratadas para a equipe técnica e a estrutura das unidades regionais;",
        "**Comunidades e associações de moradores:** participam da definição do modelo, constituem a entidade gestora "
        "e operam os sistemas."),
    P("Os beneficiários diretos são as associações de saneamento rural e as famílias das comunidades atendidas, que "
      "passam a dispor de operação regular, tarifa instituída e suporte técnico. Os beneficiários indiretos são os "
      "municípios, que passam a contar com arranjo de gestão para o saneamento rural, e a população das bacias, "
      "beneficiada pela manutenção adequada dos sistemas."),

    # ------------------------------------------------------------ 4
    ITEM("4. Processo de execução operacional"),
    P("A ação compreende seis etapas, da definição do modelo ao encerramento dos Termos de Cooperação "
      "({fig:raias-3221}). Duas premissas orientam a sequência: o modelo de gestão é pactuado antes do início das "
      "obras, e nenhum sistema é entregue sem entidade gestora constituída e capacitada para operá-lo."),
    fig_raias(COD),

    ETAPA("4.1 Etapa 1: Estudos preliminares e definição do modelo"),
    PL("Atividades:", "seleção dos instrumentos de gestão; definição dos parceiros, dos critérios e dos indicadores; "
       "enquadramento jurídico da proposta; e definição da estratégia de comunicação do modelo. Estão em análise três "
       "alternativas de arranjo ({qua:alternativas})."),
    P("Na primeira alternativa, a associação de moradores opera o sistema da respectiva localidade. Na condição de "
      "organização da sociedade civil, a associação submete-se ao Marco Regulatório das Organizações da Sociedade "
      "Civil (MROSC), e o uso da infraestrutura pública é formalizado por Acordo de Cooperação, após a aprovação de lei "
      "municipal autorizativa (BRASIL, 2014)."),
    P("Na segunda, as associações filiam-se a uma central que lhes presta apoio técnico, administrativo e financeiro. "
      "Trata-se do modelo do Sistema Integrado de Saneamento Rural (SISAR) do Ceará, que, em agosto de 2025, atendia "
      "mais de 1,13 milhão de pessoas, cerca de 56% da população rural do estado, em 174 municípios e 1.466 "
      "localidades (CEARÁ, 2025). As Centrais de Associações Comunitárias da Bahia adotam arranjo equivalente e "
      "executaram 16.888 novas ligações de água e a recuperação de outras 5.297, em 49 municípios (BAHIA, 2022)."),
    TAB("alternativas", "Quadro", "Alternativas de modelo de gestão e respectivo amparo legal",
        ["Aspecto", "Associação de moradores", "Central de associações", "Consórcio público"],
        [["**Funcionamento**", "Moradores organizados operam o sistema da localidade, com apoio da prefeitura",
          "Associações filiadas a uma central, que presta apoio técnico, administrativo e financeiro",
          "Municípios consorciados prestam o serviço de forma associada"],
         ["**Amparo legal**", "MROSC (Lei nº 13.019/2014)",
          "MROSC; a nota técnica cita também o Decreto nº 11.599/2023 e a Portaria nº 2.777/2025 da Fundação Nacional "
          "de Saúde (Funasa)",
          "Lei dos Consórcios Públicos (Lei nº 11.107/2005) e Lei nº 11.445/2007"],
         ["**Instrumento**", "Acordo de Cooperação, após lei municipal que autoriza a cessão dos ativos",
          "Acordo de Cooperação com o poder público, após lei municipal autorizativa",
          "Alteração do contrato de consórcio; contrato de rateio; cessão de uso dos ativos"],
         ["**Referência**", "Associações de moradores que já operam sistemas no Paraná",
          "SISAR (CE): 1,13 milhão de pessoas em 1.466 localidades; Centrais de Associações (BA)",
          "CISPAR: 112 municípios consorciados no Paraná"]],
        [1700, 2457, 2457, 2457], "llll",
        "Fonte: IAT (2026), com base em IAT (2026a), CEARÁ (2025) e BAHIA (2022).",
        nota="Nota: em todas as alternativas, o modelo é definido com a prefeitura e a comunidade, mediante abordagem "
             "participativa, com tarifa social e capacitação dos operadores."),
    P("Na terceira, os municípios prestam o serviço de forma associada, por meio de consórcio público (BRASIL, 2005). "
      "Esta é a alternativa preliminarmente indicada para o Paraná, em razão da participação de grande parte dos "
      "municípios em consórcios, a exemplo dos 112 municípios consorciados ao CISPAR. O objeto do consórcio existente "
      "pode ser ampliado para o abastecimento de água e o esgotamento sanitário rurais, mediante alteração contratual "
      "aprovada em assembleia e ratificada por lei de cada ente."),
    P("O contrato de rateio define a contribuição anual de cada município, e os poços, as redes e os reservatórios "
      "podem ser cedidos ao consórcio, com reversão ao município ao término do contrato. O arranjo proporciona ganho de "
      "escala, compartilha a estrutura técnica e administrativa e confere continuidade à gestão entre mandatos. A nota "
      "técnica do componente cita, ainda, o Decreto nº 11.599/2023 e a Portaria Funasa nº 2.777/2025 como fundamento "
      "dos arranjos associativos no marco legal do saneamento atualizado pela Lei nº 14.026/2020 (IAT, 2026a)."),
    COM("Conferir o fundamento legal citado pela nota técnica. O Decreto nº 11.599/2023 trata da prestação "
        "regionalizada e do apoio técnico e financeiro da União; a Portaria Funasa nº 2.777/2025 consta no portal da "
        "Funasa como seleção de propostas de abastecimento de água, esgotamento sanitário e melhorias sanitárias "
        "domiciliares em áreas rurais, e não como diretriz de modelo de gestão. Ver a planilha de referências "
        "normativas."),
    COM("A nota técnica prevê contrato de programa no arranjo consorciado. A Lei nº 14.026/2020 alterou a Lei nº "
        "11.445/2007 e restringiu esse instrumento na prestação de serviços de saneamento; confirmar com a assessoria "
        "jurídica o instrumento adequado à prestação pelo consórcio."),
    PL("Entradas:", "diretrizes da política estadual de saneamento rural, quando disponíveis; experiências de "
       "referência; legislação aplicável."),
    PL("Responsáveis:", "IAT (executa), com consulta à SEAB e às prefeituras; SECID (valida o modelo)."),
    PL("Produto:", "modelo de gestão definido, com enquadramento jurídico."),
    COM("O modelo de gestão encontra-se em definição. Registrar neste item a alternativa adotada e o parecer jurídico, "
        "após a aprovação."),

    ETAPA("4.2 Etapa 2: Pactuação com municípios e comunidades"),
    PL("Atividades:", "a pactuação inicia-se pelo município e estende-se à comunidade ({fig:adesao}). O IAT define os "
       "critérios, seleciona as comunidades e sensibiliza as prefeituras; o município formaliza a adesão e celebra com "
       "o IAT o Termo de Cooperação, que estabelece as obrigações das partes até a entrega dos sistemas. Quando o "
       "arranjo envolve cessão de bens públicos, o município aprova a lei autorizativa; em seguida, o IAT contata a "
       "comunidade, que manifesta o interesse por meio de contrato de pré-adesão."),
    FIG("adesao", "f-adesao", "Seleção e adesão dos municípios e das comunidades, por responsável",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias do IAT, dos municípios e das comunidades, da seleção das comunidades à pré-adesão, "
            "com a decisão sobre a lei autorizativa."),
    PL("Entradas:", "modelo de gestão definido (Etapa 1); lista preliminar de comunidades; minuta do Termo de "
       "Cooperação."),
    PL("Responsáveis:", "IAT e prefeituras (executam); SEAB e comunidades (consultadas); IAT (aprova os termos)."),
    PL("Produto:", "Termos de Cooperação assinados e contratos de pré-adesão."),

    ETAPA("4.3 Etapa 3: Constituição das entidades gestoras"),
    PL("Atividades:", "após a adesão da comunidade, o IAT apoia a constituição ou a regularização da associação de "
       "saneamento rural: elabora o estatuto, os manuais e as cartilhas, formaliza a adesão de cada família e acompanha "
       "o registro da associação. A tarifa é aprovada em assembleia, com tarifa social para as famílias de baixa "
       "renda, e validada pela SECID. A etapa utiliza o cadastro e os termos de adesão do trabalho técnico-social e é "
       "concluída antes do início da obra de cada sistema."),
    PL("Entradas:", "contratos de pré-adesão; cadastro e termos de adesão das famílias (trabalho técnico-social)."),
    PL("Responsáveis:", "IAT e associações (executam); prefeituras (consultadas); SECID (valida a tarifa)."),
    PL("Produto:", "associação regularizada, com tarifa instituída."),

    ETAPA("4.4 Etapa 4: Estruturação das unidades regionais de apoio"),
    PL("Atividades:", "cada uma das três unidades previstas na planilha de custos constitui estrutura regional de apoio "
       "às associações, com equipe técnica, sede, veículo, geração de energia fotovoltaica e custeio de operação e "
       "manutenção (IAT, 2026a). As unidades elaboram os manuais de desempenho operacional, estruturam o monitoramento "
       "e capacitam os dirigentes e os operadores das associações. Implanta-se uma unidade por ano, de 2028 a 2030, "
       "conforme a entrada em operação dos primeiros sistemas."),
    PL("Entradas:", "modelo e localização das unidades definidos; associações constituídas."),
    PL("Responsáveis:", "IAT (executa e aprova) e empresas contratadas (executam); associações (informadas)."),
    PL("Produto:", "unidade regional em funcionamento e pessoal capacitado."),
    COM("A nota técnica do componente estima as três unidades em R$ 6,63 milhões, e a planilha de custos, em "
        "R$ 6,90 milhões; prevalece a planilha. Confirmar a composição de cada unidade e a fonte de custeio da operação "
        "após 2030."),

    ETAPA("4.5 Etapa 5: Entrega dos sistemas e acompanhamento"),
    PL("Atividades:", "concluída a obra, a entrega é formalizada em reunião técnica com a comunidade e a entidade "
       "gestora, que atesta o recebimento por termo de aceite. A partir da entrega, a entidade gestora opera e mantém o "
       "sistema com suporte da unidade regional, e o IAT avalia o desempenho semestralmente, com base nos dados "
       "registrados no Sistema de Gestão Ambiental e de Recursos Hídricos (SIGARH) e na plataforma GeoPR. As entregas acompanham o cronograma de implantação dos sistemas de "
       "abastecimento."),
    PL("Entradas:", "sistemas de abastecimento de água e soluções de esgotamento sanitário concluídos; associação "
       "regularizada."),
    PL("Responsáveis:", "IAT e entidade gestora (executam); entidade gestora (aceita o sistema); prefeituras "
       "(consultadas)."),
    PL("Produto:", "termos de aceite assinados e relatórios semestrais de desempenho."),

    ETAPA("4.6 Etapa 6: Encerramento"),
    PL("Atividades:", "consolidação dos resultados, relatório final, prestação de contas e encerramento do Termo de "
       "Cooperação com cada município."),
    PL("Entradas:", "relatórios semestrais; Termos de Recebimento Definitivo dos sistemas."),
    PL("Responsáveis:", "IAT (executa); UGP (valida)."),
    PL("Produto:", "relatório final e Termos de Cooperação encerrados."),

    ETAPA("4.7 Modalidade de execução"),
    P("O item de custo é a implantação do modelo de gestão: três unidades de R$ 2,3 milhões, no total de R$ 6,90 "
      "milhões, com recursos do empréstimo do BIRD. Na planilha, o produto consta como “Sistema coletivo de "
      "abastecimento de água e individual de tratamento de efluentes”."),
    P("As Etapas 1, 2, 3, 5 e 6 são executadas diretamente pela equipe do IAT, com Termo de Cooperação com cada "
      "município. A Etapa 4 é executada mediante licitação, conforme o Caderno AQ: serviços de consultoria para a "
      "equipe técnica das unidades, aquisição de bens (veículos e sistemas fotovoltaicos) e serviços de adequação das "
      "sedes."),
    COM("Confirmar no Plano de Aquisições a divisão dos processos da Etapa 4 (consultoria, bens e serviços)."),
    COM("Completar as remissões aos cadernos transversais com a seção correspondente (por exemplo, “Caderno AQ, "
        "seção 4”), conforme o Guia de Identidade Visual (seção 2.5), quando a numeração desses cadernos estiver "
        "definida."),

    # ------------------------------------------------------------ 5
    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3221} apresenta o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("IAT", ["R", "R, A", "R", "R, A", "R", "R"], "R"),
        ("SECID", ["A", "I", "A", "I", "I", "I"], "A"),
        ("SEAB", ["C", "C", "–", "–", "I", "I"], "I"),
        ("Prefeituras", ["C", "R", "C", "I", "C", "C"], "I"),
        ("Associações e comunidades", ["–", "C", "R", "I", "A", "I"], "R"),
        ("Empresas contratadas", ["–", "–", "–", "R", "–", "–"], "–"),
        ("UGP", ["I", "I", "I", "I", "I", "A"], "I"),
    ], "associações de saneamento rural com modelo de gestão adotado"),

    # ------------------------------------------------------------ 6
    ITEM("6. Metas, indicadores e comprovação"),
    P("A meta física da ação é a implantação de três unidades regionais de apoio, uma por ano, de 2028 a 2030 "
      "({qua:metas-3221}). As entidades gestoras são constituídas à medida que os sistemas são concluídos."),
    metas(COD, [("Unidades regionais do modelo de gestão implantadas", "unidades", {2: 1, 3: 1, 4: 1})],
          nota_extra="Na planilha, o produto consta como “Sistema coletivo de abastecimento de água e individual de "
                     "tratamento de efluentes”."),
    P("O {qua:ind-3221} reúne os indicadores de andamento e de resultado da ação. O principal é o indicador de "
      "associações de saneamento rural com modelo de gestão adotado, medido pelo número acumulado de associações que "
      "formalizaram a adoção do modelo."),
    indicadores(COD, [
        ["Associações de saneamento rural com modelo de gestão adotado (indicador do componente)",
         "associações (acumulado)", "0", "122", "Anual; IAT, Sanepar e cadastro das associações"],
        ["Unidades regionais de apoio em funcionamento", "unidades", "0", "3", "Anual; IAT"],
        ["Sistemas recebidos pela entidade gestora com termo de aceite", "sistemas", "0", "83", "Semestral; IAT"],
        ["Domicílios atendidos com tarifa instituída", "domicílios", "0", "5.810", "Anual; associações e IAT"],
    ]),
    COM("O MOP de março previa 122 associações até 2032, no período de 2027 a 2032. Atualizar as metas anuais para o "
        "período de 2027 a 2033 e explicitar a composição do total (comunidades atendidas pelo IAT e associações do "
        "Programa Sanepar Rural)."),
    P("Os critérios de aceite e as evidências de comprovação de cada produto constam do {qua:aceite-3221}. A "
      "sustentabilidade do resultado é verificada após a entrega: a entidade gestora deve estar em operação, com "
      "tarifa cobrada, associação ativa e relatório semestral de desempenho."),
    aceite(COD, [
        ["Modelo de gestão definido", "Arranjo definido para cada conjunto de comunidades, com enquadramento jurídico",
         "Nota técnica do modelo e parecer jurídico", "SECID"],
        ["Termo de Cooperação", "Assinado pelo município, com obrigações, prazos e contrapartidas",
         "Termo assinado e publicado", "IAT"],
        ["Contratos de pré-adesão", "Assinados pelas famílias interessadas da comunidade",
         "Contratos assinados; número de associados", "IAT"],
        ["Associação regularizada", "Estatuto registrado e inscrição ativa no Cadastro Nacional da Pessoa Jurídica (CNPJ)",
         "Registro em cartório; comprovante de inscrição no CNPJ", "IAT"],
        ["Tarifa instituída", "Aprovada em assembleia, com tarifa social para famílias de baixa renda",
         "Ata da assembleia; regulamento tarifário", "SECID"],
        ["Unidade regional em funcionamento", "Equipe contratada, sede e veículo em operação",
         "Contratos; termo de recebimento dos bens; relatório de atividades", "IAT"],
        ["Pessoal capacitado", "Conteúdo e carga horária do plano de capacitação cumpridos",
         "Listas de presença e certificados", "IAT"],
        ["Sistema aceito pela entidade gestora", "Sistema recebido sem pendências", "Termo de aceite assinado", "IAT"],
        ["Desempenho acompanhado", "Relatório semestral entregue e aprovado",
         "Relatório com dados registrados no SIGARH e no GeoPR", "UGP"],
    ]),

    # ------------------------------------------------------------ 7
    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("A ação tem natureza institucional e social, e as intervenções físicas restringem-se à adequação das sedes das "
      "unidades regionais, de pequeno porte. Os riscos concentram-se na exclusão de famílias vulneráveis ou de "
      "comunidades tradicionais, nos conflitos pelo uso da água e na sustentabilidade financeira das associações. O "
      "{qua:nas-3221} indica as NAS aplicáveis e as respectivas medidas."),
    P("As NAS 3, 5, 6 e 8 não se aplicam de forma específica à ação, e a NAS 9 não se aplica ao Programa. Os "
      "instrumentos de gestão ambiental e social (Marco de Gestão Ambiental e Social – MGAS, Plano de Engajamento das "
      "Partes Interessadas – PEPI e Mecanismo de Queixas e Reclamações – MQR) constam do Caderno AS."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Riscos sociais do modelo: exclusão de famílias, conflitos pelo uso "
         "da água e inadimplência", "Triagem socioambiental das comunidades; tarifa social; avaliação semestral de "
         "desempenho (MGAS)"],
        ["NAS 2 – Condições de trabalho", "Trabalhadores das empresas que compõem as equipes das unidades regionais",
         "Cláusulas trabalhistas nos contratos; Procedimentos de Gestão de Mão de Obra"],
        ["NAS 7 – Povos indígenas e comunidades tradicionais", "Comunidades tradicionais ou indígenas nas áreas "
         "selecionadas", "Identificação na seleção; consulta culturalmente adequada; arranjo compatível com a "
         "organização da comunidade (MGAS e PEPI)"],
        ["NAS 10 – Engajamento das partes interessadas", "Participação das prefeituras e das comunidades na definição "
         "do modelo e da tarifa", "Reuniões com linguagem acessível; consulta às comunidades; divulgação do Mecanismo "
         "de Queixas e Reclamações (PEPI e MQR)"],
    ]),

    # ------------------------------------------------------------ 8
    ITEM("8. Cronograma"),
    P("As etapas acompanham a implantação dos sistemas ({fig:crono-3221}). A definição do modelo ocorre em 2027; a "
      "pactuação, de 2027 a 2030; a constituição das entidades gestoras, de 2028 a 2032, sempre antes da obra de cada "
      "sistema; e a estruturação das unidades regionais, uma por ano, de 2028 a 2030. As entregas seguem o cronograma "
      "de implantação dos sistemas de abastecimento (5 sistemas em 2028, 10 em 2029, 20 em 2030 e em 2031, 18 em 2032 "
      "e 10 em 2033), e a ação é encerrada em 2033."),
    fig_crono(COD),

    # ------------------------------------------------------------ 9
    ITEM("9. Interfaces e dependências"),
    P("A ação depende das diretrizes da política estadual de saneamento rural, do cadastro e das adesões do trabalho "
      "técnico-social e da conclusão dos sistemas de abastecimento de água e das soluções de esgotamento sanitário. Em "
      "contrapartida, fornece às demais ações os municípios aderidos e a entidade gestora definida antes de cada obra, "
      "aplica o modelo às associações do Programa Sanepar Rural e alimenta o indicador de associações reportado à UGP "
      "({fig:interf-3221})."),
    fig_interf(COD),

    # ------------------------------------------------------------ 10
    ITEM("10. Documentos complementares"),
    BUL("Termo de Cooperação entre o IAT e cada município (minuta a elaborar);",
        "Modelos de estatuto, manuais de desempenho operacional e cartilhas das associações (a elaborar);",
        "Termo de Referência da equipe técnica das unidades regionais (a elaborar);",
        "Lei nº 13.019/2014 (MROSC), Lei nº 11.107/2005 (consórcios públicos), Lei nº 11.445/2007, com a redação da "
        "Lei nº 14.026/2020 (marco legal do saneamento), e Decreto nº 11.599/2023;",
        "Programa Nacional de Saneamento Rural (BRASIL, 2019);",
        "Caderno AS (MGAS, PEPI e Mecanismo de Queixas e Reclamações) e Caderno AQ;",
        "Notas técnicas de origem (IAT, 2026a; IAT, 2026b)."),
]
