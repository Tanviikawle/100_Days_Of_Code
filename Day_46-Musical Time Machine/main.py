import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL="https://www.billboard.com/charts/hot-100/2003-04-26/"
SPOTIPY_CLIENT_ID="b1f278b638664061abf643f425cbc751"
SPOTIPY_CLIENT_SECRET="c15e45cd1d304eab8026519d27034e86"

SPOTIFY_SONG_ENDPOINT="https://api.spotify.com/v1/search"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri="http://example.com",
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

# user_id="317fune3ay4xqi2mywmbjqcru2yq"

date=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,"html.parser")



songs_list = soup.select("li ul li h3")

song_names=[song.getText().strip() for song in songs_list]

parameters={
    "year":2003,
    "type":"track"
}

song_uris=[]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)
# print(song_response)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)



    