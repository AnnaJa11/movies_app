import requests


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhYzhiZGQ2MDRkODVjNTRkYjQ1ZDVkMzY5NmE4NWZiNCIsInN1YiI6IjY1YjgzM2ViMzNhMzc2MDE3Yjg1MTRmZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.y4BhCdT6Zhm8g1_sVyIBMaievYWrq8mtMyWZc_HaYww"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"






