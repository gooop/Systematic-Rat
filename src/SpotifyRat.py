### SpotifyRat
### Logan L and Gavin C
### Started 5/15/2023

# Imports
from dotenv import load_dotenv
import os
import base64
from requests import post

load_dotenv()

spot_client_id = os.getenv("SPOT_CLIENT_ID")
spot_client_secret = os.getenv("SPOT_CLIENT_SECRET")

print(spot_client_id, spot_client_secret)

def get_token():
    auth_string = spot_client_id + ":" + spot_client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_base64), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

token = get_token()
print(token)