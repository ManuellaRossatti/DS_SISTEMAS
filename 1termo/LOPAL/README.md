# 🐍 MEU PORTIFÒLIO DE PYTHON
Meu Portfólio Python – Manu Rossatt
"Da simulação de um robô industrial à lógica de programação sólida"

📌 Sobre Este Portfólio
Este repositório documenta minha jornada de aprendizado em Python, demonstrando os conceitos que já domino através de projetos práticos e exercícios resolvidos.

# 🧠 Conceitos Dominados

Conceito	Aplicação no meu código

✅ Variáveis	Armazenamento de cores, passos, ângulos

✅ Entrada de dados	input() para interação com usuário

✅ Conversão de tipos	int(input()), float()

✅ Estruturas condicionais	if, elif, else

✅ Operadores relacionais	==, <, >, <=, >=

✅ Operadores lógicos	and, or (usados indiretamente)

✅ F-strings	Formatação moderna com f"texto {variavel}"

✅ Laço while	Contagem regressiva da bateria

✅ Laço for	Contagem de curtidas

✅ Tratamento de intervalos	range()

✅ Listas	(exercícios preparatórios)

✅ Debug/Identificação de erros	Resolução dos 10 "Caça-Erros"

🚀 Projetos em Destaque

1️⃣ Simulador de Robô Industrial

Arquivo: robo_pecas.py

Robô que coleta peças boas (verdes) e defeituosas (vermelhas) com controle de:

Passos (0-66 para vermelha / 0-36 para verde)

Rotação à direita/esquerda

Sequência completa: andar → agachar → agarrar → levantar → voltar → entregar
## Trecho do código

if cor == "Vermelho":

    andar = int(input("Quantos passos? (0-66)"))

    # ... validações e ações

## 2️⃣ Desafio "O Caça-Erros" 🐛

10 problemas identificados e corrigidos:

##	Problema	Erro Comum	Minha Solução
1	Idade	input() sem int()	Conversão explícita

2	Escrita	Concatenação errada	Uso de f-strings

3	Indentação	if sem espaçamento	Padronização PEP 8

4	Faltando :	if condicao sem dois pontos	Sintaxe correta

5	= vs ==	Atribuição no lugar de comparação	Uso correto do operador

6	Tipo misturado	str + int	Conversão ou f-string

7	Ordem dos if/elif	Condições mal organizadas	Hierarquia lógica

8	range()	range(5) vs range(1,6)	Parâmetros corretos

9	Loop infinito	Sem incremento	tentativas += 1

10	while invertido	== ao invés de !=	Operador correto

3️⃣ Utilitários Práticos
python
## Calculadora de Mesada
total = valor_semana * 4

## Conversor GB → MB
megas = gigabytes * 1024

## Média Escolar

media = (matematica + portugues) / 2

## Idade em dias

dias_vividos = idade * 365

4️⃣ Controle de Fluxo Interativo

Bateria do Celular (loop com delay):


python

while bateria >= 10:

    print(f"Bateria: {bateria}%")

    bateria -= 10

    time.sleep(1)

Carrinho de Compras:

python

while produto.lower() != "sair":

    produto = input("Produto: ")

    contador += 1

📁 Estrutura do Repositório

text

python-portfolio/

│
├── projetos/
│   ├── robo_industrial.py      # Simulador do robô
│   ├── caça_erros.py           # 10 erros corrigidos
│   └── utilitarios.py          # Calculadoras e conversores
│

├── exercicios/
│   ├── condicionais/
│   ├── loops/
│   └── tipos_dados/
│
├── README.md                   # Este arquivo
└── requirements.txt            # Dependências (se houver)

## 🎯 Habilidades Demonstradas
🔹 Pensamento lógico – sequenciamento de ações do robô

🔹 Validação de entrada – limites (0-66, 0-176, etc.)

🔹 Experiência do usuário – mensagens claras e feedback

🔹 Debugging – identificação e correção de 10 erros comuns

🔹 Código limpo – organização e comentários estratégicos

📈 Próximos Passos (Em estudo)
Funções (def)

Listas e dicionários

Tratamento de exceções (try/except)

Manipulação de arquivos

Bibliotecas externas (pandas, matplotlib)

📫 Contato
Manu Rossatt
GitHub • 

"Cada linha de código é um passo em direção a uma solução."
