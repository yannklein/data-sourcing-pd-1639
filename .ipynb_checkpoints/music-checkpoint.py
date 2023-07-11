import requests

def fetch_lyrics(artist, title):
    url = f"https://lyrics.lewagon.ai/search?artist={artist}&title={title}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['lyrics']
    except:
        return 'No Data'

# all the code in line below is executed when running `python music.py` but not when file is imported
if __name__ == "__main__":
    print(fetch_lyrics("The Beatles", "Yesterday"))