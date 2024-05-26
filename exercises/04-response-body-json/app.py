import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")



if response.status_code == 200:
    hora=response.json()
    horas = hora["hours"]
    minutos = hora["minutes"]
    segundos = hora["seconds"]
else:
    ('No se pudo obtener la hora')


print(f'Current time: {horas} hrs {minutos} min and {segundos} sec')