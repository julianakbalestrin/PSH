"""Monta o Caderno C3 com a Atividade 3.2.2 preenchida.

Uso: python3 monta.py <modelo.docx> <saida.docx>
"""
import os
import re
import shutil
import sys
import zipfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from mop import Montador, run, x  # noqa: E402
import c_atividade, c_3221, c_3222, c_3223, c_3224, c_3225, c_3226, c_3227  # noqa: E402

MODELO, SAIDA = sys.argv[1], sys.argv[2]
TRAB = os.path.join(AQUI, "trabalho")

# ------------------------------------------------------------------ conteúdo
REFERENCIAS = [
    "ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS (ABNT). **NBR 12244**: poço tubular: construção de poço tubular para "
    "captação de água subterrânea. Rio de Janeiro: ABNT, 2006.",
    "ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS (ABNT). **NBR 12212**: projeto de poço tubular para captação de água "
    "subterrânea: procedimento. Rio de Janeiro: ABNT, 2017.",
    "ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS (ABNT). **NBR 17076**: projeto de sistema de tratamento de esgoto de "
    "menor porte: requisitos. Rio de Janeiro: ABNT, 2024.",
    "BAHIA. Governo do Estado. **Centrais de abastecimento de associações são referência de política pública de "
    "saneamento rural**. Salvador, 2022. Disponível em: https://www.ba.gov.br/comunicacao/2022/05/noticias/"
    "centrais-de-abastecimento-de-associacoes-sao-referencia-de-politica-publica-de-saneamento-rural.",
    "BANCO MUNDIAL. **Quadro Ambiental e Social**. Washington, DC: Banco Mundial, 2017.",
    "BRASIL. **Lei nº 9.433, de 8 de janeiro de 1997**. Institui a Política Nacional de Recursos Hídricos, cria o "
    "Sistema Nacional de Gerenciamento de Recursos Hídricos, regulamenta o inciso XIX do art. 21 da Constituição "
    "Federal, e altera o art. 1º da Lei nº 8.001, de 13 de março de 1990, que modificou a Lei nº 7.990, de 28 de "
    "dezembro de 1989. Brasília, DF: Presidência da República, 1997.",
    "BRASIL. **Lei nº 11.107, de 6 de abril de 2005**. Dispõe sobre normas gerais de contratação de consórcios "
    "públicos e dá outras providências. Brasília, DF: Presidência da República, 2005.",
    "BRASIL. **Lei nº 11.445, de 5 de janeiro de 2007**. Estabelece as diretrizes nacionais para o saneamento básico "
    "[...]. Brasília, DF: Presidência da República, 2007.",
    "BRASIL. **Lei nº 13.019, de 31 de julho de 2014**. Estabelece o regime jurídico das parcerias entre a "
    "administração pública e as organizações da sociedade civil. Brasília, DF: Presidência da República, 2014.",
    "BRASIL. **Lei nº 13.709, de 14 de agosto de 2018**. Lei Geral de Proteção de Dados Pessoais (LGPD). Brasília, "
    "DF: Presidência da República, 2018.",
    "BRASIL. Ministério da Saúde. Fundação Nacional de Saúde. **Programa Nacional de Saneamento Rural**. Brasília, "
    "DF: Funasa, 2019.",
    "BRASIL. **Lei nº 14.026, de 15 de julho de 2020**. Atualiza o marco legal do saneamento básico e altera a Lei nº "
    "9.984, de 17 de julho de 2000, [...]. Brasília, DF: Presidência da República, 2020.",
    "BRASIL. Ministério da Saúde. **Portaria GM/MS nº 888, de 4 de maio de 2021**. Altera o Anexo XX da Portaria de "
    "Consolidação GM/MS nº 5, de 28 de setembro de 2017, para dispor sobre os procedimentos de controle e de "
    "vigilância da qualidade da água para consumo humano e seu padrão de potabilidade. Brasília, DF: Ministério da "
    "Saúde, 2021.",
    "BRASIL. **Decreto nº 11.599, de 12 de julho de 2023**. Dispõe sobre a prestação regionalizada dos serviços "
    "públicos de saneamento básico, o apoio técnico e financeiro de que trata o art. 13 da Lei nº 14.026, de 15 de "
    "julho de 2020, a alocação de recursos públicos federais e os financiamentos com recursos da União ou com "
    "recursos geridos ou operados por órgãos ou entidades da União de que trata o art. 50 da Lei nº 11.445, de 5 de "
    "janeiro de 2007. Brasília, DF: Presidência da República, 2023.",
    "BRASIL. Ministério da Saúde. Fundação Nacional de Saúde. **Portaria nº 2.777, de 30 de julho de 2025**. "
    "Brasília, DF: Funasa, 2025. Disponível em: https://bvs.saude.gov.br/bvs/saudelegis/funasa/2025/"
    "prt2777_05_08_2025.html.",
    "CEARÁ. Governo do Estado. **Modelo cearense de saneamento rural sustentável alcança mais de 1,1 milhão de pessoas "
    "no campo**. Fortaleza, 16 out. 2025. Disponível em: https://www.ceara.gov.br/2025/10/16/"
    "modelo-cearense-de-saneamento-rural-sustentavel-alcanca-mais-de-11-milhao-de-pessoas-no-campo/.",
    "INSTITUTO ÁGUA E TERRA (IAT). **Nota técnica**: Componente 3 – Segurança Hídrica para o Saneamento; "
    "Subcomponente 3.2 – Saneamento Rural. Curitiba: IAT, 2026a. Documento interno, versão de 4 mar. 2026.",
    "INSTITUTO ÁGUA E TERRA (IAT). **Nota técnica**: Subcomponente 3.2.b – implantação e reabilitação de sistemas "
    "coletivos de abastecimento de água e esgotamento sanitário no meio rural. Curitiba: IAT, 2026b. Documento interno.",
    "INSTITUTO ÁGUA E TERRA (IAT); INSTITUTO DE DESENVOLVIMENTO RURAL DO PARANÁ (IDR-PARANÁ). **Saneamento rural**: "
    "áreas prioritárias, associações de municípios, CISPAR e concentração de domicílios rurais. Curitiba, 2025. 1 mapa, "
    "formato A3.",
    "INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). **Censo Demográfico 2022**: agregados por setores "
    "censitários. Rio de Janeiro: IBGE, 2024.",
    "PARANÁ. **Lei nº 12.726, de 26 de novembro de 1999**. Institui a Política Estadual de Recursos Hídricos e adota "
    "outras providências. Curitiba: Assembleia Legislativa do Estado do Paraná, 1999.",
    "PARANÁ. Secretaria de Estado do Planejamento. **Planilha de custos do PSH-PR**: PSH_CUSTO_Consolidada, versão "
    "v2408. Curitiba: SEPL, 2026. Documento interno.",
    "SANEPAR – COMPANHIA DE SANEAMENTO DO PARANÁ. **Manual do Programa Sanepar Rural**. Curitiba: Sanepar, [s.d.]. "
    "Documento interno.",
    "TONETTI, Adriano Luiz *et al.* **Tratamento de esgotos domésticos em comunidades isoladas**: referencial para a "
    "escolha de soluções. Campinas: Unicamp, 2018.",
]

GLOSSARIO = [
    ("Contratação integrada", "regime em que a mesma empresa elabora os projetos e executa as obras de cada sistema."),
    ("Entidade gestora", "associação, central de associações ou consórcio público que opera e mantém o sistema depois "
     "da entrega."),
    ("Modelo de gestão", "arranjo institucional, jurídico e financeiro que define quem opera, mantém e cobra pelo "
     "serviço de saneamento rural."),
    ("Plano Integrado de Propriedade (PIP)", "plano elaborado pelo IDR-Paraná para cada propriedade rural aderente ao "
     "PSH-PR, com as práticas e as intervenções recomendadas."),
    ("Sistema coletivo de abastecimento de água", "conjunto de poço, tratamento, reservatório, rede e ligações "
     "domiciliares que abastece uma comunidade."),
    ("Solução individual de esgotamento sanitário", "sistema descentralizado que coleta, trata e dispõe o esgoto de um "
     "domicílio no próprio lote."),
    ("Termo de Recebimento Definitivo (TRD)", "documento que formaliza o recebimento final do sistema pelo IAT, depois "
     "da pré-operação e do aceite da entidade gestora."),
    ("Trabalho técnico-social", "conjunto de ações de mobilização, cadastro, diagnóstico, educação sanitária e "
     "ambiental e organização comunitária junto às famílias."),
    ("Unidade regional de apoio", "estrutura do modelo de gestão, com equipe técnica, sede e veículo, que presta suporte "
     "às associações de uma região."),
]

SIGLAS_NOVAS = {
    "ABNT": "Associação Brasileira de Normas Técnicas",
    "AQ": "Caderno de Aquisições do MOP (código)",
    "AS": "Caderno Ambiental e Social do MOP (código)",
    "CISPAR": "Consórcio Intermunicipal de Saneamento do Paraná",
    "CNEFE": "Cadastro Nacional de Endereços para Fins Estatísticos",
    "CNPJ": "Cadastro Nacional da Pessoa Jurídica",
    "DBO": "Demanda bioquímica de oxigênio",
    "DISAR": "Diretoria de Saneamento Ambiental e Recursos Hídricos (IAT)",
    "EPI": "Equipamento de proteção individual",
    "Funasa": "Fundação Nacional de Saúde",
    "IAT": "Instituto Água e Terra",
    "IBGE": "Instituto Brasileiro de Geografia e Estatística",
    "IDR-Paraná": "Instituto de Desenvolvimento Rural do Paraná – Iapar-Emater",
    "IPDM": "Índice Ipardes de Desempenho Municipal",
    "LGPD": "Lei Geral de Proteção de Dados Pessoais",
    "MGAS": "Marco de Gestão Ambiental e Social",
    "MQR": "Mecanismo de Queixas e Reclamações",
    "MROSC": "Marco Regulatório das Organizações da Sociedade Civil",
    "NAS": "Normas Ambientais e Sociais do Banco Mundial",
    "PAD": "Documento de Avaliação do Projeto (Project Appraisal Document)",
    "PEPI": "Plano de Engajamento das Partes Interessadas",
    "PIP": "Plano Integrado de Propriedade",
    "SANEPAR": "Companhia de Saneamento do Paraná",
    "SECID": "Secretaria de Estado das Cidades",
    "SIGARH": "Sistema de Gestão Ambiental e de Recursos Hídricos",
    "Sinisa": "Sistema Nacional de Informações em Saneamento Básico",
    "SISAR": "Sistema Integrado de Saneamento Rural",
    "TRD": "Termo de Recebimento Definitivo",
}

ELEMENTOS = (c_atividade.ELEMENTOS + c_3221.ELEMENTOS + c_3222.ELEMENTOS + c_3223.ELEMENTOS +
             c_3224.ELEMENTOS + c_3225.ELEMENTOS + c_3226.ELEMENTOS + c_3227.ELEMENTOS)


def inicio_par(doc, pos):
    """Início do <w:p> que contém a posição."""
    a = doc.rfind("<w:p>", 0, pos)
    b = doc.rfind("<w:p ", 0, pos)
    return max(a, b)


def fim_par(doc, pos):
    return doc.index("</w:p>", pos) + len("</w:p>")


def main():
    if os.path.exists(TRAB):
        shutil.rmtree(TRAB)
    with zipfile.ZipFile(MODELO) as z:
        z.extractall(TRAB)
    for raiz, _, arqs in os.walk(TRAB):
        for a in arqs:
            p = os.path.join(raiz, a)
            if os.path.islink(p):
                os.remove(p)

    docp = os.path.join(TRAB, "word", "document.xml")
    doc = open(docp, encoding="utf-8").read()

    m = Montador()
    m.processar(ELEMENTOS)
    novo = m.xml()

    # ---------------------------------------------- substitui a seção da Atividade 3.2.2
    i = doc.index("Atividade 3.2.2 – Implantar e reabilitar sistemas coletivos de abastecimento de água no meio rural "
                  "e as soluções de saneamento associadas</w:t></w:r></w:p>")
    # a primeira ocorrência em parágrafo Heading2
    while True:
        a = inicio_par(doc, i)
        if '<w:pStyle w:val="Heading2"/>' in doc[a:i]:
            break
        i = doc.index("Atividade 3.2.2 – Implantar e reabilitar", i + 10)
        i = doc.index("</w:t></w:r></w:p>", i)
    j = doc.index(">Referências</w:t>")
    b = inicio_par(doc, j)
    assert a < b
    trecho = doc[a:b]
    assert trecho.count("<w:pStyle w:val=\"TituloAcao\"/>") == 7, trecho.count("TituloAcao")
    doc = doc[:a] + novo + doc[b:]

    # ---------------------------------------------- referências
    j = doc.index(">Referências</w:t>")
    k = doc.index("ABNT NBR 6023.</w:t>", j)
    k = fim_par(doc, k)
    refs = "".join(f'<w:p><w:pPr><w:spacing w:before="0" w:after="240" w:line="240" w:lineRule="auto"/>'
                   f'<w:jc w:val="left"/></w:pPr>{m.runs(r)}</w:p>' for r in REFERENCIAS)
    doc = doc[:k] + refs + doc[k:]

    # ---------------------------------------------- glossário
    j = doc.index(">Glossário complementar</w:t>")
    k = doc.index("estão no Anexo CG-01.</w:t>", j)
    k = fim_par(doc, k)
    glos = "".join(f'<w:p><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr>'
                   f'{m.runs("**" + t + ":** " + d)}</w:p>' for t, d in GLOSSARIO)
    doc = doc[:k] + glos + doc[k:]

    # ---------------------------------------------- siglas
    j = doc.index(">Lista de siglas</w:t>")
    t0 = doc.index("<w:tbl>", j)
    t1 = doc.index("</w:tbl>", t0) + len("</w:tbl>")
    tab = doc[t0:t1]
    linhas = re.findall(r"<w:tr>.*?</w:tr>", tab, re.S)
    cab = linhas[0]
    existentes = []
    for ln in linhas[1:]:
        textos = ["".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", c)) for c in re.findall(r"<w:tc>.*?</w:tc>", ln, re.S)]
        existentes.append(textos)
    dic = {s: v for s, v in existentes}
    for s, v in SIGLAS_NOVAS.items():
        dic.setdefault(s, v)
    utp = dic.pop("UTP", None)
    ordem = sorted(dic.items(), key=lambda kv: kv[0].lower())
    if utp is not None:
        ordem.append(("UTP", utp))
    corpo = []
    for r, (s, v) in enumerate(ordem):
        fundo = "FFFFFF" if r % 2 == 0 else "F2F2F2"
        ultima = r == len(ordem) - 1
        bi, bs = ("0B3A5A", 8) if ultima else ("CCCCCC", 4)
        corpo.append("<w:tr><w:trPr><w:cantSplit/></w:trPr>" +
                     m.celula(s, 1800, "l", fundo=fundo, borda_inf=bi, borda_inf_sz=bs) +
                     m.celula(v, 7271, "l", fundo=fundo, borda_inf=bi, borda_inf_sz=bs) + "</w:tr>")
    ini_tab = tab[:tab.index(cab) + len(cab)]
    doc = doc[:t0] + ini_tab + "".join(corpo) + "</w:tbl>" + doc[t1:]

    # ---------------------------------------------- numeração das legendas e referências cruzadas
    cont = {"Figura": 0, "Quadro": 0, "Tabela": 0}
    numeros = {}
    for mm in re.finditer(r"<w:instrText[^>]*>\s*SEQ (Figura|Quadro|Tabela)\b[^<]*</w:instrText>", doc):
        tipo = mm.group(1)
        cont[tipo] += 1
        fim = doc.index("</w:p>", mm.end())
        ph = re.search(r"@@SEQ:([\w\-]+)@@", doc[mm.end():fim])
        if ph:
            numeros[ph.group(1)] = cont[tipo]
    print("contagem de legendas no caderno:", cont)
    faltam = set(m.legendas) - set(numeros)
    assert not faltam, faltam

    def seq(mo):
        return str(numeros[mo.group(1)])

    def bm(mo):
        return m.legendas[mo.group(1)]["bm"]

    def reftxt(mo):
        k = mo.group(1)
        return f'{m.legendas[k]["tipo"]} {numeros[k]}'

    refs_usadas = set(re.findall(r"@@BM:([\w\-]+)@@", doc))
    nao_def = refs_usadas - set(m.legendas)
    assert not nao_def, f"referências sem legenda: {nao_def}"
    sem_ref = set(m.legendas) - refs_usadas
    if sem_ref:
        print("AVISO: legendas sem referência no texto:", sorted(sem_ref))
    doc = re.sub(r"@@SEQ:([\w\-]+)@@", seq, doc)
    doc = re.sub(r"@@BM:([\w\-]+)@@", bm, doc)
    doc = re.sub(r"@@REFTXT:([\w\-]+)@@", reftxt, doc)
    assert "@@" not in doc
    open(docp, "w", encoding="utf-8").write(doc)

    # ---------------------------------------------- numeração (marcadores)
    nump = os.path.join(TRAB, "word", "numbering.xml")
    num = open(nump, encoding="utf-8").read()
    if 'w:numId="2"' not in num:
        num = num.replace("</w:numbering>", '<w:num w:numId="2"><w:abstractNumId w:val="2"/></w:num></w:numbering>')
    open(nump, "w", encoding="utf-8").write(num)

    # ---------------------------------------------- comentários
    comp = os.path.join(TRAB, "word", "comments.xml")
    com = open(comp, encoding="utf-8").read()
    com = com.rstrip()
    assert com.endswith("/>"), com[-50:]
    com = com[:-2] + ">" + m.comentarios_xml() + "</w:comments>"
    open(comp, "w", encoding="utf-8").write(com)

    # ---------------------------------------------- imagens e relações
    relp = os.path.join(TRAB, "word", "_rels", "document.xml.rels")
    rel = open(relp, encoding="utf-8").read()
    os.makedirs(os.path.join(TRAB, "word", "media"), exist_ok=True)
    novas = []
    for rid, orig, dest in m.midias:
        shutil.copy(orig, os.path.join(TRAB, "word", dest))
        novas.append(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
                     f'relationships/image" Target="{dest}"/>')
    rel = rel.replace("</Relationships>", "".join(novas) + "</Relationships>")
    open(relp, "w", encoding="utf-8").write(rel)

    # ---------------------------------------------- empacota ([Content_Types].xml primeiro)
    if os.path.exists(SAIDA):
        os.remove(SAIDA)
    with zipfile.ZipFile(SAIDA, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(TRAB, "[Content_Types].xml"), "[Content_Types].xml")
        for raiz, _, arqs in os.walk(TRAB):
            for a in sorted(arqs):
                p = os.path.join(raiz, a)
                rel_p = os.path.relpath(p, TRAB)
                if rel_p == "[Content_Types].xml":
                    continue
                z.write(p, rel_p)
    print(f"ok: {SAIDA} | figuras {sum(1 for v in m.legendas.values() if v['tipo']=='Figura')}, "
          f"quadros {sum(1 for v in m.legendas.values() if v['tipo']=='Quadro')}, "
          f"tabelas {sum(1 for v in m.legendas.values() if v['tipo']=='Tabela')}, "
          f"comentários {len(m.comentarios)}")


main()
