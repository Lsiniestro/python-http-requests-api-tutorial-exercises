import requests

def get_attachment_by_id(attachment_id):
    # Your code here
    respuesta=requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')
    
    if respuesta.status_code ==200:
     body= respuesta.json()
     
     for post in body["posts"]:
            # Check if the post has attachments
            if "attachments" in post:
                # Loop through each attachment
                for attachment in post["attachments"]:
                    if attachment["id"] == attachment_id:
                        return attachment["title"]
        
            print("No attachment found")
    else:
        print("Failed to fetch data from the endpoint.")

    

    return None

print(get_attachment_by_id(137))