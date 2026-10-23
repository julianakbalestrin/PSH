"""Dados estruturados das ações da Atividade 3.2.2 (usados nas figuras e no texto).

Anos do Programa: Ano 1 = 2027 ... Ano 7 = 2033 (planilha PSH_CUSTO v2408).
"""

ANOS = list(range(1, 8))


def ano_civil(a):
    return 2026 + a


ACOES = {}

ACOES["3.2.2.1"] = dict(
    titulo="Implantação dos modelos de gestão",
    curto="Modelos de gestão",
    etapas=[
        dict(nome="Estudos preliminares e escolha do modelo", produto="Modelo de gestão definido", anos=[1]),
        dict(nome="Pactuação com municípios e comunidades", produto="Termos de Cooperação e pré-adesões", anos=[1, 2, 3, 4]),
        dict(nome="Constituição das entidades gestoras", produto="Associações regularizadas, com tarifa", anos=[2, 3, 4, 5, 6]),
        dict(nome="Estruturação das unidades regionais de apoio", produto="Três unidades em funcionamento", anos=[2, 3, 4],
             rotulos={2: "1 unid.", 3: "1 unid.", 4: "1 unid."}),
        dict(nome="Entrega dos sistemas e acompanhamento", produto="Termos de aceite e relatórios semestrais", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Encerramento", produto="Relatório final e Termos de Cooperação encerrados", anos=[7]),
    ],
    entradas=["Lista preliminar de comunidades (Ação 3.2.2.3)",
              "Arcabouço legal dos arranjos de gestão",
              "Diretrizes da política estadual (Atividade 3.2.1)",
              "Cadastro e adesões das famílias (Ação 3.2.2.2)"],
    saidas=["Associações de saneamento rural com modelo de gestão adotado",
            "Tarifa instituída nas comunidades",
            "Três unidades regionais de apoio em funcionamento",
            "Sistemas recebidos pelas entidades gestoras"],
    entregas=[("Unidades regionais (unid.)", {2: 1, 3: 1, 4: 1}),
              ("Sistemas entregues (Ação 3.2.2.3)", {2: 5, 3: 10, 4: 20, 5: 20, 6: 18, 7: 10})],
    recebe=[("Atividade 3.2.1", "Diretrizes da política e do plano estadual de saneamento rural"),
            ("Ação 3.2.2.2", "Cadastro, diagnóstico e termos de adesão das famílias"),
            ("Ações 3.2.2.3 e 3.2.2.5", "Sistemas concluídos, prontos para a entrega"),
            ("Ação 3.2.2.4", "Associações formadas pelo Programa Sanepar Rural")],
    entrega=[("Ação 3.2.2.2", "Municípios aderidos e Termos de Cooperação assinados"),
             ("Ação 3.2.2.3", "Entidade gestora definida antes da obra de cada sistema"),
             ("Ação 3.2.2.4", "Modelo de gestão para as associações do Sanepar Rural"),
             ("UGP (Componente 4)", "Indicador de associações com modelo de gestão adotado")],
)

ACOES["3.2.2.2"] = dict(
    titulo="Trabalho técnico-social",
    curto="Trabalho técnico-social",
    etapas=[
        dict(nome="Contratação da empresa", produto="Contrato assinado e ordem de serviço", anos=[1]),
        dict(nome="Mobilização e sensibilização", produto="Atas e listas de presença", anos=[1, 2, 3]),
        dict(nome="Busca ativa e cadastro domiciliar", produto="Cadastro domiciliar georreferenciado", anos=[1, 2, 3]),
        dict(nome="Diagnóstico coletivo e domiciliar", produto="Diagnóstico por comunidade e por domicílio", anos=[1, 2, 3]),
        dict(nome="Enquadramento e adesão das famílias", produto="Termos de adesão assinados", anos=[2, 3]),
        dict(nome="Educação sanitária e ambiental e acompanhamento", produto="Lideranças capacitadas", anos=[2, 3, 4]),
        dict(nome="Relatório final", produto="Relatório final aprovado", anos=[4]),
    ],
    entradas=["Termos de Cooperação com os municípios (Ação 3.2.2.1)",
              "Lista preliminar de comunidades",
              "Bases do Censo 2022 e do CNEFE",
              "Termo de Referência do trabalho técnico-social"],
    saidas=["Cadastro e diagnóstico das comunidades",
            "Famílias enquadradas e termos de adesão",
            "Lideranças capacitadas",
            "Relatório final e baixa no Termo de Cooperação"],
    entregas=[("Profissionais-mês", {1: 6, 2: 12, 3: 12, 4: 6})],
    recebe=[("Ação 3.2.2.1", "Municípios aderidos, Termos de Cooperação e modelo de gestão"),
            ("Ação 3.2.2.3", "Cronograma das obras, para o acompanhamento social"),
            ("Subcomponente 1.1 / IBGE", "Bases do Censo 2022 e do CNEFE para o cadastro")],
    entrega=[("Ação 3.2.2.1", "Cadastro e adesões que formam as associações"),
             ("Ação 3.2.2.3", "Diagnóstico do abastecimento e demanda de água"),
             ("Ação 3.2.2.5", "Domicílios sem esgotamento adequado e condições do lote"),
             ("UGP (Componente 4)", "Registros de consultas e de queixas")],
)

ACOES["3.2.2.3"] = dict(
    titulo="Implantação e reabilitação dos sistemas coletivos de abastecimento de água",
    curto="Sistemas coletivos de água",
    etapas=[
        dict(nome="Estudos preliminares e regularização das áreas", produto="Áreas regularizadas e anteprojeto", anos=[1, 2, 3, 4, 5]),
        dict(nome="Perfuração e outorga do poço", produto="Poço testado e outorgado", anos=[2, 3, 4, 5, 6]),
        dict(nome="Contratação integrada, projetos e licenças", produto="Projetos aprovados e licenças emitidas", anos=[2, 3, 4, 5, 6]),
        dict(nome="Execução das obras", produto="Sistema implantado, com as built", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Pré-operação, capacitação e entrega", produto="Termo de Recebimento Definitivo", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Acompanhamento pós-implantação e encerramento", produto="Relatórios semestrais e relatório final", anos=[3, 4, 5, 6, 7]),
    ],
    entradas=["Diagnóstico das comunidades (Ação 3.2.2.2)",
              "Entidade gestora pactuada (Ação 3.2.2.1)",
              "Termo de Cooperação com o município",
              "Dados hidrogeológicos e outorga (Subcomponente 1.1)"],
    saidas=["83 sistemas coletivos em operação",
            "5.810 domicílios com água tratada",
            "Poços outorgados e obras licenciadas",
            "Termos de Recebimento Definitivo"],
    entregas=[("Sistemas (unid.)", {2: 5, 3: 10, 4: 20, 5: 20, 6: 18, 7: 10}),
              ("Domicílios atendidos", {2: 350, 3: 700, 4: 1400, 5: 1400, 6: 1260, 7: 700})],
    recebe=[("Ação 3.2.2.1", "Entidade gestora pactuada e Termo de Cooperação"),
            ("Ação 3.2.2.2", "Diagnóstico do abastecimento e demanda de água"),
            ("Ação 3.2.2.7", "Relatórios de supervisão e medições verificadas"),
            ("Subcomponente 1.1", "Outorga, SIGARH e dados de águas subterrâneas")],
    entrega=[("Ação 3.2.2.5", "Comunidades com água, que recebem o esgotamento"),
             ("Ação 3.2.2.1", "Sistemas concluídos para a entrega à entidade gestora"),
             ("Ação 3.2.2.7", "Contratos e cronogramas das obras a supervisionar"),
             ("UGP (Componente 4)", "Pessoas atendidas com água gerida de forma segura")],
)

ACOES["3.2.2.4"] = dict(
    titulo="Programa Sanepar Rural",
    curto="Programa Sanepar Rural",
    etapas=[
        dict(nome="Levantamento técnico e estudo de engenharia", produto="Estudo técnico da comunidade", anos=[1, 2, 3, 4]),
        dict(nome="Termo de Compromisso com o município", produto="Termo de Compromisso assinado", anos=[1, 2, 3, 4]),
        dict(nome="Projetos de engenharia", produto="Projeto do sistema", anos=[1, 2, 3, 4]),
        dict(nome="Obras, com materiais e apoio da Sanepar", produto="Sistema implantado", anos=[1, 2, 3, 4, 5]),
        dict(nome="Organização comunitária e treinamento", produto="Associação formada e treinada", anos=[1, 2, 3, 4, 5]),
        dict(nome="Monitoramento e suporte pós-obra", produto="Relatório técnico aprovado", anos=[1, 2, 3, 4, 5]),
    ],
    entradas=["Contrato de Concessão ou de Programa com a Sanepar",
              "Critérios do manual do Programa Sanepar Rural",
              "Demanda das comunidades e dos municípios",
              "Modelo de gestão (Ação 3.2.2.1)"],
    saidas=["222 sistemas coletivos implantados",
            "Cerca de 43,5 mil pessoas atendidas",
            "Associações de moradores formadas",
            "Contrapartida comprovada: R$ 67,15 milhões"],
    entregas=[("Sistemas (unid.)", {1: 45, 2: 41, 3: 42, 4: 43, 5: 51})],
    recebe=[("Ação 3.2.2.1", "Modelo de gestão para as associações de moradores"),
            ("Atividade 3.2.1", "Diretrizes da política estadual de saneamento rural"),
            ("Municípios", "Termo de Compromisso e execução das obras")],
    entrega=[("UGP (Componente 4)", "Pessoas atendidas e comprovação da contrapartida"),
             ("Ação 3.2.2.1", "Associações formadas, que adotam o modelo de gestão"),
             ("Componente 3", "Indicador de pessoas com água gerida de forma segura")],
)

ACOES["3.2.2.5"] = dict(
    titulo="Esgotamento sanitário nas comunidades atendidas com água",
    curto="Esgoto nas comunidades",
    etapas=[
        dict(nome="Identificação dos domicílios", produto="Lista de domicílios por comunidade", anos=[2, 3, 4]),
        dict(nome="Contratação das soluções e das obras", produto="Contrato assinado", anos=[2]),
        dict(nome="Projeto individual por domicílio", produto="Projeto aprovado", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Instalação e verificação técnica", produto="Sistema verificado e validado", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Orientação do proprietário", produto="Proprietário orientado", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Medição, comprovação e pagamento", produto="Relatório técnico aprovado e pagamento", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Finalização", produto="Lote encerrado", anos=[7]),
    ],
    entradas=["Diagnóstico domiciliar e termos de adesão (Ação 3.2.2.2)",
              "Comunidades com sistema de água (Ação 3.2.2.3)",
              "ABNT NBR 17076:2024",
              "Termo de Referência das soluções descentralizadas"],
    saidas=["4.067 domicílios com solução de esgoto",
            "Proprietários orientados em uso e manutenção",
            "Relatórios técnicos aprovados e pagos"],
    entregas=[("Domicílios atendidos", {2: 245, 3: 477, 4: 856, 5: 956, 6: 956, 7: 577})],
    recebe=[("Ação 3.2.2.2", "Diagnóstico domiciliar e termos de adesão"),
            ("Ação 3.2.2.3", "Comunidades com sistema de água e cronograma das obras"),
            ("Ação 3.2.2.7", "Supervisão das instalações e medições verificadas")],
    entrega=[("UGP (Componente 4)", "Pessoas com, pelo menos, esgotamento sanitário"),
             ("Ação 3.2.2.1", "Domicílios atendidos, para o acompanhamento da gestão"),
             ("Bacias e mananciais", "Menor carga de esgoto lançada no solo e na água")],
)

ACOES["3.2.2.6"] = dict(
    titulo="Esgotamento sanitário em propriedades de mananciais (área do IDR-Paraná)",
    curto="Esgoto em mananciais (IDR-Paraná)",
    etapas=[
        dict(nome="Indicação dos domicílios pelo IDR-Paraná", produto="Lista de domicílios por manancial", anos=[2, 3, 4, 5, 6]),
        dict(nome="Contratação das soluções e das obras", produto="Contrato assinado", anos=[3]),
        dict(nome="Projeto sanitário da propriedade", produto="Projeto aprovado", anos=[3, 4, 5, 6, 7]),
        dict(nome="Instalação e verificação técnica", produto="Sistema verificado e validado", anos=[3, 4, 5, 6, 7]),
        dict(nome="Orientação do proprietário", produto="Proprietário orientado", anos=[3, 4, 5, 6, 7]),
        dict(nome="Medição, comprovação e pagamento", produto="Relatório aprovado pelo IAT e pelo IDR-Paraná", anos=[3, 4, 5, 6, 7]),
        dict(nome="Finalização", produto="Lote encerrado", anos=[7]),
    ],
    entradas=["Planos Integrados de Propriedade (Subcomponente 2.3)",
              "Diagnóstico das microbacias (IDR-Paraná)",
              "Domicílios com esgoto inadequado (Censo 2022)",
              "ABNT NBR 17076:2024"],
    saidas=["2.300 domicílios com solução de esgoto",
            "Soluções inadequadas substituídas",
            "Validação conjunta do IAT e do IDR-Paraná"],
    entregas=[("Domicílios atendidos", {3: 460, 4: 460, 5: 460, 6: 460, 7: 460})],
    recebe=[("Subcomponente 2.3", "Planos Integrados de Propriedade elaborados pelo IDR-Paraná"),
            ("IDR-Paraná", "Diagnóstico das microbacias e adesão dos proprietários"),
            ("Ação 3.2.2.7", "Supervisão das instalações e medições verificadas")],
    entrega=[("Subcomponente 3.1", "Menor carga de esgoto nos mananciais de abastecimento"),
             ("UGP (Componente 4)", "Pessoas com, pelo menos, esgotamento sanitário"),
             ("IDR-Paraná", "Registro das propriedades atendidas, para a assistência técnica")],
)

ACOES["3.2.2.7"] = dict(
    titulo="Supervisão e gerenciamento das obras",
    curto="Supervisão das obras",
    etapas=[
        dict(nome="Contratação da supervisora", produto="Contrato assinado", anos=[2]),
        dict(nome="Mobilização e plano de supervisão", produto="Plano de supervisão aprovado", anos=[3]),
        dict(nome="Acompanhamento das obras", produto="Registros de campo e de não conformidades", anos=[3, 4, 5, 6]),
        dict(nome="Medições e relatórios", produto="Relatórios mensais aprovados", anos=[3, 4, 5, 6]),
        dict(nome="Recebimento das obras e encerramento", produto="Relatório final de supervisão", anos=[4, 5, 6]),
    ],
    entradas=["Contratos e cronogramas das obras (Ações 3.2.2.3, 3.2.2.5 e 3.2.2.6)",
              "Projetos aprovados e licenças",
              "Termo de Referência da supervisão",
              "Requisitos ambientais e sociais das obras"],
    saidas=["Relatórios mensais de supervisão",
            "Medições verificadas",
            "Não conformidades registradas e tratadas",
            "Apoio ao recebimento das obras"],
    entregas=[("Profissionais-mês", {3: 6, 4: 12, 5: 12, 6: 6})],
    recebe=[("Ação 3.2.2.3", "Contratos, projetos e cronogramas das obras de água"),
            ("Ações 3.2.2.5 e 3.2.2.6", "Contratos e cronogramas das instalações de esgoto"),
            ("IAT", "Designação da fiscalização e procedimentos de medição")],
    entrega=[("IAT (fiscalização)", "Relatórios para medição, pagamento e recebimento"),
             ("Ações 3.2.2.3, 3.2.2.5 e 3.2.2.6", "Não conformidades a corrigir"),
             ("UGP (Componente 4)", "Informações de progresso físico e de conformidade")],
)

# Custos anuais por ação (R$ milhões), planilha PSH_CUSTO v2408, aba Consolidado R$
CUSTOS = {
    "3.2.2.1": {2: 2.30, 3: 2.30, 4: 2.30},
    "3.2.2.2": {1: 1.079011800, 2: 2.158023600, 3: 2.158023600, 4: 1.079011800},
    "3.2.2.3": {2: 6.50, 3: 13.00, 4: 26.00, 5: 26.00, 6: 23.40, 7: 13.00},
    "3.2.2.4": {1: 13.610898900, 2: 12.401041220, 3: 12.703505640, 4: 13.005970060, 5: 15.425685420},
    "3.2.2.5": {2: 1.960, 3: 3.816, 4: 6.848, 5: 7.648, 6: 7.648, 7: 4.616},
    "3.2.2.6": {3: 3.68, 4: 3.68, 5: 3.68, 6: 3.68, 7: 3.68},
    "3.2.2.7": {3: 1.798333200, 4: 3.596666400, 5: 3.596666400, 6: 1.798333200},
}
