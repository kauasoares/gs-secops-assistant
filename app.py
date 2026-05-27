from flask import Flask, render_template_string, request, jsonify
from agent import get_secops_agent

app = Flask(__name__)
agent = get_secops_agent()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>SecOps Assistant Web</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #1e1e2f; color: #fff; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }
        .container { width: 100%; max-width: 800px; background: #2a2a40; padding: 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
        h2 { text-align: center; color: #4CAF50; }
        #chatbox { width: 100%; height: 400px; background: #1e1e2f; border: 1px solid #444; border-radius: 5px; padding: 15px; overflow-y: auto; margin-bottom: 20px; box-sizing: border-box; }
        .msg { margin-bottom: 15px; padding: 10px 15px; border-radius: 8px; line-height: 1.5; }
        .user { background-color: #3b5998; margin-left: 20%; text-align: right; }
        .bot { background-color: #2e7d32; margin-right: 20%; text-align: left; }
        form { display: flex; gap: 10px; }
        input[type="text"] { flex-grow: 1; padding: 12px; border: none; border-radius: 5px; background: #fff; color: #000; }
        button { padding: 12px 20px; border: none; border-radius: 5px; background: #4CAF50; color: #fff; font-weight: bold; cursor: pointer; }
        button:hover { background: #45a049; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🛡️ SecOps Assistant Web</h2>
        <div id="chatbox"></div>
        <form id="chat-form">
            <input type="text" id="user-input" placeholder="Pergunte sobre DNS, Hashes, Sub-redes ou Senhas..." required autocomplete="off">
            <button type="submit">Enviar</button>
        </form>
    </div>

    <script>
        const form = document.getElementById('chat-form');
        const chatbox = document.getElementById('chatbox');
        const input = document.getElementById('user-input');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const msg = input.value;
            chatbox.innerHTML += `<div class="msg user"><b>Você:</b><br>${msg}</div>`;
            input.value = '';
            chatbox.scrollTop = chatbox.scrollHeight;

            // Feedback visual enquanto aguarda
            const loadingId = 'loading-' + Date.now();
            chatbox.innerHTML += `<div class="msg bot" id="${loadingId}"><i>O Agente está processando...</i></div>`;
            chatbox.scrollTop = chatbox.scrollHeight;

            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: msg })
                });
                const data = await response.json();
                
                document.getElementById(loadingId).remove();
                
                // Formata quebras de linha básicas
                const formattedResponse = data.response.replace(/\\n/g, '<br>');
                chatbox.innerHTML += `<div class="msg bot"><b>Agente:</b><br>${formattedResponse}</div>`;
            } catch (error) {
                document.getElementById(loadingId).innerText = "Erro ao se conectar com o servidor.";
            }
            chatbox.scrollTop = chatbox.scrollHeight;
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"response": "Mensagem vazia."}), 400
    
    # O método run() do Agno retorna um objeto RunResponse. Pegamos o conteúdo.
    run_response = agent.run(user_message)
    return jsonify({"response": run_response.content})

if __name__ == '__main__':
    print("🌐 Iniciando servidor Flask. Acesse http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)