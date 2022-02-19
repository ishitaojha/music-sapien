from contextlib import redirect_stderr
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from authy.api import AuthyApiClient


# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="3a10fae4ecfa482290a5f5e2fbfd9971",
#                                                 client_secret="78420d4e52124fa78ff47d7bc6843a60"))

# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

# result = sp.recommendations(seed_genres=["indian"], limit=5, market="IN")

# for i in result['tracks']:
#     # print(i['name'], i['preview_url'])
#     print(i['id'], i['external_urls']['spotify'])

# result = sp.recommendation_genre_seeds()

# for gen in result['genres']:
#     print(gen)


authy_api = AuthyApiClient('RBQ4VjPPzxmahhCQ5qd7y5TVni2plbw1')

sms = authy_api.users.request_sms(478338, {'force':True})

if sms.ok():
    print(sms.content)

