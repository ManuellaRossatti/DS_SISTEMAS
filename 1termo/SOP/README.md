# Aula: Sistemas Operacionais (SO)
## Arquitetura, Gerenciamento e Ecossistemas (Windows, Linux, iOS)

---

## 1. O que é um Sistema Operacional?
O SO é a camada de software que atua como intermediária entre o **hardware** e o **usuário/aplicativos**.

### Principais Funções:
*   **Gerenciamento de Processos:** Escalonamento e execução de programas.
*   **Gerenciamento de Memória:** Alocação de RAM para processos ativos.
*   **Gerenciamento de Arquivos:** Organização de dados em discos (NTFS, EXT4, APFS).
*   **Interface do Usuário:** GUI (Gráfica) ou CLI (Linha de Comando).

---

## 2. Windows: O Gigante Corporativo e Doméstico
Desenvolvido pela Microsoft, focado em compatibilidade e facilidade de uso.

*   **Núcleo (Kernel):** NT (New Technology).
*   **Sistema de Arquivos:** NTFS.
*   **Pontos Fortes:** Maior biblioteca de softwares do mundo, suporte a hardware legado, dominante no mercado corporativo e gamer.
*   **Comando Útil (PowerShell):** `Get-Process` (Lista processos ativos).

---

## 3. Linux: O Rei dos Servidores e do Open Source
Não é um sistema único, mas um **Kernel** que compõe diversas distribuições (Ubuntu, Debian, Fedora, Arch).

*   **Filosofia:** Código aberto (Open Source).
*   **Arquitetura:** Monolítica modular.
*   **Pontos Fortes:** Segurança, estabilidade, altamente customizável e gratuito.
*   **Comandos Essenciais (Terminal):**
    *   `ls`: Listar arquivos.
    *   `sudo apt update`: Atualizar repositórios.
    *   `top`: Monitorar recursos do sistema em tempo real.

---

## 4. iOS: Ecossistema Fechado e Mobile
Sistema operacional da Apple para iPhone, baseado no Kernel **XNU** (Darwin), com raízes no Unix/BSD.

*   **Foco:** Otimização entre hardware e software, fluidez e segurança.
*   **Arquitetura de Segurança:** Sandboxing (cada app roda isolado) e criptografia de hardware.
*   **Diferencial:** Ciclo de atualizações unificado para todos os dispositivos compatíveis.

---

## 5. Comparativo Técnico


| Característica | Windows | Linux | iOS |
| :--- | :--- | :--- | :--- |
| **Licença** | Proprietária | Open Source (GPL) | Proprietária |
| **Kernel** | Híbrido (NT) | Monolítico | Microkernel (Mach/BSD) |
| **Interface** | Desktop/Touch | Várias (GNOME, KDE) | Mobile/Touch (Cocoa Touch) |
| **Uso Principal** | Desktop, Games | Servidores, IoT, Dev | Dispositivos Mobile Apple |

---

## 6. Outros Conteúdos Relevantes

### Virtualização e Containers
*   **Máquinas Virtuais (VM):** Simulam um hardware completo (Ex: VirtualBox, VMware).
*   **Docker:** Compartilha o kernel do hospedeiro, sendo muito mais leve que uma VM.

### Gerenciamento de Memória
*   **Memória Virtual (Paging):** Uso de parte do HD/SSD como se fosse memória RAM para evitar travamentos.

---

## 7. Desafio Prático
1.  **Windows:** Abra o Gerenciador de Tarefas e identifique qual processo consome mais memória.
2.  **Linux:** Se estiver em uma distro, use o comando `df -h` para verificar o espaço em disco.
3.  **Reflexão:** Por que o Linux é preferido para servidores e o iOS para usuários que buscam simplicidade?
