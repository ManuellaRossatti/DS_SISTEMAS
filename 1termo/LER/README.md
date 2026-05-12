# Aula: Engenharia de Requisitos
## Do Levantamento à Documentação Técnica

---

## 1. Fundamentos: Requisitos Funcionais vs. Não Funcionais

A primeira etapa é entender a diferença entre o **o que** o sistema faz e **como** ele se comporta.

### **Requisitos Funcionais (RF)**
Descrevem as funcionalidades e serviços do sistema.
*   *Exemplo:* "O sistema deve permitir o cadastro de novos usuários."
*   *Exemplo:* "O sistema deve gerar um relatório mensal de vendas em PDF."

### **Requisitos Não Funcionais (RNF)**
Descrevem restrições, propriedades e qualidades do sistema (desempenho, segurança, usabilidade).
*   *Exemplo:* "O sistema deve responder a qualquer consulta em menos de 2 segundos."
*   *Exemplo:* "A senha do usuário deve ser criptografada com AES-256."

---

## 2. Técnicas de Levantamento (Passo a Passo)

### **A. Entrevista**
1.  **Preparação:** Identifique os stakeholders e crie um roteiro.
2.  **Abertura:** Estabeleça confiança e explique o objetivo.
3.  **Execução:** Use perguntas abertas. Escute mais do que fale.
4.  **Fechamento:** Resuma os pontos e defina os próximos passos.

### **B. Questionário**
*   **Uso:** Ideal para coletar dados de um grande volume de pessoas.
*   **Dica:** Misture perguntas de múltipla escolha (quantitativo) com campos de texto (qualitativo).

### **C. Brainstorming**
1.  **Fase de Geração:** Todas as ideias são bem-vindas. Ninguém critica ninguém.
2.  **Fase de Filtro:** Agrupe ideias semelhantes e descarte o que é tecnicamente inviável.
3.  **Fase de Priorização:** Escolha as ideias que trazem mais valor ao negócio.

---

## 3. Gestão Ágil: Scrum e Kanban

### **Scrum**
*   **Product Backlog:** Lista mestre de tudo o que o sistema precisa ter.
*   **User Stories:** Requisitos escritos sob a perspectiva do usuário: 
    *   *"Como [quem], eu quero [o quê] para [valor/motivo]."*

### **Kanban**
*   Visualização do fluxo de requisitos:
    *   **To Do (A fazer)** -> **Doing (Análise/Levantamento)** -> **Done (Validado)**.

---

## 4. Prototipagem e Diagramas

### **Prototipagem**
*   **Baixa Fidelidade:** Papel ou wireframes simples (validação de fluxo).
*   **Alta Fidelidade:** Protótipos interativos (Figma) para validar a experiência do usuário (UX).

### **Diagramas UML (Essenciais)**
*   **Caso de Uso:** Mostra a interação do Ator com o Sistema.
*   **Fluxograma:** Define o passo a passo lógico do requisito funcional.

---

## 5. Relatórios Técnicos (Documentação)

Um bom relatório de requisitos deve conter:
1.  **Introdução:** Objetivo do documento.
2.  **Descrição Geral:** Perspectiva do produto.
3.  **Lista de RF:** Numerados (RF01, RF02...).
4.  **Lista de RNF:** Numerados (RNF01, RNF02...).
5.  **Critérios de Aceite:** O que define que aquele requisito foi concluído com sucesso.

---

## 6. Exercício Prático: "O Sistema da Biblioteca"

**Tarefa:**
1.  Realize um **Brainstorming** em grupo para listar funções de uma biblioteca.
2.  Defina **2 Requisitos Funcionais** e **1 Requisito Não Funcional**.
3.  Desenhe um **Protótipo de Papel** da tela de busca de livros.
4.  Crie uma **User Story** para o bibliotecário.
