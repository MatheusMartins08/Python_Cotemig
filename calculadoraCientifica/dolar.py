import requests

url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
#requests = biblioteca para fazer requisições HTTP
# Permite acessar APIs (sites que retornam dados)

def cotacao_dolar():
    response = requests.get(url) #url = endereço da API requests.get = faz uma requisição do tipo GET mesma coisa que abrir um navegador
    if response.status_code == 200: # status_code = código HTTP da resposta 404 é não encontrado, 500 erro no servidor
        data = response.json() #A API retorna texto em formato JSON
       
        dolar = data["USDBRL"]["bid"]  #guardo o valor
        return dolar
    else:
        return print("Erro ao buscar cotação")