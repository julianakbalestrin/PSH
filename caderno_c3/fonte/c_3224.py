from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM
from comum import matriz, metas, indicadores, aceite, nas, fig_ipo, fig_crono, fig_interf

COD = "3.2.2.4"

ELEMENTOS = [
    ACAO("Ação 3.2.2.4 – Programa Sanepar Rural"),

    ITEM("1. Contextualização"),
    P("A ação implanta 222 sistemas coletivos de abastecimento de água em comunidades rurais de municípios que têm "
      "Contrato de Concessão ou de Programa em vigor com a Sanepar, entre 2027 e 2031. A Sanepar elabora os estudos e "
      "os projetos, presta apoio técnico, ambiental e socioeconômico às comunidades e fornece treinamento, materiais "
      "hidráulicos e equipamentos; o município executa as obras; e a comunidade forma a associação de moradores que "
      "opera o sistema (IAT, 2026b; SANEPAR, [s.d.])."),
    P("Mesmo nos municípios atendidos pela Sanepar, as comunidades rurais ficam fora das redes urbanas e dependem de "
      "nascentes e poços rasos, sujeitos à contaminação e às estiagens. O Programa Sanepar Rural leva a essas "
      "comunidades sistemas coletivos com água tratada, aproveitando a capacidade técnica da companhia e a estrutura de "
      "gestão local das associações."),
    P("A ação é a maior parcela do indicador do Componente 3 de pessoas atendidas com água gerida de forma segura: "
      "cerca de 43,5 mil das 59.780 pessoas previstas. É também a contrapartida do Estado na Atividade 3.2.2: "
      "R$ 67,15 milhões, cerca de US$ 12,3 milhões ao câmbio de R$ 5,46 do PAD, aplicados com recursos próprios da "
      "Sanepar (PARANÁ, 2026)."),
    PL("Inclui:", "o levantamento técnico e o estudo de engenharia; o Termo de Compromisso e Responsabilidade ao "
       "Contrato de Concessão ou de Programa; os projetos de engenharia dos sistemas; o fornecimento de materiais "
       "hidráulicos e o apoio técnico às obras municipais; a mobilização e a organização comunitária; o treinamento e "
       "a educação ambiental; e o monitoramento e o suporte pós-obra."),
    PL("Não inclui:", "os sistemas implantados pelo IAT (Ação 3.2.2.3) nem recursos do empréstimo do BIRD."),
    PL("Valor previsto:", "R$ 67,15 milhões (empréstimo BIRD: R$ 0,00 milhões; contrapartida: R$ 67,15 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    ITEM("2. Área de atuação"),
    P("A ação abrange os municípios com Contrato de Concessão ou de Programa em vigor com a Sanepar, em todo o Estado. "
      "As comunidades atendidas são escolhidas pelos critérios do manual do Programa Sanepar Rural, a partir da demanda "
      "das comunidades e dos municípios e da viabilidade técnica do sistema."),
    COM("O Acordo de Empréstimo, item (j)(vii), pede a identificação das áreas rurais da Parte 3.2. Solicitar à Sanepar "
        "a lista dos municípios e das comunidades atendidas, com os critérios de priorização do manual do programa."),

    ITEM("3. Arranjo institucional e partes interessadas"),
    P("A Sanepar é a executora da ação, com a sua estrutura técnica e os recursos de contrapartida. Os municípios "
      "assinam o Termo de Compromisso e Responsabilidade e executam as obras. As comunidades formam as associações de "
      "moradores e recebem o treinamento. O IAT acompanha a interface com o modelo de gestão (Ação 3.2.2.1) e com a "
      "outorga de uso da água, e a UGP consolida a comprovação da contrapartida e o reporte ao Banco Mundial."),
    COM("Indicar a diretoria e a gerência da Sanepar responsáveis pelo Programa Sanepar Rural."),
    BUL("**Executor:** Sanepar;",
        "**Intervenientes:** municípios; IAT (modelo de gestão e outorga); UGP;",
        "**Público envolvido:** comunidades rurais e associações de moradores."),
    P("Os beneficiários diretos são os moradores das comunidades atendidas pelos 222 sistemas, cerca de 43,5 mil "
      "pessoas. Os beneficiários indiretos são os municípios e os serviços de saúde, com a redução das doenças de "
      "veiculação hídrica."),

    ITEM("4. Processo de execução operacional"),
    P("As atividades seguem o manual do Programa Sanepar Rural ({fig:ipo-3224}). Em cada comunidade, a Sanepar faz o "
      "levantamento técnico e o projeto, formaliza a parceria com o município e fornece os materiais; o município executa "
      "a obra com o apoio técnico da companhia; e a comunidade forma a associação e recebe o treinamento. Após a obra, a "
      "Sanepar acompanha a qualidade da água e dá suporte às associações ({fig:sanepar})."),
    fig_ipo(COD),
    FIG("sanepar", "f-sanepar", "Programa Sanepar Rural, por responsável",
        "Fonte: IAT (2026), com base em IAT (2026b) e SANEPAR ([s.d.]).",
        alt="Fluxograma em raias para a Sanepar, o município e a comunidade, do estudo técnico ao suporte pós-obra."),

    ETAPA("4.1 Etapa 1: Levantamento técnico e estudo de engenharia"),
    PL("Atividades:", "levantamento das condições da comunidade e estudo técnico de engenharia do sistema."),
    PL("Entradas:", "demanda da comunidade e do município; critérios do manual do programa."),
    PL("Responsáveis:", "Sanepar (executa e aprova); município (consultado)."),
    PL("Produto:", "estudo técnico da comunidade."),

    ETAPA("4.2 Etapa 2: Termo de Compromisso com o município"),
    PL("Atividades:", "formalização da parceria por Termo de Compromisso e Responsabilidade ao Contrato de Concessão "
       "ou de Programa, com as obrigações de cada parte."),
    PL("Entradas:", "estudo técnico; Contrato de Concessão ou de Programa vigente."),
    PL("Responsáveis:", "Sanepar e município (executam); a Sanepar aprova."),
    PL("Produto:", "Termo de Compromisso e Responsabilidade assinado."),

    ETAPA("4.3 Etapa 3: Projetos de engenharia"),
    PL("Atividades:", "elaboração do projeto de engenharia do sistema de abastecimento de água."),
    PL("Entradas:", "estudo técnico; Termo de Compromisso."),
    PL("Responsáveis:", "Sanepar (executa e aprova); município (informado)."),
    PL("Produto:", "projeto do sistema."),

    ETAPA("4.4 Etapa 4: Obras, com materiais e apoio da Sanepar"),
    PL("Atividades:", "fornecimento dos materiais hidráulicos pela Sanepar; execução das obras pelo município, "
       "diretamente ou por contratação própria, com o apoio técnico da companhia."),
    PL("Entradas:", "projeto aprovado; materiais; outorga e licenças, quando exigidas."),
    PL("Responsáveis:", "município (executa a obra); Sanepar (fornece materiais, apoia e aprova a obra)."),
    PL("Produto:", "sistema implantado."),

    ETAPA("4.5 Etapa 5: Organização comunitária e treinamento"),
    PL("Atividades:", "apoio à formação da associação de moradores; treinamento em uso racional da água, higiene e "
       "manutenção preventiva; educação ambiental."),
    PL("Entradas:", "comunidade mobilizada; modelo de gestão (Ação 3.2.2.1)."),
    PL("Responsáveis:", "Sanepar (executa e aprova); comunidade (executa); IAT (consultado sobre o modelo de gestão)."),
    PL("Produto:", "associação formada e treinada."),

    ETAPA("4.6 Etapa 6: Monitoramento e suporte pós-obra"),
    PL("Atividades:", "acompanhamento pós-obra da qualidade da água e suporte operacional às associações; relatório "
       "técnico de cada sistema; reporte anual à UGP dos sistemas implantados, das pessoas atendidas e dos valores "
       "aplicados."),
    PL("Entradas:", "sistema implantado; associação formada."),
    PL("Responsáveis:", "Sanepar (executa e aprova o relatório técnico); UGP (informada)."),
    PL("Produto:", "relatório técnico aprovado."),

    ETAPA("4.7 Modalidade de execução"),
    P("O item de custo é o de sistemas coletivos de abastecimento de água, com recursos de contrapartida: 222 sistemas "
      "a R$ 302.464,42, em média, total de R$ 67,15 milhões, integralmente com recursos próprios da Sanepar. A execução "
      "é por convênio, formalizado em Termo de Compromisso e Responsabilidade entre a Sanepar e cada município, conforme "
      "o manual do programa. As aquisições da Sanepar seguem o seu Regulamento de Licitações e Contratos, e as obras "
      "contratadas pelos municípios, a legislação de licitações. A Sanepar comprova à UGP os valores aplicados e os "
      "sistemas implantados, para registro da contrapartida."),
    COM("Confirmar com a UGP e o Banco Mundial se as aquisições e as obras financiadas com contrapartida seguem as "
        "regras da Sanepar e dos municípios e quais requisitos do Programa se aplicam a elas."),

    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3224} indica o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("Sanepar", ["R, A", "R, A", "R, A", "A", "R, A", "R, A"], "R, A"),
        ("Municípios", ["C", "R", "I", "R", "C", "I"], "I"),
        ("Comunidades e associações", ["C", "–", "–", "I", "R", "C"], "R"),
        ("IAT", ["–", "–", "–", "–", "C", "I"], "I"),
        ("UGP", ["–", "–", "–", "–", "–", "I"], "I"),
    ], "sistemas implantados e pessoas atendidas"),

    ITEM("6. Metas, indicadores e comprovação"),
    P("A meta é implantar 222 sistemas de 2027 a 2031 ({qua:metas-3224})."),
    metas(COD, [
        ("Sistemas coletivos de abastecimento de água", "sistemas", {1: 45, 2: 41, 3: 42, 4: 43, 5: 51}),
        ("Pessoas atendidas", "pessoas", {1: 8820, 2: 8036, 3: 8232, 4: 8428, 5: 9996}),
    ], nota_extra="Pessoas estimadas com 70 domicílios por sistema e 2,8 pessoas por domicílio, como no indicador do "
                  "Componente 3."),
    P("Os indicadores estão no {qua:ind-3224}. A Sanepar informa à UGP, a cada ano, os sistemas implantados, as pessoas "
      "atendidas, com desagregação por sexo e para jovens de 15 a 24 anos, e os valores de contrapartida aplicados."),
    indicadores(COD, [
        ["Sistemas implantados pelo Programa Sanepar Rural", "sistemas", "0", "222", "Anual; Sanepar"],
        ["Pessoas atendidas com água gerida de forma segura (parcela do indicador do Componente 3)",
         "pessoas", "0", "43.500", "Anual; Sanepar, com desagregação por sexo e jovens"],
        ["Contrapartida aplicada", "R$ milhões", "0", "67,15", "Anual; Sanepar e UGP"],
    ]),
    COM("O MOP de março atribuía ao Sanepar Rural a meta total do indicador (59.780 pessoas), que inclui os sistemas "
        "do IAT. A parcela da Sanepar é de cerca de 43.500 pessoas. Confirmar com a Sanepar e citar o manual do programa "
        "com título, versão e data."),
    P("Os critérios de aceite e as evidências de cada produto estão no {qua:aceite-3224}. A evidência de conclusão de "
      "cada sistema é o relatório técnico aprovado pela Sanepar."),
    aceite(COD, [
        ["Termo de Compromisso", "Assinado pela Sanepar e pelo município", "Termo assinado", "Sanepar"],
        ["Projeto do sistema", "Aprovado conforme as normas da Sanepar", "Projeto aprovado", "Sanepar"],
        ["Sistema implantado", "Obra concluída e em operação, com água dentro do padrão de potabilidade",
         "Relatório técnico aprovado; laudos de qualidade da água", "Sanepar"],
        ["Associação treinada", "Associação constituída e treinada em operação e manutenção",
         "Registro da associação; listas de presença", "Sanepar"],
        ["Contrapartida comprovada", "Valores aplicados registrados por sistema",
         "Relatório financeiro da Sanepar", "UGP"],
    ]),

    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("Os riscos são semelhantes aos dos sistemas do IAT: impactos temporários das obras, segurança dos trabalhadores e "
      "da comunidade, uso das áreas das estruturas, qualidade da água e participação das comunidades. Por integrar o "
      "Programa, a ação observa os instrumentos do Caderno Ambiental e Social do MOP ({qua:nas-3224})."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Obras em cada comunidade", "Triagem socioambiental; licenças quando "
         "exigidas; procedimentos ambientais da Sanepar"],
        ["NAS 2 – Condições de trabalho", "Trabalhadores das obras municipais e da Sanepar", "Uso de EPI e protocolos de "
         "saúde e segurança do trabalho"],
        ["NAS 3 – Eficiência de recursos e prevenção da poluição", "Captação de água e resíduos de obra",
         "Outorga; controle de perdas; destinação adequada dos resíduos"],
        ["NAS 4 – Saúde e segurança da comunidade", "Valas, trânsito de máquinas e qualidade da água",
         "Sinalização das obras; monitoramento da qualidade da água pela Sanepar"],
        ["NAS 5 – Aquisição de terras", "Áreas para captação e reservação", "Verificação da titularidade e anuência; sem "
         "reassentamento involuntário"],
        ["NAS 10 – Engajamento das partes interessadas", "Comunidades e associações", "Mobilização e organização "
         "comunitária; canal de queixas da Sanepar e Mecanismo de Queixas e Reclamações do Programa"],
    ], nota="Nota: as NAS 6, 7 e 8 são verificadas na triagem de cada sistema."),
    COM("Confirmar com a UGP quais instrumentos do Caderno Ambiental e Social se aplicam às ações executadas com "
        "recursos de contrapartida."),

    ITEM("8. Cronograma"),
    P("A ação ocorre de 2027 a 2031 ({fig:crono-3224}): 45 sistemas em 2027, 41 em 2028, 42 em 2029, 43 em 2030 e 51 "
      "em 2031. Os estudos, os termos e os projetos de cada ano preparam as obras do ano seguinte, e o suporte pós-obra "
      "continua como rotina da Sanepar depois de 2031."),
    fig_crono(COD),

    ITEM("9. Interfaces e dependências"),
    P("A ação recebe da Ação 3.2.2.1 o modelo de gestão para as associações de moradores e da Atividade 3.2.1 as "
      "diretrizes da política estadual. Entrega à UGP o número de pessoas atendidas e a comprovação da contrapartida e "
      "alimenta o indicador de pessoas com água gerida de forma segura ({fig:interf-3224})."),
    fig_interf(COD),

    ITEM("10. Documentos complementares"),
    BUL("Manual do Programa Sanepar Rural (SANEPAR, [s.d.]);",
        "Contratos de Concessão e de Programa entre a Sanepar e os municípios;",
        "Modelo do Termo de Compromisso e Responsabilidade;",
        "Regulamento de Licitações e Contratos da Sanepar;",
        "Portaria GM/MS nº 888/2021 (padrão de potabilidade);",
        "Caderno Ambiental e Social do MOP."),
]
