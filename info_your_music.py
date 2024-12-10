import requests
import os
import pyfiglet
welcome = pyfiglet.figlet_format("INFO YOU ARTIST", font="slant")

api_key = os.getenv("LAST_FM_API_KEY")


def artist_info(artist_name):
    response = requests.get(
        f"https://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={artist_name}&api_key={
            api_key}&format=json")
    data = response.json()
    specif_info = data['artist']['bio']['summary']
    print(specif_info)


# artist_info()

def top_track(artist_name):
    response = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist_name}&api_key={api_key
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


# top_track()

def top_albums(artist_name):
    response = requests.get(
        f"http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist={artist_name}&api_key={api_key}&format=json")
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

# Artists like this type feature


def similar_artitst(artist_name):
    response = requests.get(
        f"http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist={artist_name}&api_key={api_key}&format=json")
    data = response.json()
    i = 0
    artists = data['similarartists']['artist']
    for artist in artists:
        i = i + 1
        if i > 5:
            break
        like_artists = artist['name']
        print(f"{i}: {like_artists}")


def main():
    print(f"{welcome}\n")
    while True:
        artist_name = input("Type the artist you like: ")
        try:
            artist_info(artist_name)
        except KeyError:
            print("Invalid input")
            continue
        user_choice = input(f"Wanna know more about {
                            artist_name} ? Choose: \n 1.Top Tracks \n 2. Top Albums \n 3. Similar Artists \n q to quit \n ")
        if user_choice == "1":
            top_track(artist_name)
            continue
        elif user_choice == "2":
            top_albums(artist_name)
            continue
        elif user_choice == "3":
            similar_artitst(artist_name)
            continue
        elif user_choise == "q":
            break


main()
