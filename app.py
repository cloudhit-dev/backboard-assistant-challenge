import requests

API_KEY = "espr_d50PVrO-aeKDSsReBXf5Au76XGu5sZFFrHEqbW8b5bs"
URL = "https://api.backboard.io/v1/assistants"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "name": "GHW Assistant",
    "model": "gpt-4",
    "system_prompt": "You are a helpful assistant for Global Hack Week."
}

response = requests.post(URL, headers=headers, json=data)

if response.status_code == 200 or response.status_code == 201:
    print("Success")
    print(response.json())
else:
    print(f"Error: {response.status_code}")