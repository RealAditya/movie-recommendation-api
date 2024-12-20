from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Fetch the TMDb API key from the environment
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

if not TMDB_API_KEY:
    raise RuntimeError("TMDB_API_KEY is not set in the environment!")

# Endpoint to get popular movies
@app.route('/movies/popular', methods=['GET'])
def get_popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data['results'])
    return jsonify({"error": "Failed to fetch popular movies"}), 500

# Endpoint to recommend movies based on user preferences
@app.route('/movies/recommend', methods=['POST'])
def recommend_movies():
    user_preferences = request.json.get('preferences', [])
    if not user_preferences:
        return jsonify({"error": "No preferences provided"}), 400
    
    # Mock recommendation logic
    recommendations = [f"Mock Movie based on {pref}" for pref in user_preferences]
    return jsonify({"recommendations": recommendations})

# Endpoint to fetch movie details by ID
@app.route('/movies/details/<int:movie_id>', methods=['GET'])
def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    return jsonify({"error": f"Failed to fetch details for movie ID {movie_id}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
