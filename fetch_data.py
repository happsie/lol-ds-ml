import requests
import json
import os
import sys
from dotenv import load_dotenv

if os.path.isfile("match_list.json") or os.path.isfile("matches_data.json"):
    print("data already exists, will not download")
    sys.exit()

# Fetch match list from riot api
load_dotenv(override=True)
API_KEY = os.getenv("RIOT_API_KEY")
PUUID = os.getenv("PUUID")

headers = {"X-RIOT-TOKEN": API_KEY}
match_list_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?start=0&count=50"
resp = requests.get(match_list_url, headers=headers)
match_list_res = resp.json()
print(match_list_res)

with open("match_list.json", "w") as file:
    json.dump(match_list_res, file)

# Fetch specific match

matches = []
for mid in match_list_res:
    match_url = "https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}".format(match_id=mid)
    resp = requests.get(match_url, headers=headers)
    match_res = resp.json()
    if match_res["info"]["gameMode"] != "CLASSIC":
        continue
    matches.append(match_res)

print(match_res)
with open("matches_data.json", "w") as file:
    json.dump(matches, file)
    