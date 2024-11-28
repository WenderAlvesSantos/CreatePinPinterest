import requests

# Substitua pelos seus dados do aplicativo do Pinterest
CLIENT_ID = 'seu_client_id'
CLIENT_SECRET = 'seu_client_secret'
ACCESS_TOKEN = 'seu_token_de_acesso'

# URL para criar um Pin
PIN_URL = "https://api.pinterest.com/v1/pins/"

# Dados do Pin (personalize com suas informações)
data = {
    'board': 'seu_nome_de_board',  # Nome do board onde o Pin será adicionado
    'note': 'Descrição do seu Pin',  # Descrição do Pin
    'link': 'https://link_para_o_seu_site.com',  # URL do seu site ou link relacionado
    'image_url': 'https://url_da_imagem.jpg'  # URL da imagem do Pin
}

# Cabeçalhos de autorização (com o token de acesso)
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

# Fazer a requisição para cadastrar o Pin
response = requests.post(PIN_URL, data=data, headers=headers)

# Verificar a resposta
if response.status_code == 201:
    print("Pin criado com sucesso!")
    print(response.json())  # Exibe os detalhes do Pin criado
else:
    print(f"Erro ao criar o Pin: {response.status_code}")
    print(response.text)
