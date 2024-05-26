import requests

# Your code here

respuesta=requests.get('https://assets.breatheco.de/apis/fake/sample/project1.php')

if respuesta.status_code ==200:
    body= respuesta.json()

    nombre= body['name']
    print(nombre)
else:
    print('Error de conexion')