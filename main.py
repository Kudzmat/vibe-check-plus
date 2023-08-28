from datetime import date
import os
from dotenv import load_dotenv
import spotipy
import pprint

from spotipy.oauth2 import SpotifyOAuth

load_dotenv()  # load the environment variables

# storing environment variables
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_USER_ID = os.getenv('SPOTIFY_USER_ID')
PLAYLIST_ID = os.getenv('PLAYLIST_ID')

# set scope for app authorization
SCOPE = "user-library-read user-top-read playlist-modify-public user-follow-read user-library-read " \
        "playlist-read-private playlist-modify-private "


def playlist():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    # pick a playlist to add the songs to
    # To find the Spotify playlist id enter the playlist page, click the (...) button near the play button
    # Click "Copy Playlist Link" under the Share menu. The playlist id is the string right after "playlist/"
    playlist_id = PLAYLIST_ID

    # getting today's date
    current_date = (date.today()).strftime('%m-%d-%Y')

    # saving playlist name with today's date
    playlist_name = f'Vibe Check -> {current_date}'

    artists_ids = []  # spotify's recommended artist IDs will be added to this list
    tracks = []  # the recommended tracks will be added to this list
    artist_list = ['Tinashe', 'Jhene Aiko', 'Brent Faiyaz', 'Toro Y Moi',
                   'Frank Ocean']  # calling the artist list from the previous route

    # putting artist ids in a list so we can use them in the recommendations function
    for artist in artist_list:
        # search for the artist
        name_result = sp.search(artist, limit=1, type='artist', market='US')

        # get artist ID
        artist_info = name_result['artists']['items'][0]
        artist_id = artist_info['id']

        # add artist to list
        artists_ids.append(artist_id)

    # getting 5 song recommendation and appending them to tracks
    result = sp.recommendations(seed_artists=artists_ids, limit=5, country='US')
    for item in result['tracks']:
        # append the track['uri']
        tracks.append(item['uri'])

    # adding songs to our playlist
    return tracks

    # sp.playlist_add_items(playlist_id=playlist_id, items=[song for song in tracks])

    # updating the playlist name with last updated date
    # sp.playlist_change_details(name=playlist_name, playlist_id=playlist_id)

    # takes you to playlist page on Spotify


def get_info(track_list):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    for track in track_list:
        tune = sp.search(q=track)
        info = tune['tracks']

        song_preview = info['items'][0]['preview_url']
        song_name = info['items'][0]['name']
        song_art = info['items'][0]['album']['images'][1]['url']
        artist_name = info['items'][0]['artists'][0]['name']
        song_id = info['items'][0]['album']['id']

        recommendations.append({
            'song_id': song_id,
            'song_name': song_name,
            'song_art': song_art,
            'song_preview': song_preview,
            'artist_name': artist_name,
        })
        # Introduce a delay of 1 second before the next API call
        time.sleep(1)

    pprint.pprint(recommendations)


track_list = playlist()
get_info(track_list)
