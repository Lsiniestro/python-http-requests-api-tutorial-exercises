import requests

def get_titles():
    # Your code here
    titles= []
    respuesta=requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')
    if respuesta.status_code ==200:
     body= respuesta.json()

    
    

    return titles


print(get_titles())