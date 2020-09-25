import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("CLIENT_ID"),
                                               client_secret=os.environ.get("CLIENT_SECRET"),
                                               redirect_uri="https://blog.thedojo.mx",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
