from flask import Flask, render_template, request, redirect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from predict_genre import predict_genre

app = Flask(__name__)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="3a10fae4ecfa482290a5f5e2fbfd9971",
                                                client_secret="78420d4e52124fa78ff47d7bc6843a60"))

genre = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/quiz")
def quiz():
    return render_template('quiz.html')

@app.route('/get_answers', methods=['POST'])
def get_answers():
    data = request.get_json().get("answers")
    global genre
    genre = predict_genre(data)
    return redirect('/song')
    

@app.route("/song")
def song():
    global genre
    list_songs = []
    print(genre)
    result = sp.recommendations(seed_genres=list(genre), limit=5)
    for track in result['tracks']:
        id = track['id']
        list_songs.append(f"https://open.spotify.com/embed/track/{id}")
    return render_template('songs.html', songs = list_songs)

if __name__ == "__main__":
    app.run(debug=True)
