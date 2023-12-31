import json
import csv
import os
import sys

if not os.path.isfile("matches_data.json"):
    sys.exit()

f = open('matches_data.json')
matches_dict = json.load(f)

match_data = []
for match in matches_dict:
    for participant in match["info"]["participants"]:
        match_data.append({
            "summoner name": participant["summonerName"],
            "game duration": match["info"]["gameDuration"],
            "win": 1 if participant["win"] == True else 0,
            "champion": participant["championName"],
            "champion id": participant["championId"],
            "champion level": participant["champLevel"],
            "deaths": participant["deaths"],
            "kills": participant["kills"],
            "assists": participant["assists"],
            "role": participant["role"],
            "wards killed": participant["wardsKilled"],
            "wards placed": participant["wardsPlaced"],
            "dragon kills": participant["dragonKills"],
            "baron kills": participant["baronKills"],
            "damage dealt to objectives": participant["damageDealtToObjectives"],
            "damage dealt to turrets": participant["damageDealtToTurrets"],
            "turrets lost": participant["turretsLost"],
            "turret kills": participant["turretKills"],
            "total minions killed": participant["totalMinionsKilled"],
            "inhibitor takedowns": participant["inhibitorTakedowns"],
            "inhibitor kills": participant["inhibitorKills"]
        })

matches_formatted_file = open('matches_formatted.csv', 'w', encoding="utf-8")
writer = csv.writer(matches_formatted_file)
writer.writerow(["summoner name", "game duration", "win", "champion", "champion id", "champion level", "deaths", "kills", "assists", "role", "wards killed", "wards placed", "dragon kills", "baron kills", "damage dealt to objectives", "damage dealt to turrets", "turrets lost", "turret kills", "total minions killed", "inhibitor takedowns", "inhibitor kills"])
for match_dict in match_data:
    writer.writerow(match_dict.values())
matches_formatted_file.close()