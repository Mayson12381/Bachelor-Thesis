import json
from classes import Round, Player, Kevlar

def get_bomb_plant_index(frames: list) -> int:
    for index, frame in enumerate(frames):
        if frame["bombPlanted"] == True:
            return index


def getKevlarType(kevlar, hasHelmet):
    if hasHelmet:
        return Kevlar.HELMET
    if kevlar >= 0:
        return Kevlar.KEVLAR
    else:
        return Kevlar.NONE


def getMainWeapon(inv: list):
    return ""


def getUtility(inv: list):
    return []


data = json.load(open('example_demo.json'))
jsonObj = {
    "id": 1,
    "rounds": []
}

for round in data["gameRounds"]:
    if round["bombPlantTick"]:
        bomb_plant_index = get_bomb_plant_index(round["frames"])
        # frame of plant
        fop = round["frames"][bomb_plant_index]
        # frame of interest
        foi = round["frames"][bomb_plant_index - 30]
        # print(foi["seconds"]) # 30771

        ct_players = [
            Player(
                hp=player["hp"],
                kevlar=getKevlarType(player["armor"], player["hasHelmet"]).value,
                has_defuser=player["hasDefuse"],
                area_name=player["areaName"],
                weapon=getMainWeapon(player["inventory"]),
                utility=getUtility(player["inventory"]),
            ).__dict__ for player in foi["ct"]["players"]]

        t_players = [
            Player(
                hp=player["hp"],
                kevlar=getKevlarType(player["armor"], player["hasHelmet"]).value,
                has_defuser=player["hasDefuse"],
                area_name=player["areaName"],
                weapon=getMainWeapon(player["inventory"]),
                utility=getUtility(player["inventory"]),
            ).__dict__ for player in foi["t"]["players"]]

        round = Round(
            bomb_planted=round["bombPlantTick"] != None,
            ct_alive_at_plant=fop["ct"]["alivePlayers"],
            ct_buy_type=round["ctBuyType"],
            ct_players=ct_players,
            ct_spend=round["ctSpend"],
            t_alive_at_plant=fop["t"]["alivePlayers"],
            t_buy_type=round["tBuyType"],
            t_players=t_players,
            t_spend=round["tSpend"],
            t_won=round["winningSide"] == "T"
        )

        # print(vars(round))
        # print(vars(ct_players[0]))
        jsonObj["rounds"].append(json.dumps(round.__dict__))




with open('data.json', 'w') as outfile:
    json.dump(jsonObj, outfile)

