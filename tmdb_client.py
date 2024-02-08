import requests
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhYzhiZGQ2MDRkODVjNTRkYjQ1ZDVkMzY5NmE4NWZiNCIsInN1YiI6IjY1YjgzM2ViMzNhMzc2MDE3Yjg1MTRmZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.y4BhCdT6Zhm8g1_sVyIBMaievYWrq8mtMyWZc_HaYww"

def get_popular_movies(list_type):
    endpoint = {
        "popular": "https://api.themoviedb.org/3/movie/popular",
        "top_rated": "https://api.themoviedb.org/3/movie/top_rated",
        "upcoming": "https://api.themoviedb.org/3/movie/upcoming",
        "now_playing": "https://api.themoviedb.org/3/movie/now_playing"
    }
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint[list_type], headers=headers)
    return response.json()


def get_movies(list_type, how_many):
    data = get_popular_movies(list_type)
    return data["results"][:how_many]


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id, how_many):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"][:how_many]


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


# movies = get_movies(list_type)
# for movie in movies:
#     print(movie["title"])

# list_type = ["popular", "top_rated", "upcoming", "now_playing"]

# def get_type_movies(list_type):
#     endpoints = {
#         "popular": "https://api.themoviedb.org/3/movie/popular",
#         "top_rated": "https://api.themoviedb.org/3/movie/top_rated",
#         "upcoming": "https://api.themoviedb.org/3/movie/upcoming",
#         "now_playing": "https://api.themoviedb.org/3/movie/now_playing"
#     }
#     endpoint = endpoints.get(list_type)
#     if endpoint:
#         data = fetch_movies(endpoint)
#         return data.get("results", [])[:how_many]
#     else:
#         return []
#     endpoint = "https://api.themoviedb.org/3/movie/now_playing"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

# def get_top_rated_movies():
#     endpoint = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=vote_average.desc&without_genres=99,10755&vote_count.gte=200"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

# def get_upcoming_movies():
#     endpoint = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_release_type=2|3&release_date.gte={min_date}&release_date.lte={max_date}"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

# def get_now_playing_movies():
#     endpoint = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_release_type=2|3&release_date.gte={min_date}&release_date.lte={max_date}"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

# def get_movies(list_name, how_many):
#     data = None 
#     if list_name == "popular":
#         data = get_popular_movies()
#     elif list_name == "top_rated":
#         data = get_top_rated_movies()
#     elif list_name == "upcoming":
#         data = get_upcoming_movies()
#     elif list_name == "now_playing":
#         data = get_now_playing_movies()
#     else:
#         return "Invalid list name"
    
#     return data["results"][:how_many]