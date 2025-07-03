from flask import Flask, render_template, request

app = Flask(__name__)

# Dicionário com perguntas e respostas
perguntas_respostas = {
    "oq são combustiveis fósseis?": "Os combustíveis fósseis são fontes de energia formadas a partir da decomposição de matéria orgânica ao longo de milhões de anos...",
    "quais são as principais fontes de energia aqui no brasil?": "Em 2022, as principais fontes foram hídricas, eólicas e etanol...",
    "o que é transição energética?": "Transição energética é a mudança do uso de fontes poluentes para fontes limpas e renováveis...",
    "por que é importante usar energia renovável?": "Porque elas não se esgotam, poluem menos e combatem o aquecimento global.",
    "o que é crise de energia?": "É quando a produção de energia não consegue atender à demanda da população...",
    "quais são os desafios da transição energética?": "Desafios incluem alto custo inicial, dependência de fósseis, e resistência de empresas.",
    "como a energia solar funciona?": "Painéis solares transformam luz do sol em eletricidade por meio de células fotovoltaicas.",
    "energia eólica é confiável?": "Sim, mas depende da velocidade do vento e geralmente é usada junto com outras fontes."
}

@app.route('/', methods=['GET', 'POST'])
def index():
    resposta = ''
    if request.method == 'POST':
        pergunta = request.form['pergunta'].strip().lower()
        resposta = perguntas_respostas.get(pergunta, "Desculpe, não tenho uma resposta para essa pergunta.")
    return render_template('index.html', resposta=resposta)

# SÓ este bloco deve estar no final:
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
