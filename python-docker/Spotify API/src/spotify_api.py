import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

print("Getting credentials...")
scope = " ".join([
    "user-library-read",
    "playlist-read-private",
    "playlist-read-collaborative",
    "user-follow-read"
])
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               open_browser=False))
print("Done!\n")

# auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)

# results = sp.current_user_playlists(limit=50)
# for i, item in enumerate(results['items']):
#     print("%d %s" % (i, item['name']))
playlists = sp.user_playlists("xhamyd", limit=100)
print(f"Found {len(playlists["items"])} playlists...")

for i, playlist in enumerate(playlists['items']):
    print(f"{i}) {playlist['name']}")
    print(f"    id = {playlist['id']}")
    print(f"    owner = {playlist['owner']['display_name']}")
    print(f"    public = {playlist['public']}")
    print(f"    collaborative = {playlist['collaborative']}")

    tracks = sp.playlist_items(playlist['id'], fields="items,next", limit=200)
    info_tracks = list()
    while tracks:
        for track in tracks['items']:
            track_obj = track['track']
            info_tracks.append(dict(name=track_obj['name'],
                                    artists=", ".join(artist['name'] for artist in track_obj['artists']),
                                    album=track_obj['album']['name']))

        # Queries are limited, so keep querying until we have exhausted the list
        if tracks['next']:
            print(f"Found {len(info_tracks)} tracks, still searching...")
            tracks = sp.next(tracks)
        else:
            tracks = None

    print("=== Tracks: ===")
    # TODO: write data to file directly
    for j, track in enumerate(info_tracks):
        print(f"{j}: \"{track['name']}\" by {track['artists']} ({track['album']})")
    print()

print("Done!\n")
