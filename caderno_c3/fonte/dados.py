"""Dados estruturados das ações da Atividade 3.2.2 (usados nas figuras e no texto).

Anos do Programa: Ano 1 = 2027 ... Ano 7 = 2033 (planilha PSH_CUSTO v2408).
As figuras e as legendas citam as ações pelo nome: "curto" (figuras), "de" e "a" (legendas).
"""

ANOS = list(range(1, 8))


def ano_civil(a):
    return 2026 + a


ACOES = {}

ACOES["3.2.2.1"] = dict(
    titulo="Implantação dos modelos de gestão",
    curto="Modelos de gestão",
    de="da implantação dos modelos de gestão",
    a="à implantação dos modelos de gestão",
    etapas=[
        dict(nome="Estudos preliminares e definição do modelo", produto="Modelo de gestão definido", anos=[1]),
        dict(nome="Pactuação com municípios e comunidades", produto="Termos de Cooperação e pré-adesões", anos=[1, 2, 3, 4]),
        dict(nome="Constituição das entidades gestoras", produto="Associações regularizadas, com tarifa", anos=[2, 3, 4, 5, 6]),
        dict(nome="Estruturação das unidades regionais de apoio", produto="Três unidades em funcionamento", anos=[2, 3, 4],
             rotulos={2: "1 unid.", 3: "1 unid.", 4: "1 unid."}),
        dict(nome="Entrega dos sistemas e acompanhamento", produto="Termos de aceite e relatórios semestrais", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Encerramento", produto="Relatório final e Termos de Cooperação encerrados", anos=[7]),
    ],
    entregas=[("Unidades regionais (unid.)", {2: 1, 3: 1, 4: 1}),
              ("Sistemas de abastecimento entregues", {2: 5, 3: 10, 4: 20, 5: 20, 6: 18, 7: 10})],
    recebe=[("Política estadual de saneamento rural", "Diretrizes da política e do plano estadual"),
            ("Trabalho técnico-social", "Cadastro, diagnóstico e termos de adesão das famílias"),
            ("Obras de abastecimento e de esgotamento", "Sistemas concluídos, aptos à entrega"),
            ("Programa Sanepar Rural", "Associações constituídas nas comunidades atendidas")],
    entrega=[("Trabalho técnico-social", "Municípios aderidos e Termos de Cooperação assinados"),
             ("Sistemas de abastecimento de água", "Entidade gestora definida antes da obra de cada sistema"),
             ("Programa Sanepar Rural", "Modelo de gestão aplicável às associações"),
             ("UGP", "Indicador de associações com modelo de gestão adotado")],
)

ACOES["3.2.2.2"] = dict(
    titulo="Trabalho técnico-social",
    curto="Trabalho técnico-social",
    de="do trabalho técnico-social",
    a="ao trabalho técnico-social",
    etapas=[
        dict(nome="Contratação da empresa", produto="Contrato assinado e ordem de serviço", anos=[1]),
        dict(nome="Mobilização e sensibilização", produto="Atas e listas de presença", anos=[1, 2, 3]),
        dict(nome="Busca ativa e cadastro domiciliar", produto="Cadastro domiciliar georreferenciado", anos=[1, 2, 3]),
        dict(nome="Diagnóstico coletivo e domiciliar", produto="Diagnóstico por comunidade e por domicílio", anos=[1, 2, 3]),
        dict(nome="Enquadramento e adesão das famílias", produto="Termos de adesão assinados", anos=[2, 3]),
        dict(nome="Educação sanitária e ambiental e acompanhamento", produto="Lideranças capacitadas", anos=[2, 3, 4]),
        dict(nome="Relatório final", produto="Relatório final aprovado", anos=[4]),
    ],
    entregas=[("Profissionais-mês", {1: 6, 2: 12, 3: 12, 4: 6})],
    recebe=[("Modelos de gestão", "Municípios aderidos, Termos de Cooperação e modelo de gestão"),
            ("Sistemas de abastecimento de água", "Cronograma das obras, para o acompanhamento social"),
            ("IBGE", "Bases do Censo 2022 e do CNEFE para o cadastro")],
    entrega=[("Modelos de gestão", "Cadastro e adesões que dão origem às associações"),
             ("Sistemas de abastecimento de água", "Diagnóstico do abastecimento e demanda de água"),
             ("Esgotamento nas comunidades", "Domicílios sem esgotamento adequado e condições do lote"),
             ("UGP", "Registros das consultas e das queixas")],
)

ACOES["3.2.2.3"] = dict(
    titulo="Implantação e reabilitação dos sistemas coletivos de abastecimento de água",
    curto="Sistemas coletivos de abastecimento de água",
    de="da implantação dos sistemas coletivos de abastecimento de água",
    a="à implantação dos sistemas coletivos de abastecimento de água",
    etapas=[
        dict(nome="Estudos preliminares e regularização das áreas", produto="Áreas regularizadas e anteprojeto", anos=[1, 2, 3, 4, 5]),
        dict(nome="Perfuração e outorga do poço", produto="Poço testado e outorgado", anos=[2, 3, 4, 5, 6]),
        dict(nome="Contratação integrada, projetos e licenças", produto="Projetos aprovados e licenças emitidas", anos=[2, 3, 4, 5, 6]),
        dict(nome="Execução das obras", produto="Sistema implantado, com as built", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Pré-operação, capacitação e entrega", produto="Termo de Recebimento Definitivo", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Acompanhamento pós-implantação e encerramento", produto="Relatórios semestrais e relatório final", anos=[3, 4, 5, 6, 7]),
    ],
    entregas=[("Sistemas (unid.)", {2: 5, 3: 10, 4: 20, 5: 20, 6: 18, 7: 10}),
              ("Domicílios atendidos", {2: 350, 3: 700, 4: 1400, 5: 1400, 6: 1260, 7: 700})],
    recebe=[("Modelos de gestão", "Entidade gestora pactuada e Termo de Cooperação"),
            ("Trabalho técnico-social", "Diagnóstico do abastecimento e demanda de água"),
            ("Supervisão das obras", "Relatórios de supervisão e medições verificadas"),
            ("Instrumentos de recursos hídricos", "Outorga, SIGARH e dados de águas subterrâneas")],
    entrega=[("Esgotamento nas comunidades", "Comunidades atendidas com água"),
             ("Modelos de gestão", "Sistemas concluídos para a entrega à entidade gestora"),
             ("Supervisão das obras", "Contratos e cronogramas das obras a supervisionar"),
             ("UGP", "Pessoas atendidas com água gerida de forma segura")],
)

ACOES["3.2.2.4"] = dict(
    titulo="Programa Sanepar Rural",
    curto="Programa Sanepar Rural",
    de="do Programa Sanepar Rural",
    a="ao Programa Sanepar Rural",
    etapas=[
        dict(nome="Levantamento técnico e estudo de engenharia", produto="Estudo técnico da comunidade", anos=[1, 2, 3, 4]),
        dict(nome="Termo de Compromisso com o município", produto="Termo de Compromisso assinado", anos=[1, 2, 3, 4]),
        dict(nome="Projetos de engenharia", produto="Projeto do sistema", anos=[1, 2, 3, 4]),
        dict(nome="Execução das obras com apoio da Sanepar", produto="Sistema implantado", anos=[1, 2, 3, 4, 5]),
        dict(nome="Organização comunitária e capacitação", produto="Associação constituída e capacitada", anos=[1, 2, 3, 4, 5]),
        dict(nome="Monitoramento e suporte pós-obra", produto="Relatório técnico aprovado", anos=[1, 2, 3, 4, 5]),
    ],
    entregas=[("Sistemas (unid.)", {1: 45, 2: 41, 3: 42, 4: 43, 5: 51})],
    recebe=[("Modelos de gestão", "Modelo de gestão aplicável às associações de moradores"),
            ("Política estadual de saneamento rural", "Diretrizes setoriais"),
            ("Municípios", "Termo de Compromisso e execução das obras")],
    entrega=[("UGP", "Pessoas atendidas e comprovação da contrapartida"),
             ("Modelos de gestão", "Associações constituídas, que adotam o modelo de gestão"),
             ("Indicadores do componente", "Pessoas atendidas com água gerida de forma segura")],
)

ACOES["3.2.2.5"] = dict(
    titulo="Esgotamento sanitário nas comunidades atendidas com água",
    curto="Esgotamento sanitário nas comunidades",
    de="do esgotamento sanitário nas comunidades",
    a="ao esgotamento sanitário nas comunidades",
    etapas=[
        dict(nome="Identificação dos domicílios", produto="Lista de domicílios por comunidade", anos=[2, 3, 4]),
        dict(nome="Contratação das soluções e das obras", produto="Contrato assinado", anos=[2]),
        dict(nome="Projeto individual por domicílio", produto="Projeto aprovado", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Instalação e verificação técnica", produto="Sistema verificado e validado", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Orientação do proprietário", produto="Proprietário orientado", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Medição, comprovação e pagamento", produto="Relatório técnico aprovado e pagamento", anos=[2, 3, 4, 5, 6, 7]),
        dict(nome="Encerramento", produto="Lote encerrado", anos=[7]),
    ],
    entregas=[("Domicílios atendidos", {2: 245, 3: 477, 4: 856, 5: 956, 6: 956, 7: 577})],
    recebe=[("Trabalho técnico-social", "Diagnóstico domiciliar e termos de adesão"),
            ("Sistemas de abastecimento de água", "Comunidades atendidas e cronograma das obras"),
            ("Supervisão das obras", "Acompanhamento das instalações e medições verificadas")],
    entrega=[("UGP", "Pessoas atendidas com, pelo menos, esgotamento sanitário"),
             ("Modelos de gestão", "Domicílios atendidos, para o acompanhamento da gestão"),
             ("Bacias e mananciais", "Redução da carga de esgoto lançada no solo e na água")],
)

ACOES["3.2.2.6"] = dict(
    titulo="Esgotamento sanitário em propriedades de mananciais (área da SEAB)",
    curto="Esgotamento sanitário em mananciais",
    de="do esgotamento sanitário em mananciais",
    a="ao esgotamento sanitário em mananciais",
    etapas=[
        dict(nome="Indicação dos domicílios pela SEAB", produto="Lista de domicílios por manancial", anos=[2, 3, 4, 5, 6]),
        dict(nome="Contratação das soluções e das obras", produto="Contrato assinado", anos=[3]),
        dict(nome="Projeto sanitário da propriedade", produto="Projeto aprovado", anos=[3, 4, 5, 6, 7]),
        dict(nome="Instalação e verificação técnica", produto="Sistema verificado e validado", anos=[3, 4, 5, 6, 7]),
        dict(nome="Orientação do proprietário", produto="Proprietário orientado", anos=[3, 4, 5, 6, 7]),
        dict(nome="Medição, comprovação e pagamento", produto="Relatório aprovado pelo IAT, com validação da SEAB", anos=[3, 4, 5, 6, 7]),
        dict(nome="Encerramento", produto="Lote encerrado", anos=[7]),
    ],
    entregas=[("Domicílios atendidos", {3: 460, 4: 460, 5: 460, 6: 460, 7: 460})],
    recebe=[("Componente 2", "Planos Integrados de Propriedade (PIP)"),
            ("SEAB", "Diagnóstico das microbacias e adesão dos proprietários"),
            ("Supervisão das obras", "Acompanhamento das instalações e medições verificadas")],
    entrega=[("Gestão de riscos nos mananciais", "Redução da carga de esgoto nos mananciais de abastecimento"),
             ("UGP", "Pessoas atendidas com, pelo menos, esgotamento sanitário"),
             ("SEAB", "Registro das propriedades atendidas, para a assistência técnica")],
)

ACOES["3.2.2.7"] = dict(
    titulo="Supervisão e gerenciamento das obras",
    curto="Supervisão e gerenciamento das obras",
    de="da supervisão e gerenciamento das obras",
    a="à supervisão e gerenciamento das obras",
    etapas=[
        dict(nome="Contratação da supervisora", produto="Contrato assinado", anos=[2]),
        dict(nome="Mobilização e plano de supervisão", produto="Plano de supervisão aprovado", anos=[3]),
        dict(nome="Acompanhamento das obras", produto="Registros de campo e de não conformidades", anos=[3, 4, 5, 6]),
        dict(nome="Medições e relatórios", produto="Relatórios mensais aprovados", anos=[3, 4, 5, 6]),
        dict(nome="Recebimento das obras e encerramento", produto="Relatório final de supervisão", anos=[4, 5, 6]),
    ],
    entregas=[("Profissionais-mês", {3: 6, 4: 12, 5: 12, 6: 6})],
    recebe=[("Sistemas de abastecimento de água", "Contratos, projetos e cronogramas das obras"),
            ("Esgotamento sanitário", "Contratos e cronogramas das instalações nas comunidades e nos mananciais"),
            ("IAT", "Designação da fiscalização e procedimentos de medição")],
    entrega=[("IAT (fiscalização)", "Relatórios para medição, pagamento e recebimento"),
             ("Executores das obras", "Não conformidades a corrigir"),
             ("UGP", "Informações de progresso físico e de conformidade")],
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
