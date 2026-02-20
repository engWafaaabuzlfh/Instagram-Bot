import requests
access_token = "EAARQOGUEiwwBOZCihpYw3ZCcww6kCprHMxFcNlSL7fc6cRpJ12t1VnDWHF4CcakYWDxfNFjvfdw8LFlggNjiHXW2pZBNNJToGbeeI09g1n8zdqtYcIZCvZBRZB3ChKRLctB8CQajiiWEEMdGhEJBixJ0yzqUoDgZCfhVoEnVDbBnOCATP1EekkpCCMU7WFZCEw1AmGWRYFA2tOl1QgQI2KPOZBuEZD"
url = f"https://graph.facebook.com/v20.0/141869042351846/conversations?platform=instagram&access_token={access_token}"

response = requests.get(url)

if response.status_code == 200:
    print(response.json())


import requests

url = "https://graph.facebook.com/v20.0/me/messages"

recipient_id = "IGSID"
message_text = "TEXT-OR-LINK"

headers = {
    "Content-Type": "application/json"
}

data = {
    "recipient": {"id": recipient_id},
    "message": {"text": message_text}
}

response = requests.post(url, headers=headers, params={"access_token": access_token}, json=data)

print(response.status_code)
print(response.json())
