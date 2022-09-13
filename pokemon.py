import requests

if response.status_code == 200:
        payload = response.json()
        results = payload.get('results',[])
        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)

