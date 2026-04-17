import requests

def app():
    api_url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
    response = requests.get(api_url)
    dump = response.json()
    dump = dump["joke"]
    print(dump)

if __name__ == "__main__":
    app()
