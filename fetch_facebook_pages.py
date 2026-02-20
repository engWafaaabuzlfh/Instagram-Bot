import requests

user_access_token = "user access token"  # Replace with your actual access token
url = f"https://graph.facebook.com/v20.0/me/accounts"

params = {
    'access_token': user_access_token,
    'fields': 'id,name,email'  # Adjust fields as per your requirements
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Success!")
    print(response.json())
