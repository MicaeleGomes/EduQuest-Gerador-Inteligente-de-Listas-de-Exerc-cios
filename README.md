# EduQuest: Gerador Inteligente de Listas de Exercícios

**EduQuest** é uma ferramenta para gerar listas de exercícios a partir de um banco de questões. Ela categoriza as questões em três níveis de dificuldade: básica, intermediária e avançada. O script processa um JSON de questões aleatórias e gera um novo JSON com as listas prontas e organizadas.

## Funcionalidades

- **Carregamento de Questões**: Lê um arquivo JSON organizado com questões e retorna os dados.
- **Definição de Regras**: Define três conjuntos de regras para selecionar questões para diferentes níveis de dificuldade.
- **Seleção de Questões**: Seleciona questões com base nas regras especificadas.
- **Processamento de Questões**: Processa e categoriza as questões em listas de acordo com as regras definidas.
- **Salvar Resultados**: Salva as listas de questões processadas em um novo arquivo JSON.

## Como Funciona

1. **Função `ler_questoes_do_arquivo`**
   - Lê as questões do arquivo JSON fornecido e retorna os dados.

2. **Função `selecionar_questoes_por_regras`**
   - Seleciona questões de acordo com um conjunto de regras especificadas.

3. **Função `processar_questoes`**
   - Processa as questões lidas e as categoriza em três níveis de dificuldade: prática básica, prática intermediária e prática avançada.

4. **Função `salvar_em_json`**
   - Salva as listas de questões processadas em um novo arquivo JSON.

## Pré-requisitos

Para usar o **EduQuest**, você precisa ter um arquivo JSON contendo as questões que deseja utilizar para gerar as listas. Certifique-se de que a estrutura do arquivo JSON esteja de acordo com o formato esperado pelo script.

## Arquivos

**questoes_organizadas.json:** Arquivo de entrada contendo as questões.
**listas_questoes_processadas.json:** Arquivo de saída com as questões processadas e categorizadas.

## Observações

As regras para seleção de questões podem ser ajustadas conforme necessário para atender a diferentes critérios de dificuldade e tipos de resposta.
A estrutura do arquivo JSON de entrada deve estar de acordo com o formato esperado pelo código para garantir o processamento correto.
