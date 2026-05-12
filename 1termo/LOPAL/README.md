# 🐍 Meu Portfólio de Python
> **Manu Rossatt**  
> *"Da simulação de um robô industrial à lógica de programação sólida"*

---

## 📌 Sobre Este Portfólio
Este repositório documenta minha jornada de aprendizado em Python, demonstrando os conceitos que já domino através de projetos práticos e exercícios resolvidos.

---

## 🧠 Conceitos Dominados


| Conceito | Aplicação no meu código |
| :--- | :--- |
| ✅ **Variáveis** | Armazenamento de cores, passos, ângulos |
| ✅ **Entrada de dados** | `input()` para interação com usuário |
| ✅ **Conversão de tipos** | `int(input())`, `float()` |
| ✅ **Estruturas condicionais** | `if`, `elif`, `else` |
| ✅ **Operadores relacionais** | `==`, `<`, `>`, `<=`, `>=` |
| ✅ **Operadores lógicos** | `and`, `or` |
| ✅ **F-strings** | Formatação moderna com `f"texto {variavel}"` |
| ✅ **Laço while** | Contagem regressiva da bateria |
| ✅ **Laço for** | Contagem de curtidas |
| ✅ **Tratamento de intervalos** | Uso de `range()` |
| ✅ **Listas** | Exercícios preparatórios e coleções |
| ✅ **Debug/Refatoração** | Resolução dos 10 "Caça-Erros" |

---

## 🚀 Projetos em Destaque

### 1️⃣ Simulador de Robô Industrial
**Arquivo:** `robo_pecas.py`  
Simulação de um robô que coleta peças boas (verdes) e defeituosas (vermelhas) com validações rígidas:
*   **Passos:** 0-66 (vermelha) / 0-36 (verde).
*   **Ações:** Sequência completa de *Andar → Agachar → Agarrar → Levantar → Voltar → Entregar*.

```python
# Exemplo de validação lógica
if cor == "Vermelho":
    andar = int(input("Quantos passos? (0-66): "))
    if 0 <= andar <= 66:
        print("Movimentando braço robótico...")
    else:
        print("Erro: Limite de segurança excedido!")
```

### 2️⃣ Desafio "O Caça-Erros" 🐛
Identificação e correção de 10 problemas comuns de sintaxe e lógica:


| nº | Problema | Erro Comum | Minha Solução |
| :--- | :--- | :--- | :--- |
| 1 | Idade | `input()` sem `int()` | Conversão explícita |
| 2 | Escrita | Concatenação errada | Uso de f-strings |
| 3 | Indentação | `if` sem espaçamento | Padronização PEP 8 |
| 4 | Faltando `:` | Erro de sintaxe no `if` | Adição dos dois pontos |
| 5 | `=` vs `==` | Atribuição na comparação | Uso correto de `==` |
| 9 | Loop infinito | Sem incremento | `tentativas += 1` |
| 10 | `while` invertido | `==` ao invés de `!=` | Operador de diferença |

---

## 🛠️ Utilitários Práticos

Abaixo, alguns exemplos de lógica aplicada para automação de cálculos simples:

```python
# Média Escolar
media = (matematica + portugues) / 2

# Controle de Bateria (Loop com delay)
import time
while bateria >= 10:
    print(f"Bateria: {bateria}%")
    bateria -= 10
    time.sleep(1)
```

---

## 📁 Estrutura do Repositório

```text
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
└── README.md                   # Documentação do portfólio
```

---

## 🎯 Habilidades Demonstradas
*   **Pensamento Lógico:** Sequenciamento de ações complexas.
*   **Validação de Dados:** Proteção contra entradas inválidas do usuário.
*   **Código Limpo:** Organização seguindo as recomendações da comunidade.
*   **Resolução de Problemas:** Capacidade de *debugging* e análise crítica.

---

## 📈 Próximos Passos (Em estudo)
- [ ] Funções (`def`)
- [ ] Dicionários
- [ ] Tratamento de exceções (`try/except`)
- [ ] Bibliotecas de análise de dados (Pandas/Matplotlib)

---

## 📫 Contato
**Manu Rossatt**  
[GitHub](https://github.com) • [LinkedIn](https://linkedin.com)

*"Cada linha de código é um passo em direção a uma solução."*
