import requests



def get_post_tags(post_id):
    # Your code here
    
    respuesta=requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')
    
    if respuesta.status_code ==200:
     body= respuesta.json()

    for post in body["posts"]:
        if post['id'] == post_id:
           return post['tags']
        
    

    
    return None


print(get_post_tags(146))