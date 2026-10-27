from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM, TAB
from comum import matriz, metas, indicadores, aceite, nas, fig_raias, fig_crono, fig_interf

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
    ACAO("Ação 3.2.2.6 – Esgotamento sanitário em propriedades de mananciais (área da SEAB)"),
    COM("Ajuste do nome da ação (Orientações para elaboração dos cadernos, seção 6): “área do IDR-Paraná” passa a "
        "“área da SEAB”. A mesma alteração está registrada, em controle de alterações, no quadro de atividades e ações "
        "do Subcomponente 3.2. Informar à UGP."),

    ITEM("1. Contextualização"),
    P("A ação implanta soluções individuais de esgotamento sanitário em 2.300 domicílios rurais situados em mananciais "
      "de abastecimento público da área prioritária do PSH-PR, em propriedades atendidas pela SEAB, entre 2029 e 2033. "
      "Além do atendimento a domicílios sem solução, a ação substitui sistemas inadequados de disposição do esgoto "
      "(IAT, 2026a)."),
    P("O esgoto lançado sem tratamento no solo e nos cursos d'água de um manancial compromete a qualidade da água bruta "
      "destinada ao abastecimento público, com aporte de matéria orgânica, nutrientes e microrganismos patogênicos. Nos "
      "nove mananciais selecionados, 2.236 domicílios particulares permanentes ocupados apresentam destinação "
      "inadequada do esgoto, segundo os dados do Censo 2022 e do CNEFE (IAT, 2026a)."),
    P("A ação reduz a carga poluidora nos mananciais e complementa a gestão de riscos nas bacias de abastecimento "
      "público, no próprio componente, e as práticas agropecuárias implantadas nas mesmas propriedades no Componente 2. "
      "Contribui também para o indicador de pessoas atendidas com, pelo menos, esgotamento sanitário, com cerca de 6,4 "
      "mil pessoas."),
    PL("Inclui:", "a indicação dos domicílios pela SEAB; a contratação das soluções e das obras; o projeto sanitário de "
       "cada propriedade; a instalação conforme a ABNT NBR 17076:2024; a verificação técnica; a orientação do "
       "proprietário; e a medição, a comprovação e o pagamento, com validação técnica do IAT e da SEAB."),
    PL("Não inclui:", "a elaboração dos Planos Integrados de Propriedade (PIP), realizada no Componente 2, nem redes "
       "coletoras ou intervenções no interior das moradias."),
    PL("Valor previsto:", "R$ 18,40 milhões (empréstimo BIRD: R$ 18,40 milhões; contrapartida: R$ 0,00 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    ITEM("2. Área de atuação"),
    P("A área de atuação resulta da aplicação sucessiva de critérios ({fig:selecao-mananciais}): microbacias "
      "prioritárias do PSH-PR; mananciais de abastecimento público selecionados por critérios de qualidade e de "
      "quantidade da água; domicílios rurais permanentes ocupados; ausência de destinação adequada do esgoto, segundo o "
      "Censo 2022; e existência de diagnóstico da microbacia e de adesão da propriedade ao PSH-PR e às ações da SEAB "
      "(IAT, 2026a)."),
    FIG("selecao-mananciais", "f-selecao-mananciais", "Critérios de seleção dos domicílios em mananciais",
        "Fonte: IAT (2026), com base em IAT (2026a).",
        alt="Funil com os cinco critérios de seleção dos domicílios em mananciais, que resulta em 2.236 domicílios e "
            "na meta de 2.300."),
    P("A aplicação dos critérios resultou em 2.236 domicílios com esgotamento inadequado em nove mananciais, dos quais "
      "1.925 no manancial do Rio Pirapó ({tab:mananciais}). Para o dimensionamento da ação, o número foi arredondado "
      "para 2.300 domicílios, margem que absorve as incertezas das bases de dados, as variações cadastrais e as "
      "demandas futuras."),
    TAB("mananciais", "Tabela", "Domicílios com esgotamento inadequado nos mananciais selecionados",
        ["Manancial", "Critério", "Domicílios permanentes", "Esgotamento inadequado", "%"],
        MANANCIAIS, [2900, 1900, 1700, 1700, 871], "llrrr",
        "Fonte: Adaptado de IAT (2026a), com dados do Censo Demográfico 2022 agregados por setor censitário e do CNEFE "
        "(IBGE, 2024).",
        nota="Nota: domicílios particulares permanentes ocupados. Para o dimensionamento, adotaram-se 2.300 domicílios.",
        negrito_ultima=True),
    COM("Na tabela da nota técnica, o Rio Marumbi consta com 90%, mas 120 de 128 domicílios correspondem a 94%. "
        "Conferir."),
    COM("O Acordo de Empréstimo, item (j)(vii) das definições, exige a identificação das áreas rurais da Parte 3.2. "
        "Incluir o mapa dos nove mananciais, com as microbacias e os municípios."),

    ITEM("3. Arranjo institucional e partes interessadas"),
    P("O IAT, por meio da DISAR, contrata a empresa, fiscaliza a instalação e efetua o pagamento, com apoio da "
      "supervisora das obras. A SEAB indica os domicílios a partir dos PIP, apoia a mobilização dos proprietários e "
      "participa da validação técnica dos resultados. A empresa contratada elabora o projeto de cada propriedade e "
      "executa a instalação, e o proprietário autoriza, acompanha e confirma a execução."),
    BUL("**Coexecutora:** SEAB, na indicação dos domicílios, na mobilização e na validação técnica;",
        "**Intervenientes:** empresa contratada; empresa supervisora das obras; UGP, que acompanha a execução;",
        "**Público envolvido:** proprietários e moradores das propriedades rurais dos mananciais."),
    P("Os beneficiários diretos são os moradores dos 2.300 domicílios, cerca de 6,4 mil pessoas. Os beneficiários "
      "indiretos são as populações abastecidas pelos mananciais, com a melhoria da qualidade da água bruta."),

    ITEM("4. Processo de execução operacional"),
    P("A ação adota o mesmo procedimento de instalação, verificação, medição e pagamento do esgotamento sanitário nas "
      "comunidades ({fig:instalacao} e {fig:medicao}), com as etapas por responsável apresentadas na "
      "{fig:raias-3226}. As diferenças referem-se à origem da demanda, ao território e à validação ({qua:diferencas}): "
      "os domicílios são indicados pela SEAB a partir dos PIP, e não pelo trabalho técnico-social; o território "
      "corresponde aos mananciais de abastecimento público; e a validação técnica de cada lote conta com a "
      "participação da SEAB."),
    TAB("diferencas", "Quadro", "Diferenças entre as ações de esgotamento sanitário",
        ["Aspecto", "Esgotamento sanitário nas comunidades", "Esgotamento sanitário em mananciais"],
        [["Origem da demanda", "Diagnóstico do trabalho técnico-social",
          "PIP, com indicação dos domicílios pela SEAB"],
         ["Território", "Comunidades atendidas pelos sistemas de abastecimento de água",
          "Nove mananciais da área prioritária do PSH-PR"],
         ["Base do levantamento", "Censo 2022 e CNEFE: 70% dos 5.810 domicílios sem esgotamento adequado",
          "Censo 2022 e CNEFE: 2.236 domicílios, arredondados para 2.300"],
         ["Meta", "4.067 domicílios", "2.300 domicílios"],
         ["Prazo", "2028 a 2033", "2029 a 2033"],
         ["Validação", "IAT", "IAT, com a SEAB"]],
        [2200, 3435, 3436], "lll", "Fonte: IAT (2026), com base em IAT (2026a) e PARANÁ (2026)."),
    fig_raias(COD),

    ETAPA("4.1 Etapa 1: Indicação dos domicílios pela SEAB"),
    PL("Atividades:", "indicação pela SEAB, a partir dos PIP e do diagnóstico das microbacias, dos domicílios sem "
       "destinação adequada do esgoto; confirmação da adesão e autorização da intervenção pelo proprietário."),
    PL("Entradas:", "PIP; diagnóstico das microbacias; critérios do item 2."),
    PL("Responsáveis:", "SEAB (executa); IAT (aprova a lista); proprietários (consultados)."),
    PL("Produto:", "lista de domicílios por manancial."),
    COM("Confirmar o cronograma dos PIP no Componente 2, que condiciona o início das instalações em 2029."),

    ETAPA("4.2 Etapa 2: Contratação das soluções e das obras"),
    PL("Atividades:", "elaboração do Termo de Referência das soluções descentralizadas e das obras civis; publicação do "
       "edital; licitação; contratação. A contratação pode integrar o processo do esgotamento sanitário nas "
       "comunidades, em lotes próprios."),
    PL("Entradas:", "lista de domicílios; especificações conforme a ABNT NBR 17076:2024."),
    PL("Responsáveis:", "IAT (executa e aprova); SEAB (consultada); UGP e Banco Mundial (consultados, quando houver "
       "revisão prévia)."),
    PL("Produto:", "contrato assinado."),

    ETAPA("4.3 Etapa 3: Projeto sanitário da propriedade"),
    PL("Atividades:", "elaboração, pela empresa contratada, do projeto de cada propriedade, considerada a topografia do "
       "terreno, o número de moradores, a capacidade de infiltração do solo e a solução de tratamento adequada, "
       "inclusive o manejo do lodo."),
    PL("Entradas:", "contrato; dados do PIP."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova); SEAB e proprietário (consultados)."),
    PL("Produto:", "projeto aprovado."),

    ETAPA("4.4 Etapa 4: Instalação e verificação técnica"),
    PL("Atividades:", "execução das obras civis e instalação dos dispositivos; verificação do funcionamento, da "
       "estanqueidade e da garantia; correções, quando necessárias, conforme a {fig:instalacao}."),
    PL("Entradas:", "projeto aprovado; autorização do proprietário."),
    PL("Responsáveis:", "empresa contratada (executa); supervisora (acompanha); IAT (aprova)."),
    PL("Produto:", "sistema verificado e validado."),

    ETAPA("4.5 Etapa 5: Orientação do proprietário"),
    PL("Atividades:", "orientação quanto ao funcionamento, ao uso adequado, à manutenção preventiva e à limpeza "
       "periódica, durante a instalação, com apoio da equipe técnica da SEAB que atende a propriedade."),
    PL("Entradas:", "sistema em instalação; material de orientação."),
    PL("Responsáveis:", "empresa contratada (executa); SEAB (consultada); IAT (aprova o material)."),
    PL("Produto:", "proprietário orientado."),

    ETAPA("4.6 Etapa 6: Medição, comprovação e pagamento"),
    PL("Atividades:", "relatórios de medição e evidências; assinatura do proprietário; auditoria documental e "
       "verificação *in loco*; relatório de medição final; amostragem *in loco*; ordenação da despesa e pagamento, "
       "conforme a {fig:medicao}. O IAT aprova cada lote após a validação técnica realizada com a SEAB."),
    PL("Entradas:", "sistemas validados; assinaturas dos proprietários."),
    PL("Responsáveis:", "empresa contratada (executa); SEAB (consultada na validação); IAT (aprova e efetua o "
       "pagamento)."),
    PL("Produto:", "relatório técnico aprovado pelo IAT, com a validação da SEAB, e comprovante de pagamento, por "
       "lote."),
    COM("A nota técnica prevê validação conjunta. Na matriz, a SEAB figura como C (consultada antes da aprovação), "
        "porque o Guia de Identidade Visual admite um único A por etapa. Confirmar o papel com a SEAB e registrá-lo no "
        "protocolo de validação."),

    ETAPA("4.7 Etapa 7: Encerramento"),
    PL("Atividades:", "encerramento de cada lote e do contrato; registro das propriedades atendidas, para a assistência "
       "técnica prestada pela SEAB."),
    PL("Entradas:", "relatórios aprovados e pagamentos realizados."),
    PL("Responsáveis:", "IAT (executa); UGP (valida)."),
    PL("Produto:", "lote encerrado."),

    ETAPA("4.8 Modalidade de execução"),
    P("O item de custo é o sistema individual de tratamento de efluentes: 2.300 domicílios a R$ 8.000,00, no total de "
      "R$ 18,40 milhões, com recursos do empréstimo do BIRD. A execução ocorre mediante licitação de obras, com o "
      "projeto e a instalação no mesmo contrato, conforme o Caderno AQ. O eventual agrupamento com o esgotamento "
      "sanitário nas comunidades em um mesmo processo, em lotes distintos, é definido no Plano de Aquisições."),

    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3226} apresenta o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("IAT", ["A", "R, A", "A", "A", "A", "A", "R"], "A"),
        ("SEAB", ["R", "C", "C", "I", "C", "C", "I"], "C"),
        ("Empresa contratada", ["–", "–", "R", "R", "R", "R", "I"], "R"),
        ("Supervisora", ["–", "–", "–", "R", "–", "C", "–"], "–"),
        ("Proprietários", ["C", "–", "C", "I", "R", "R", "I"], "I"),
        ("UGP", ["I", "C", "I", "I", "I", "I", "A"], "I"),
        ("Banco Mundial", ["–", "C", "–", "–", "–", "–", "–"], "–"),
    ], "domicílios dos mananciais com solução individual instalada e aprovada"),

    ITEM("6. Metas, indicadores e comprovação"),
    P("A meta é de 460 domicílios por ano, de 2029 a 2033 ({qua:metas-3226})."),
    metas(COD, [("Sistema individual de tratamento de efluentes", "domicílios", {3: 460, 4: 460, 5: 460, 6: 460, 7: 460})]),
    P("Os indicadores constam do {qua:ind-3226}; o de pessoas atendidas é calculado da mesma forma que no esgotamento "
      "sanitário nas comunidades."),
    indicadores(COD, [
        ["Domicílios de mananciais com solução individual instalada e aprovada", "domicílios", "0", "2.300", "Por lote; IAT e SEAB"],
        ["Pessoas atendidas com, pelo menos, esgotamento sanitário (parcela do indicador do componente)",
         "pessoas", "0", "6.440", "Anual; IAT, com desagregação por sexo e jovens"],
        ["Mananciais com instalações concluídas", "mananciais", "0", "9", "Anual; IAT"],
    ]),
    P("Os critérios de aceite são os mesmos do esgotamento sanitário nas comunidades, com validação técnica realizada "
      "com a SEAB ({qua:aceite-3226})."),
    aceite(COD, [
        ["Lista de domicílios", "Domicílios dos mananciais sem destinação adequada, com adesão do proprietário",
         "Lista da SEAB, com os PIP de origem", "IAT"],
        ["Projeto sanitário", "Solução adequada à propriedade, conforme a ABNT NBR 17076:2024", "Projeto aprovado", "IAT"],
        ["Sistema instalado", "Execução conforme o projeto; teste de estanqueidade aprovado",
         "Relatório de medição; laudo de verificação; registro fotográfico", "IAT, com a SEAB"],
        ["Execução confirmada", "Execução confirmada pelo proprietário", "Assinatura do proprietário", "IAT"],
        ["Lote aprovado", "Auditoria documental, verificação *in loco* e amostragem aprovadas",
         "Relatório técnico aprovado; comprovante de pagamento", "IAT, com a SEAB"],
    ]),

    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("Os riscos são os mesmos do esgotamento sanitário nas comunidades, com atenção adicional à proteção dos recursos "
      "hídricos, por se tratar de instalações em mananciais de abastecimento público ({qua:nas-3226})."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Instalação em propriedades de mananciais", "Dimensionamento conforme a "
         "ABNT NBR 17076:2024; distâncias mínimas de nascentes e cursos d'água; verificação técnica (MGAS)"],
        ["NAS 2 – Condições de trabalho", "Trabalhadores das empresas contratadas", "Uso de EPI; treinamento de "
         "segurança; Procedimentos de Gestão de Mão de Obra"],
        ["NAS 3 – Eficiência de recursos e prevenção da poluição", "Contaminação do solo e da água do manancial; lodo",
         "Testes de estanqueidade; orientação sobre o manejo do lodo; Plano de Gerenciamento de Resíduos Sólidos"],
        ["NAS 4 – Saúde e segurança da comunidade", "Valas abertas nas propriedades", "Sinalização, isolamento e "
         "proteção das valas"],
        ["NAS 10 – Engajamento das partes interessadas", "Proprietários rurais", "Autorização prévia; apoio da equipe "
         "técnica da SEAB; Mecanismo de Queixas e Reclamações (PEPI e MQR)"],
    ], nota="Nota: a NAS 5 não se aplica, por não haver aquisição de terras; a NAS 6 é verificada na triagem das "
            "propriedades situadas em áreas de preservação."),

    ITEM("8. Cronograma"),
    P("A SEAB indica os domicílios a partir de 2028, a contratação ocorre em 2029 e as instalações estendem-se de 2029 "
      "a 2033, com 460 domicílios por ano ({fig:crono-3226})."),
    fig_crono(COD),

    ITEM("9. Interfaces e dependências"),
    P("A ação depende dos PIP e do diagnóstico das microbacias, elaborados no Componente 2, e da supervisão das "
      "instalações. Fornece à gestão de riscos nas bacias de abastecimento a redução da carga de esgoto nos mananciais, "
      "à UGP o número de pessoas atendidas para o indicador do componente e à SEAB o registro das propriedades "
      "atendidas ({fig:interf-3226})."),
    fig_interf(COD),

    ITEM("10. Documentos complementares"),
    BUL("ABNT NBR 17076:2024 (ABNT, 2024);",
        "Planos Integrados de Propriedade (Componente 2);",
        "Protocolo de validação técnica IAT–SEAB (a elaborar);",
        "Termo de Referência e edital das soluções e das obras (a elaborar);",
        "Caderno AQ e Caderno AS."),
]
