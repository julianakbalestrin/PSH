from mop import ACAO, ITEM, ETAPA, P, PL, BUL, FIG, COM
from comum import matriz, metas, indicadores, aceite, nas, fig_raias, fig_crono, fig_interf

COD = "3.2.2.5"

ELEMENTOS = [
    ACAO("Ação 3.2.2.5 – Esgotamento sanitário nas comunidades atendidas com água"),

    ITEM("1. Contextualização"),
    P("A ação instala soluções individuais de esgotamento sanitário em 4.067 domicílios das comunidades que recebem os "
      "sistemas coletivos de água da Ação 3.2.2.3, entre 2028 e 2033. São sistemas descentralizados, instalados em cada "
      "domicílio, que coletam, tratam e dispõem ou reaproveitam o esgoto perto de onde ele é gerado, solução adequada à "
      "baixa densidade do meio rural (IAT, 2026a)."),
    P("No meio rural do Paraná, apenas 1,46% dos moradores declaram ligação à rede geral ou pluvial, segundo o Censo "
      "2022, e o Sinisa indica que cerca de 3,9% da população rural é atendida por rede coletora (IAT, 2026a). Sem "
      "tratamento adequado, o esgoto lançado no solo e nos corpos d'água leva matéria orgânica, nutrientes e "
      "microrganismos patogênicos aos mananciais superficiais e subterrâneos usados para abastecimento. Por isso, a "
      "ampliação do abastecimento vem acompanhada do esgotamento: com mais água em casa, aumenta o volume de esgoto, que, "
      "sem tratamento, contaminaria a própria fonte da comunidade."),
    P("As soluções seguem a ABNT NBR 17076:2024, que substituiu as normas NBR 7229 e NBR 13969 e define alternativas de "
      "tratamento local para vazões de até 12.000 L/dia e carga orgânica de até 3,80 kg DBO/dia (ABNT, 2024). A "
      "eficiência depende da simplicidade de construção e operação: mesmo uma boa tecnologia falha se for mal construída "
      "ou mal operada. Por isso, a escolha privilegia soluções simples, adequadas à realidade de cada domicílio "
      "(TONETTI et al., 2018), e prevê o manejo e a destinação adequada do lodo."),
    P("A {fig:esquema-esgoto} mostra um exemplo de arranjo."),
    FIG("esquema-esgoto", "f-esquema-esgoto", "Exemplo de solução individual de esgotamento sanitário",
        "Fonte: IAT (2026), com base em ABNT (2024) e Tonetti et al. (2018). Esquema ilustrativo, sem escala.",
        alt="Esquema em corte com domicílio, caixa de inspeção, tanque séptico, filtro anaeróbio e vala de infiltração."),
    P("A ação contribui para o indicador do Componente 3 de pessoas atendidas com, pelo menos, esgotamento sanitário: "
      "cerca de 11,4 mil das 17.800 pessoas previstas. As demais vêm da Ação 3.2.2.6."),
    PL("Inclui:", "a contratação das soluções e das obras civis; o projeto individual de cada domicílio; a instalação "
       "conforme a ABNT NBR 17076:2024; a verificação técnica; a orientação do proprietário em uso e manutenção; a "
       "medição, a comprovação e o pagamento; e a substituição de soluções inadequadas."),
    PL("Não inclui:", "redes coletoras nem obras dentro das moradias. A manutenção depois da entrega, inclusive a "
       "limpeza periódica, é feita pelo proprietário, com a orientação recebida."),
    COM("Definir quem recolhe e destina o lodo das soluções individuais depois da entrega (proprietário, associação, "
        "município ou serviço contratado)."),
    PL("Valor previsto:", "R$ 32,54 milhões (empréstimo BIRD: R$ 32,54 milhões; contrapartida: R$ 0,00 milhões), "
       "conforme a planilha PSH_CUSTO_Consolidada."),

    ITEM("2. Área de atuação"),
    P("A ação atua nas 83 comunidades atendidas pela Ação 3.2.2.3 (ver o mapa da {fig:mapa}). O número de domicílios "
      "foi estimado com os dados do Censo 2022 por setor censitário e do Cadastro Nacional de Endereços para Fins "
      "Estatísticos (CNEFE): dos 5.810 domicílios dessas comunidades, 4.067, ou 70%, não têm esgotamento adequado "
      "(IAT, 2026a). Os domicílios atendidos são confirmados, um a um, pelo diagnóstico do trabalho técnico-social "
      "(Ação 3.2.2.2)."),

    ITEM("3. Arranjo institucional e partes interessadas"),
    P("O IAT, por meio da DISAR, contrata a empresa, fiscaliza a instalação, valida as medições e faz o pagamento. A "
      "empresa contratada elabora o projeto de cada domicílio e executa a instalação, e o proprietário autoriza a "
      "intervenção, acompanha a obra e confirma a execução. A supervisora da Ação 3.2.2.7 apoia a fiscalização, e a UGP "
      "acompanha a execução."),
    BUL("**Intervenientes:** empresa contratada; supervisora (Ação 3.2.2.7); prefeituras, que apoiam a articulação "
        "local;",
        "**Público envolvido:** proprietários e moradores dos domicílios atendidos."),
    P("Os beneficiários diretos são os moradores dos 4.067 domicílios, cerca de 11,4 mil pessoas, que não têm "
      "esgotamento adequado. Os beneficiários indiretos são os demais moradores das comunidades e das bacias, que ganham "
      "com a menor carga de esgoto no solo e na água."),

    ITEM("4. Processo de execução operacional"),
    P("A partir do diagnóstico de cada domicílio, a ação segue sete etapas, cada uma na raia de quem a executa "
      "({fig:raias-3225}). O proprietário participa em dois momentos: autoriza a intervenção na Etapa 1 e confirma a "
      "execução na Etapa 6. A evidência de conclusão de cada lote é o relatório técnico aprovado, com o comprovante de "
      "pagamento."),
    fig_raias(COD),

    ETAPA("4.1 Etapa 1: Identificação dos domicílios"),
    PL("Atividades:", "seleção, a partir do diagnóstico do trabalho técnico-social, dos domicílios sem esgotamento "
       "adequado; confirmação da adesão e da autorização do proprietário para a intervenção."),
    PL("Entradas:", "diagnóstico domiciliar e termos de adesão (Ação 3.2.2.2)."),
    PL("Responsáveis:", "IAT (executa e aprova); proprietários (consultados)."),
    PL("Produto:", "lista de domicílios por comunidade."),

    ETAPA("4.2 Etapa 2: Contratação das soluções e das obras"),
    PL("Atividades:", "elaboração e aprovação do Termo de Referência das soluções descentralizadas e das obras civis de "
       "instalação; edital; licitação; contratação das empresas."),
    PL("Entradas:", "lista de domicílios; especificações conforme a ABNT NBR 17076:2024."),
    PL("Responsáveis:", "IAT (executa e aprova); UGP e Banco Mundial (consultados, quando houver revisão prévia)."),
    PL("Produto:", "contrato assinado."),

    ETAPA("4.3 Etapa 3: Projeto individual por domicílio"),
    PL("Atividades:", "a empresa elabora o projeto de cada domicílio, considerando o terreno, o número de moradores, a "
       "infiltração do solo e a solução de tratamento adequada, inclusive o manejo do lodo."),
    PL("Entradas:", "contrato; dados do diagnóstico domiciliar."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova); proprietário (consultado)."),
    PL("Produto:", "projeto aprovado."),

    ETAPA("4.4 Etapa 4: Instalação e verificação técnica"),
    PL("Atividades:", "execução das obras civis e instalação dos dispositivos; verificação técnica do funcionamento, da "
       "estanqueidade e da garantia. Se o sistema atender aos requisitos, é validado; se não, a empresa faz as correções "
       "e o sistema é verificado de novo ({fig:instalacao})."),
    FIG("instalacao", "f-instalacao", "Projeto, instalação e verificação técnica das soluções individuais",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias para a empresa contratada, o IAT e a supervisora, do projeto individual à validação "
            "do sistema, com a decisão técnica e as correções."),
    PL("Entradas:", "projeto aprovado; autorização do proprietário."),
    PL("Responsáveis:", "empresa contratada (executa); supervisora (acompanha); IAT (aprova)."),
    PL("Produto:", "sistema verificado e validado."),

    ETAPA("4.5 Etapa 5: Orientação do proprietário"),
    PL("Atividades:", "durante a instalação, o proprietário é orientado sobre o funcionamento do sistema, o uso "
       "adequado, a manutenção preventiva, a limpeza periódica e o registro da manutenção."),
    PL("Entradas:", "sistema em instalação; material de orientação aprovado pelo IAT."),
    PL("Responsáveis:", "empresa contratada (executa); IAT (aprova o material); proprietário (participa)."),
    PL("Produto:", "proprietário orientado, com registro de presença."),

    ETAPA("4.6 Etapa 6: Medição, comprovação e pagamento"),
    PL("Atividades:", "como os sistemas são instalados domicílio a domicílio, o pagamento depende de uma cadeia de "
       "comprovação ({fig:medicao}). A empresa registra em relatórios de medição as intervenções e reúne as evidências; "
       "o proprietário assina o registro que confirma a execução; o IAT faz a auditoria documental e as verificações "
       "*in loco*; a empresa consolida o relatório de medição final; e o IAT avalia por amostragem a qualidade das "
       "unidades antes da ordenação das despesas e do pagamento."),
    FIG("medicao", "f-medicao", "Medição, comprovação, verificação e pagamento, por responsável",
        "Fonte: IAT (2026), com base em IAT (2026b).",
        alt="Fluxograma em raias para a empresa contratada, o proprietário e o IAT, da medição à amostragem e ao "
            "pagamento do lote."),
    PL("Entradas:", "sistemas validados; assinaturas dos proprietários."),
    PL("Responsáveis:", "empresa contratada (executa); proprietário (confirma); IAT (verifica, aprova e paga)."),
    PL("Produto:", "relatório técnico aprovado e comprovante de pagamento, por lote."),
    COM("Definir o tamanho da amostra da verificação in loco e quem executa cada verificação."),

    ETAPA("4.7 Etapa 7: Finalização"),
    PL("Atividades:", "encerramento formal de cada lote e do contrato; consolidação dos resultados para o indicador do "
       "Componente 3."),
    PL("Entradas:", "relatórios aprovados e pagamentos realizados."),
    PL("Responsáveis:", "IAT (executa); UGP (valida)."),
    PL("Produto:", "lote encerrado."),

    ETAPA("4.8 Modalidade de execução"),
    P("O item de custo é o sistema individual de tratamento de efluentes: 4.067 domicílios a R$ 8.000,00, total de "
      "R$ 32,54 milhões, financiados pelo empréstimo do BIRD. A execução é por licitação de obras, com o projeto e a "
      "instalação no mesmo contrato, conforme o Caderno AQ."),
    COM("A nota técnica prevê a compra centralizada dos materiais pelo IAT, com as obras executadas por empresa "
        "contratada; o MOP de março atribuía toda a instalação à empresa. Definir quem adquire os materiais."),

    ITEM("5. Matriz de responsabilidades"),
    P("O {qua:raci-3225} indica o papel de cada parte em cada etapa."),
    matriz(COD, [
        ("IAT", ["R, A", "R, A", "A", "A", "A", "A", "R"], "A"),
        ("Empresa contratada", ["–", "–", "R", "R", "R", "R", "I"], "R"),
        ("Supervisora (Ação 3.2.2.7)", ["–", "–", "–", "R", "–", "C", "–"], "–"),
        ("Proprietários", ["C", "–", "C", "I", "R", "R", "I"], "I"),
        ("Prefeituras", ["I", "–", "–", "I", "–", "–", "I"], "I"),
        ("UGP", ["I", "C", "I", "I", "I", "I", "A"], "I"),
        ("Banco Mundial", ["–", "C", "–", "–", "–", "–", "–"], "–"),
    ], "domicílios com solução individual instalada e aprovada"),

    ITEM("6. Metas, indicadores e comprovação"),
    P("O {qua:metas-3225} distribui os 4.067 domicílios ao longo do Programa, acompanhando a implantação dos sistemas "
      "de água."),
    metas(COD, [("Sistema individual de tratamento de efluentes", "domicílios",
                 {2: 245, 3: 477, 4: 856, 5: 956, 6: 956, 7: 577})]),
    P("Os indicadores estão no {qua:ind-3225}. O indicador do Componente 3 conta o número acumulado de domicílios com "
      "solução instalada e aprovada, multiplicado por 2,8, com desagregação por sexo e para jovens de 15 a 24 anos."),
    indicadores(COD, [
        ["Domicílios com solução individual instalada e aprovada", "domicílios", "0", "4.067", "Por lote; IAT"],
        ["Pessoas atendidas com, pelo menos, esgotamento sanitário (parcela do indicador do Componente 3)",
         "pessoas", "0", "11.388", "Anual; IAT, com desagregação por sexo e jovens"],
        ["Unidades aprovadas na amostragem *in loco*", "% da amostra", "–", "100", "Por lote; relatório de amostragem"],
    ]),
    P("Os critérios de aceite estão no {qua:aceite-3225}. A evidência de conclusão de cada lote é o relatório técnico "
      "aprovado com o comprovante de pagamento."),
    aceite(COD, [
        ["Projeto individual", "Solução adequada ao terreno e ao número de moradores, conforme a ABNT NBR 17076:2024",
         "Projeto aprovado", "IAT"],
        ["Sistema instalado", "Execução conforme o projeto; teste de estanqueidade aprovado",
         "Relatório de medição; laudo de verificação; registro fotográfico", "IAT"],
        ["Proprietário orientado", "Orientação sobre uso, manutenção e lodo realizada", "Registro de presença", "IAT"],
        ["Execução confirmada", "Proprietário confirma as melhorias", "Assinatura do proprietário", "IAT"],
        ["Lote aprovado", "Auditoria documental, verificação *in loco* e amostragem aprovadas",
         "Relatório técnico aprovado; comprovante de pagamento", "IAT"],
    ]),

    ITEM("7. Gestão de riscos e impactos ambientais e sociais"),
    P("Os riscos estão na contaminação do solo por instalação incorreta, no manejo inadequado do lodo, nos acidentes "
      "durante as obras, na segurança das famílias com valas abertas e na comunicação com os proprietários. As obras "
      "ocorrem dentro dos lotes, com autorização do proprietário, sem aquisição de terras ({qua:nas-3225})."),
    nas(COD, [
        ["NAS 1 – Avaliação e gestão de riscos", "Instalação em cada domicílio", "Dimensionamento técnico conforme a "
         "ABNT NBR 17076:2024; verificação técnica obrigatória (MGAS)"],
        ["NAS 2 – Condições de trabalho", "Trabalhadores das empresas contratadas", "Uso de EPI; treinamento de "
         "segurança; Procedimentos de Gestão de Mão de Obra"],
        ["NAS 3 – Eficiência de recursos e prevenção da poluição", "Contaminação do solo e da água; lodo e resíduos de "
         "obra", "Testes de estanqueidade; orientação sobre a limpeza e a destinação do lodo; Plano de Gerenciamento de "
         "Resíduos Sólidos"],
        ["NAS 4 – Saúde e segurança da comunidade", "Valas abertas nos lotes, com crianças e animais por perto",
         "Sinalização, isolamento e proteção das valas; obras com prazo curto em cada domicílio"],
        ["NAS 10 – Engajamento das partes interessadas", "Proprietários e moradores", "Autorização prévia; reuniões em "
         "linguagem simples; Mecanismo de Queixas e Reclamações (PEPI e MQR)"],
    ], nota="Nota: a NAS 5 não se aplica, porque não há aquisição de terras; as NAS 6, 7 e 8 são verificadas na triagem "
            "das comunidades."),

    ITEM("8. Cronograma"),
    P("A contratação ocorre em 2028, e os projetos, as instalações, a orientação e as medições, de 2028 a 2033, no ritmo "
      "da planilha: 245 domicílios em 2028, 477 em 2029, 856 em 2030, 956 em 2031 e em 2032 e 577 em 2033 "
      "({fig:crono-3225})."),
    fig_crono(COD),

    ITEM("9. Interfaces e dependências"),
    P("A ação recebe do trabalho técnico-social o diagnóstico domiciliar e os termos de adesão, da Ação 3.2.2.3 as "
      "comunidades com sistema de água e o cronograma das obras, e da Ação 3.2.2.7 a supervisão das instalações. "
      "Entrega o número de pessoas atendidas para o indicador do Componente 3 e reduz a carga de esgoto lançada no solo "
      "e na água ({fig:interf-3225})."),
    fig_interf(COD),

    ITEM("10. Documentos complementares"),
    BUL("ABNT NBR 17076:2024 (ABNT, 2024);",
        "Termo de Referência e edital das soluções descentralizadas e das obras civis (a elaborar);",
        "Modelo de autorização e de confirmação da execução pelo proprietário (a elaborar);",
        "Material de orientação do proprietário sobre uso, manutenção e lodo (a elaborar);",
        "Tonetti et al. (2018), referência para a escolha das soluções;",
        "Caderno AQ e Caderno AS."),
]
