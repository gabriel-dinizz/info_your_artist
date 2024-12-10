import requests
import os

api_key = os.getenv("LAST_FM_API_KEY")


def artist_info():
    response = requests.get(
        f"https://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=eminem&api_key={
            api_key}&format=json")
    data = response.json()
    specif_info = data['artist']['bio']['summary']
    print(specif_info)


# artist_info()

def top_track():
    response = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=cher&api_key={api_key
                                                                                                                }&format=json")

    i = 0
    data = response.json()
    tracks = data['toptracks']['track']
    for track in tracks:
        i = i + 1
        if i > 5:
            break
        playcount = track['name']
        print(f"{i}: {playcount}")


top_track()


def top_albums():
    response = requests.get(
        f"http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist=cher&api_key={api_key}&format=json")
    i = 0
    data = response.json()
    albums = data["topalbums"]["album"]
    for album in albums:
        i = i + 1
        if i > 5:
            break
        album_name = album['name']
        print(f"{i}: {album_name}")


# top_albums()
