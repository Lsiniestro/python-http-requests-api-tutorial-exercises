import requests

# Your code here

respuesta=requests.get('https://assets.breatheco.de/apis/fake/sample/project_list.php')

if respuesta.status_code ==200:
    body= respuesta.json()

    imagen= body[2]['images'][2]
    print(imagen)

