from requests.auth import HTTPBasicAuth
import requests
import base64

class ManipulaRepositorios:
    
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = 'token'
        self.headers = {'Authorization' : 'Bearer' + self.access_token, 
                        'Accept': 'application/vnd.github.v3+json',
                        'X-GitHub-Api-Version': '2022-11-28'}
        
        
    def cria_repo(self, nome_repo):
        data = {
            "name" : nome_repo,
            "description" : "Dados dos repositorios de alguma empresa",
            "private" : False
        }
        #response = requests.post(f'{self.api_base_url}/user/repos',
        #                         json=data, headers=self.headers)
        
        response = requests.post(f'{self.api_base_url}/user/repos', json=data,headers=self.headers,
                                 auth=HTTPBasicAuth('dgghenri@gmail.com', 'senha'))
        
        print(f'status_code criação do repositório: {response.status_code}')
        
        
    def add_arquivo(self, nome_arquivo, caminho_arquivo):
        # Codificando o arquivo
        with open('caminho_arquivo', 'rb') as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)
        
        # Realiza o upload
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            'message' : "Adicionando um novo arquivo",
            "content" : encoded_content.decode("utf-8")
        }
        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')
        
        
# Instancia um objeto
novo_repo = ManipulaRepositorios('DieggoHenrique')

# Criando o repositorio
nome_repo = 'linguagens-repositorios-empresa'
novo_repo.cria_repo(nome_repo)

# Adicionando arquivos salvos no repositório criado
path = '/Users/dieggo.araujo/Desktop/Documentos/projeto_requests/'
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')