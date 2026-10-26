"""Levanta as citações de normas na Atividade 3.2.2 (textos, quadros, figuras e comentários)."""
import importlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # pasta fonte/

PADROES = [
    ('N-001', r'Acordo de Empréstimo'),
    ('N-002', r'\bNAS\b|Normas Ambientais e Sociais'),
    ('N-003', r'Regulamento de Aquisições'),
    ('N-004', r'Lei nº 9\.433'),
    ('N-005', r'Lei nº 11\.107|Lei dos Consórcios Públicos|\(BRASIL, 2005\)'),
    ('N-006', r'Lei nº 11\.445'),
    ('N-007', r'Lei nº 13\.019|MROSC|\(BRASIL, 2014\)'),
    ('N-008', r'Lei nº 13\.709|Lei Geral de Proteção de Dados|LGPD|\(BRASIL, 2018\)'),
    ('N-009', r'Lei nº 14\.026'),
    ('N-010', r'Lei nº 14\.133'),
    ('N-011', r'Decreto nº 11\.599'),
    ('N-012', r'Portaria (?:Funasa )?nº 2\.777'),
    ('N-013', r'Portaria GM/MS nº 888|padrão de potabilidade|\(BRASIL, 2021\)'),
    ('N-014', r'Portaria de Consolidação GM/MS nº 5'),
    ('N-015', r'Programa Nacional de Saneamento Rural|\(BRASIL, 2019\)'),
    ('N-016', r'NBR 17076|\(ABNT, 2024\)'),
    ('N-017', r'NBR 7229'),
    ('N-018', r'NBR 13969'),
    ('N-019', r'NBR 12212'),
    ('N-020', r'NBR 12244'),
    ('N-021', r'Lei Estadual nº 12\.726'),
    ('N-022', r'Regulamento de Licitações e Contratos'),
]

MODS = ['c_atividade', 'c_3221', 'c_3222', 'c_3223', 'c_3224', 'c_3225', 'c_3226', 'c_3227']


def limpa(t):
    t = re.sub(r'\{(fig|qua|tab):[\w\-]+\}', lambda m: {'fig': 'Figura', 'qua': 'Quadro', 'tab': 'Tabela'}[m.group(1)], t)
    t = t.replace('**', '').replace('*', '').replace('[[', '').replace(']]', '')
    return re.sub(r'\s+', ' ', t).strip()


def trecho(t, pos, n=170):
    a = max(0, pos - 70)
    b = min(len(t), pos + n - 70)
    s = t[a:b].strip()
    return ('…' if a > 0 else '') + s + ('…' if b < len(t) else '')


def textos(el):
    """(tipo, texto, rótulo do elemento) de um elemento de conteúdo."""
    tipo = el[0]
    if tipo in ('P', 'COM', 'H2', 'ACAO', 'ITEM', 'ETAPA'):
        yield tipo, el[1], ''
    elif tipo == 'BUL':
        for it in el[1]:
            yield 'BUL', it, ''
    elif tipo == 'FIG':
        d = el[1]
        yield 'FIG', d['titulo'] + '. ' + d['fonte'], f"Figura “{d['titulo']}”"
    elif tipo == 'TAB':
        d = el[1]
        rot = f"{d['tipo']} “{d['titulo']}”"
        for ln in d['linhas']:
            rotulo_linha = limpa(str(ln[0]))
            for c in ln:
                yield 'TAB', str(c), f"{rot}, linha “{rotulo_linha}”"
        if d.get('nota'):
            yield 'TAB', d['nota'], rot


def levantar():
    oc = []
    for m in MODS:
        mod = importlib.import_module(m)
        acao, item, etapa = 'Atividade 3.2.2', 'Apresentação da atividade', ''
        for el in mod.ELEMENTOS:
            if el[0] == 'ACAO':
                acao = re.match(r'Ação ([\d.]+)', el[1]).group(1)
                item, etapa = '', ''
                continue
            if el[0] == 'ITEM':
                item, etapa = el[1], ''
                continue
            if el[0] == 'ETAPA':
                etapa = el[1]
                continue
            for tipo, t, rot in textos(el):
                t = limpa(t)
                for nid, pad in PADROES:
                    for mm in re.finditer(pad, t):
                        oc.append(dict(norma=nid, acao=acao, item=item, etapa=etapa, tipo=tipo, rotulo=rot,
                                       trecho=trecho(t, mm.start())))
                        break
    # uma linha por norma e por item/etapa da ação (mantém o primeiro trecho, marca se houver comentário)
    vistos, saida = {}, []
    for o in oc:
        grupo = {'P': 'texto', 'BUL': 'texto', 'TAB': 'quadro', 'FIG': 'figura', 'COM': 'comentário'}.get(o['tipo'], 'texto')
        o['grupo'] = grupo
        k = (o['norma'], o['acao'], o['item'], o['etapa'], grupo)
        if k in vistos:
            vistos[k]['n'] += 1
            continue
        o['n'] = 1
        vistos[k] = o
        saida.append(o)
    return saida


if __name__ == '__main__':
    r = levantar()
    from collections import Counter
    print(len(r), Counter(o['norma'] for o in r))
    for o in r[:12]:
        print(o['norma'], o['acao'], '|', o['item'], '|', o['etapa'], '|', o['tipo'], '|', o['trecho'][:90])
