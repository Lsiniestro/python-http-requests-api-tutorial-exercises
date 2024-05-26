import requests

url = 'https://assets.breatheco.de/apis/fake/sample/post.php'
datos = {'prueba': 'texto de prueba'}

mensaje = requests.post(url, json = datos)

print(mensaje.text)
# Your code here
