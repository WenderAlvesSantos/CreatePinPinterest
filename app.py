import streamlit as st
import requests

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
        st.success("Pin criado com sucesso!")
        st.json(response.json())
    else:
        st.error(f"Erro ao criar o Pin: {response.status_code}")
        st.text(response.text)

# Função para exibir a Política de Privacidade
def exibir_politica_privacidade():
    st.title("Política de Privacidade")
    st.write("""
    Esta Política de Privacidade descreve como coletamos, usamos e protegemos suas informações. Ao utilizar este serviço, você concorda com os termos descritos nesta política.

    **Coleta de Dados**: Coletamos informações fornecidas por você ao criar um Pin no Pinterest, como nome de board, descrição e links de imagem.

    **Uso das Informações**: As informações fornecidas são usadas exclusivamente para cadastrar Pins no Pinterest e não são compartilhadas com terceiros.

    **Segurança**: Garantimos que todas as informações fornecidas são protegidas e utilizadas apenas para a finalidade de criar Pins.

    **Alterações na Política**: Reservamo-nos o direito de alterar esta Política de Privacidade a qualquer momento. Quaisquer mudanças serão informadas aqui.
    """)

# Página de Cadastro de Pin
def pagina_cadastro():
    st.title("Cadastrar Pin no Pinterest")

    # Campos do formulário
    board = st.text_input("Nome do Board")
    note = st.text_area("Descrição do Pin")
    link = st.text_input("Link do Site")
    image_url = st.text_input("URL da Imagem")

    if st.button("Cadastrar Pin"):
        if board and note and link and image_url:
            cadastrar_pin(board, note, link, image_url)
        else:
            st.error("Por favor, preencha todos os campos!")

# Função principal para a navegação
def main():
    # Obter os parâmetros de consulta da URL
    query_params = st.experimental_get_query_params()

    # Verificar qual página o usuário quer acessar
    if 'page' in query_params and query_params['page'][0] == 'politica-privacy':
        exibir_politica_privacidade()
    else:
        pagina_cadastro()

# Executar a aplicação
if __name__ == "__main__":
    main()
