from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM
from comum import matriz, metas, indicadores, aceite, nas, fig_ipo, fig_crono, fig_interf

COD = "3.2.2.1"

ELEMENTOS = [
    ACAO("Ação 3.2.2.1 – Implantação dos modelos de gestão"),

    # ------------------------------------------------------------ 1
    ITEM("1. Contextualização"),
    P("A ação implanta os modelos de gestão que vão operar e manter os sistemas de água e de esgoto da Atividade "
      "3.2.2 depois das obras. Seus objetivos são definir, com as prefeituras e as comunidades, o arranjo de gestão "
      "de cada sistema; constituir ou regularizar as associações de saneamento rural que assumirão a operação; "
      "instituir a tarifa que sustenta o serviço; e estruturar três unidades regionais de apoio técnico às "
      "associações (IAT, 2026a; IAT, 2026b)."),
    P("O problema a enfrentar é a falta de quem cuide dos sistemas. No Paraná ainda não há uma política de "
      "saneamento rural que estabeleça um modelo de gestão. As ações existentes são descentralizadas e concentradas no "
      "abastecimento de água: são executadas pela Sanepar, por serviços municipais, por iniciativas conjuntas do "
      "Estado e dos municípios e, em alguns casos, pelas próprias comunidades. A autogestão comunitária, comum no meio "
      "rural, costuma falhar por falta de capacidade técnica, financeira e institucional e de apoio do poder público, "
      "o que compromete a regularidade e a qualidade do serviço. A dispersão das comunidades e a limitação de pessoal "
      "e de recursos dos municípios agravam o quadro (BRASIL, 2019; IAT, 2026a)."),
    P("A ação responde pela sustentabilidade do que a atividade constrói. Sem uma entidade preparada para operar o "
      "sistema, cobrar a tarifa e fazer a manutenção, o investimento em poços, redes e soluções de esgoto se perde em "
      "poucos anos. Por isso, o modelo de gestão é pactuado antes das obras e acompanha os sistemas até a entrega. O "
      "resultado é medido pelo indicador do Componente 3 de associações de saneamento rural com modelo de gestão "
      "adotado."),
    PL("Inclui:", "a escolha e o enquadramento jurídico do modelo; a pactuação com os municípios, formalizada em Termo "
       "de Cooperação; a constituição ou a regularização das associações e a adesão das famílias; estatutos, manuais "
       "e cartilhas; a instituição da tarifa, com tarifa social; a estruturação das três unidades regionais de apoio, "
       "com equipe técnica, sede e veículo, geração de energia fotovoltaica e custeio de operação e manutenção; e o "
       "acompanhamento das entidades gestoras até o encerramento."),
    PL("Não inclui:", "as obras dos sistemas (Ações 3.2.2.3, 3.2.2.5 e 3.2.2.6), o trabalho técnico-social com as "
       "famílias (Ação 3.2.2.2) e a formulação da política estadual de saneamento rural (Atividade 3.2.1)."),
    PL("Valor previsto:", "R$ 6,90 milhões (empréstimo BIRD: R$ 6,90 milhões; contrapartida: R$ 0,00 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    # ------------------------------------------------------------ 2
    ITEM("2. Área de atuação"),
    P("A ação atua nas comunidades que recebem os sistemas coletivos de água do IAT, escolhidas pelos critérios "
      "descritos na Ação 3.2.2.3: comunidades ou conjuntos de comunidades com 70 ou mais domicílios ocupados, em "
      "municípios de médio baixo ou médio desempenho no IPDM, com prioridade para pedidos já encaminhados ao IAT e "
      "para associações que já operam sistemas. O número mínimo de domicílios é o que torna a gestão viável. A seleção "
      "preliminar indicou 83 comunidades, com 5.810 domicílios (IAT, 2026a). Os modelos de gestão também se aplicam às "
      "associações formadas pelo Programa Sanepar Rural (Ação 3.2.2.4)."),
    P("A {fig:mapa} é o mapa inicial das áreas em que a ação pode atuar. Ele mostra 2.571 locais em que os domicílios "
      "rurais estão a menos de 350 m uns dos outros, agrupados em nove classes conforme o número de domicílios, os "
      "limites das associações de municípios e os 112 municípios consorciados ao CISPAR. A presença do consórcio "
      "indica onde o arranjo intermunicipal tem base institucional, e as maiores concentrações de domicílios, na "
      "Região Metropolitana de Curitiba e no Centro-Sul e no Sudeste do Estado, indicam onde cabem as unidades "
      "regionais de apoio. A localização das três unidades será definida depois da seleção final das comunidades."),
    FIG("mapa", "f-mapa",
        "Áreas prioritárias, associações de municípios, CISPAR e concentração de domicílios rurais",
        "Fonte: IAT e IDR-Paraná (2025). Hidrografia: IAT (2020) e GeoPR (2025); limites político-administrativos: GeoPR (2025).",
        alt="Mapa do Paraná com as áreas prioritárias do PSH-PR, as associações de municípios, os municípios do CISPAR "
            "e os locais com concentração de domicílios rurais."),
    COM("O Acordo de Empréstimo, item (j)(vii), pede a identificação das áreas rurais da Parte 3.2. O mapa mostra o "
        "potencial, não as 83 comunidades selecionadas. Incluir a lista ou o mapa das comunidades e a localização das "
        "três unidades regionais."),

    # ------------------------------------------------------------ 3
    ITEM("3. Arranjo institucional e partes interessadas"),
    P("A ação é coordenada pelo IAT, por meio da Diretoria de Saneamento Ambiental e Recursos Hídricos (DISAR), que "
      "responde pela escolha do modelo, pela pactuação com os municípios, pelas contratações e pelo acompanhamento das "
      "entidades gestoras. A Secretaria de Estado das Cidades (SECID) valida a implantação do modelo e a instituição da "
      "tarifa. A UGP acompanha a execução e consolida o reporte ao Banco Mundial."),
    COM("Indicar a gerência do IAT responsável pela ação (instituição › diretoria › gerência)."),
    P("As partes interessadas são:"),
    BUL("**Coexecutores:** o IDR-Paraná, na mobilização social e na articulação local, e a Sanepar, nas associações "
        "formadas pelo Programa Sanepar Rural;",
        "**Intervenientes:** a SECID, que valida o modelo e a tarifa; as prefeituras, que participam da governança, "
        "assinam o Termo de Cooperação, aprovam a lei autorizativa quando necessária e apoiam as associações; os "
        "consórcios públicos intermunicipais, como o CISPAR, se for adotado o arranjo consorciado; e as empresas "
        "contratadas para a equipe técnica e a estrutura das unidades regionais;",
        "**Comunidades e associações de moradores:** participam da escolha do modelo, constituem a entidade gestora e "
        "operam os sistemas."),
    P("Os beneficiários diretos são as associações de saneamento rural e as famílias das comunidades atendidas pela "
      "Atividade 3.2.2, que passam a contar com operação regular, tarifa e suporte técnico. Os beneficiários indiretos "
      "são os municípios, que ganham um arranjo de gestão para o saneamento rural, e os moradores das bacias, "
      "beneficiados pela boa manutenção dos sistemas."),

    # ------------------------------------------------------------ 4
    ITEM("4. Processo de execução operacional"),
    P("A ação se organiza em seis etapas, da escolha do modelo ao encerramento do Termo de Cooperação "
      "({fig:ipo-3221}). As entradas são a lista preliminar de comunidades, o arcabouço legal dos arranjos de gestão, "
      "as diretrizes da política estadual (Atividade 3.2.1) e o cadastro e as adesões das famílias (Ação 3.2.2.2). As "
      "saídas são as associações regularizadas e em operação, com tarifa instituída, as três unidades regionais em "
      "funcionamento e o aceite formal dos sistemas pelas entidades gestoras. Duas regras orientam a sequência: o "
      "modelo é pactuado antes das obras, e nenhum sistema é entregue sem uma entidade preparada para operá-lo."),
    fig_ipo(COD),

    ETAPA("4.1 Etapa 1: Estudos preliminares e escolha do modelo"),
    PL("Atividades:", "o IAT seleciona os instrumentos de gestão, define os parceiros, os critérios e os indicadores, "
       "faz o enquadramento jurídico da proposta e define os meios de comunicação do modelo. Três alternativas estão em "
       "análise ({fig:alternativas}). Na primeira, a associação de moradores opera o sistema da sua localidade; como "
       "organização da sociedade civil, ela se sujeita ao Marco Regulatório das Organizações da Sociedade Civil (MROSC), "
       "e o uso da infraestrutura pública é formalizado por Acordo de Cooperação, assinado depois que o município aprova "
       "a lei autorizativa (BRASIL, 2014). Na segunda, as associações se filiam a uma central que lhes presta apoio "
       "técnico, administrativo e financeiro. É o modelo do Sistema Integrado de Saneamento Rural (SISAR) do Ceará, que "
       "em agosto de 2025 atendia mais de 1,13 milhão de pessoas, cerca de 56% da população rural do estado, em 174 "
       "municípios e 1.466 localidades (CEARÁ, 2025), e das Centrais de Associações Comunitárias da Bahia, que fizeram "
       "16.888 novas ligações de água e recuperaram outras 5.297 em 49 municípios (BAHIA, 2022). Na terceira, os "
       "municípios prestam o serviço de forma associada, por meio de um consórcio público (BRASIL, 2005)."),
    FIG("alternativas", "f-alternativas", "Alternativas de modelo de gestão e seu amparo legal",
        "Fonte: IAT (2026), com base em IAT (2026a).",
        alt="Quadro esquemático que compara a associação de moradores, a central de associações e o consórcio público "
            "quanto ao funcionamento, ao amparo legal, ao instrumento e às referências."),
    P("O consórcio é a alternativa preliminar apontada para o Paraná. Muitos municípios já integram consórcios, como "
      "os 112 consorciados ao CISPAR, e o objeto do consórcio existente pode ser ampliado para a água e o esgoto rurais "
      "por alteração contratual aprovada em assembleia e ratificada por lei de cada ente. O contrato de programa "
      "formaliza a prestação e as regras de tarifa; o contrato de rateio define a contribuição anual de cada município; "
      "e os poços, as redes e os reservatórios podem ser cedidos ao consórcio, voltando ao município ao final do "
      "contrato. O arranjo dá escala, compartilha a estrutura técnica e administrativa e mantém a gestão de um mandato "
      "para outro. Segundo a nota técnica do Componente 3, o Decreto nº 11.599/2023 e a Portaria nº 2.777/2025 dão "
      "respaldo aos arranjos associativos no novo marco do saneamento (IAT, 2026a)."),
    PL("Entradas:", "diretrizes da política estadual (Atividade 3.2.1), quando disponíveis; experiências de referência; "
       "legislação aplicável."),
    PL("Responsáveis:", "IAT (executa), com consulta ao IDR-Paraná e às prefeituras; a SECID valida o modelo."),
    PL("Produto:", "modelo de gestão definido, com enquadramento jurídico."),
    COM("O modelo de gestão ainda está em definição. Registrar aqui a alternativa escolhida e o parecer jurídico assim "
        "que forem aprovados."),

    ETAPA("4.2 Etapa 2: Pactuação com municípios e comunidades"),
    PL("Atividades:", "a pactuação começa pelo município e chega à comunidade ({fig:adesao}). O IAT define os "
       "critérios, seleciona as áreas e sensibiliza as prefeituras. O município formaliza a adesão e assina com o IAT o "
       "Termo de Cooperação, que registra as obrigações de cada parte até a entrega dos sistemas. Quando o arranjo "
       "envolve a cessão de bens públicos, o município aprova a lei autorizativa. Em seguida, o IAT procura a "
       "comunidade, que manifesta o interesse por meio de contratos de pré-adesão."),
    FIG("adesao", "f-adesao", "Seleção e adesão dos municípios e das comunidades, por responsável",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias para o IAT, o município e a comunidade, da definição dos critérios à pré-adesão da comunidade."),
    PL("Entradas:", "modelo de gestão definido (Etapa 1); lista preliminar de comunidades; minuta do Termo de Cooperação."),
    PL("Responsáveis:", "IAT e prefeituras (executam); IDR-Paraná e comunidades (consultados); o IAT aprova os termos."),
    PL("Produto:", "Termos de Cooperação assinados e contratos de pré-adesão."),

    ETAPA("4.3 Etapa 3: Constituição das entidades gestoras"),
    PL("Atividades:", "com a adesão da comunidade, o IAT apoia a constituição ou a regularização da associação de "
       "saneamento rural: prepara o estatuto, os manuais e as cartilhas, colhe a adesão de cada família e acompanha o "
       "registro da associação. A tarifa é definida em assembleia, com tarifa social para as famílias de baixa renda, e "
       "validada pela SECID. Esta etapa usa o cadastro e os termos de adesão do trabalho técnico-social (Ação 3.2.2.2) e "
       "termina antes do início da obra de cada sistema."),
    PL("Entradas:", "contratos de pré-adesão; cadastro e termos de adesão das famílias (Ação 3.2.2.2)."),
    PL("Responsáveis:", "IAT e associações (executam); prefeituras (consultadas); SECID (valida a tarifa)."),
    PL("Produto:", "associação regularizada, com tarifa instituída."),

    ETAPA("4.4 Etapa 4: Estruturação das unidades regionais de apoio"),
    PL("Atividades:", "cada uma das três unidades previstas na planilha de custos é uma estrutura regional de apoio às "
       "associações, com equipe técnica, sede e veículo, geração de energia fotovoltaica e custeio de operação e "
       "manutenção (IAT, 2026a). As unidades preparam os manuais de desempenho operacional, montam a estrutura de "
       "monitoramento e treinam os dirigentes e os operadores das associações. Uma unidade é implantada por ano, de 2028 "
       "a 2030, à medida que os primeiros sistemas ficam prontos."),
    PL("Entradas:", "modelo e localização das unidades definidos; associações constituídas."),
    PL("Responsáveis:", "IAT (executa e fiscaliza) e empresas contratadas (executam); associações (informadas)."),
    PL("Produto:", "unidade regional em funcionamento e pessoas capacitadas."),
    COM("A nota técnica do Componente 3 estima as três unidades em R$ 6,63 milhões, e a planilha de custos, em "
        "R$ 6,90 milhões; prevalece a planilha. Confirmar a composição de cada unidade e quem custeia a sua operação "
        "depois de 2030."),

    ETAPA("4.5 Etapa 5: Entrega dos sistemas e acompanhamento"),
    PL("Atividades:", "concluída a obra, a entrega é formalizada em reunião técnica com a comunidade e a entidade "
       "gestora, que confirma o recebimento por termo de aceite. A partir daí, a entidade opera e mantém o sistema com o "
       "suporte da unidade regional, e o IAT avalia o desempenho a cada semestre, com os dados registrados no SIGARH e "
       "no GeoPR. As entregas seguem o ritmo da Ação 3.2.2.3."),
    PL("Entradas:", "sistemas concluídos (Ações 3.2.2.3 e 3.2.2.5); associação regularizada."),
    PL("Responsáveis:", "IAT e entidade gestora (executam); a entidade gestora aceita o sistema; prefeituras (consultadas)."),
    PL("Produto:", "termos de aceite assinados e relatórios semestrais de desempenho."),

    ETAPA("4.6 Etapa 6: Encerramento"),
    PL("Atividades:", "consolidação dos resultados, relatório final, prestação de contas e encerramento do Termo de "
       "Cooperação com cada município."),
    PL("Entradas:", "relatórios semestrais; Termos de Recebimento Definitivo dos sistemas."),
    PL("Responsáveis:", "IAT (executa); UGP (valida)."),
    PL("Produto:", "relatório final e Termos de Cooperação encerrados."),

    ETAPA("4.7 Modalidade de execução"),
    P("O item de custo é a implantação do modelo de gestão: três unidades de R$ 2,3 milhões, total de R$ 6,90 milhões, "
      "financiados pelo empréstimo do BIRD. Na planilha, o produto aparece como “Sistema coletivo de abastecimento de "
      "água e individual de tratamento de efluentes”. As Etapas 1, 2, 3, 5 e 6 são de execução direta pela equipe do "
      "IAT, com Termo de Cooperação com cada município. A Etapa 4 é executada por licitação, conforme o Caderno de "
      "Aquisições: serviços de consultoria para a equipe técnica das unidades, aquisição de bens (veículos e sistemas "
      "fotovoltaicos) e serviços de adequação das sedes."),
    COM("Confirmar no Plano de Aquisições a divisão dos processos da Etapa 4 (consultoria, bens e serviços)."),

    # ------------------------------------------------------------ 5
    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3221} indica o papel de cada parte em cada etapa da ação."),
    matriz(COD, [
        ("IAT", ["R", "R, A", "R", "R, A", "R", "R"], "R"),
        ("SECID", ["A", "I", "A", "I", "I", "I"], "A"),
        ("IDR-Paraná", ["C", "C", "–", "–", "I", "I"], "I"),
        ("Prefeituras", ["C", "R", "C", "I", "C", "C"], "I"),
        ("Associações e comunidades", ["–", "C", "R", "I", "A", "I"], "R"),
        ("Empresas contratadas", ["–", "–", "–", "R", "–", "–"], "–"),
        ("UGP", ["I", "I", "I", "I", "I", "A"], "I"),
    ], "associações de saneamento rural com modelo de gestão adotado"),

    # ------------------------------------------------------------ 6
    ITEM("6. Metas, indicadores e comprovação"),
    P("A meta física da ação é a implantação das três unidades regionais de apoio, uma por ano, de 2028 a 2030 "
      "({qua:metas-3221}). As entidades gestoras, por sua vez, são constituídas à medida que os sistemas ficam prontos."),
    metas(COD, [("Unidades regionais do modelo de gestão implantadas", "unidades", {2: 1, 3: 1, 4: 1})],
          nota_extra="Na planilha, o produto aparece como “Sistema coletivo de abastecimento de água e individual de "
                     "tratamento de efluentes”."),
    P("O {qua:ind-3221} reúne os indicadores que acompanham o andamento e o resultado da ação. O principal é o "
      "indicador do Componente 3 de associações de saneamento rural com modelo de gestão adotado, medido pelo número "
      "acumulado de associações que assinaram acordos para adotar o modelo."),
    indicadores(COD, [
        ["Associações de saneamento rural com modelo de gestão adotado (indicador do Componente 3)",
         "associações (acumulado)", "0", "122", "Anual; IAT, Sanepar e cadastro das associações"],
        ["Unidades regionais de apoio em funcionamento", "unidades", "0", "3", "Anual; IAT"],
        ["Sistemas recebidos pela entidade gestora com termo de aceite", "sistemas", "0", "83", "Semestral; IAT"],
        ["Domicílios atendidos com tarifa instituída", "domicílios", "0", "5.810", "Anual; associações e IAT"],
    ]),
    COM("O MOP de março previa 122 associações até 2032, com períodos de 2027 a 2032. Atualizar as metas anuais para "
        "o período de 2027 a 2033 e explicar a composição do total (comunidades do IAT e associações do Sanepar Rural)."),
    P("Cada produto tem critério de aceite e evidência de comprovação definidos ({qua:aceite-3221}). A sustentabilidade "
      "do resultado é verificada depois da entrega: a entidade gestora precisa estar em operação, com tarifa cobrada, "
      "associação ativa e relatório semestral de desempenho."),
    aceite(COD, [
        ["Modelo de gestão definido", "Arranjo escolhido para cada conjunto de comunidades, com enquadramento jurídico",
         "Nota técnica do modelo e parecer jurídico", "SECID"],
        ["Termo de Cooperação", "Assinado pelo município, com obrigações, prazos e contrapartidas",
         "Termo assinado e publicado", "IAT"],
        ["Contratos de pré-adesão", "Assinados pelas famílias interessadas da comunidade",
         "Contratos assinados; número de associados", "IAT"],
        ["Associação regularizada", "Estatuto registrado e inscrição no CNPJ ativa",
         "Registro em cartório; comprovante do CNPJ", "IAT"],
        ["Tarifa instituída", "Aprovada em assembleia, com tarifa social para famílias de baixa renda",
         "Ata da assembleia; regulamento tarifário", "SECID"],
        ["Unidade regional em funcionamento", "Equipe contratada, sede e veículo em operação",
         "Contratos; termo de recebimento dos bens; relatório de atividades", "IAT"],
        ["Pessoas capacitadas", "Conteúdo e carga horária do plano de capacitação cumpridos",
         "Listas de presença e certificados", "IAT"],
        ["Sistema aceito pela entidade gestora", "Sistema recebido sem pendências", "Termo de aceite assinado", "IAT"],
        ["Desempenho acompanhado", "Relatório semestral entregue e aprovado",
         "Relatório com dados no SIGARH e no GeoPR", "UGP"],
    ]),

    # ------------------------------------------------------------ 7
    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("A ação é institucional e social; a adequação das sedes das unidades regionais é de pequeno porte. Os riscos "
      "estão na exclusão de famílias vulneráveis ou de comunidades tradicionais, em conflitos pelo uso da água e na "
      "sustentabilidade financeira das associações. O {qua:nas-3221} indica as NAS aplicáveis e as medidas. As NAS 3, "
      "5, 6 e 8 não se aplicam de forma específica, e a NAS 9 não se aplica ao Programa. Os instrumentos estão no "
      "Caderno Ambiental e Social do MOP."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Riscos sociais do modelo: exclusão de famílias, conflitos pelo uso "
         "da água e inadimplência", "Triagem socioambiental das comunidades; tarifa social; avaliação semestral de "
         "desempenho (MGAS)"],
        ["NAS 2 – Condições de trabalho", "Trabalhadores das empresas que compõem as equipes das unidades regionais",
         "Cláusulas trabalhistas nos contratos; Procedimentos de Gestão de Mão de Obra"],
        ["NAS 7 – Povos indígenas e comunidades tradicionais", "Comunidades tradicionais ou indígenas nas áreas "
         "selecionadas", "Identificação na seleção; consulta culturalmente adequada; arranjo compatível com a "
         "organização da comunidade (MGAS e PEPI)"],
        ["NAS 10 – Engajamento das partes interessadas", "Participação das prefeituras e das comunidades na escolha do "
         "modelo e da tarifa", "Reuniões em linguagem simples; consulta às comunidades; divulgação do Mecanismo de "
         "Queixas e Reclamações (PEPI e MQR)"],
    ]),

    # ------------------------------------------------------------ 8
    ITEM("8. Cronograma"),
    P("As etapas acompanham a implantação dos sistemas ({fig:crono-3221}). A escolha do modelo ocorre em 2027; a "
      "pactuação com municípios e comunidades, de 2027 a 2030; e a constituição das entidades gestoras, de 2028 a "
      "2032, sempre antes da obra de cada sistema. As unidades regionais são implantadas uma por ano, de 2028 a 2030. "
      "As entregas seguem o ritmo da Ação 3.2.2.3: 5 sistemas em 2028, 10 em 2029, 20 em 2030 e em 2031, 18 em 2032 e "
      "10 em 2033, quando a ação é encerrada."),
    fig_crono(COD),

    # ------------------------------------------------------------ 9
    ITEM("9. Interfaces e dependências"),
    P("A ação depende das diretrizes da política estadual (Atividade 3.2.1), do cadastro e das adesões do trabalho "
      "técnico-social (Ação 3.2.2.2) e dos sistemas concluídos (Ações 3.2.2.3 e 3.2.2.5). Em troca, entrega aos demais "
      "os municípios aderidos e a entidade gestora definida antes de cada obra, aplica o modelo às associações do "
      "Programa Sanepar Rural e alimenta o indicador de associações reportado à UGP ({fig:interf-3221})."),
    fig_interf(COD),

    # ------------------------------------------------------------ 10
    ITEM("10. Documentos complementares"),
    BUL("Termo de Cooperação entre o IAT e cada município (minuta a elaborar);",
        "Modelos de estatuto, manuais de desempenho operacional e cartilhas das associações (a elaborar);",
        "Termo de Referência da equipe técnica das unidades regionais (a elaborar);",
        "Lei nº 13.019/2014 (MROSC), Lei nº 11.107/2005 (consórcios públicos), Decreto nº 11.599/2023 e Portaria "
        "nº 2.777/2025;",
        "Programa Nacional de Saneamento Rural (BRASIL, 2019);",
        "Caderno Ambiental e Social do MOP (MGAS, PEPI e Mecanismo de Queixas e Reclamações) e Caderno de Aquisições;",
        "Notas técnicas de origem (IAT, 2026a; IAT, 2026b)."),
]
