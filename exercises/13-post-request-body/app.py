import requests

#response = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php")
url= 'https://assets.breatheco.de/apis/fake/sample/save-project-json.php'   
datos ={
    "id": 2323,
    "title": "Very big project"
}
headers = {
    "Content-Type": "application/json"
}

mensaje = requests.post(url, json = datos, headers=headers)

print(mensaje.text)