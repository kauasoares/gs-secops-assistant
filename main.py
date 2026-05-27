from agent import get_secops_agent

def main():
    print("="*50)
    print("🛡️  SecOps Assistant CLI Iniciado!")
    print("Digite 'sair', 'exit' ou 'quit' para encerrar a sessão.")
    print("="*50)
    
    agent = get_secops_agent()
    
    # Recupera a sessão para demonstrar a persistência
    session_id = agent.session_id
    print(f"[Memória ativada - ID da Sessão: {session_id}]\n")
    
    while True:
        try:
            user_input = input("🧑 Você: ")
            if user_input.lower() in ['sair', 'exit', 'quit']:
                print("Encerrando o agente... Até logo!")
                break
            
            print("\n🤖 Agente:")
            # stream=True faz a resposta aparecer digitando aos poucos
            agent.print_response(user_input, stream=True)
            print("-" * 50)
        except KeyboardInterrupt:
            print("\nEncerrando...")
            break

if __name__ == "__main__":
    main()