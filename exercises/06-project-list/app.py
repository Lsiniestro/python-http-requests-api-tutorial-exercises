import requests

# Your code here
respuesta=requests.get('https://assets.breatheco.de/apis/fake/sample/project_list.php')

if respuesta.status_code ==200:
    body= respuesta.json()

    nombre= body[1]['name']
    print(nombre)

