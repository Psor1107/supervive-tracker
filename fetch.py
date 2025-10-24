import requests

BASE_URL = "https://supervive.op.gg/api"
URL = f"{BASE_URL}/players/steam-9f6d3b6dce454d5a96b574d4752ff879/matches?page=1"
URL_MATCH = f"{BASE_URL}/matches/steam-576242b4-6253-4891-bc09-d3ace669a66b"

respose = requests.get(URL_MATCH)
data = respose.json()
print(data)