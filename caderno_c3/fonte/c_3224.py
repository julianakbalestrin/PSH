from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM
from comum import matriz, metas, indicadores, aceite, nas, fig_raias, fig_crono, fig_interf

COD = "3.2.2.4"

ELEMENTOS = [
    ACAO("Ação 3.2.2.4 – Programa Sanepar Rural"),

    ITEM("1. Contextualização"),
    P("A ação implanta 222 sistemas coletivos de abastecimento de água em comunidades rurais de municípios com "
      "Contrato de Concessão ou de Programa vigente com a Sanepar, entre 2027 e 2031. A Sanepar elabora os estudos e os "
      "projetos, presta apoio técnico, ambiental e socioeconômico às comunidades e fornece capacitação, materiais "
      "hidráulicos e equipamentos; o município executa as obras; e a comunidade constitui a associação de moradores "
      "responsável pela operação do sistema (IAT, 2026b; SANEPAR, [s.d.])."),
    P("Mesmo nos municípios atendidos pela Sanepar, as comunidades rurais situam-se fora do alcance das redes urbanas e "
      "dependem de nascentes e poços rasos, sujeitos à contaminação e às estiagens. O Programa Sanepar Rural implanta "
      "nessas comunidades sistemas coletivos com água tratada, com base na capacidade técnica da companhia e na "
      "estrutura de gestão local das associações."),
    P("A ação responde pela maior parcela do indicador de pessoas atendidas com água gerida de forma segura: cerca de "
      "43,5 mil das 59.780 pessoas previstas. Constitui também a contrapartida do Estado na atividade, no valor de "
      "R$ 67,15 milhões (cerca de US$ 12,3 milhões, à taxa de câmbio de R$ 5,46 adotada no Documento de Avaliação do "
      "Projeto – PAD), aplicados com "
      "recursos próprios da Sanepar (PARANÁ, 2026)."),
    PL("Inclui:", "o levantamento técnico e o estudo de engenharia; o Termo de Compromisso e Responsabilidade vinculado "
       "ao Contrato de Concessão ou de Programa; os projetos de engenharia dos sistemas; o fornecimento de materiais "
       "hidráulicos e o apoio técnico às obras municipais; a mobilização e a organização comunitária; a capacitação e a "
       "educação ambiental; e o monitoramento e o suporte pós-obra."),
    PL("Não inclui:", "os sistemas implantados pelo IAT nem recursos do empréstimo do BIRD."),
    PL("Valor previsto:", "R$ 67,15 milhões (empréstimo BIRD: R$ 0,00 milhões; contrapartida: R$ 67,15 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    ITEM("2. Área de atuação"),
    P("A ação abrange os municípios com Contrato de Concessão ou de Programa vigente com a Sanepar, em todo o Estado. "
      "As comunidades atendidas são selecionadas pelos critérios do manual do Programa Sanepar Rural, com base na "
      "demanda das comunidades e dos municípios e na viabilidade técnica do sistema."),
    COM("O Acordo de Empréstimo, item (j)(vii) das definições, exige a identificação das áreas rurais da Parte 3.2. "
        "Solicitar à Sanepar a lista dos municípios e das comunidades atendidas, com os critérios de priorização do "
        "manual do programa."),

    ITEM("3. Arranjo institucional e partes interessadas"),
    P("A Sanepar é a executora da ação, com estrutura técnica e recursos de contrapartida próprios. Os municípios "
      "celebram o Termo de Compromisso e Responsabilidade e executam as obras, e as comunidades constituem as "
      "associações de moradores e participam da capacitação. O IAT acompanha a compatibilização com o modelo de gestão "
      "e com a outorga de direito de uso de recursos hídricos, e a UGP consolida a comprovação da contrapartida e o "
      "reporte ao Banco Mundial."),
    COM("Indicar a diretoria e a gerência da Sanepar responsáveis pelo Programa Sanepar Rural."),
    BUL("**Executora:** Sanepar;",
        "**Intervenientes:** municípios; IAT (modelo de gestão e outorga); UGP;",
        "**Público envolvido:** comunidades rurais e associações de moradores."),
    P("Os beneficiários diretos são os moradores das comunidades atendidas pelos 222 sistemas, cerca de 43,5 mil "
      "pessoas. Os beneficiários indiretos são os municípios e os serviços de saúde, com a redução das doenças de "
      "veiculação hídrica."),

    ITEM("4. Processo de execução operacional"),
    P("As atividades observam o manual do Programa Sanepar Rural e compreendem seis etapas ({fig:raias-3224}). Em cada "
      "comunidade, a Sanepar executa o levantamento técnico e o projeto, formaliza a parceria com o município e fornece "
      "os materiais; o município executa a obra com apoio técnico da companhia; e a comunidade constitui a associação e "
      "participa da capacitação. Concluída a obra, a Sanepar monitora a qualidade da água e presta suporte às "
      "associações."),
    FIG("raias-3224", "g-raias-3224", "Fluxograma do Programa Sanepar Rural: entradas, etapas por responsável e saídas",
        "Fonte: IAT (2026), com base em IAT (2026b) e SANEPAR ([s.d.]).",
        alt="Fluxograma em raias da Sanepar, dos municípios e das associações, do estudo técnico ao suporte pós-obra, "
            "com as entradas no topo e as saídas na base."),

    ETAPA("4.1 Etapa 1: Levantamento técnico e estudo de engenharia"),
    PL("Atividades:", "levantamento das condições da comunidade e estudo técnico de engenharia do sistema."),
    PL("Entradas:", "demanda da comunidade e do município; critérios do manual do programa."),
    PL("Responsáveis:", "Sanepar (executa e aprova); município (consultado)."),
    PL("Produto:", "estudo técnico da comunidade."),

    ETAPA("4.2 Etapa 2: Termo de Compromisso com o município"),
    PL("Atividades:", "formalização da parceria por Termo de Compromisso e Responsabilidade vinculado ao Contrato de "
       "Concessão ou de Programa, com as obrigações de cada parte."),
    PL("Entradas:", "estudo técnico; Contrato de Concessão ou de Programa vigente."),
    PL("Responsáveis:", "Sanepar e município (executam); Sanepar (aprova)."),
    PL("Produto:", "Termo de Compromisso e Responsabilidade assinado."),

    ETAPA("4.3 Etapa 3: Projetos de engenharia"),
    PL("Atividades:", "elaboração do projeto de engenharia do sistema de abastecimento de água."),
    PL("Entradas:", "estudo técnico; Termo de Compromisso."),
    PL("Responsáveis:", "Sanepar (executa e aprova); município (informado)."),
    PL("Produto:", "projeto do sistema."),

    ETAPA("4.4 Etapa 4: Execução das obras com apoio da Sanepar"),
    PL("Atividades:", "fornecimento dos materiais hidráulicos pela Sanepar; execução das obras pelo município, "
       "diretamente ou por contratação própria, com apoio técnico da companhia."),
    PL("Entradas:", "projeto aprovado; materiais; outorga e licenças, quando exigidas."),
    PL("Responsáveis:", "município (executa a obra); Sanepar (fornece os materiais, presta apoio técnico e aprova a "
       "obra)."),
    PL("Produto:", "sistema implantado."),

    ETAPA("4.5 Etapa 5: Organização comunitária e capacitação"),
    PL("Atividades:", "apoio à constituição da associação de moradores; capacitação em uso racional da água, higiene e "
       "manutenção preventiva; educação ambiental."),
    PL("Entradas:", "comunidade mobilizada; modelo de gestão."),
    PL("Responsáveis:", "Sanepar (executa e aprova); comunidade (executa); IAT (consultado quanto ao modelo de gestão)."),
    PL("Produto:", "associação constituída e capacitada."),

    ETAPA("4.6 Etapa 6: Monitoramento e suporte pós-obra"),
    PL("Atividades:", "monitoramento pós-obra da qualidade da água e suporte operacional às associações; relatório "
       "técnico de cada sistema; reporte anual à UGP dos sistemas implantados, das pessoas atendidas e dos valores "
       "aplicados."),
    PL("Entradas:", "sistema implantado; associação constituída."),
    PL("Responsáveis:", "Sanepar (executa e aprova o relatório técnico); UGP (informada)."),
    PL("Produto:", "relatório técnico aprovado."),

    ETAPA("4.7 Modalidade de execução"),
    P("O item de custo é o de sistemas coletivos de abastecimento de água com recursos de contrapartida: 222 sistemas "
      "ao custo médio de R$ 302.464,42, no total de R$ 67,15 milhões, integralmente com recursos próprios da Sanepar. A "
      "execução ocorre por convênio, formalizado em Termo de Compromisso e Responsabilidade entre a Sanepar e cada "
      "município, conforme o manual do programa."),
    P("As aquisições da Sanepar observam o Regulamento de Licitações e Contratos da companhia, e as obras contratadas "
      "pelos municípios, a legislação de licitações aplicável. A Sanepar comprova à UGP os valores aplicados e os "
      "sistemas implantados, para registro da contrapartida."),
    COM("Confirmar com a UGP e o Banco Mundial se as aquisições e as obras financiadas com contrapartida seguem as "
        "regras da Sanepar e dos municípios e quais requisitos do Programa se aplicam."),

    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3224} apresenta o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("Sanepar", ["R, A", "R, A", "R, A", "A", "R, A", "R, A"], "R, A"),
        ("Municípios", ["C", "R", "I", "R", "C", "I"], "I"),
        ("Comunidades e associações", ["C", "–", "–", "I", "R", "C"], "R"),
        ("IAT", ["–", "–", "–", "–", "C", "I"], "I"),
        ("UGP", ["–", "–", "–", "–", "–", "I"], "I"),
    ], "sistemas implantados e pessoas atendidas"),

    ITEM("6. Metas, indicadores e comprovação"),
    P("A meta é a implantação de 222 sistemas de 2027 a 2031 ({qua:metas-3224})."),
    metas(COD, [
        ("Sistemas coletivos de abastecimento de água", "sistemas", {1: 45, 2: 41, 3: 42, 4: 43, 5: 51}),
        ("Pessoas atendidas", "pessoas", {1: 8820, 2: 8036, 3: 8232, 4: 8428, 5: 9996}),
    ], nota_extra="Pessoas estimadas com 70 domicílios por sistema e 2,8 pessoas por domicílio, conforme o indicador "
                  "do componente."),
    P("Os indicadores constam do {qua:ind-3224}. A Sanepar informa anualmente à UGP os sistemas implantados, as "
      "pessoas atendidas, com desagregação por sexo e para jovens de 15 a 24 anos, e os valores de contrapartida "
      "aplicados."),
    indicadores(COD, [
        ["Sistemas implantados pelo Programa Sanepar Rural", "sistemas", "0", "222", "Anual; Sanepar"],
        ["Pessoas atendidas com água gerida de forma segura (parcela do indicador do componente)",
         "pessoas", "0", "43.500", "Anual; Sanepar, com desagregação por sexo e jovens"],
        ["Contrapartida aplicada", "R$ milhões", "0", "67,15", "Anual; Sanepar e UGP"],
    ]),
    COM("O MOP de março atribuía ao Programa Sanepar Rural a meta total do indicador (59.780 pessoas), que inclui os "
        "sistemas do IAT. A parcela da Sanepar é de cerca de 43.500 pessoas. Confirmar com a Sanepar e citar o manual do "
        "programa com título, versão e data."),
    P("Os critérios de aceite e as evidências de cada produto constam do {qua:aceite-3224}. A evidência de conclusão "
      "de cada sistema é o relatório técnico aprovado pela Sanepar."),
    aceite(COD, [
        ["Termo de Compromisso", "Assinado pela Sanepar e pelo município", "Termo assinado", "Sanepar"],
        ["Projeto do sistema", "Aprovado conforme as normas da Sanepar", "Projeto aprovado", "Sanepar"],
        ["Sistema implantado", "Obra concluída e em operação, com água conforme o padrão de potabilidade",
         "Relatório técnico aprovado; laudos de qualidade da água", "Sanepar"],
        ["Associação capacitada", "Associação constituída e capacitada em operação e manutenção",
         "Registro da associação; listas de presença", "Sanepar"],
        ["Contrapartida comprovada", "Valores aplicados registrados por sistema",
         "Relatório financeiro da Sanepar", "UGP"],
    ]),

    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("Os riscos são análogos aos dos sistemas implantados pelo IAT: impactos temporários das obras, segurança dos "
      "trabalhadores e da comunidade, uso das áreas das estruturas, qualidade da água e participação das comunidades. "
      "Por integrar o Programa, a ação observa os instrumentos do Caderno AS ({qua:nas-3224})."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Obras em cada comunidade", "Triagem socioambiental; licenças, quando "
         "exigidas; procedimentos ambientais da Sanepar"],
        ["NAS 2 – Condições de trabalho", "Trabalhadores das obras municipais e da Sanepar", "Uso de EPI e protocolos de "
         "saúde e segurança do trabalho"],
        ["NAS 3 – Eficiência de recursos e prevenção da poluição", "Captação de água e resíduos de obra",
         "Outorga; controle de perdas; destinação adequada dos resíduos"],
        ["NAS 4 – Saúde e segurança da comunidade", "Valas, trânsito de máquinas e qualidade da água",
         "Sinalização das obras; monitoramento da qualidade da água pela Sanepar"],
        ["NAS 5 – Aquisição de terras", "Áreas para captação e reservação", "Verificação da titularidade e anuência; "
         "ausência de reassentamento involuntário"],
        ["NAS 10 – Engajamento das partes interessadas", "Comunidades e associações", "Mobilização e organização "
         "comunitária; canal de atendimento da Sanepar e Mecanismo de Queixas e Reclamações do Programa"],
    ], nota="Nota: as NAS 6, 7 e 8 são verificadas na triagem de cada sistema."),
    COM("Confirmar com a UGP quais instrumentos do Caderno AS se aplicam às ações executadas com recursos de "
        "contrapartida."),

    ITEM("8. Cronograma"),
    P("A ação ocorre de 2027 a 2031 ({fig:crono-3224}): 45 sistemas em 2027, 41 em 2028, 42 em 2029, 43 em 2030 e 51 "
      "em 2031. Os estudos, os termos e os projetos de cada ano antecedem as obras do ano seguinte, e o suporte "
      "pós-obra prossegue como atividade de rotina da Sanepar após 2031."),
    fig_crono(COD),

    ITEM("9. Interfaces e dependências"),
    P("A ação recebe dos modelos de gestão o arranjo aplicável às associações de moradores e da política estadual de "
      "saneamento rural as diretrizes setoriais. Fornece à UGP o número de pessoas atendidas e a comprovação da "
      "contrapartida e alimenta o indicador de pessoas atendidas com água gerida de forma segura "
      "({fig:interf-3224})."),
    fig_interf(COD),

    ITEM("10. Documentos complementares"),
    BUL("Manual do Programa Sanepar Rural (SANEPAR, [s.d.]);",
        "Contratos de Concessão e de Programa entre a Sanepar e os municípios;",
        "Modelo do Termo de Compromisso e Responsabilidade;",
        "Regulamento de Licitações e Contratos da Sanepar;",
        "Portaria GM/MS nº 888/2021 (padrão de potabilidade);",
        "Caderno AS."),
]
