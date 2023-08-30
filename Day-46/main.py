import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from get_list import get_list_and_date

scope = "playlist-modify-private"

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_url = os.environ.get("SPOTIFY_REDIRECT_URL")


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_url,
                                               show_dialog=True,
                                               cache_path=".cache"))

songs_list, user_date = get_list_and_date()

song_uri = []
# getting user-id
user = sp.current_user()
user_id = user["id"]


for song in songs_list:
    result = sp.search(q=f"{song}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify.Skipped")


playlist_name = f"{user_date} Billboard 25"
user_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

sp.playlist_add_items(playlist_id=user_playlist["id"], items=song_uri)

print("Playlist has been created successfully")
