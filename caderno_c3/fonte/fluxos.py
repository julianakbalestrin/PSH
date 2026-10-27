"""Fluxogramas em raias de visão geral do item 4 de cada ação (entradas, etapas e saídas).

Cada etapa fica na raia de quem a executa (R na matriz de responsabilidades) e leva o
círculo com o seu número. Aprovações de outra instituição e interações com o Banco
aparecem quando são controles da etapa.
"""
from raias import Raias, col

ALTO = 2.5         # raia com Início ou Fim acima das atividades
BAIXO = -0.42      # deslocamento das atividades na raia alta
CIMA = 0.8         # deslocamento de Início e Fim na raia alta
BANCO = "banco=1.72cm"
NAO_OBJECAO = "Emitir a não objeção, se aplicável"


def r3221():
    R = Raias([("IAT", "IAT", ALTO), ("SEC", "SECID", 1.45), ("MUN", "Municípios", 1.45),
               ("ASS", "Associações e comunidades", 1.45), ("EMP", "Empresas contratadas", 1.45)],
              entradas=[("Diretrizes da política estadual de saneamento rural", [1]),
                        ("Arcabouço legal dos arranjos de gestão", [1]),
                        ("Lista preliminar de comunidades", [2]),
                        ("Cadastro e adesões das famílias", [3])],
              saidas=[("Associações com modelo de gestão e tarifa", [3]),
                      ("Três unidades regionais em funcionamento", [4]),
                      ("Sistemas recebidos pelas entidades gestoras", [5]),
                      ("Relatório final e Termos de Cooperação encerrados", [6])])
    R.no("ini", "inicio", "IAT", col(1), "Início", dy=CIMA)
    R.ativ("n1", "IAT", 1, "Definir o modelo de gestão", 1, dy=BAIXO)
    R.ativ("v1", "SEC", 1, "Validar o modelo")
    R.ativ("n2", "MUN", 2, "Assinar o Termo de Cooperação", 2)
    R.ativ("n3", "ASS", 3, "Constituir a associação e a tarifa", 3)
    R.ativ("n4", "EMP", 4, "Estruturar as unidades regionais", 4)
    R.ativ("n5", "ASS", 5, "Aceitar e operar o sistema", 5)
    R.ativ("n6", "IAT", 6, "Encerrar o Termo de Cooperação", 6, dy=BAIXO)
    R.no("fim", "inicio", "IAT", col(6), "Fim", dy=CIMA)
    R.seta("(ini) -- (n1)")
    R.seta("(n1) -- (v1)")
    R.seta("(v1.east) -| (n2.north)")
    R.seta("(n2.east) -| (n3.north)")
    R.seta("(n3.east) -| (n4.north)")
    R.seta("(n4.east) -| (n5.south)")
    R.seta("(n5.east) -| (n6.south)")
    R.seta("(n6) -- (fim)")
    return R


def r3222():
    R = Raias([("IAT", "IAT", ALTO), ("BM", "Banco Mundial", 1.45), ("EMP", "Empresa contratada", 1.45),
               ("FAM", "Famílias e associações", 1.45)],
              entradas=[("Termos de Cooperação com os municípios", [1]),
                        ("Termo de Referência do trabalho técnico-social", [1]),
                        ("Lista preliminar de comunidades", [2]),
                        ("Bases do Censo 2022 e do CNEFE", [3])],
              saidas=[("Cadastro e diagnóstico das comunidades", [3, 4]),
                      ("Famílias enquadradas e termos de adesão", [5]),
                      ("Lideranças capacitadas", [6]),
                      ("Relatório final e registro no Termo de Cooperação", [7])])
    R.no("ini", "inicio", "IAT", col(1), "Início", dy=CIMA)
    R.ativ("n1", "IAT", 1, "Contratar a empresa", 1, dy=BAIXO)
    R.no("b1", BANCO, "BM", col(1), NAO_OBJECAO)
    R.ativ("n2", "EMP", 1, "Mobilizar e sensibilizar", 2)
    R.ativ("n3", "EMP", 2, "Realizar a busca ativa e o cadastro", 3)
    R.ativ("n4", "EMP", 3, "Elaborar o diagnóstico", 4)
    R.ativ("n5", "EMP", 4, "Enquadrar as famílias", 5)
    R.ativ("f5", "FAM", 4, "Assinar o termo de adesão")
    R.ativ("n6", "EMP", 5, "Capacitar e acompanhar as obras", 6)
    R.ativ("n7", "EMP", 6, "Elaborar o relatório final", 7)
    R.no("fim", "inicio", "IAT", col(6), "Fim", dy=CIMA)
    R.seta("(ini) -- (n1)")
    R.seta("(n1) -- (b1)")
    R.seta("(b1) -- (n2)")
    R.seta("(n2) -- (n3)")
    R.seta("(n3) -- (n4)")
    R.seta("(n4) -- (n5)")
    R.seta("(n5) -- (f5)")
    R.seta("(f5.east) -| (n6.south)")
    R.seta("(n6) -- (n7)")
    R.seta("(n7) -- (fim)")
    return R


def r3223():
    R = Raias([("IAT", "IAT", ALTO), ("MUN", "Municípios", 1.45), ("BM", "Banco Mundial", 1.45),
               ("EMP", "Empresas contratadas", 1.45), ("SUP", "Supervisora", 1.45),
               ("GES", "Entidade gestora", 1.45)],
              entradas=[("Diagnóstico das comunidades", [1]),
                        ("Entidade gestora pactuada", [1]),
                        ("Termo de Cooperação com o município", [1]),
                        ("Dados hidrogeológicos e outorga", [2])],
              saidas=[("Poços outorgados e obras licenciadas", [2, 3]),
                      ("83 sistemas coletivos implantados", [4]),
                      ("5.810 domicílios com água tratada", [5]),
                      ("Termos de Recebimento Definitivo", [5]),
                      ("Relatórios semestrais e relatório final", [6])])
    R.no("ini", "inicio", "IAT", col(1), "Início", dy=CIMA)
    R.ativ("n1", "IAT", 1, "Estudar e regularizar as áreas", 1, dy=BAIXO)
    R.ativ("m1", "MUN", 1, "Regularizar as áreas públicas")
    R.ativ("n2", "IAT", 2, "Perfurar e outorgar o poço", 2, dy=BAIXO)
    R.no("d2", "decisao=1.2cm", "IAT", col(3), "Poço viável?", dy=BAIXO)
    R.no("b3", BANCO, "BM", col(3), NAO_OBJECAO)
    R.ativ("n3", "EMP", 3, "Elaborar os projetos", 3)
    R.ativ("n4", "EMP", 4, "Executar as obras", 4)
    R.ativ("s4", "SUP", 4, "Supervisionar as obras")
    R.ativ("n5", "EMP", 5, "Pré-operar e capacitar os operadores", 5)
    R.ativ("e5", "GES", 5, "Aceitar o sistema")
    R.ativ("n6", "IAT", 6, "Emitir o TRD e acompanhar a operação", 6, dy=BAIXO)
    R.no("fim", "inicio", "IAT", col(6), "Fim", dy=CIMA)
    R.seta("(ini) -- (n1)")
    R.seta("(n1) -- (m1)")
    R.seta("(m1.east) -| (n2.south)")
    R.seta("(n2) -- (d2)")
    R.seta("(d2.north) -- ++(0,0.3) -| (n2.north)")
    R.rot("($(d2.north)+(0.08,0.02)$)", "não")
    R.seta("(d2.south) -- (b3.north)")
    R.rot("($(d2.south)+(0.08,-0.04)$)", "sim", "north west")
    R.seta("(b3) -- (n3)")
    R.seta("(n3) -- (n4)")
    R.seta("(n4) -- (s4)")
    R.seta("(s4.east) -- ++(0.13,0) |- (n5.west)")
    R.seta("(n5) -- (e5)")
    R.seta("(e5.east) -| (n6.south)")
    R.seta("(n6) -- (fim)")
    return R


def r3224():
    R = Raias([("SAN", "Sanepar", ALTO), ("MUN", "Municípios", 1.45),
               ("COM", "Associações e comunidades", 1.45)],
              entradas=[("Critérios do manual do Programa Sanepar Rural", [1]),
                        ("Demanda das comunidades e dos municípios", [1]),
                        ("Contrato de Concessão ou de Programa", [2]),
                        ("Modelo de gestão das associações", [5])],
              saidas=[("222 sistemas coletivos implantados", [4]),
                      ("Associações constituídas e capacitadas", [5]),
                      ("Cerca de 43,5 mil pessoas atendidas", [6]),
                      ("Contrapartida de R$ 67,15 milhões comprovada", [6])])
    R.no("ini", "inicio", "SAN", col(1), "Início", dy=CIMA)
    R.ativ("n1", "SAN", 1, "Elaborar o estudo técnico", 1, dy=BAIXO)
    R.ativ("n2", "MUN", 2, "Assinar o Termo de Compromisso", 2)
    R.ativ("n3", "SAN", 3, "Elaborar o projeto do sistema", 3, dy=BAIXO)
    R.ativ("m4", "SAN", 4, "Fornecer materiais e apoio técnico", dy=BAIXO)
    R.ativ("n4", "MUN", 4, "Executar a obra", 4)
    R.ativ("n5", "COM", 5, "Constituir e capacitar a associação", 5)
    R.ativ("n6", "SAN", 6, "Monitorar e prestar suporte pós-obra", 6, dy=BAIXO)
    R.no("fim", "inicio", "SAN", col(6), "Fim", dy=CIMA)
    R.seta("(ini) -- (n1)")
    R.seta("(n1.east) -| (n2.north)")
    R.seta("(n2.east) -| (n3.south)")
    R.seta("(n3) -- (m4)")
    R.seta("(m4) -- (n4)")
    R.seta("(n4.east) -| (n5.north)")
    R.seta("(n5.east) -| (n6.south)")
    R.seta("(n6) -- (fim)")
    return R


def r3225():
    R = Raias([("IAT", "IAT", ALTO), ("BM", "Banco Mundial", 1.45), ("EMP", "Empresa contratada", 1.45),
               ("SUP", "Supervisora", 1.45), ("PRO", "Proprietários", 1.45)],
              entradas=[("Diagnóstico domiciliar e termos de adesão", [1]),
                        ("Comunidades atendidas com água", [1]),
                        ("Termo de Referência das soluções", [2]),
                        ("ABNT NBR 17076:2024", [3, 4])],
              saidas=[("4.067 domicílios com solução de esgotamento", [4]),
                      ("Proprietários orientados", [5]),
                      ("Relatórios técnicos aprovados e pagos", [6]),
                      ("Lotes encerrados", [7])])
    R.no("ini", "inicio", "IAT", col(1), "Início", dy=CIMA)
    R.ativ("n1", "IAT", 1, "Identificar os domicílios", 1, dy=BAIXO)
    R.ativ("n2", "IAT", 2, "Contratar as soluções e as obras", 2, dy=BAIXO)
    R.no("b2", BANCO, "BM", col(2), NAO_OBJECAO)
    R.ativ("n3", "EMP", 2, "Elaborar o projeto individual", 3)
    R.ativ("n4", "EMP", 3, "Instalar e verificar a solução", 4)
    R.ativ("s4", "SUP", 3, "Acompanhar a instalação")
    R.ativ("n5", "EMP", 4, "Orientar o proprietário", 5)
    R.ativ("n6", "EMP", 5, "Medir e comprovar a execução", 6)
    R.ativ("p6", "PRO", 5, "Confirmar a execução")
    R.ativ("n7", "IAT", 6, "Encerrar o lote e o contrato", 7, dy=BAIXO)
    R.no("fim", "inicio", "IAT", col(6), "Fim", dy=CIMA)
    R.seta("(ini) -- (n1)")
    R.seta("(n1) -- (n2)")
    R.seta("(n2) -- (b2)")
    R.seta("(b2) -- (n3)")
    R.seta("(n3) -- (n4)")
    R.seta("(n4) -- (s4)")
    R.seta("(s4.east) -| (n5.south)")
    R.seta("(n5) -- (n6)")
    R.seta("(n6) -- (p6)")
    R.seta("(p6.east) -| (n7.south)")
    R.seta("(n7) -- (fim)")
    return R


def r3226():
    R = Raias([("SEA", "SEAB", ALTO), ("IAT", "IAT", ALTO), ("BM", "Banco Mundial", 1.45),
               ("EMP", "Empresa contratada", 1.45), ("SUP", "Supervisora", 1.45),
               ("PRO", "Proprietários", 1.45)],
              entradas=[("Planos Integrados de Propriedade", [1]),
                        ("Diagnóstico das microbacias", [1]),
                        ("Termo de Referência das soluções", [2]),
                        ("ABNT NBR 17076:2024", [3, 4])],
              saidas=[("2.300 domicílios com solução de esgotamento", [4]),
                      ("Proprietários orientados", [5]),
                      ("Relatórios validados com a SEAB", [6]),
                      ("Lotes encerrados", [7])])
    R.no("ini", "inicio", "SEA", col(1), "Início", dy=CIMA)
    R.ativ("n1", "SEA", 1, "Indicar os domicílios", 1, dy=BAIXO)
    R.ativ("a1", "IAT", 1, "Aprovar a lista", dy=BAIXO)
    R.ativ("n2", "IAT", 2, "Contratar as soluções e as obras", 2, dy=BAIXO)
    R.no("b2", BANCO, "BM", col(2), NAO_OBJECAO)
    R.ativ("n3", "EMP", 2, "Elaborar o projeto da propriedade", 3)
    R.ativ("n4", "EMP", 3, "Instalar e verificar a solução", 4)
    R.ativ("s4", "SUP", 3, "Acompanhar a instalação")
    R.ativ("n5", "EMP", 4, "Orientar o proprietário", 5)
    R.ativ("n6", "EMP", 5, "Medir e comprovar a execução", 6)
    R.ativ("p6", "PRO", 5, "Confirmar a execução")
    R.ativ("n7", "IAT", 6, "Encerrar o lote e o contrato", 7, dy=BAIXO)
    R.no("fim", "inicio", "IAT", col(6), "Fim", dy=CIMA)
    R.seta("(ini) -- (n1)")
    R.seta("(n1) -- (a1)")
    R.seta("(a1) -- (n2)")
    R.seta("(n2) -- (b2)")
    R.seta("(b2) -- (n3)")
    R.seta("(n3) -- (n4)")
    R.seta("(n4) -- (s4)")
    R.seta("(s4.east) -| (n5.south)")
    R.seta("(n5) -- (n6)")
    R.seta("(n6) -- (p6)")
    R.seta("(p6.east) -| (n7.south)")
    R.seta("(n7) -- (fim)")
    return R


def r3227():
    R = Raias([("IAT", "IAT", 1.75), ("BM", "Banco Mundial", 1.45), ("SUP", "Supervisora", 1.45),
               ("EXE", "Executores das obras", 1.45)],
              entradas=[("Termo de Referência da supervisão", [1]),
                        ("Contratos e cronogramas das obras", [2]),
                        ("Projetos aprovados e licenças", [2]),
                        ("Requisitos ambientais e sociais das obras", [3])],
              saidas=[("Não conformidades registradas e tratadas", [3]),
                      ("Medições verificadas", [4]),
                      ("Relatórios mensais aprovados", [4]),
                      ("Relatório final de supervisão", [5])])
    R.no("ini", "inicio", "IAT", 2.95, "Início")
    R.ativ("n1", "IAT", 4.7, "Contratar a supervisora", 1)
    R.no("b1", BANCO, "BM", 4.7, NAO_OBJECAO)
    R.ativ("n2", "SUP", 4.7, "Mobilizar e elaborar o plano", 2)
    R.ativ("n3", "SUP", 6.9, "Acompanhar as obras", 3)
    R.ativ("x3", "EXE", 6.9, "Corrigir as não conformidades", w=2.05)
    R.ativ("n4", "SUP", 9.1, "Verificar medições e relatar", 4)
    R.ativ("a4", "IAT", 11.3, "Aprovar os relatórios mensais")
    R.ativ("n5", "SUP", 13.5, "Apoiar o recebimento e encerrar", 5)
    R.no("fim", "inicio", "SUP", 15.2, "Fim")
    R.seta("(ini) -- (n1)")
    R.seta("(n1) -- (b1)")
    R.seta("(b1) -- (n2)")
    R.seta("(n2) -- (n3)")
    R.seta("(n3) -- (x3)")
    R.seta("(x3.east) -| (n4.south)")
    R.seta("(n4.east) -| (a4.south)")
    R.seta("(a4.east) -| (n5.north)")
    R.seta("(n5) -- (fim)")
    return R


FLUXOS = {"3.2.2.1": r3221, "3.2.2.2": r3222, "3.2.2.3": r3223, "3.2.2.4": r3224,
          "3.2.2.5": r3225, "3.2.2.6": r3226, "3.2.2.7": r3227}
