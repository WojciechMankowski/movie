import requests
import json
def API():
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"

    title_movie = input("Jakiego filmu szukaż? ")
    headers = {
        'x-rapidapi-key': "f79e279747msh954850d254dfb24p14c651jsnfe5e014b1f94",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params={"q": title_movie})

    movie = []
    movie_title = []
    dane = json.loads(response.text)
    dane = dane['d'][0]
    for key, item in dane.items():
        print(key, item)
        if key == 'l':
            movie.append(f"Tytuł: {item}")
        elif key == "y":
            movie.append(f"Rok wydania: {item}")
        elif key == "s":
            movie.append(f"Twórca: {item}")

    return movie
def WriteMove(movie):
    print("Informacje o Twoim filmie:")
    for index in range(len(movie)):
        print(movie[index])
WriteMove(API())