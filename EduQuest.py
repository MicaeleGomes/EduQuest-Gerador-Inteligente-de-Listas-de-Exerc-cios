import json
from collections import defaultdict

def selecionar_questoes_por_regras(questoes, regras):
    selecionadas = []
    contadores = defaultdict(int)

    for questao in questoes:
        for regra in regras:
            condicao, limite = regra
            if condicao(questao) and contadores[condicao.__name__] < limite:
                selecionadas.append(questao)
                contadores[condicao.__name__] += 1
                if len(selecionadas) == 10:
                    return selecionadas
    return selecionadas

def processar_questoes(dados):
    categorias = defaultdict(lambda: {'basica': [], 'intermediaria': [], 'avancada': []})

    for categoria_id, niveis in dados.items():
        todas_questoes = []
        for dificuldade, tipos in niveis.items():
            for tipo, origens in tipos.items():
                for origem, questoes in origens.items():
                    todas_questoes.extend(questoes)

        regras_basica = [
            (lambda q: q['difficulty'] == 'facil' and q['answerType'] == "MultipleChoice", 2),
            (lambda q: q['difficulty'] == 'media' and q['answerType'] == "MultipleChoice", 4),
            (lambda q: q['difficulty'] == 'media' and q['answerType'] == "MultipleChoice", 2),
            (lambda q: q['difficulty'] == 'dificil' and q['answerType'] == "MultipleChoice", 1),
            (lambda q: q['difficulty'] == 'dificil' and q['answerType'] == "Discursive", 1)
        ]
        
        regras_intermediaria = [
            (lambda q: q['difficulty'] == 'dificil' and q['answerType'] == "MultipleChoice", 2),
            (lambda q: q['difficulty'] == 'dificil' and q['answerType'] == "MultipleChoice", 1),
            (lambda q: q['difficulty'] == 'dificil' and q['answerType'] == "Discursive", 1),
            (lambda q: q['difficulty'] == 'muito_dificil' and q['answerType'] == "Discursive", 3),
            (lambda q: q['difficulty'] == 'muito_dificil' and q['answerType'] == "MultipleChoice", 2),
            (lambda q: q['difficulty'] == 'extremamente_dificil' and q['answerType'] == "MultipleChoice", 1)
        ]
        
        regras_avancada = [
            (lambda q: q['difficulty'] == 'dificil' and q['answerType'] == "Discursive", 2),
            (lambda q: q['difficulty'] == 'muito_dificil' and q['answerType'] == "Discursive", 1),
            (lambda q: q['difficulty'] == 'muito_dificil' and q['answerType'] == "Discursive", 6),
            (lambda q: q['difficulty'] == 'extremamente_dificil' and q['answerType'] == "Discursive", 1)
        ]

        categorias[categoria_id]['basica'] = selecionar_questoes_por_regras(todas_questoes, regras_basica)
        categorias[categoria_id]['intermediaria'] = selecionar_questoes_por_regras(todas_questoes, regras_intermediaria)
        categorias[categoria_id]['avancada'] = selecionar_questoes_por_regras(todas_questoes, regras_avancada)

    return categorias

def ler_questoes_do_arquivo(caminho_do_arquivo):
    with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def salvar_em_json(categorias, nome_arquivo_saida):
    with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo:
        json.dump(categorias, arquivo, ensure_ascii=False, indent=4)

# Caminhos de arquivos
caminho_do_arquivo = 'questoes.json'
nome_arquivo_saida = 'listas_de_questoes.json'

# Processamento principal
dados = ler_questoes_do_arquivo(caminho_do_arquivo)
categorias = processar_questoes(dados)
salvar_em_json(categorias, nome_arquivo_saida)

print(f"As questões foram processadas e salvas em '{nome_arquivo_saida}'")
