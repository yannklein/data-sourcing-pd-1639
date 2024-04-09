import requests

def fetch_lyrics(artist, title):
    try:
        url = f"https://lyrics.lewagon.ai/search"
        response = requests.get(url, params={
            'artist': artist,
            'title': title
        })
        data = response.json()
        return data['lyrics']
    except:
        return 'No lyrics'