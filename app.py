from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Substitua pelos seus dados do aplicativo do Pinterest
CLIENT_ID = 'seu_client_id'
CLIENT_SECRET = 'seu_client_secret'
ACCESS_TOKEN = 'seu_token_de_acesso'

# URL para criar um Pin
PIN_URL = "https://api.pinterest.com/v1/pins/"

# Função para cadastrar o Pin
def cadastrar_pin(board, note, link, image_url):
    data = {
        'board': board,
        'note': note,
        'link': link,
        'image_url': image_url
    }

    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }

    response = requests.post(PIN_URL, json=data, headers=headers)

    if response.status_code == 201:
        return "Pin criado com sucesso!"
    else:
        return f"Erro ao criar o Pin: {response.status_code}"

# Rota para a página de cadastro de Pin
@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        board = request.form['board']
        note = request.form['note']
        link = request.form['link']
        image_url = request.form['image_url']
        
        if board and note and link and image_url:
            message = cadastrar_pin(board, note, link, image_url)
        else:
            message = "Por favor, preencha todos os campos!"
    
    return render_template('index.html', message=message)

# Rota para a Política de Privacidade
@app.route('/politica-privacy')
def politica_privacidade():
    return render_template('politica_privacidade.html')

# Rodar o servidor
if __name__ == "__main__":
    app.run(debug=True)
