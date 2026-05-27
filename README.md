# 🛡️ SecOps Assistant (Agente Agno de Segurança)

Este projeto é um Agente de IA desenvolvido em Python utilizando o framework **Agno** (anteriormente Phidata). O assistente foi desenhado para auxiliar em tarefas de Infraestrutura e Segurança (SecOps), possuindo ferramentas reais para análises técnicas.

## 🛠️ Tools Implementadas (Ferramentas)
1. **`analyze_password_strength`**: Analisa a complexidade de uma senha.
2. **`generate_hash`**: Gera hashes criptográficos (MD5, SHA1, SHA256) a partir de um texto.
3. **`check_dns_records`**: Executa requisições reais para verificar registros DNS (TXT, MX, A) de domínios.
4. **`calculate_subnet`**: Processa um bloco CIDR (ex: `192.168.0.0/24`) e calcula máscara, broadcast e hosts.

---

## ⚙️ Configuração do Ambiente (.env)
Antes de rodar, renomeie o arquivo `.env.example` para `.env` e adicione sua chave de API do Google Gemini:
```env
GEMINI_API_KEY=AIzaSy...sua_chave...
AGENT_MODEL=gemini-2.5-flash