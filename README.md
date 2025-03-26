# **Automação de Relatórios de Chamados do GLPI**

Este projeto automatiza a extração e o envio de relatórios de chamados do GLPI, uma ferramenta de gerenciamento de TI. Ele foi desenvolvido para usuários com acesso limitado às funcionalidades do GLPI, mas que desejam gerar relatórios específicos para facilitar a visualização e análise de questões importantes.

O sistema coleta dados sobre chamados com SLAs excedidos, SLAs que vencerão no mesmo dia e chamados sem técnico atribuído. Em seguida, organiza essas informações por setor e envia relatórios detalhados por e-mail para os destinatários configurados. Isso otimiza o monitoramento de chamados, garantindo que as equipes possam tomar ações rapidamente e melhorar o gerenciamento do atendimento.

## **Funcionalidades**

- **Automatização do processo de extração de dados do GLPI**: Acesso ao sistema GLPI para obter informações sobre chamados e SLAs.
- **Relatórios divididos por categoria**: Chamados com SLAs vencidos, SLAs que vencerão hoje, e chamados sem técnico.
- **Divisão por setores**: Organiza os chamados por setor para facilitar a visualização e análise.
- **Envio de e-mail**: Relatórios gerados são automaticamente enviados para os destinatários com formatação adequada.

## **Pré-requisitos**

Antes de rodar o projeto, você precisa garantir que tenha as seguintes bibliotecas e ferramentas instaladas:

### **Bibliotecas Python**

- `selenium` – Para automação de navegação no GLPI.
- `getpass` – Para segurança na entrada de senhas.
- `msvcrt` – Para capturar entradas no terminal (Windows).
- `datetime` – Para manipulação de datas e horários.
- `locale` – Para manipulação de locais de data e hora.
- `smtplib` – Para envio de e-mails.
- `email.mime.multipart` e `email.mime.text` – Para formatação de e-mails.

### **Outras dependências**
- **GLPI**: O sistema GLPI deve estar configurado e acessível através de um navegador.
  
## **Estrutura do Projeto**

O projeto está organizado nas seguintes partes:

- **`glpi.py`**: Contém a automação para acessar o GLPI e extrair os dados necessários.
- **`enviar_email.py`**: Contém funções para enviar e-mails com os relatórios gerados.
- **`formatacao_email.py`**: Responsável por formatar o corpo do e-mail de maneira estruturada.
- **`gerar_relatorios.py`**: Gera os relatórios com base nas informações extraídas.
- **`main.py`**: Arquivo principal que executa a automação de todo o processo.

## **Bibliotecas Utilizadas**

- **Selenium**: Para automatizar a navegação no navegador e interagir com o GLPI.
- **Smtplib e email.mime**: Para envio e formatação de e-mails.
- **Datetime**: Para calcular e verificar os SLAs dos chamados.
- **Getpass e msvcrt**: Para lidar com a entrada de senhas e interações com o sistema.
- **Bibliotecas personalizadas**:
  - `glpi.py` para integração com o GLPI.
  - `enviar_email.py` para envio de relatórios por e-mail.
  - `formatacao_email.py` para formatação dos relatórios.
  - `gerar_relatorios.py` para criação dos relatórios.
