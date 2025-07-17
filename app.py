from flask import Flask, render_template, request
import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
BOT_ID = os.getenv("BOT_ID")
WORKSPACE_ID = os.getenv("WORKSPACE_ID")

app = Flask(__name__)

def enviar_mensagem_botpress(mensagem, user_id="user_01"):
    url = f"https://api.botpress.cloud/v1/bots/{BOT_ID}/workspaces/{WORKSPACE_ID}/converse/{user_id}"
    headers = {
        "X-Client-Id": CLIENT_ID,
        "Content-Type": "application/json"
    }
    data = {
        "type": "text",
        "text": mensagem
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        json_resp = response.json()
        # Ajuste aqui para pegar a resposta textual do bot no formato correto
        # Normalmente a resposta está em json_resp['responses'] como lista
        respostas = json_resp.get('responses', [])
        if respostas:
            return ' '.join([r.get('text', '') for r in respostas])
        else:
            return "Sem resposta do bot."
    else:
        return f"Erro: {response.status_code} - {response.text}"

@app.route('/', methods=['GET', 'POST'])
def index():
    resposta = ''
    if request.method == 'POST':
        pergunta = request.form['pergunta'].strip()
        resposta = enviar_mensagem_botpress(pergunta)
    return render_template('index.html', resposta=resposta)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)








