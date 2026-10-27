from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM
from comum import matriz, metas, indicadores, aceite, nas, fig_raias, fig_crono, fig_interf

COD = "3.2.2.5"

ELEMENTOS = [
    ACAO("Ação 3.2.2.5 – Esgotamento sanitário nas comunidades atendidas com água"),

    ITEM("1. Contextualização"),
    P("A ação implanta soluções individuais de esgotamento sanitário em 4.067 domicílios das comunidades atendidas pelos "
      "sistemas coletivos de abastecimento de água do IAT, entre 2028 e 2033. Trata-se de sistemas descentralizados, "
      "implantados em cada domicílio, que coletam, tratam e promovem a disposição final ou o reúso do esgoto próximo ao "
      "ponto de geração, solução adequada à baixa densidade de ocupação do meio rural (IAT, 2026a)."),
    P("No meio rural do Paraná, apenas 1,46% dos moradores declaram ligação à rede geral ou pluvial, segundo o Censo "
      "2022, e o Sistema Nacional de Informações em Saneamento Básico (Sinisa) indica que cerca de 3,9% da população "
      "rural é atendida por rede coletora (IAT, 2026a). O esgoto lançado sem tratamento no solo e nos corpos hídricos "
      "aporta matéria orgânica, nutrientes e microrganismos patogênicos aos mananciais superficiais e subterrâneos "
      "utilizados para abastecimento. Como a ampliação do abastecimento de água eleva o volume de esgoto gerado, as "
      "soluções de esgotamento sanitário acompanham a implantação dos sistemas de abastecimento, de modo a evitar a "
      "contaminação da própria fonte de abastecimento da comunidade."),
    P("As soluções observam a ABNT NBR 17076:2024, que substituiu as normas ABNT NBR 7229:1993 e NBR 13969:1997 e "
      "estabelece alternativas de tratamento local para vazões de até 12.000 L/dia e carga orgânica de até 3,80 kg de "
      "demanda bioquímica de oxigênio (DBO) por dia (ABNT, 2024). O desempenho dessas soluções depende da simplicidade de construção e de operação, uma vez "
      "que mesmo tecnologias adequadas apresentam falhas quando mal executadas ou mal operadas. Por esse motivo, a "
      "seleção privilegia soluções de baixa complexidade, compatíveis com as condições de cada domicílio (TONETTI et "
      "al., 2018), e contempla o manejo e a destinação adequada do lodo."),
    P("A {fig:esquema-esgoto} apresenta um exemplo de arranjo."),
    FIG("esquema-esgoto", "f-esquema-esgoto", "Exemplo de solução individual de esgotamento sanitário",
        "Fonte: IAT (2026), com base em ABNT (2024) e Tonetti et al. (2018). Esquema ilustrativo, sem escala.",
        alt="Esquema em corte com domicílio, caixa de inspeção, tanque séptico, filtro anaeróbio e vala de infiltração."),
    P("A ação contribui para o indicador de pessoas atendidas com, pelo menos, esgotamento sanitário, com cerca de 11,4 "
      "mil das 17.800 pessoas previstas; as demais decorrem do esgotamento sanitário em mananciais."),
    PL("Inclui:", "a contratação das soluções e das obras civis; o projeto individual de cada domicílio; a instalação "
       "conforme a ABNT NBR 17076:2024; a verificação técnica; a orientação do proprietário quanto ao uso e à "
       "manutenção; a medição, a comprovação e o pagamento; e a substituição de soluções inadequadas."),
    PL("Não inclui:", "redes coletoras nem intervenções no interior das moradias. A manutenção após a entrega, inclusive "
       "a limpeza periódica, cabe ao proprietário, conforme a orientação recebida."),
    COM("Definir o responsável pela coleta e pela destinação do lodo das soluções individuais após a entrega "
        "(proprietário, associação, município ou serviço contratado)."),
    PL("Valor previsto:", "R$ 32,54 milhões (empréstimo BIRD: R$ 32,54 milhões; contrapartida: R$ 0,00 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    ITEM("2. Área de atuação"),
    P("A ação abrange as 83 comunidades atendidas pelos sistemas coletivos de abastecimento de água ({fig:mapa}). O "
      "número de domicílios foi estimado com os dados do Censo 2022 por setor censitário e do CNEFE: dos 5.810 "
      "domicílios dessas comunidades, 4.067 (70%) não dispõem de esgotamento sanitário adequado (IAT, 2026a). Os "
      "domicílios atendidos são confirmados individualmente pelo diagnóstico do trabalho técnico-social."),

    ITEM("3. Arranjo institucional e partes interessadas"),
    P("O IAT, por meio da DISAR, contrata a empresa, fiscaliza a instalação, valida as medições e efetua o pagamento. "
      "A empresa contratada elabora o projeto de cada domicílio e executa a instalação, e o proprietário autoriza a "
      "intervenção, acompanha a obra e confirma a execução. A supervisora das obras apoia a fiscalização, e a UGP "
      "acompanha a execução."),
    BUL("**Intervenientes:** empresa contratada; empresa supervisora das obras; prefeituras, no apoio à articulação "
        "local;",
        "**Público envolvido:** proprietários e moradores dos domicílios atendidos."),
    P("Os beneficiários diretos são os moradores dos 4.067 domicílios sem esgotamento sanitário adequado, cerca de 11,4 "
      "mil pessoas. Os beneficiários indiretos são os demais moradores das comunidades e das bacias, em razão da "
      "redução da carga de esgoto lançada no solo e nos corpos hídricos."),

    ITEM("4. Processo de execução operacional"),
    P("A partir do diagnóstico de cada domicílio, a ação compreende sete etapas ({fig:raias-3225}). O proprietário "
      "participa em dois momentos: autoriza a intervenção na Etapa 1 e confirma a execução na Etapa 6. A evidência de "
      "conclusão de cada lote é o relatório técnico aprovado, acompanhado do comprovante de pagamento."),
    fig_raias(COD),

    ETAPA("4.1 Etapa 1: Identificação dos domicílios"),
    PL("Atividades:", "seleção, com base no diagnóstico do trabalho técnico-social, dos domicílios sem esgotamento "
       "sanitário adequado; confirmação da adesão e da autorização do proprietário para a intervenção."),
    PL("Entradas:", "diagnóstico domiciliar e termos de adesão (trabalho técnico-social)."),
    PL("Responsáveis:", "IAT (executa e aprova); proprietários (consultados)."),
    PL("Produto:", "lista de domicílios por comunidade."),

    ETAPA("4.2 Etapa 2: Contratação das soluções e das obras"),
    PL("Atividades:", "elaboração e aprovação do Termo de Referência das soluções descentralizadas e das obras civis de "
       "instalação; publicação do edital; licitação; contratação das empresas."),
    PL("Entradas:", "lista de domicílios; especificações conforme a ABNT NBR 17076:2024."),
    PL("Responsáveis:", "IAT (executa e aprova); UGP e Banco Mundial (consultados, quando houver revisão prévia)."),
    PL("Produto:", "contrato assinado."),

    ETAPA("4.3 Etapa 3: Projeto individual por domicílio"),
    PL("Atividades:", "elaboração, pela empresa contratada, do projeto de cada domicílio, considerada a topografia do "
       "terreno, o número de moradores, a capacidade de infiltração do solo e a solução de tratamento adequada, "
       "inclusive o manejo do lodo."),
    PL("Entradas:", "contrato; dados do diagnóstico domiciliar."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova); proprietário (consultado)."),
    PL("Produto:", "projeto aprovado."),

    ETAPA("4.4 Etapa 4: Instalação e verificação técnica"),
    PL("Atividades:", "execução das obras civis e instalação dos dispositivos; verificação técnica do funcionamento, da "
       "estanqueidade e da garantia. O sistema que atende aos requisitos é validado; o que não atende é corrigido pela "
       "empresa e submetido a nova verificação ({fig:instalacao})."),
    FIG("instalacao", "f-instalacao", "Projeto, instalação e verificação técnica das soluções individuais",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias da empresa contratada, do IAT e da supervisora, do projeto individual à validação do "
            "sistema, com a decisão técnica e as correções."),
    PL("Entradas:", "projeto aprovado; autorização do proprietário."),
    PL("Responsáveis:", "empresa contratada (executa); supervisora (acompanha); IAT (aprova)."),
    PL("Produto:", "sistema verificado e validado."),

    ETAPA("4.5 Etapa 5: Orientação do proprietário"),
    PL("Atividades:", "orientação do proprietário, durante a instalação, quanto ao funcionamento do sistema, ao uso "
       "adequado, à manutenção preventiva, à limpeza periódica e ao registro da manutenção."),
    PL("Entradas:", "sistema em instalação; material de orientação aprovado pelo IAT."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova o material); proprietário (participa)."),
    PL("Produto:", "proprietário orientado, com registro de presença."),

    ETAPA("4.6 Etapa 6: Medição, comprovação e pagamento"),
    PL("Atividades:", "como as soluções são implantadas domicílio a domicílio, o pagamento depende de cadeia de "
       "comprovação ({fig:medicao}). A empresa registra as intervenções em relatórios de medição e reúne as evidências; "
       "o proprietário assina o registro de confirmação da execução; o IAT realiza a auditoria documental e as "
       "verificações *in loco*; a empresa consolida o relatório de medição final; e o IAT avalia, por amostragem, a "
       "qualidade das unidades antes da ordenação da despesa e do pagamento."),
    FIG("medicao", "f-medicao", "Medição, comprovação, verificação e pagamento, por responsável",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias da empresa contratada, do proprietário e do IAT, da medição à amostragem e ao "
            "pagamento do lote."),
    PL("Entradas:", "sistemas validados; assinaturas dos proprietários."),
    PL("Responsáveis:", "empresa contratada (executa); proprietário (confirma); IAT (verifica, aprova e efetua o "
       "pagamento)."),
    PL("Produto:", "relatório técnico aprovado e comprovante de pagamento, por lote."),
    COM("Definir o tamanho da amostra da verificação *in loco* e o responsável por cada verificação."),

    ETAPA("4.7 Etapa 7: Encerramento"),
    PL("Atividades:", "encerramento formal de cada lote e do contrato; consolidação dos resultados para o indicador do "
       "componente."),
    PL("Entradas:", "relatórios aprovados e pagamentos realizados."),
    PL("Responsáveis:", "IAT (executa); UGP (valida)."),
    PL("Produto:", "lote encerrado."),

    ETAPA("4.8 Modalidade de execução"),
    P("O item de custo é o sistema individual de tratamento de efluentes: 4.067 domicílios a R$ 8.000,00, no total de "
      "R$ 32,54 milhões, com recursos do empréstimo do BIRD. A execução ocorre mediante licitação de obras, com o "
      "projeto e a instalação no mesmo contrato, conforme o Caderno AQ."),
    COM("A nota técnica prevê a aquisição centralizada dos materiais pelo IAT, com as obras executadas por empresa "
        "contratada; o MOP de março atribuía toda a instalação à empresa. Definir o responsável pela aquisição dos "
        "materiais."),

    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3225} apresenta o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("IAT", ["R, A", "R, A", "A", "A", "A", "A", "R"], "A"),
        ("Empresa contratada", ["–", "–", "R", "R", "R", "R", "I"], "R"),
        ("Supervisora", ["–", "–", "–", "R", "–", "C", "–"], "–"),
        ("Proprietários", ["C", "–", "C", "I", "R", "R", "I"], "I"),
        ("Prefeituras", ["I", "–", "–", "I", "–", "–", "I"], "I"),
        ("UGP", ["I", "C", "I", "I", "I", "I", "A"], "I"),
        ("Banco Mundial", ["–", "C", "–", "–", "–", "–", "–"], "–"),
    ], "domicílios com solução individual instalada e aprovada"),

    ITEM("6. Metas, indicadores e comprovação"),
    P("O {qua:metas-3225} distribui os 4.067 domicílios ao longo do Programa, de forma compatível com o cronograma de "
      "implantação dos sistemas de abastecimento."),
    metas(COD, [("Sistema individual de tratamento de efluentes", "domicílios",
                 {2: 245, 3: 477, 4: 856, 5: 956, 6: 956, 7: 577})]),
    P("Os indicadores constam do {qua:ind-3225}. O indicador do componente corresponde ao número acumulado de "
      "domicílios com solução instalada e aprovada multiplicado por 2,8, com desagregação por sexo e para jovens de 15 "
      "a 24 anos."),
    indicadores(COD, [
        ["Domicílios com solução individual instalada e aprovada", "domicílios", "0", "4.067", "Por lote; IAT"],
        ["Pessoas atendidas com, pelo menos, esgotamento sanitário (parcela do indicador do componente)",
         "pessoas", "0", "11.388", "Anual; IAT, com desagregação por sexo e jovens"],
        ["Unidades aprovadas na amostragem *in loco*", "% da amostra", "–", "100", "Por lote; relatório de amostragem"],
    ]),
    P("Os critérios de aceite constam do {qua:aceite-3225}. A evidência de conclusão de cada lote é o relatório técnico "
      "aprovado, acompanhado do comprovante de pagamento."),
    aceite(COD, [
        ["Projeto individual", "Solução adequada ao terreno e ao número de moradores, conforme a ABNT NBR 17076:2024",
         "Projeto aprovado", "IAT"],
        ["Sistema instalado", "Execução conforme o projeto; teste de estanqueidade aprovado",
         "Relatório de medição; laudo de verificação; registro fotográfico", "IAT"],
        ["Proprietário orientado", "Orientação sobre uso, manutenção e manejo do lodo realizada", "Registro de presença",
         "IAT"],
        ["Execução confirmada", "Execução confirmada pelo proprietário", "Assinatura do proprietário", "IAT"],
        ["Lote aprovado", "Auditoria documental, verificação *in loco* e amostragem aprovadas",
         "Relatório técnico aprovado; comprovante de pagamento", "IAT"],
    ]),

    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("Os riscos referem-se à contaminação do solo por instalação inadequada, ao manejo inadequado do lodo, a "
      "acidentes durante as obras, à segurança das famílias em razão de valas abertas e à comunicação com os "
      "proprietários. As obras ocorrem no interior dos lotes, com autorização do proprietário, sem aquisição de terras "
      "({qua:nas-3225})."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Instalação em cada domicílio", "Dimensionamento técnico conforme a "
         "ABNT NBR 17076:2024; verificação técnica obrigatória (MGAS)"],
        ["NAS 2 – Condições de trabalho", "Trabalhadores das empresas contratadas", "Uso de EPI; treinamento de "
         "segurança; Procedimentos de Gestão de Mão de Obra"],
        ["NAS 3 – Eficiência de recursos e prevenção da poluição", "Contaminação do solo e da água; lodo e resíduos de "
         "obra", "Testes de estanqueidade; orientação sobre a limpeza e a destinação do lodo; Plano de Gerenciamento de "
         "Resíduos Sólidos"],
        ["NAS 4 – Saúde e segurança da comunidade", "Valas abertas nos lotes, com circulação de crianças e animais",
         "Sinalização, isolamento e proteção das valas; execução em prazo reduzido em cada domicílio"],
        ["NAS 10 – Engajamento das partes interessadas", "Proprietários e moradores", "Autorização prévia; reuniões "
         "com linguagem acessível; Mecanismo de Queixas e Reclamações (PEPI e MQR)"],
    ], nota="Nota: a NAS 5 não se aplica, por não haver aquisição de terras; as NAS 6, 7 e 8 são verificadas na "
            "triagem das comunidades."),

    ITEM("8. Cronograma"),
    P("A contratação ocorre em 2028, e os projetos, as instalações, a orientação e as medições, de 2028 a 2033, "
      "conforme a planilha de custos: 245 domicílios em 2028, 477 em 2029, 856 em 2030, 956 em 2031 e em 2032 e 577 em "
      "2033 ({fig:crono-3225})."),
    fig_crono(COD),

    ITEM("9. Interfaces e dependências"),
    P("A ação recebe do trabalho técnico-social o diagnóstico domiciliar e os termos de adesão; da implantação dos "
      "sistemas de abastecimento, as comunidades atendidas e o cronograma das obras; e da supervisão das obras, o "
      "acompanhamento das instalações. Fornece o número de pessoas atendidas para o indicador do componente e reduz a "
      "carga de esgoto lançada no solo e nos corpos hídricos ({fig:interf-3225})."),
    fig_interf(COD),

    ITEM("10. Documentos complementares"),
    BUL("ABNT NBR 17076:2024 (ABNT, 2024);",
        "Termo de Referência e edital das soluções descentralizadas e das obras civis (a elaborar);",
        "Modelo de autorização e de confirmação da execução pelo proprietário (a elaborar);",
        "Material de orientação do proprietário sobre uso, manutenção e manejo do lodo (a elaborar);",
        "Tonetti et al. (2018), referência para a seleção das soluções;",
        "Caderno AQ e Caderno AS."),
]
