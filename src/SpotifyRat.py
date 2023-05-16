##### SpotifyRat
##### Logan L and Gavin C
##### Started 5/15/2023

# Imports
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

# Access Spotify API
spot_client_id = os.getenv("SPOT_CLIENT_ID")
spot_client_secret = os.getenv("SPOT_CLIENT_SECRET")

#Access Cont - Token
def get_token():
    auth_string = spot_client_id + ":" + spot_client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

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

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

### Search Functions

# Search Artist
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists.")
        return None
    
    return json_result[0]

# Search Track
def search_for_track(token, track_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={track_name}&type=track&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    if len(json_result) == 0:
        print("No track with this name exists.")
        return None
    
    return json_result[0]

# Search Playlist
def search_for_playlist(token, playlist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={playlist_name}&type=playlist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["playlists"]["items"]
    if len(json_result) == 0:
        print("No playlist with this name exists.")
        return None
    
    return json_result[0]

# Get Top Tracks from Artist
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

### Playlist Functions

# Append to Playlist

### Tomfoolery

# Result of Search
token = get_token()
result_artist = search_for_artist(token, "acdc")
result_track = search_for_track(token, "all time low")
result_playlist = search_for_playlist(token, "breakcore mix exe")
artist_id = result_artist["id"]
track_id = result_track["id"]
playlist_id = result_playlist["id"]

songs = get_songs_by_artist(token, artist_id)

# Testing
print(result_track["album"]["artists"][0]["name"])

for i, song in enumerate(songs):
    print(f"{i + 1}. {song['name']}")
