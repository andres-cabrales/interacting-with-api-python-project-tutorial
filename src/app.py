import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from matplotlib import pyplot as plt

# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

queen_uri = 'spotify:artist:1dfeR4HaWDbWqFHLkxsg1d'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET")
))

results = spotify.artist_top_tracks(queen_uri, country = 'CL')

track_names_list = []
track_popularity_list = []
track_duration_list = []

for track in results['tracks'][:10]:
    track_names_list.append(track['name'])
    track_popularity_list.append(track['popularity'])
    track_duration_list.append(track['duration_ms'])

tracks_df = pd.DataFrame({'name':track_names_list, 'popularity':track_popularity_list, 'duration_ms':track_duration_list})
tracks_df =  tracks_df.sort_values(by='popularity', ascending=True)

top_3_result = tracks_df[:3]

sns.scatterplot(data = tracks_df, x= 'duration_ms', y='popularity')
plt.show(block=True)