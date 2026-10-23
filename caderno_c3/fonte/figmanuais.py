"""Fluxogramas e esquemas desenhados à mão (TikZ) para a Atividade 3.2.2."""
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(AQUI, "fig")
CAB = "\\documentclass[11pt,border=4pt]{standalone}\n\\input{estilo}\n\\begin{document}\n"
FIM = "\n\\end{document}\n"

F = {}

# ------------------------------------------------------------------ articulação das ações
F["f-articulacao"] = r"""
\begin{tikzpicture}[
  acao/.style={etapa=4.75cm, minimum height=1.45cm},
  acao1/.style={etapa=4.4cm, minimum height=1.45cm},
  sane/.style={draw=cBlue, fill=cBlueBg, rounded corners=2pt, align=center, inner sep=3.5pt,
    minimum height=1.45cm, text width=4.75cm, line width=0.6pt},
  ext/.style={externo=4.75cm, minimum height=1.05cm},
  ext1/.style={externo=4.4cm, minimum height=1.05cm},
  lig/.style={font=\tiny\itshape, text=cGrayText, fill=white, inner sep=1pt, align=center}
]
  \node[cab=4.4cm] (h1) at (2.45,0) {Preparação};
  \node[cab=5.7cm] (h2) at (9.1,0) {Implantação};
  \node[cab=2.9cm, fill=cTeal] (h3) at (13.925,0) {Resultado};

  \node[ext1] (x1) at (2.45,-1.2) {\textbf{Atividade 3.2.1}\\ {\scriptsize política e plano estadual de saneamento rural}};
  \node[ext] (x3) at (8.625,-1.2) {\textbf{Subcomponente 1.1}\\ {\scriptsize outorga, SIGARH e águas subterrâneas}};

  \node[acao1] (a1) at (2.45,-3.05) {\textbf{3.2.2.1 Modelos de gestão}\\
    {\scriptsize pactuação, associações e tarifa\\ 3 unidades regionais, R\$ 6,90 mi}};
  \node[acao1] (a2) at (2.45,-5.15) {\textbf{3.2.2.2 Trabalho técnico-social}\\
    {\scriptsize mobilização, cadastro e adesão\\ 36 profissionais-mês, R\$ 6,47 mi}};
  \node[ext1] (x2) at (2.45,-7.25) {\textbf{Subcomponente 2.3}\\ {\scriptsize Planos Integrados de Propriedade (IDR-Paraná)}};

  \node[acao] (b1) at (8.625,-3.05) {\textbf{3.2.2.3 Sistemas de água}\\
    {\scriptsize 83 sistemas, 5.810 domicílios\\ R\$ 107,90 mi}};
  \node[acao] (b2) at (8.625,-5.15) {\textbf{3.2.2.5 Esgoto nas comunidades}\\
    {\scriptsize 4.067 domicílios\\ R\$ 32,54 mi}};
  \node[acao] (b3) at (8.625,-7.25) {\textbf{3.2.2.6 Esgoto em mananciais}\\
    {\scriptsize 2.300 domicílios (área do IDR-Paraná)\\ R\$ 18,40 mi}};
  \node[sane] (b4) at (8.625,-9.35) {\textbf{3.2.2.4 Programa Sanepar Rural}\\
    {\scriptsize 222 sistemas\\ R\$ 67,15 mi de contrapartida}};

  \node[draw=cNavy, fill=cNavy!7, dashed, rounded corners=2pt, line width=0.6pt,
        fit={(11.3,-2.3) (12.02,-8.0)}, inner sep=0pt] (band) {};
  \node[rotate=90, font=\scriptsize, text=cNavy, align=center] at (band.center)
    {\textbf{3.2.2.7 Supervisão das obras}\\ R\$ 10,79 mi};

  \node[marcoteal=2.9cm, minimum height=1.2cm] (c1) at (13.925,-3.05) {Sistemas entregues às entidades gestoras};
  \node[etapa=2.9cm, minimum height=1.2cm] (c2) at (13.925,-5.15) {Operação com tarifa e apoio das unidades regionais};
  \node[draw=cTeal, fill=white, rounded corners=2pt, align=center, text width=2.9cm,
        inner sep=3.5pt, minimum height=1.3cm] (c3) at (13.925,-7.6)
        {\textbf{Indicadores do Componente 3}\\ {\scriptsize pessoas com água gerida de forma segura, pessoas com esgotamento sanitário e associações com modelo de gestão}};

  \draw[seta] (x1) -- (a1) node[lig, midway] {diretrizes};
  \draw[seta] (x3) -- (b1) node[lig, midway] {outorga};
  \draw[seta] (a1) -- (a2) node[lig, midway] {municípios aderidos};
  \draw[seta] (a1) -- (b1) node[lig, midway, above=2pt] {entidade\\ gestora};
  \draw[seta] (a2.north east) -- (b1.south west) node[lig, pos=0.5] {diagnóstico};
  \draw[seta] (a2) -- (b2) node[lig, midway, below=2pt] {domicílios\\ sem esgoto};
  \draw[seta] (b1) -- (b2) node[lig, midway] {mesmas comunidades};
  \draw[seta] (x2) -- (b3) node[lig, midway, above=2pt] {domicílios\\ indicados};
  \draw[seta] (band.east |- c1) -- (c1.west);
  \draw[seta] (c1) -- (c2);
  \draw[seta] (c2) -- (c3);
  \draw[seta] (b4.east) -- (12.18,-9.35) |- (c3.west);
  \draw[setatracejada] (a1.west) -- ++(-0.2,0) |- (b4.west)
    node[lig, pos=0.78, above=2pt] {modelo de gestão para as associações do Sanepar Rural};

  \begin{scope}[shift={(0.1,-10.65)}]
    \fill[cTealBg, draw=cTeal] (0,0) rectangle (0.35,0.25);
    \node[anchor=west, font=\scriptsize] at (0.45,0.125) {Ações do IAT (empréstimo BIRD)};
    \fill[cBlueBg, draw=cBlue] (5.2,0) rectangle (5.55,0.25);
    \node[anchor=west, font=\scriptsize] at (5.65,0.125) {Ação da Sanepar (contrapartida)};
    \fill[cGrayBg, draw=cGrayLine] (10.4,0) rectangle (10.75,0.25);
    \node[anchor=west, font=\scriptsize] at (10.85,0.125) {Outras partes do Programa};
  \end{scope}
\end{tikzpicture}
"""

# ------------------------------------------------------------------ alternativas de modelo de gestão
F["f-alternativas"] = r"""
\begin{tikzpicture}[node distance=0.28cm,
    cel/.style={draw=cTeal!70, fill=white, align=center, font=\scriptsize,
                text width=3.95cm, minimum height=1.2cm, inner sep=3pt, rounded corners=1pt},
    rot/.style={font=\scriptsize\bfseries, text=cNavy, align=right, text width=1.85cm, anchor=east}]
  \node[marco=3.95cm, minimum height=1.0cm] (a0) at (0,0) {Associação de moradores};
  \node[marco=3.95cm, minimum height=1.0cm, right=0.32cm of a0] (b0) {Central de associações};
  \node[marco=3.95cm, minimum height=1.0cm, right=0.32cm of b0] (c0) {Consórcio público};

  \node[cel, below=of a0] (a1) {Moradores organizados operam o sistema da localidade, com apoio da prefeitura};
  \node[cel, below=of b0] (b1) {Associações filiadas a uma central que presta apoio técnico, administrativo e financeiro};
  \node[cel, below=of c0] (c1) {Municípios consorciados prestam o serviço de forma associada};

  \node[cel, below=of a1] (a2) {MROSC\\ (Lei nº 13.019/2014)};
  \node[cel, below=of b1] (b2) {MROSC; Decreto nº 11.599/2023;\\ Portaria nº 2.777/2025};
  \node[cel, below=of c1] (c2) {Lei dos Consórcios Públicos\\ (Lei nº 11.107/2005)};

  \node[cel, below=of a2] (a3) {Acordo de Cooperação, após lei municipal que autoriza a cessão dos ativos};
  \node[cel, below=of b2] (b3) {Acordo de Cooperação com o poder público, após lei municipal autorizativa};
  \node[cel, below=of c2] (c3) {Alteração do contrato de consórcio; contratos de programa e de rateio; cessão de uso dos ativos};

  \node[cel, fill=cGrayBg, below=of a3] (a4) {Associações de moradores que já operam sistemas no Paraná};
  \node[cel, fill=cGrayBg, below=of b3] (b4) {SISAR (CE): 1,13 milhão de pessoas em 1.466 localidades; Centrais (BA)};
  \node[cel, fill=cGrayBg, below=of c3] (c4) {CISPAR: 112 municípios consorciados no Paraná};

  \node[rot] at ($(a1.west)+(-0.12,0)$) {Como funciona};
  \node[rot] at ($(a2.west)+(-0.12,0)$) {Amparo legal};
  \node[rot] at ($(a3.west)+(-0.12,0)$) {Instrumento};
  \node[rot] at ($(a4.west)+(-0.12,0)$) {Referência};

  \node[transversal=12.3cm, below=0.55cm of b4, font=\scriptsize] (r) {Em todas as alternativas: definição com a prefeitura
    e a comunidade, abordagem participativa, tarifa com tarifa social e capacitação dos operadores};
  \foreach \n in {a4, b4, c4} \draw[seta] (\n) -- (\n |- r.north);
\end{tikzpicture}
"""

# ------------------------------------------------------------------ seleção e adesão, por responsável
F["f-adesao"] = r"""
\begin{tikzpicture}[passo/.style={etapa=2.25cm, minimum height=1.05cm, font=\scriptsize}]
  \foreach \i/\t in {0/IAT, 1/Município, 2/Comunidade} {
    \node[raia=15.35cm, minimum height=1.9cm] at (0,{-\i*1.95}) {};
    \node[tituloraia] at (0.9,{-\i*1.95-0.95}) {\t};
  }
  \draw[cGrayLine] (1.8,0) -- (1.8,-5.8);
  \node[passo] (p1) at (3.25,-0.95)  {Definição dos critérios de seleção};
  \node[passo] (p2) at (5.95,-0.95)  {Seleção das áreas e das comunidades};
  \node[passo] (p3) at (8.65,-0.95)  {Sensibilização das prefeituras};
  \node[passo] (p6) at (14.05,-0.95) {Contato inicial com a comunidade};
  \node[passo] (p4) at (8.65,-2.9)   {Adesão formal ao Programa};
  \node[passo] (p5) at (11.35,-2.9)  {Termo de Cooperação com o IAT};
  \node[passo] (p7) at (14.05,-4.85) {Pré-adesão da comunidade};
  \draw[seta] (p1) -- (p2);
  \draw[seta] (p2) -- (p3);
  \draw[seta] (p3) -- (p4);
  \draw[seta] (p4) -- (p5);
  \draw[seta] (p5.north) |- (p6.west);
  \draw[seta] (p6) -- (p7);
  \node[rotulo, fill=none, below=2pt of p2] {lista preliminar};
  \node[rotulo, fill=none, below=2pt of p5] {termo assinado};
  \node[rotulo, fill=none, left=2pt of p7, align=right] {contratos de\\ pré-adesão};
\end{tikzpicture}
"""

# ------------------------------------------------------------------ trabalho técnico-social
F["f-tts"] = r"""
\begin{tikzpicture}[node distance=0.36cm,
    passo/.style={etapa=5.9cm, minimum height=0.9cm},
    liga/.style={draw=cTeal!60, densely dotted, line width=0.7pt}]
  \node[passo] (t1) {\textbf{Contratação da empresa}\\ {\scriptsize Termo de Referência, edital e licitação}};
  \node[passo, below=of t1] (t2) {\textbf{Mobilização e sensibilização}\\ {\scriptsize municípios, comunidades, associações e proprietários}};
  \node[passo, below=of t2] (t3) {\textbf{Busca ativa e cadastro domiciliar}\\ {\scriptsize visita a todos os domicílios, inclusive em áreas remotas}};
  \node[passo, below=of t3] (t4) {\textbf{Diagnóstico coletivo e domiciliar}\\ {\scriptsize formas atuais de abastecimento e de esgotamento}};
  \node[passo, below=of t4] (t5) {\textbf{Enquadramento das famílias}\\ {\scriptsize critérios sociais, territoriais e técnicos}};
  \node[passo, below=of t5] (t6) {\textbf{Termos de adesão}\\ {\scriptsize compromisso com o uso e a manutenção}};
  \node[passo, below=of t6] (t7) {\textbf{Educação sanitária e ambiental}\\ {\scriptsize lideranças capacitadas e acompanhamento das obras}};
  \node[marco=5.9cm, below=of t7] (t8) {Relatório final e baixa no Termo de Cooperação};
  \foreach \a/\b in {t1/t2,t2/t3,t3/t4,t4/t5,t5/t6,t6/t7,t7/t8}
    \draw[seta] (\a) -- (\b);

  \node[produto=3.1cm, right=0.75cm of t1] (q1) {Contrato assinado};
  \node[produto=3.1cm, right=0.75cm of t2] (q2) {Atas e listas de presença};
  \node[produto=3.1cm, right=0.75cm of t3] (q3) {Cadastro domiciliar georreferenciado};
  \node[produto=3.1cm, right=0.75cm of t4] (q4) {Diagnóstico por comunidade e por domicílio};
  \node[produto=3.1cm, right=0.75cm of t5] (q5) {Famílias a serem atendidas};
  \node[produto=3.1cm, right=0.75cm of t6] (q6) {Termos de adesão assinados};
  \node[produto=3.1cm, right=0.75cm of t7] (q7) {Listas de presença e certificados};
  \node[produto=3.1cm, right=0.75cm of t8] (q8) {Relatório aprovado pelo IAT e pelo IDR-Paraná};
  \foreach \a/\b in {t1/q1,t2/q2,t3/q3,t4/q4,t5/q5,t6/q6,t7/q7,t8/q8}
    \draw[liga] (\a) -- (\b);

  \node[externo=3.05cm, left=0.75cm of t4, font=\scriptsize] (u1) {Captação e projeto do sistema de água (Ação 3.2.2.3)};
  \node[externo=3.05cm, left=0.75cm of t5, font=\scriptsize] (u2) {Esgotamento nas comunidades (Ação 3.2.2.5)};
  \node[externo=3.05cm, left=0.75cm of t6, font=\scriptsize] (u3) {Associações e modelo de gestão (Ação 3.2.2.1)};
  \draw[setatracejada] (t4) -- (u1);
  \draw[setatracejada] (t5) -- (u2);
  \draw[setatracejada] (t6) -- (u3);
  \node[font=\scriptsize\bfseries, text=cTeal, above=0.08cm of q1] {Produtos};
  \node[font=\scriptsize\bfseries, text=cGrayText, above=0.08cm of u1] {Quem usa o resultado};
\end{tikzpicture}
"""


def funil(camadas, resultado, nota):
    """Funil de critérios: camadas = [(texto, cor, cor_texto)], de cima para baixo."""
    L = [r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    h, gap = 1.05, 0.09
    w0, dw = 15.4, 1.45
    y = 0.0
    for i, (txt, cor, ct) in enumerate(camadas):
        wt = w0 - i * (dw + 0.0)
        wb = wt - dw
        L.append(rf"  \fill[{cor}] ({-wt/2},{y}) -- ({wt/2},{y}) -- ({wb/2},{y-h}) -- ({-wb/2},{y-h}) -- cycle;")
        L.append(rf"  \node[text width={(wt+wb)/2-2.0:.2f}cm, align=center, font=\footnotesize, text={ct}] at (0,{y-h/2}) {{{txt}}};")
        y -= h + gap
    wb = w0 - len(camadas) * dw
    L.append(rf"  \draw[seta] (0,{y+gap}) -- (0,{y-0.35});")
    L.append(rf"  \node[marco=7.2cm, minimum height=1.05cm, anchor=north] at (0,{y-0.35}) {{{resultado}}};")
    if nota:
        L.append(rf"  \node[font=\scriptsize\itshape, text=cGrayText, anchor=north, text width=12cm, align=center] at (0,{y-1.65}) {{{nota}}};")
    L.append(r"\end{tikzpicture}")
    return "\n".join(L)


F["f-selecao-comunidades"] = funil(
    [("Comunidades rurais de todo o Paraná, nas Microrregiões de Água e Esgoto", "cTeal!10", "cText"),
     (r"Comunidade ou conjunto de comunidades com 70 ou mais domicílios ocupados", "cTeal!22", "cText"),
     (r"Município com IPDM de 0,4 a menos de 0,8 (médio baixo ou médio desempenho)", "cTeal!38", "cText"),
     (r"Pedido do município ao IAT ou associação com sistema a complementar", "cTeal!62", "white"),
     (r"Sem impedimento à perfuração: aquífero, geologia, qualidade da água e restrições legais", "cTeal!88", "white")],
    r"Seleção preliminar: 83 comunidades\\ \normalfont\scriptsize 5.810 domicílios, cerca de 16,3 mil pessoas",
    r"A lista final é confirmada pelo trabalho técnico-social (Ação 3.2.2.2) e pela viabilidade do poço (Etapa 2).")

F["f-selecao-mananciais"] = funil(
    [("Microbacias prioritárias do PSH-PR", "cTeal!10", "cText"),
     (r"Mananciais de abastecimento público selecionados por critério quali-quantitativo", "cTeal!22", "cText"),
     (r"Domicílios rurais permanentes ocupados (Censo 2022 e CNEFE)", "cTeal!38", "cText"),
     (r"Domicílios sem destinação adequada do esgoto", "cTeal!62", "white"),
     (r"Propriedade com diagnóstico e adesão ao PSH-PR e ao IDR-Paraná", "cTeal!88", "white")],
    r"2.236 domicílios em nove mananciais\\ \normalfont\scriptsize 2.300 adotados para o dimensionamento",
    r"O arredondamento absorve as incertezas das bases, as variações cadastrais e as demandas futuras.")

# ------------------------------------------------------------------ esquema do sistema coletivo de água
F["f-esquema-saa"] = r"""
\begin{tikzpicture}[x=1cm,y=1cm,
   num/.style={circle, fill=cNavy, text=white, font=\scriptsize\bfseries, inner sep=1.2pt, minimum size=0.42cm}]
  % solo e aquífero
  \fill[cAmberBg] (0,0) rectangle (15.6,-3.5);
  \fill[cBlueBg] (0,-2.35) rectangle (15.6,-3.5);
  \fill[pattern=dots, pattern color=cBlue!45] (0,-2.35) rectangle (15.6,-3.5);
  \node[font=\scriptsize\itshape, text=cBlue, anchor=west] at (2.3,-2.95) {aquífero (água subterrânea)};
  \node[font=\scriptsize\itshape, text=cAmber, anchor=west] at (2.3,-1.3) {solo e rocha};
  \draw[cGreen, line width=1.4pt] (0,0) -- (15.6,0);
  % poço
  \fill[white] (1.25,0.3) rectangle (1.75,-3.1);
  \draw[cNavy, line width=0.7pt] (1.25,0.3) -- (1.25,-3.1) -- (1.75,-3.1) -- (1.75,0.3);
  \draw[cNavy, line width=0.6pt, dash pattern=on 2pt off 1.5pt] (1.25,-2.45) -- (1.25,-3.05);
  \draw[cNavy, line width=0.6pt, dash pattern=on 2pt off 1.5pt] (1.75,-2.45) -- (1.75,-3.05);
  \fill[cBlue!35] (1.27,-1.9) rectangle (1.73,-3.08);
  \fill[cNavy] (1.36,-2.9) rectangle (1.64,-2.45);
  \draw[cNavy, line width=1pt] (1.5,-2.45) -- (1.5,0.3);
  \fill[cNavy] (1.1,0.3) rectangle (1.9,0.55);
  \node[num] at (0.65,0.85) {1};
  % adutora até a casa química
  \draw[cBlue, line width=2.2pt] (1.9,0.42) -- (3.7,0.42);
  % casa química
  \fill[white] (3.7,0) rectangle (5.6,1.35);
  \draw[cNavy, line width=0.7pt] (3.7,0) rectangle (5.6,1.35);
  \fill[cNavy] (3.55,1.35) -- (4.65,1.95) -- (5.75,1.35) -- cycle;
  \node[font=\tiny, align=center] at (4.65,0.68) {cloração\\ e controle};
  \node[num] at (4.65,2.35) {2};
  % ligação ao reservatório
  \draw[cBlue, line width=2.2pt] (5.6,0.42) -- (7.05,0.42) -- (7.05,2.75) -- (7.4,2.75);
  % reservatório elevado
  \draw[cNavy, line width=0.9pt] (7.6,0) -- (7.75,2.2);
  \draw[cNavy, line width=0.9pt] (9.0,0) -- (8.85,2.2);
  \draw[cNavy, line width=0.5pt] (7.68,1.1) -- (8.92,1.1);
  \fill[cBlueBg] (7.4,2.2) rectangle (9.2,3.05);
  \draw[cNavy, line width=0.8pt] (7.4,2.2) rectangle (9.2,3.6);
  \draw[cBlue, line width=0.5pt] (7.4,3.05) -- (9.2,3.05);
  \node[num] at (8.3,4.0) {3};
  % rede de distribuição
  \draw[cBlue, line width=1.8pt] (8.3,2.2) -- (8.3,-0.4) -- (14.9,-0.4);
  \node[num] at (9.6,-0.85) {4};
  % casas com hidrômetro
  \foreach \x in {10.9, 12.65, 14.4} {
    \draw[cBlue, line width=1.1pt] (\x-0.75,-0.4) -- (\x-0.75,0.15) -- (\x-0.45,0.15);
    \node[circle, draw=cNavy, fill=white, line width=0.6pt, inner sep=1.4pt] at (\x-0.75,0.15) {};
    \fill[white] (\x-0.45,0) rectangle (\x+0.45,0.8);
    \draw[cNavy, line width=0.7pt] (\x-0.45,0) rectangle (\x+0.45,0.8);
    \fill[cTeal] (\x-0.6,0.8) -- (\x,1.25) -- (\x+0.6,0.8) -- cycle;
    \fill[cBlueBg] (\x-0.15,0) rectangle (\x+0.15,0.45);
  }
  \node[num] at (10.15,0.75) {5};
  \node[num] at (15.25,0.55) {6};
  % legenda
  \begin{scope}[shift={(10.0,4.3)}]
    \node[anchor=north west, align=left, font=\scriptsize, text width=5.5cm, inner sep=0pt] at (0,0) {
      \textbf{1} Poço tubular profundo com bomba submersa\\[1pt]
      \textbf{2} Casa química: cloração da água\\[1pt]
      \textbf{3} Reservatório\\[1pt]
      \textbf{4} Rede de distribuição\\[1pt]
      \textbf{5} Ligação domiciliar com hidrômetro\\[1pt]
      \textbf{6} Domicílio atendido};
  \end{scope}
  % anotações
  \node[font=\tiny\itshape, text=cGrayText, align=left, anchor=west] at (1.95,-0.55) {outorga de uso e análises\\ físico-químicas e bacteriológicas};
  \node[font=\tiny\itshape, text=cGrayText, align=center] at (12.65,-0.85) {operação e manutenção pela entidade gestora};
\end{tikzpicture}
"""

# ------------------------------------------------------------------ captação, projeto e licenciamento
F["f-captacao"] = r"""
\begin{tikzpicture}[node distance=0.32cm,
    passo/.style={etapa=5.35cm, minimum height=0.82cm, font=\scriptsize}]
  \node[cab=5.35cm, fill=cTeal] (h1) at (0,0) {Captação subterrânea (Etapas 1 e 2)};
  \node[passo, below=0.3cm of h1] (c1) {Estudos preliminares: viabilidade, titularidade e situação fundiária das áreas};
  \node[passo, below=of c1] (c2) {Estudos geológicos e hidrogeológicos; locação e projeto construtivo do poço};
  \node[passo, below=of c2] (c3) {Anuência prévia de perfuração};
  \node[passo, below=of c3] (c4) {Perfuração do poço};
  \node[passo, below=of c4] (c5) {Teste de vazão e análises físico-químicas e bacteriológicas};
  \node[decisao, text width=1.9cm, below=0.4cm of c5] (d1) {Vazão e qualidade suficientes?};
  \node[correcao=2.4cm, left=0.55cm of d1] (k1) {Nova locação ou substituição da comunidade};
  \node[passo, below=0.4cm of d1] (c6) {Estudos ambientais e sociais e outorga de direito de uso da água};

  \node[cab=5.35cm, fill=cNavy] (h2) at (7.6,0) {Projeto e licenciamento (Etapa 3)};
  \node[passo] (p1) at (h2 |- c1) {Anteprojeto da solução de tratamento e de reservação};
  \node[passo] (p2) at (h2 |- c2) {Contratação integrada (projetos executivos e obras)};
  \node[passo] (p3) at (h2 |- c3) {Projeto básico: casa química, reservatório, eletromecânica e rede};
  \node[passo] (p4) at (h2 |- c4) {Projeto executivo};
  \node[passo] (p5) at (h2 |- c5) {Aprovação dos projetos pelo IAT};
  \node[passo] (p6) at (h2 |- c6) {Estudos ambientais e sociais e obtenção das licenças};

  \coordinate (meio) at ($(c6.south)!0.5!(p6.south)$);
  \node[marco=12.6cm, below=0.6cm of meio] (obra) {Execução das obras (Etapa 4), somente com outorga e licenças obtidas};

  \foreach \a/\b in {c1/c2,c2/c3,c3/c4,c4/c5,c5/d1,p1/p2,p2/p3,p3/p4,p4/p5,p5/p6}
    \draw[seta] (\a) -- (\b);
  \draw[seta] (d1) -- node[rotulo, right] {Sim} (c6);
  \draw[seta] (d1) -- node[rotulo, above] {Não} (k1);
  \draw[seta] (k1.north) |- (c2.west);
  \draw[seta] (c5.east) -- ++(0.55,0) |- (p1.west);
  \node[rotate=90, font=\tiny\itshape, text=cGrayText, anchor=south] at ($(c5.east)+(0.53,1.75)$) {vazão e qualidade orientam o projeto};
  \draw[seta] (c6.south) -- (c6.south |- obra.north);
  \draw[seta] (p6.south) -- (p6.south |- obra.north);
\end{tikzpicture}
"""

# ------------------------------------------------------------------ execução das obras, por responsável
F["f-obras"] = r"""
\begin{tikzpicture}[passo/.style={etapa=2.15cm, minimum height=1.05cm, font=\scriptsize}]
  \foreach \i/\t in {0/Executor da obra, 1/Supervisora (Ação 3.2.2.7), 2/Fiscalização do IAT} {
    \node[raia=15.35cm, minimum height=1.9cm] at (0,{-\i*1.95}) {};
    \node[tituloraia] at (0.9,{-\i*1.95-0.95}) {\t};
  }
  \draw[cGrayLine] (1.8,0) -- (1.8,-5.8);
  \node[passo] (o1) at (3.2,-4.85)  {Ordem de serviço e designação do fiscal};
  \node[passo] (o2) at (5.75,-0.95) {Execução da obra conforme o projeto};
  \node[passo] (o3) at (5.75,-2.9)  {Acompanhamento e relatório mensal};
  \node[passo] (o4) at (8.4,-4.85)  {Verificação e relatório de fiscalização};
  \node[decisao, text width=1.35cm] (d) at (11.2,-4.85) {Conforme projeto e normas?};
  \node[correcao=2.15cm] (o5) at (11.2,-0.95) {Correção das não conformidades};
  \node[marco=2.15cm, minimum height=1.05cm, font=\scriptsize\bfseries] (o7) at (14.3,-4.85) {Atesto de recebimento, laudos e \textit{as built}};
  \draw[seta] (o1) |- (o2);
  \draw[seta] (o2) -- (o3);
  \draw[seta] (o3.south) |- (o4.west);
  \draw[seta] (o4) -- (d);
  \draw[seta] (d) -- node[rotulo, right] {Não} (o5);
  \draw[seta] (o5.west) -| (o4.north);
  \draw[seta] (d) -- node[rotulo, above] {Sim} (o7);
\end{tikzpicture}
"""

# ------------------------------------------------------------------ pré-operação, entrega e operação
F["f-entrega"] = r"""
\begin{tikzpicture}[node distance=0.1cm,
    ida/.style={fase=2.95cm, font=\scriptsize\bfseries},
    volta/.style={fase=2.95cm, signal to=west, signal from=east, fill=cBlueBg, draw=cBlue, font=\scriptsize\bfseries}]
  \node[ida] (e1) {Pré-operação\\ e testes};
  \node[ida, right=of e1] (e2) {Capacitação dos\\ operadores locais};
  \node[ida, right=of e2] (e3) {Reunião técnica\\ de entrega};
  \node[ida, right=of e3] (e4) {Aceite da\\ entidade gestora};
  \node[volta, below=1.2cm of e4] (e5) {Operação pela\\ entidade gestora};
  \node[volta, left=of e5] (e6) {Suporte técnico\\ pós-implantação};
  \node[volta, left=of e6] (e7) {Avaliação semestral\\ de desempenho};
  \node[volta, fill=cNavy, draw=cNavy, text=white, left=of e7] (e8) {TRD e encerramento\\ do Termo de Cooperação};
  \draw[seta] (e4.south) -- (e5.north);
  \node[produto=2.9cm, above=0.25cm of e1] {laudos e testes de funcionamento};
  \node[produto=2.9cm, above=0.25cm of e2] {listas de presença e certificados};
  \node[produto=2.9cm, above=0.25cm of e4] {termo de aceite assinado};
  \node[produto=2.9cm, below=0.25cm of e7] {relatórios no SIGARH e no GeoPR};
  \node[produto=2.9cm, below=0.25cm of e8] {relatório final e prestação de contas};
  \node[font=\scriptsize\bfseries, text=cTeal, anchor=south west] at ($(e3.north west)+(0,0.3)$) {Transferência do sistema};
  \node[font=\scriptsize\bfseries, text=cBlue, anchor=north west] at ($(e5.south west)+(0,-0.3)$) {Operação e encerramento};
\end{tikzpicture}
"""

# ------------------------------------------------------------------ Programa Sanepar Rural, por responsável
F["f-sanepar"] = r"""
\begin{tikzpicture}[passo/.style={etapa=2.25cm, minimum height=1.05cm, font=\scriptsize},
    passos/.style={draw=cBlue, fill=cBlueBg, rounded corners=2pt, align=center, inner sep=3.5pt,
      minimum height=1.05cm, text width=2.25cm, font=\scriptsize, line width=0.6pt}]
  \foreach \i/\t in {0/Sanepar, 1/Município, 2/Comunidade} {
    \node[raia=15.35cm, minimum height=1.9cm] at (0,{-\i*1.95}) {};
    \node[tituloraia] at (0.9,{-\i*1.95-0.95}) {\t};
  }
  \draw[cGrayLine] (1.8,0) -- (1.8,-5.8);
  \node[passos] (s1) at (3.25,-0.95)  {Levantamento e estudo técnico de engenharia};
  \node[passos] (s3) at (5.95,-0.95)  {Projeto de engenharia do sistema};
  \node[passos] (s4) at (8.65,-0.95)  {Fornecimento de materiais hidráulicos};
  \node[passos] (s8) at (14.05,-0.95) {Monitoramento e suporte pós-obra};
  \node[passo] (s2) at (3.25,-2.9)    {Termo de Compromisso e Responsabilidade};
  \node[passo] (s5) at (8.65,-2.9)    {Execução das obras, com apoio técnico da Sanepar};
  \node[passo] (s6) at (11.35,-4.85)  {Formação da associação de moradores};
  \node[passo] (s7) at (14.05,-4.85)  {Treinamento e educação ambiental};
  \draw[seta] (s1) -- (s2);
  \draw[seta] (s2.east) -| (s3.south);
  \draw[seta] (s3) -- (s4);
  \draw[seta] (s4) -- (s5);
  \draw[seta] (s5.south) |- (s6.west);
  \draw[seta] (s6) -- (s7);
  \draw[seta] (s7) -- (s8);
\end{tikzpicture}
"""

# ------------------------------------------------------------------ esquema da solução individual de esgoto
F["f-esquema-esgoto"] = r"""
\begin{tikzpicture}[x=1cm,y=1cm,
   num/.style={circle, fill=cNavy, text=white, font=\scriptsize\bfseries, inner sep=1.2pt, minimum size=0.42cm}]
  \fill[cAmberBg] (0,0) rectangle (15.6,-2.9);
  \draw[cGreen, line width=1.4pt] (0,0) -- (15.6,0);
  % casa
  \fill[white] (0.3,0) rectangle (2.1,1.3);
  \draw[cNavy, line width=0.7pt] (0.3,0) rectangle (2.1,1.3);
  \fill[cTeal] (0.1,1.3) -- (1.2,2.0) -- (2.3,1.3) -- cycle;
  \fill[cBlueBg] (0.95,0) rectangle (1.45,0.75);
  \node[num] at (1.2,2.45) {1};
  % tubulação
  \draw[cGrayText, line width=2pt] (1.6,-0.45) -- (2.95,-0.45);
  % caixa de inspeção
  \fill[white] (2.95,-0.15) rectangle (3.55,-0.85);
  \draw[cNavy, line width=0.7pt] (2.95,0) -- (2.95,-0.85) -- (3.55,-0.85) -- (3.55,0);
  \node[num] at (3.25,0.5) {2};
  \draw[cGrayText, line width=2pt] (3.55,-0.45) -- (4.3,-0.45);
  % tanque séptico com duas câmaras
  \fill[white] (4.3,-0.1) rectangle (7.3,-2.0);
  \fill[cAmber!35] (4.32,-1.6) rectangle (7.28,-1.98);
  \fill[cBlue!15] (4.32,-0.6) rectangle (7.28,-1.6);
  \draw[cNavy, line width=0.8pt] (4.3,0) -- (4.3,-2.0) -- (7.3,-2.0) -- (7.3,0);
  \draw[cNavy, line width=0.7pt] (5.9,-0.1) -- (5.9,-1.5);
  \node[font=\tiny, text=cAmber] at (5.8,-1.79) {lodo};
  \node[num] at (5.8,0.5) {3};
  \draw[cGrayText, line width=2pt] (7.3,-0.5) -- (8.05,-0.5);
  % filtro anaeróbio
  \fill[white] (8.05,-0.1) rectangle (10.05,-2.0);
  \fill[pattern=crosshatch dots, pattern color=cGrayText] (8.07,-0.8) rectangle (10.03,-1.75);
  \draw[cNavy, line width=0.8pt] (8.05,0) -- (8.05,-2.0) -- (10.05,-2.0) -- (10.05,0);
  \node[num] at (9.05,0.5) {4};
  \draw[cGrayText, line width=2pt] (10.05,-0.55) -- (11.0,-0.55);
  % disposição final no solo
  \draw[cNavy, line width=0.6pt] (11.0,-0.3) -- (11.0,-1.0) -- (15.1,-1.0) -- (15.1,-0.3);
  \draw[cGrayText, line width=2pt, dash pattern=on 4pt off 2pt] (11.0,-0.55) -- (15.0,-0.55);
  \foreach \x in {11.5,12.3,13.1,13.9,14.7}
    \draw[-{Stealth[length=1.6mm]}, cBlue, decorate, decoration={snake, amplitude=0.6pt, segment length=4pt}] (\x,-1.05) -- (\x,-1.9);
  \node[num] at (13.05,0.5) {5};
  % legenda
  \node[anchor=north west, align=left, font=\scriptsize, text width=15.4cm, inner sep=0pt] at (0.1,-3.15) {
    \textbf{1} Domicílio \qquad \textbf{2} Caixa de inspeção \qquad
    \textbf{3} Tanque séptico, com remoção periódica do lodo\\[2pt]
    \textbf{4} Filtro anaeróbio \qquad
    \textbf{5} Disposição final no solo (vala de infiltração ou sumidouro)};
  \node[transversal=14.8cm, anchor=north, font=\scriptsize] at (7.8,-4.25) {Exemplo ilustrativo. A solução de cada domicílio é definida no projeto individual,
    conforme a ABNT NBR 17076:2024, as condições do terreno e o número de moradores.};
\end{tikzpicture}
"""

# ------------------------------------------------------------------ instalação e verificação técnica
F["f-instalacao"] = r"""
\begin{tikzpicture}[node distance=0.42cm]
  \node[etapa=4.6cm] (proj) {\textbf{Projeto individual do domicílio}\\
    {\scriptsize terreno, número de moradores e solução de tratamento}};
  \node[etapa=4.6cm, below=of proj] (inst) {\textbf{Instalação da solução}\\ {\scriptsize obras civis e dispositivos}};
  \node[etapa=4.6cm, below=of inst] (atest) {\textbf{Verificação técnica}\\ {\scriptsize funcionamento, estanqueidade e garantia}};
  \node[decisao, text width=1.7cm, below=0.5cm of atest] (dec) {Atende aos requisitos?};
  \node[correcao=3.0cm, left=1.0cm of dec] (corr) {Correções técnicas pela empresa};
  \node[marco=4.6cm, below=0.55cm of dec] (reg) {Sistema validado e registrado};
  \node[etapa=4.2cm, fill=cGreenBg, draw=cGreen, right=2.1cm of inst] (cap) {\textbf{Orientação do proprietário}\\
    {\scriptsize funcionamento, uso adequado, manutenção preventiva e lodo}};
  \draw[seta] (proj) -- (inst);
  \draw[seta] (inst) -- (atest);
  \draw[seta] (atest) -- (dec);
  \draw[seta] (dec) -- node[rotulo, above] {Não} (corr);
  \draw[seta] (corr) |- (atest.west);
  \draw[seta] (dec) -- node[rotulo, right] {Sim} (reg);
  \draw[setatracejada, <->] (inst) -- node[rotulo, above=1pt, font=\tiny\itshape] {ao mesmo tempo} (cap);
  \draw[seta] (cap.south) |- (reg.east);
\end{tikzpicture}
"""

# ------------------------------------------------------------------ medição, comprovação e pagamento
F["f-medicao"] = r"""
\begin{tikzpicture}[passo/.style={etapa=4.25cm, minimum height=0.82cm, font=\scriptsize}]
  \def\alt{12.0cm}
  \node[raia=4.95cm, minimum height=\alt] at (0,0)     {};
  \node[raia=4.95cm, minimum height=\alt] at (5.25,0)  {};
  \node[raia=4.95cm, minimum height=\alt] at (10.5,0)  {};
  \node[font=\scriptsize\bfseries, text=cNavy] at (2.475,-0.35)  {Empresa contratada};
  \node[font=\scriptsize\bfseries, text=cNavy] at (7.725,-0.35)  {Proprietário (beneficiário)};
  \node[font=\scriptsize\bfseries, text=cNavy] at (12.975,-0.35) {IAT (fiscalização e validação)};
  \node[passo] (m1) at (2.475,-1.2)   {Relatório de medição do projeto e da instalação};
  \node[passo] (m2) at (2.475,-2.45)  {Comprovação: documentos e evidências da intervenção};
  \node[passo] (m3) at (7.725,-3.7)   {Assinatura que confirma a execução das melhorias};
  \node[passo] (m4) at (12.975,-4.95) {Auditoria documental};
  \node[passo] (m5) at (12.975,-6.2)  {Verificação \textit{in loco} das intervenções};
  \node[passo] (m6) at (2.475,-7.45)  {Relatório de medição final do lote};
  \node[passo] (m7) at (12.975,-8.7)  {Amostragem \textit{in loco} da qualidade das unidades};
  \node[passo] (m8) at (12.975,-9.95) {Ordenação das despesas e pagamento};
  \node[marco=4.25cm, minimum height=0.82cm] (m9) at (7.725,-11.25) {Finalização do lote};
  \draw[seta] (m1) -- (m2);
  \draw[seta] (m2) |- (m3);
  \draw[seta] (m3) -| (m4);
  \draw[seta] (m4) -- (m5);
  \draw[seta] (m5) -| (m6);
  \draw[seta] (m6) |- (m7);
  \draw[seta] (m7) -- (m8);
  \draw[seta] (m8) |- (m9);
\end{tikzpicture}
"""

# ------------------------------------------------------------------ ciclo mensal de supervisão
F["f-ciclo-supervisao"] = r"""
\begin{tikzpicture}[
   passo/.style={etapa=3.3cm, minimum height=1.0cm, font=\scriptsize},
   circ/.style={-{Stealth[length=2.2mm]}, line width=1pt, draw=cTeal}]
  \node[marco=3.0cm, minimum height=1.5cm, font=\footnotesize\bfseries] (c) at (0,0) {Obras de água e de esgoto\\
    {\normalfont\scriptsize Ações 3.2.2.3, 3.2.2.5 e 3.2.2.6}};
  \foreach \i/\t in {
     1/{\textbf{Plano de supervisão} aprovado pelo IAT},
     2/{\textbf{Visitas de campo} e controle de qualidade},
     3/{\textbf{Registro de não conformidades}, inclusive ambientais e sociais},
     4/{\textbf{Correção} pelo executor e nova verificação},
     5/{\textbf{Verificação das medições} executadas},
     6/{\textbf{Relatório mensal} ao IAT e à UGP}} {
    \node[passo] (n\i) at ({90-(\i-1)*60}:3.55cm) {\t};
  }
  \foreach \a/\b in {1/2,2/3,3/4,4/5,5/6,6/1}
    \draw[circ] (n\a) to[bend left=18] (n\b);
\end{tikzpicture}
"""


def escrever():
    for nome, corpo in F.items():
        with open(os.path.join(FIG, nome + ".tex"), "w", encoding="utf-8") as f:
            f.write(CAB + corpo + FIM)
    print(len(F), "figuras escritas")


if __name__ == "__main__":
    escrever()
