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
playlists = sp.user_playlists("xhamyd")
print(f"Found {len(playlists["items"])} playlists...")

for i, playlist in enumerate(playlists['items']):
    print(f"{i}) {playlist['name']}")
    print(f"    id = {playlist['id']}")
    print(f"    owner = {playlist['owner']['display_name']}")
    print(f"    public = {playlist['public']}")
    print(f"    collaborative = {playlist['collaborative']}")
    print()

print("\nDone!\n")
