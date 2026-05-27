import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.db.sqlite import SqliteDb

# Importando nossas tools próprias
from tools import analyze_password_strength, generate_hash, check_dns_records, calculate_subnet

# Carrega variáveis do arquivo .env
load_dotenv()

# Configuração de persistência com o novo SqliteDb
db = SqliteDb(
    db_file="agent_memory.db",
    session_table="secops_agent_sessions"
)

def get_secops_agent():
    return Agent(
        name="SecOps Assistant",
        model=Gemini(id=os.getenv("AGENT_MODEL", "gemini-2.5-flash")),
        tools=[analyze_password_strength, generate_hash, check_dns_records, calculate_subnet],
        db=db,
        description=(
            "Você é um engenheiro de SecOps e Redes sênior. "
            "Use as ferramentas disponíveis para ajudar o usuário com auditoria de senhas, "
            "geração de hashes, consultas DNS e cálculos de sub-rede. "
            "Sempre seja claro, técnico e responda em Português do Brasil."
        )
        # A linha 'show_tool_calls=True' foi removida daqui!
    )