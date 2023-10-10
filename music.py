import requests

def fetch_lyrics(artist, title):
    url = "https://lyrics.lewagon.ai/search"
    try:
        data = requests.get(url, params={"artist": artist, "title": title}).json()
        return data['lyrics']
    except:
        return "N/A"
# line 12 is executed when running "python music.py", but not when importing music.py
if __name__ == "__main__":
    artist_name = "Ed Sheeran"
    song_title = "Shape of you"
    print(fetch_lyrics(artist_name, "Shape of me"))