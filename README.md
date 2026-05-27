# 🛡️ SecOps Assistant (Agente Agno de Segurança)

Este projeto é um Agente de IA desenvolvido em Python utilizando o framework **Agno** (anteriormente Phidata). Focado em operações de **Cyber** Defense, o assistente foi desenhado para auxiliar em tarefas de Infraestrutura e Segurança (SecOps), possuindo ferramentas reais para análises técnicas avançadas.

O projeto cumpre todos os requisitos da Global Solution, incluindo persistência de memória (SQLite), execução via CLI, interface Web (Flask) e containerização (Docker).

---

## 🛠️ Tools Implementadas (Ferramentas)
O agente não utiliza respostas simuladas. Ele possui 4 integrações nativas que executam processamento real:

1. **`analyze_password_strength`**: Analisa a força e complexidade de uma senha com base em requisitos estruturais de segurança.
2. **`generate_hash`**: Gera hashes criptográficos (MD5, SHA1, SHA256) a partir de um texto para checagem de integridade.
3. **`check_dns_records`**: Executa requisições reais de rede para verificar registros DNS (TXT, MX, A) para auditoria e service discovery de domínios (ex: `rm566669.com.br`).
4. **`calculate_subnet`**: Processa um bloco CIDR (ex: `192.168.0.0/24`) e calcula máscara, endereço de broadcast e hosts utilizáveis.

---

## ⚙️ Configuração do Ambiente (.env)
Antes de rodar a aplicação, renomeie o arquivo `.env.example` para `.env` e adicione a sua chave de API de integração:

```env
# Insira sua chave de API do Google Gemini
GOOGLE_API_KEY=...sua_chave_aqui...

# Definição do modelo de IA
AGENT_MODEL=gemini-2.5-flash
```
---

## 🚀 Instalação e Execução (Local)

1. **`Preparando o ambiente`**

 ```
python -m venv venv
# Ativação no Windows:
.\venv\Scripts\activate
# Ativação no Linux/Mac:
source venv/bin/activate
```

Instale as depedencias listadas no requirements.txt

```
pip install -r requirements.txt
```

---

2. **`Executando o Assistente`**
O projeto possui duas frentes de execução

**`Modo Terminal(CLI)`**

```
python main.py
```

**`Modo WEB(Flask)`**

```
python app.py
```

---

## 🐳 Containerização (Docker)

Para garantir a portabilidade e isolamento do serviço, o ambiente foi containerizado. Certifique-se de que o Docker Daemon está em execução.

1. **`Construir a imagem`**

```
docker build -t secops-agent .
```
   
2. **`Executar o container (Modo Web)`**
   
```
docker run -p 5000:5000 --env-file .env secops-agent
```

---

## 📂 Estrutura do Projeto

agent.py: Configuração do agente, persistência (SqliteDb) e integração com o modelo (Gemini).

tools.py: Lógica das funções de segurança utilizadas pelo agente.

main.py: Ponto de entrada para a interface de linha de comando (CLI).

app.py: Servidor Flask e interface Web (HTML/JS integrado).

agent_memory.db: Banco de dados SQLite auto-gerado para retenção de histórico.
