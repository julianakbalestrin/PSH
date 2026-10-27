"""Fluxogramas detalhados, diagramas e esquemas da atividade, no padrão do Guia de
Identidade Visual do MOP: processos com mais de um ator em raias, com os 8 símbolos;
diagramas com caixas brancas e destaque em Azul-escuro; esquemas em traço simples na cor
do Caderno C3 (Azul-petróleo).
"""
import os

from raias import Raias, col

AQUI = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(AQUI, "fig")
CAB = "\\documentclass[border=2pt]{standalone}\n\\input{estilo}\n\\begin{document}\n"
FIM = "\n\\end{document}\n"

ALTO, BAIXO, CIMA = 2.5, -0.42, 0.8

F = {}


def atv(w=1.9):
    return f"atividade={w - 0.18:.2f}cm"


# ------------------------------------------------------------------ articulação das ações
F["f-articulacao"] = r"""
\begin{tikzpicture}[x=1cm, y=1cm,
  acao/.style={destaque=#1, minimum height=1.35cm, font=\fonte{8}{9.6}\mdseries},
  acao/.default=3.79cm,
  outra/.style={caixa=#1, align=center, minimum height=1.0cm},
  outra/.default=3.79cm,
  res/.style={documento=#1, minimum height=1.15cm},
  res/.default=3.75cm,
  lig/.style={rotulo, font=\fonte{7}{8}, align=center}]
  % títulos das colunas
  \node[titulocol=4.0cm] at (2.35,0) {Preparação};
  \node[titulocol=4.8cm] at (8.0,0) {Implantação};
  \node[titulocol=3.9cm] at (13.62,0) {Resultados};
  \draw[cinza20, line width=0.6pt] (0.35,-0.32) -- (4.35,-0.32);
  \draw[cinza20, line width=0.6pt] (5.6,-0.32) -- (10.4,-0.32);
  \draw[cinza20, line width=0.6pt] (11.65,-0.32) -- (15.6,-0.32);

  \node[outra] (x1) at (2.35,-1.25) {\textbf{Política estadual}\\ diretrizes e plano de saneamento rural};
  \node[outra] (x3) at (7.6,-1.25) {\textbf{Recursos hídricos}\\ outorga, SIGARH e águas subterrâneas};

  \node[acao] (a1) at (2.35,-3.3) {\textbf{Modelos de gestão}\\ associações, tarifa e 3 unidades regionais\\ R\$ 6,90 mi};
  \node[acao] (a2) at (2.35,-5.6) {\textbf{Trabalho técnico-social}\\ mobilização, cadastro e adesão\\ R\$ 6,47 mi};
  \node[outra] (x2) at (2.35,-7.9) {\textbf{Componente 2}\\ Planos Integrados de Propriedade};

  \node[acao] (b1) at (7.6,-3.3) {\textbf{Sistemas de abastecimento de água}\\ 83 sistemas, 5.810 domicílios\\ R\$ 107,90 mi};
  \node[acao] (b2) at (7.6,-5.6) {\textbf{Esgotamento nas comunidades}\\ 4.067 domicílios\\ R\$ 32,54 mi};
  \node[acao] (b3) at (7.6,-7.9) {\textbf{Esgotamento em mananciais}\\ 2.300 domicílios (área da SEAB)\\ R\$ 18,40 mi};
  \node[acao] (b4) at (7.6,-10.2) {\textbf{Programa Sanepar Rural}\\ 222 sistemas\\ R\$ 67,15 mi de contrapartida};

  % supervisão das obras: faixa ao lado das ações com obras
  \fill[azulEscuro] (9.8,-2.55) rectangle (10.4,-8.65);
  \node[rotate=90, text=white, font=\fonte{8}{9.4}, align=center] at (10.1,-5.6)
    {\textbf{Supervisão das obras}\\ R\$ 10,79 mi};

  \node[res] (c1) at (13.62,-3.3) {\textbf{Sistemas entregues às entidades gestoras}};
  \node[res] (c2) at (13.62,-5.6) {Operação com tarifa e apoio das unidades regionais};
  \node[res, minimum height=1.6cm] (c3) at (13.62,-8.1) {\textbf{Indicadores do Componente 3}\\ água gerida de forma segura, esgotamento sanitário e associações com modelo de gestão};

  \draw[conector] (x1) -- node[lig, right=2pt] {diretrizes} (a1);
  \draw[conector] (x3) -- node[lig, right=2pt] {outorga} (b1);
  \draw[conector] (a1) -- node[lig, right=2pt] {municípios\\ aderidos} (a2);
  \draw[conector] (a1) -- node[lig, above=2pt] {entidade\\ gestora} (b1);
  \draw[conector] ($(a2.east)+(0,0.3)$) -- ++(0.42,0) |- ($(b1.west)+(0,-0.42)$);
  \node[lig, rotate=90] at (4.71,-4.75) {diagnóstico};
  \draw[conector] ($(a2.east)+(0,-0.25)$) -- node[lig, below=2pt] {domicílios\\ sem\\ esgoto} ($(b2.west)+(0,-0.25)$);
  \draw[conector] (b1) -- node[lig, right=2pt] {mesmas\\ comunidades} (b2);
  \draw[conector] (x2) -- node[lig, above=2pt] {domicílios\\ indicados} (b3);
  \draw[conector] (a1.west) -- (0.12,0 |- a1.west) |- (b4.west);
  \node[lig, anchor=south] at (2.85,-10.15) {modelo de gestão para as associações\\ do Programa Sanepar Rural};
  \draw[conector] (10.4,0 |- c1.west) -- (c1.west);
  \draw[conector] (c1) -- (c2);
  \draw[conector] (c2) -- (c3);
  \draw[conector] (b4.east) -| (c3.south);

  % legenda
  \begin{scope}[shift={(0.2,-11.55)}]
    \fill[azulEscuro] (0,0) rectangle (0.45,0.3);
    \node[anchor=west] at (0.55,0.15) {Ações da atividade};
    \draw[cinza60, line width=0.7pt, fill=white] (4.6,0) rectangle (5.05,0.3);
    \node[anchor=west] at (5.15,0.15) {Outras partes do Programa};
    \node[documento=0.25cm, minimum height=0.38cm, inner ysep=1pt] at (9.75,0.15) {};
    \node[anchor=west] at (10.1,0.15) {Resultados};
  \end{scope}
\end{tikzpicture}
"""


# ------------------------------------------------------------------ adesão dos municípios e das comunidades
def f_adesao():
    R = Raias([("IAT", "IAT", ALTO), ("MUN", "Municípios", 1.9), ("COM", "Comunidades", 1.5)])
    R.no("ini", "inicio", "IAT", col(1), "Início", dy=CIMA)
    R.ativ("c1", "IAT", 1, "Selecionar as comunidades", dy=BAIXO)
    R.ativ("c2", "IAT", 2, "Sensibilizar as prefeituras", dy=BAIXO)
    R.ativ("m1", "MUN", 2, "Aderir e assinar o Termo de Cooperação")
    R.no("d", "decisao=1.3cm", "MUN", col(3) - 0.15, "Cede bens públicos?")
    R.ativ("m2", "MUN", col(4) + 0.3, "Aprovar a lei autorizativa")
    R.ativ("c4", "IAT", col(4) + 0.3, "Contatar a comunidade", dy=BAIXO)
    R.ativ("k1", "COM", 5, "Assinar o contrato de pré-adesão")
    R.no("fim", "inicio", "COM", col(6), "Fim")
    R.seta("(ini) -- (c1)")
    R.seta("(c1) -- (c2)")
    R.seta("(c2) -- (m1)")
    R.seta("(m1) -- (d)")
    R.seta("(d) -- (m2)")
    R.rot("($(d.east)!0.5!(m2.west)+(0,0.04)$)", "sim", "south")
    R.seta("(d.north) |- (c4.west)")
    R.rot("($(d.north)+(0.06,0.05)$)", "não")
    R.seta("(m2) -- (c4)")
    R.seta("(c4.east) -| (k1.north)")
    R.seta("(k1) -- (fim)")
    return R


# ------------------------------------------------------------------ captação, projeto e licenciamento
def f_captacao():
    R = Raias([("DIS", "IAT (DISAR)", ALTO), ("LIC", "IAT (licenças e outorga)", 1.5),
               ("LAB", "Laboratório", 1.45), ("EMP", "Empresa contratada", 1.45)])
    R.no("ini", "inicio", "DIS", col(1), "Início", dy=CIMA)
    R.ativ("a1", "DIS", 1, "Estudar as áreas e locar o poço", 1, dy=BAIXO)
    R.ativ("b1", "LIC", 2, "Emitir a anuência de perfuração")
    R.ativ("a3", "DIS", 3, "Perfurar o poço", 2, dy=BAIXO)
    R.ativ("t1", "LAB", 3, "Testar a vazão e a qualidade da água")
    R.no("d", "decisao=1.2cm", "DIS", col(4), "Poço viável?", dy=BAIXO)
    R.ativ("b2", "LIC", 5, "Emitir a outorga de uso da água")
    R.ativ("e1", "EMP", 5, "Elaborar os projetos e os estudos", 3)
    R.ativ("b3", "LIC", 6, "Emitir as licenças")
    R.ativ("a4", "DIS", 6, "Aprovar os projetos", dy=BAIXO)
    R.no("fim", "inicio", "DIS", col(6), "Fim", dy=CIMA)
    R.seta("(ini) -- (a1)")
    R.seta("(a1.east) -| (b1.north)")
    R.seta("(b1.east) -- ++(0.17,0) |- (a3.west)")
    R.seta("(a3) -- (t1)")
    R.seta("(t1.east) -| (d.south)")
    yl = R.topo("DIS", 0.78)
    R.seta(f"(d.north) |- ({col(1) + 0.72},{yl}) -- ($(a1.north)+(0.72,0)$)")
    R.rot(f"({col(3)},{yl + 0.02})", "não: nova locação", "south")
    R.seta("(d.east) -| (b2.north)")
    R.rot("($(d.east)+(0.05,0.02)$)", "sim")
    R.seta("(b2) -- (e1)")
    R.seta("(e1.east) -| (b3.south)")
    R.seta("(b3) -- (a4)")
    R.seta("(a4) -- (fim)")
    return R


# ------------------------------------------------------------------ execução, supervisão e fiscalização das obras
def f_obras():
    R = Raias([("IAT", "IAT (fiscalização)", ALTO), ("EMP", "Empresa executora", 1.6),
               ("SUP", "Supervisora", 1.45)])
    R.no("ini", "inicio", "IAT", col(1), "Início", dy=CIMA)
    R.ativ("o1", "IAT", 1, "Emitir a ordem de serviço", dy=BAIXO)
    R.ativ("o2", "EMP", 2, "Executar a obra", 4)
    R.ativ("o3", "SUP", 3, "Supervisionar e relatar")
    R.ativ("o4", "IAT", 4, "Verificar a conformidade", dy=BAIXO)
    R.no("d", "decisao=1.45cm", "IAT", col(5), "Conforme?", dy=BAIXO)
    R.ativ("x1", "EMP", 5, "Corrigir as não conformidades", w=2.12)
    R.no("doc", "documento=1.62cm", "IAT", col(6) + 0.12, r"Atesto, laudos e \textit{as built}", dy=BAIXO)
    R.no("fim", "inicio", "IAT", col(6) + 0.12, "Fim", dy=CIMA)
    R.seta("(ini) -- (o1)")
    R.seta("(o1.east) -| (o2.north)")
    R.seta("(o2.east) -| (o3.north)")
    R.seta("(o3.east) -| (o4.south)")
    R.seta("(o4) -- (d)")
    R.seta("(d) -- (x1)")
    R.rot("($(d.south)+(0.06,-0.04)$)", "não", "north west")
    R.seta("(x1.west) -| ($(o4.south)+(0.55,0)$)")
    R.seta("(d) -- (doc)")
    R.rot("($(d.east)!0.5!(doc.west)+(0,0.04)$)", "sim", "south")
    R.seta("(doc) -- (fim)")
    return R


# ------------------------------------------------------------------ transferência, operação e encerramento
def f_entrega():
    R = Raias([("EMP", "Empresa executora", ALTO), ("IAT", "IAT", ALTO), ("GES", "Entidade gestora", 1.5)])
    R.no("ini", "inicio", "EMP", col(1), "Início", dy=CIMA)
    R.ativ("e1", "EMP", 1, "Pré-operar e testar o sistema", dy=BAIXO)
    R.ativ("e2", "EMP", 2, "Capacitar os operadores locais", dy=BAIXO)
    R.ativ("i1", "IAT", 3, "Realizar a reunião de entrega", dy=BAIXO)
    R.ativ("g1", "GES", 3, "Assinar o termo de aceite")
    R.ativ("i2", "IAT", 4, "Emitir o TRD", dy=BAIXO)
    R.ativ("g2", "GES", col(5) - 0.5, "Operar e informar os dados")
    R.no("s1", "sistema=1.5cm", "IAT", col(6), "SIGARH e GeoPR", dy=BAIXO)
    R.no("fim", "inicio", "IAT", col(6), "Fim", dy=CIMA)
    R.seta("(ini) -- (e1)")
    R.seta("(e1) -- (e2)")
    R.seta("(e2.east) -| (i1.north)")
    R.seta("(i1) -- (g1)")
    R.seta("(g1.east) -| (i2.south)")
    R.seta("(i2.east) -| (g2.north)")
    R.seta("(g2.east) -| (s1.south)")
    R.rot("($(g2.east)!0.5!(g2.east -| s1.south)+(0,0.04)$)", r"dados\\ semestrais", "south")
    R.seta("(s1) -- (fim)")
    return R


# ------------------------------------------------------------------ projeto, instalação e verificação técnica
def f_instalacao():
    R = Raias([("EMP", "Empresa contratada", ALTO), ("IAT", "IAT", ALTO), ("SUP", "Supervisora", 1.5)])
    R.no("ini", "inicio", "EMP", col(1), "Início", dy=CIMA)
    R.ativ("e1", "EMP", 1, "Elaborar o projeto individual", 3, dy=BAIXO)
    R.ativ("i1", "IAT", 2, "Aprovar o projeto", dy=BAIXO)
    R.ativ("e2", "EMP", 3, "Instalar a solução e orientar o proprietário", 4, dy=BAIXO)
    R.ativ("s1", "SUP", 3, "Acompanhar a instalação")
    R.ativ("i2", "IAT", 4, "Verificar o sistema", dy=BAIXO)
    R.no("d", "decisao=1.45cm", "IAT", col(5), "Aprovado?", dy=BAIXO)
    R.ativ("x1", "EMP", 5, "Corrigir as não conformidades", dy=BAIXO, w=2.12)
    R.no("doc", "documento=1.62cm", "IAT", col(6) + 0.12, "Sistema validado e registrado", dy=BAIXO)
    R.no("fim", "inicio", "IAT", col(6) + 0.12, "Fim", dy=CIMA)
    R.seta("(ini) -- (e1)")
    R.seta("(e1.south) |- (i1.west)")
    R.seta("(i1.north) |- (e2.west)")
    R.seta("(e2) -- (s1)")
    R.seta("(s1.east) -| (i2.south)")
    R.seta("(i2) -- (d)")
    R.seta("(d) -- (x1)")
    R.rot("($(d.north)+(0.06,0.04)$)", "não")
    R.seta("(x1.west) -| (i2.north)")
    R.seta("(d) -- (doc)")
    R.rot("($(d.east)!0.5!(doc.west)+(0,0.04)$)", "sim", "south")
    R.seta("(doc) -- (fim)")
    return R


# ------------------------------------------------------------------ medição, comprovação e pagamento
def f_medicao():
    R = Raias([("EMP", "Empresa contratada", ALTO), ("PRO", "Proprietário", 1.5), ("IAT", "IAT", ALTO)])
    R.no("ini", "inicio", "EMP", col(1), "Início", dy=CIMA)
    R.ativ("m1", "EMP", 1, "Medir e reunir as evidências", dy=BAIXO)
    R.ativ("p1", "PRO", 2, "Assinar a confirmação da execução")
    R.ativ("a1", "IAT", 3, "Auditar os documentos", dy=-BAIXO)
    R.no("a2", atv(), "IAT", col(4), r"Verificar \textit{in loco}", dy=-BAIXO)
    R.ativ("m3", "EMP", 5, "Consolidar a medição final do lote", dy=BAIXO)
    R.ativ("a3", "IAT", 6, "Verificar por amostragem e pagar", dy=-BAIXO)
    R.no("fim", "inicio", "IAT", col(6), "Fim", dy=-CIMA)
    R.seta("(ini) -- (m1)")
    R.seta("(m1.east) -| (p1.north)")
    R.seta("(p1.east) -| (a1.north)")
    R.seta("(a1) -- (a2)")
    R.seta("(a2.east) -| (m3.south)")
    R.seta("(m3.east) -| (a3.north)")
    R.seta("(a3) -- (fim)")
    return R


# ------------------------------------------------------------------ ciclo mensal de supervisão
def f_ciclo_supervisao():
    R = Raias([("SUP", "Supervisora", ALTO), ("EXE", "Executor da obra", 1.6),
               ("IAT", "IAT (fiscalização)", 1.9), ("UGP", "UGP", 1.5)])
    R.no("ini", "inicio", "SUP", col(1), "Início", dy=CIMA)
    R.ativ("s1", "SUP", 1, "Visitar as obras e controlar a qualidade", dy=BAIXO)
    R.no("d1", "decisao=1.45cm", "SUP", col(2), "Conforme?", dy=BAIXO)
    R.ativ("x1", "EXE", 2, "Corrigir a não conformidade")
    R.ativ("s2", "SUP", col(3) + 0.18, "Verificar as medições", dy=BAIXO)
    R.ativ("s3", "SUP", col(4) + 0.12, "Emitir o relatório mensal", dy=BAIXO)
    R.ativ("i1", "IAT", col(4) + 0.12, "Aprovar o relatório")
    R.ativ("u1", "UGP", col(4) + 0.12, "Consolidar o progresso físico")
    R.no("d2", "decisao=1.45cm", "IAT", col(5), "Obra concluída?")
    R.no("fim", "inicio", "IAT", col(6), "Fim")
    R.seta("(ini) -- (s1)")
    R.seta("(s1) -- (d1)")
    R.seta("(d1) -- (x1)")
    R.rot("($(d1.south)+(0.06,-0.04)$)", "não", "north west")
    R.seta("(x1.west) -| (s1.south)")
    R.seta("(d1) -- (s2)")
    R.rot("($(d1.east)!0.5!(s2.west)+(0,0.04)$)", "sim", "south")
    R.seta("(s2) -- (s3)")
    R.seta("(s3) -- (i1)")
    R.seta("(i1) -- (u1)")
    R.seta("(u1.east) -| (d2.south)")
    R.seta(f"(d2.north) |- ({col(1) + 0.72},{R.topo('SUP', 0.28)}) -- ($(s1.north)+(0.72,0)$)")
    R.rot(f"({col(5) + 0.06},{R.topo('SUP', 0.28) + 0.02})", "não: próximo mês")
    R.seta("(d2) -- (fim)")
    R.rot("($(d2.east)!0.5!(fim.west)+(0,0.04)$)", "sim", "south")
    return R


for nome, fun in [("f-adesao", f_adesao), ("f-captacao", f_captacao), ("f-obras", f_obras),
                  ("f-entrega", f_entrega), ("f-instalacao", f_instalacao), ("f-medicao", f_medicao),
                  ("f-ciclo-supervisao", f_ciclo_supervisao)]:
    F[nome] = fun().tikz()


# ------------------------------------------------------------------ funis de seleção
def funil(camadas, resultado, nota):
    """Funil de critérios numerados; o resultado é um documento (produto)."""
    L = [r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    h, gap = 0.95, 0.1
    w0, dw = 15.2, 1.3
    y = 0.0
    for i, txt in enumerate(camadas):
        wt = w0 - i * dw
        wb = wt - dw
        L.append(rf"  \filldraw[fill=cinza5, draw=cinza60, line width=0.7pt] ({-wt/2},{y}) -- ({wt/2},{y}) -- ({wb/2},{y-h}) -- ({-wb/2},{y-h}) -- cycle;")
        L.append(rf"  \node[text width={(wt + wb) / 2 - 2.4:.2f}cm, align=center, font=\fonte{{8.5}}{{10}}] at (0,{y-h/2}) {{{txt}}};")
        L.append(rf"  \node[numero] at ({-(wt + wb) / 4 + 0.55:.2f},{y-h/2}) {{{i + 1}}};")
        y -= h + gap
    L.append(rf"  \draw[conector] (0,{y+gap}) -- (0,{y-0.4});")
    L.append(rf"  \node[documento=6.8cm, minimum height=1.15cm, anchor=north, font=\fonte{{9}}{{11}}] at (0,{y-0.4}) {{{resultado}}};")
    if nota:
        L.append(rf"  \node[text=cinza80, anchor=north, text width=12cm, align=center] at (0,{y-1.75}) {{{nota}}};")
    L.append(r"\end{tikzpicture}")
    return "\n".join(L)


F["f-selecao-comunidades"] = funil(
    ["Comunidades rurais de todo o Paraná, nas Microrregiões de Água e Esgoto",
     "Comunidade ou conjunto de comunidades com 70 ou mais domicílios ocupados",
     "Município com IPDM de 0,4 a menos de 0,8 (médio baixo ou médio desempenho)",
     "Pedido do município ao IAT ou associação com sistema a complementar",
     "Sem impedimento à perfuração: aquífero, geologia, qualidade da água e restrições legais"],
    r"\textbf{Seleção preliminar: 83 comunidades}\\ \fonte{8}{9.4}5.810 domicílios, cerca de 16,3 mil pessoas",
    r"A lista final é confirmada pelo trabalho técnico-social e pela viabilidade do poço.")

F["f-selecao-mananciais"] = funil(
    ["Microbacias prioritárias do PSH-PR",
     "Mananciais de abastecimento público selecionados por critério quali-quantitativo",
     "Domicílios rurais permanentes ocupados (Censo 2022 e CNEFE)",
     "Domicílios sem destinação adequada do esgoto",
     "Propriedade com diagnóstico e adesão ao PSH-PR e às ações da SEAB"],
    r"\textbf{2.236 domicílios em nove mananciais}\\ \fonte{8}{9.4}2.300 adotados para o dimensionamento",
    r"O arredondamento absorve as incertezas das bases, as variações cadastrais e as demandas futuras.")


# ------------------------------------------------------------------ esquema do sistema coletivo de água
F["f-esquema-saa"] = r"""
\begin{tikzpicture}[x=1cm,y=1cm,
   num/.style={circle, fill=petroleo, text=white, font=\fonte{8}{9}\bfseries, inner sep=0pt,
     minimum size=0.44cm},
   traco/.style={draw=petroleo, line width=0.8pt},
   cano/.style={draw=petroleo, line width=2pt},
   nota/.style={font=\fonte{7.5}{8.8}, text=cinza80}]
  % solo e aquífero
  \fill[cinza5] (0,0) rectangle (15.6,-3.5);
  \fill[petroleo12] (0,-2.35) rectangle (15.6,-3.5);
  \fill[pattern=dots, pattern color=petroleo!60] (0,-2.35) rectangle (15.6,-3.5);
  \draw[cinza60, line width=0.5pt] (0,-2.35) -- (15.6,-2.35);
  \node[nota, anchor=west, fill=petroleo12, inner sep=1.5pt] at (2.3,-2.95) {aquífero (água subterrânea)};
  \node[nota, anchor=west] at (2.3,-1.3) {solo e rocha};
  \draw[cinza60, line width=1.2pt] (0,0) -- (15.6,0);
  % poço
  \fill[white] (1.25,0.3) rectangle (1.75,-3.1);
  \draw[traco] (1.25,0.3) -- (1.25,-3.1) -- (1.75,-3.1) -- (1.75,0.3);
  \draw[traco, dash pattern=on 2pt off 1.5pt] (1.25,-2.45) -- (1.25,-3.05);
  \draw[traco, dash pattern=on 2pt off 1.5pt] (1.75,-2.45) -- (1.75,-3.05);
  \fill[petroleo12] (1.27,-1.9) rectangle (1.73,-3.08);
  \filldraw[traco, fill=white] (1.36,-2.9) rectangle (1.64,-2.45);
  \draw[traco] (1.5,-2.45) -- (1.5,0.3);
  \filldraw[traco, fill=white] (1.1,0.3) rectangle (1.9,0.55);
  \node[num] at (0.65,0.85) {1};
  % adutora até a casa química
  \draw[cano] (1.9,0.42) -- (3.7,0.42);
  % casa química
  \filldraw[traco, fill=white] (3.7,0) rectangle (5.6,1.35);
  \filldraw[traco, fill=white] (3.55,1.35) -- (4.65,1.95) -- (5.75,1.35) -- cycle;
  \node[nota, align=center] at (4.65,0.68) {cloração\\ e controle};
  \node[num] at (4.65,2.35) {2};
  % ligação ao reservatório
  \draw[cano] (5.6,0.42) -- (7.05,0.42) -- (7.05,2.75) -- (7.4,2.75);
  % reservatório elevado
  \draw[traco] (7.6,0) -- (7.75,2.2);
  \draw[traco] (9.0,0) -- (8.85,2.2);
  \draw[traco, line width=0.5pt] (7.68,1.1) -- (8.92,1.1);
  \fill[petroleo12] (7.4,2.2) rectangle (9.2,3.05);
  \draw[traco] (7.4,2.2) rectangle (9.2,3.6);
  \draw[traco, line width=0.5pt] (7.4,3.05) -- (9.2,3.05);
  \node[num] at (8.3,4.0) {3};
  % rede de distribuição
  \draw[cano, line width=1.6pt] (8.3,2.2) -- (8.3,-0.4) -- (14.9,-0.4);
  \node[num] at (8.75,-0.8) {4};
  % domicílios com hidrômetro
  \foreach \x in {10.9, 12.65, 14.4} {
    \draw[traco, line width=1.1pt] (\x-0.75,-0.4) -- (\x-0.75,0.15) -- (\x-0.45,0.15);
    \node[circle, draw=petroleo, fill=white, line width=0.7pt, inner sep=1.4pt] at (\x-0.75,0.15) {};
    \filldraw[traco, fill=white] (\x-0.45,0) rectangle (\x+0.45,0.8);
    \filldraw[traco, fill=white] (\x-0.6,0.8) -- (\x,1.25) -- (\x+0.6,0.8) -- cycle;
    \draw[traco, line width=0.6pt] (\x-0.15,0) rectangle (\x+0.15,0.45);
  }
  \node[num] at (10.15,0.75) {5};
  \node[num] at (15.25,0.55) {6};
  % legenda
  \begin{scope}[shift={(9.55,4.35)}]
    \foreach \n/\t [count=\k from 0] in {1/Poço tubular profundo com bomba submersa,
        2/{Casa de química: desinfecção por cloração}, 3/Reservatório, 4/Rede de distribuição,
        5/Ligação domiciliar com hidrômetro, 6/Domicílio atendido} {
      \node[num, minimum size=0.36cm, font=\fonte{7}{8}\bfseries] at (0.18,{-0.2-\k*0.42}) {\n};
      \node[anchor=west, font=\fonte{8}{9.4}] at (0.42,{-0.2-\k*0.42}) {\t};
    }
  \end{scope}
  % anotações
  \node[nota, align=left, anchor=west] at (1.95,-0.6) {outorga de uso e análises\\ físico-químicas e bacteriológicas};
  \node[nota, align=center] at (12.55,-1.05) {operação e manutenção pela entidade gestora};
\end{tikzpicture}
"""

# ------------------------------------------------------------------ esquema da solução individual de esgoto
F["f-esquema-esgoto"] = r"""
\begin{tikzpicture}[x=1cm,y=1cm,
   num/.style={circle, fill=petroleo, text=white, font=\fonte{8}{9}\bfseries, inner sep=0pt,
     minimum size=0.44cm},
   traco/.style={draw=petroleo, line width=0.8pt},
   cano/.style={draw=cinza60, line width=2pt},
   nota/.style={font=\fonte{7.5}{8.8}, text=cinza80}]
  \fill[cinza5] (0,0) rectangle (15.6,-2.9);
  \draw[cinza60, line width=1.2pt] (0,0) -- (15.6,0);
  % domicílio
  \filldraw[traco, fill=white] (0.3,0) rectangle (2.1,1.3);
  \filldraw[traco, fill=white] (0.1,1.3) -- (1.2,2.0) -- (2.3,1.3) -- cycle;
  \draw[traco, line width=0.6pt] (0.95,0) rectangle (1.45,0.75);
  \node[num] at (1.2,2.45) {1};
  % tubulação
  \draw[cano] (1.6,-0.45) -- (2.95,-0.45);
  % caixa de inspeção
  \fill[white] (2.95,-0.15) rectangle (3.55,-0.85);
  \draw[traco] (2.95,0) -- (2.95,-0.85) -- (3.55,-0.85) -- (3.55,0);
  \node[num] at (3.25,0.5) {2};
  \draw[cano] (3.55,-0.45) -- (4.3,-0.45);
  % tanque séptico com duas câmaras
  \fill[white] (4.3,-0.1) rectangle (7.3,-2.0);
  \fill[petroleo12] (4.32,-0.6) rectangle (7.28,-1.6);
  \fill[pattern=north east lines, pattern color=petroleo!70] (4.32,-1.6) rectangle (7.28,-1.98);
  \draw[traco] (4.3,0) -- (4.3,-2.0) -- (7.3,-2.0) -- (7.3,0);
  \draw[traco, line width=0.7pt] (5.9,-0.1) -- (5.9,-1.5);
  \node[nota, fill=white, inner sep=1pt] at (6.6,-1.79) {lodo};
  \node[num] at (5.8,0.5) {3};
  \draw[cano] (7.3,-0.5) -- (8.05,-0.5);
  % filtro anaeróbio
  \fill[white] (8.05,-0.1) rectangle (10.05,-2.0);
  \fill[pattern=crosshatch dots, pattern color=petroleo] (8.07,-0.8) rectangle (10.03,-1.75);
  \draw[traco] (8.05,0) -- (8.05,-2.0) -- (10.05,-2.0) -- (10.05,0);
  \node[num] at (9.05,0.5) {4};
  \draw[cano] (10.05,-0.55) -- (11.0,-0.55);
  % disposição final no solo
  \draw[traco, line width=0.6pt] (11.0,-0.3) -- (11.0,-1.0) -- (15.1,-1.0) -- (15.1,-0.3);
  \draw[cano, dash pattern=on 4pt off 2pt] (11.0,-0.55) -- (15.0,-0.55);
  \foreach \x in {11.5,12.3,13.1,13.9,14.7}
    \draw[-{Latex[length=1.6mm]}, draw=petroleo, line width=0.7pt] (\x,-1.05) -- (\x,-1.85);
  \node[num] at (13.05,0.5) {5};
  % legenda
  \begin{scope}[shift={(0.1,-3.35)}]
    \foreach \n/\t/\x/\y in {1/Domicílio/0/0, 2/Caixa de inspeção/3.2/0,
        3/{Tanque séptico, com remoção periódica do lodo}/7.4/0, 4/Filtro anaeróbio/0/-0.5,
        5/{Disposição final no solo (vala de infiltração ou sumidouro)}/3.2/-0.5} {
      \node[num, minimum size=0.36cm, font=\fonte{7}{8}\bfseries] at (\x+0.18,\y) {\n};
      \node[anchor=west, font=\fonte{8}{9.4}] at (\x+0.42,\y) {\t};
    }
  \end{scope}
  \node[text=cinza80, anchor=north, text width=15cm, align=center] at (7.8,-4.25)
    {Exemplo ilustrativo. A solução de cada domicílio é definida no projeto individual, conforme a
     ABNT NBR 17076:2024, as condições do terreno e o número de moradores.};
\end{tikzpicture}
"""


def escrever():
    for nome, corpo in F.items():
        with open(os.path.join(FIG, nome + ".tex"), "w", encoding="utf-8") as f:
            f.write(CAB + corpo + FIM)
    print(len(F), "figuras escritas")


if __name__ == "__main__":
    escrever()
