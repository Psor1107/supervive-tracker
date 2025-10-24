from flask import Flask, render_template, request
import requests
import random
from time import sleep

app = Flask(__name__)

app.config['APPLICATION_ROOT'] = '/kptracker'

BASE_URL = "https://supervive.op.gg/api"
URL = f"{BASE_URL}/players/steam-9f6d3b6dce454d5a96b574d4752ff879/matches?page="
URL2 = f"{BASE_URL}/players/steam-6abea0abf75b47389ebd96e54dab675b/matches?page="

PAGES = 1

TOTAL_W = 0
TOTAL_L = 0
LAST_ID = None

@app.route("/")
def index():
    
    global TOTAL_W, TOTAL_L, LAST_ID

    try:
        with open("total.txt","r") as f:
            lines = f.read().splitlines()
            TOTAL_W = int(lines[0])
            TOTAL_L = int(lines[1])
            LAST_ID = lines[2] if len(lines) > 2 else None
    except FileNotFoundError:
        TOTAL_W = -1
        TOTAL_L = -1
        LAST_ID = Error

    return render_template("index.html", total_w = TOTAL_W, total_l = TOTAL_L)

@app.route("/update")
def update():
    
    global TOTAL_W, TOTAL_L
    
    matches = []
    matches2 = []

    try:
        with open("total.txt", "r") as f:
            lines = f.read().splitlines()
            TOTAL_W = int(lines[0])
            TOTAL_L = int(lines[1])
            LAST_ID = lines[2] if len(lines) > 2 else None
    except (FileNotFoundError, ValueError):
        TOTAL_W, TOTAL_L = -1, -1
        LAST_ID = Error

    for page in range(1, PAGES + 1):
        print(f"agora na pagina {page}...")
        resp1 = requests.get(f"{URL}{page}")
        sleep(random.uniform(0.5, 1.5))
        resp2 = requests.get(f"{URL2}{page}")
        sleep(random.uniform(0.5, 1.5))
        if resp1.status_code == 200 and resp2.status_code == 200:
            matches.extend(resp1.json()["data"])
            matches2.extend(resp2.json()["data"])
        else:
            print(f"eh tarde demais, eles estao vindo... {resp1.status_code}, {resp2.status_code}\n")
            return "erro ao buscar dados"

    mapa2 = {m["match_id"]: m for m in matches2}
    processed = []

    for m in matches:
        if LAST_ID is not None and m["match_id"] == LAST_ID:
            break
        processed.append(m)
    if processed:
        for m in processed:
            m2 = mapa2.get(m["match_id"])
            if not m2 or m2.get("hero_asset_id") != "hero:hookguy":
                continue
            if m.get("placement") == 1:
                TOTAL_W += 1
            elif m.get("placement") == 2:
                TOTAL_L += 1

        NEW_LAST_ID = matches[0]["match_id"]

        with open("total.txt", "w") as f:
            f.write(f"{TOTAL_W}\n")
            f.write(f"{TOTAL_L}\n")
            f.write(f"{NEW_LAST_ID}\n")

    return "updated\n"

if __name__ == "__main__":
    # apenas para desenvolvimento
    app.run(host="0.0.0.0", port=80, debug=True)