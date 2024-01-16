import requests

def fetch_lyrics(artist_name, song):
    url = 'https://lyrics.lewagon.ai/search'
    try:
        response = requests.get(url, params={
            'artist': artist_name,
            'title': song
        })
        # response.status_code is 200 or 404?
        data = response.json()
        return data['lyrics']
    except:
        return 'No data'