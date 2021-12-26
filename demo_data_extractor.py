import json
from classes import Round, Kevlar
import pandas as pd
from os import walk

def get_bomb_plant_index(frames: list) -> int:
    for index, frame in enumerate(frames):
        if frame["bombPlanted"] == True:
            return index


def getKevlarType(kevlar, hasHelmet) -> Kevlar:
    if hasHelmet:
        return Kevlar.HELMET
    if kevlar >= 0:
        return Kevlar.KEVLAR
    else:
        return Kevlar.NONE


def getMainWeapon(inv: dict):
    if not inv: return { 'weapon_name': "None", 'weapon_type': "None" }
    rifle = ""
    pistol = ""
    for slot in inv:
        if slot["weaponClass"] == "Rifle":
            rifle = slot["weaponName"]
        if slot["weaponClass"] == "Pistols":
            pistol = slot["weaponName"]
    if not rifle and not pistol: return { 'weapon_name': "None", 'weapon_type': "None" }
    if rifle: return { 'weapon_name': rifle, 'weapon_type': "Rifle" }
    else: return { 'weapon_name': pistol, 'weapon_type': "Pistol" }


def getRifleAmount(players: dict):
    rifle_amount = 0
    if not players: return rifle_amount
    for player in players:
        if player["inventory"]:
            for slot in player["inventory"]:
                if slot["weaponClass"] == "Rifle":
                    rifle_amount += 1
    return rifle_amount


def getPistolAmount(players: dict):
    pistol_amount = 0
    if not players: return pistol_amount
    for player in players:
        if player["inventory"]:
            for slot in player["inventory"]:
                if slot["weaponClass"] == "Pistols":
                    pistol_amount += 1
    return pistol_amount


def getUtility(inv: list):
    grenades = {
        "molotov": False,
        "grenade": False,
        "smoke": False,
        "flash1": False,
        "flash2": False,
    }

    if not inv: return grenades

    for slot in inv:
        if slot["weaponClass"] == "Grenade":
            if slot["weaponName"] == "Molotov" or slot["weaponName"] == "Incendiary Grenade":
                grenades["molotov"] = True
            if slot["weaponName"] == "HE Grenade":
                grenades["grenade"] = True
            if slot["weaponName"] == "Smoke Grenade":
                grenades["smoke"] = True
            if slot["weaponName"] == "Flashbang":
                grenades["flash1"] = True
                if slot["ammoInReserve"]:
                    grenades["flash2"] = True

    return grenades


def extract_data_from_parsed_demo(parsed_demo_path: str, file_name: str):
    data = json.load(open(parsed_demo_path))
    rounds = []

    for round in data["gameRounds"]:
        if (not round["isWarmup"]
        and round["frames"]
        and len(round["frames"]) > 20
        and round["weaponFires"]
        and round["winningTeam"]):
            if round["bombPlantTick"]:
                bomb_plant_index = get_bomb_plant_index(round["frames"])
            else:
                bomb_plant_index = len(round["frames"]) - 1
            # frame of plant
            fop = round["frames"][bomb_plant_index]
            # frame of interest
            foi = round["frames"][bomb_plant_index - 20]
            # print(foi["seconds"]) # 30771

            if foi["t"]["players"] and len(foi["t"]["players"]) == 5 and foi["ct"]["players"] and len(foi["ct"]["players"]) == 5:
                round_object = Round(
                    demo_name=data["matchID"].split("/")[2],
                    t_team_name=round["tTeam"],
                    ct_team_name=round["ctTeam"],
                    round_number=round["roundNum"],
                    round_end_reason=round["roundEndReason"],
                    bomb_planted=round["bombPlantTick"] != None,
                    bombsite=fop["bombsite"],
                    t_rifles=getRifleAmount(foi["t"]["players"]),
                    t_pistols=getPistolAmount(foi["t"]["players"]),
                    ct_alive_at_poi=foi["ct"]["alivePlayers"],
                    ct_alive_at_pop=fop["ct"]["alivePlayers"],
                    ct_buy_type=round["ctBuyType"],
                    ct_spend=round["ctSpend"],
                    t_alive_at_poi=foi["t"]["alivePlayers"],
                    t_alive_at_pop=fop["t"]["alivePlayers"],
                    t_buy_type=round["tBuyType"],
                    t_spend=round["tSpend"],
                    t_won=round["winningSide"] == "T",
                    t_1_hp=foi["t"]["players"][0]["hp"],
                    t_1_kevlar=getKevlarType(foi["t"]["players"][0]["armor"], foi["t"]["players"][0]["hasHelmet"]).value,
                    t_1_has_defuser=foi["t"]["players"][0]["hasDefuse"],
                    t_1_area_name=foi["t"]["players"][0]["areaName"],
                    t_1_weapon=getMainWeapon(foi["t"]["players"][0]["inventory"])["weapon_name"],
                    t_1_weapon_type=getMainWeapon(foi["t"]["players"][0]["inventory"])["weapon_type"],
                    t_1_has_molotov=getUtility(foi["t"]["players"][0]["inventory"])["molotov"],
                    t_1_has_grenade=getUtility(foi["t"]["players"][0]["inventory"])["grenade"],
                    t_1_has_smoke=getUtility(foi["t"]["players"][0]["inventory"])["smoke"],
                    t_1_has_flash1=getUtility(foi["t"]["players"][0]["inventory"])["flash1"],
                    t_1_has_flash2=getUtility(foi["t"]["players"][0]["inventory"])["flash2"],
                    t_2_hp=foi["t"]["players"][1]["hp"],
                    t_2_kevlar=getKevlarType(foi["t"]["players"][1]["armor"], foi["t"]["players"][1]["hasHelmet"]).value,
                    t_2_has_defuser=foi["t"]["players"][1]["hasDefuse"],
                    t_2_area_name=foi["t"]["players"][1]["areaName"],
                    t_2_weapon=getMainWeapon(foi["t"]["players"][1]["inventory"])["weapon_name"],
                    t_2_weapon_type=getMainWeapon(foi["t"]["players"][1]["inventory"])["weapon_type"],
                    t_2_has_molotov=getUtility(foi["t"]["players"][1]["inventory"])["molotov"],
                    t_2_has_grenade=getUtility(foi["t"]["players"][1]["inventory"])["grenade"],
                    t_2_has_smoke=getUtility(foi["t"]["players"][1]["inventory"])["smoke"],
                    t_2_has_flash1=getUtility(foi["t"]["players"][1]["inventory"])["flash1"],
                    t_2_has_flash2=getUtility(foi["t"]["players"][1]["inventory"])["flash2"],
                    t_3_hp=foi["t"]["players"][2]["hp"],
                    t_3_kevlar=getKevlarType(foi["t"]["players"][2]["armor"], foi["t"]["players"][2]["hasHelmet"]).value,
                    t_3_has_defuser=foi["t"]["players"][2]["hasDefuse"],
                    t_3_area_name=foi["t"]["players"][2]["areaName"],
                    t_3_weapon=getMainWeapon(foi["t"]["players"][2]["inventory"])["weapon_name"],
                    t_3_weapon_type=getMainWeapon(foi["t"]["players"][2]["inventory"])["weapon_type"],
                    t_3_has_molotov=getUtility(foi["t"]["players"][2]["inventory"])["molotov"],
                    t_3_has_grenade=getUtility(foi["t"]["players"][2]["inventory"])["grenade"],
                    t_3_has_smoke=getUtility(foi["t"]["players"][2]["inventory"])["smoke"],
                    t_3_has_flash1=getUtility(foi["t"]["players"][2]["inventory"])["flash1"],
                    t_3_has_flash2=getUtility(foi["t"]["players"][2]["inventory"])["flash2"],
                    t_4_hp=foi["t"]["players"][3]["hp"],
                    t_4_kevlar=getKevlarType(foi["t"]["players"][3]["armor"], foi["t"]["players"][3]["hasHelmet"]).value,
                    t_4_has_defuser=foi["t"]["players"][3]["hasDefuse"],
                    t_4_area_name=foi["t"]["players"][3]["areaName"],
                    t_4_weapon=getMainWeapon(foi["t"]["players"][3]["inventory"])["weapon_name"],
                    t_4_weapon_type=getMainWeapon(foi["t"]["players"][3]["inventory"])["weapon_type"],
                    t_4_has_molotov=getUtility(foi["t"]["players"][3]["inventory"])["molotov"],
                    t_4_has_grenade=getUtility(foi["t"]["players"][3]["inventory"])["grenade"],
                    t_4_has_smoke=getUtility(foi["t"]["players"][3]["inventory"])["smoke"],
                    t_4_has_flash1=getUtility(foi["t"]["players"][3]["inventory"])["flash1"],
                    t_4_has_flash2=getUtility(foi["t"]["players"][3]["inventory"])["flash2"],
                    t_5_hp=foi["t"]["players"][4]["hp"],
                    t_5_kevlar=getKevlarType(foi["t"]["players"][4]["armor"], foi["t"]["players"][4]["hasHelmet"]).value,
                    t_5_has_defuser=foi["t"]["players"][4]["hasDefuse"],
                    t_5_area_name=foi["t"]["players"][4]["areaName"],
                    t_5_weapon=getMainWeapon(foi["t"]["players"][4]["inventory"])["weapon_name"],
                    t_5_weapon_type=getMainWeapon(foi["t"]["players"][4]["inventory"])["weapon_type"],
                    t_5_has_molotov=getUtility(foi["t"]["players"][4]["inventory"])["molotov"],
                    t_5_has_grenade=getUtility(foi["t"]["players"][4]["inventory"])["grenade"],
                    t_5_has_smoke=getUtility(foi["t"]["players"][4]["inventory"])["smoke"],
                    t_5_has_flash1=getUtility(foi["t"]["players"][4]["inventory"])["flash1"],
                    t_5_has_flash2=getUtility(foi["t"]["players"][4]["inventory"])["flash2"],
                    ct_1_hp=foi["ct"]["players"][0]["hp"],
                    ct_1_kevlar=getKevlarType(foi["ct"]["players"][0]["armor"], foi["ct"]["players"][0]["hasHelmet"]).value,
                    ct_1_has_defuser=foi["ct"]["players"][0]["hasDefuse"],
                    ct_1_area_name=foi["ct"]["players"][0]["areaName"],
                    ct_1_weapon=getMainWeapon(foi["ct"]["players"][0]["inventory"])["weapon_name"],
                    ct_1_weapon_type=getMainWeapon(foi["ct"]["players"][0]["inventory"])["weapon_type"],
                    ct_1_has_molotov=getUtility(foi["ct"]["players"][0]["inventory"])["molotov"],
                    ct_1_has_grenade=getUtility(foi["ct"]["players"][0]["inventory"])["grenade"],
                    ct_1_has_smoke=getUtility(foi["ct"]["players"][0]["inventory"])["smoke"],
                    ct_1_has_flash1=getUtility(foi["ct"]["players"][0]["inventory"])["flash1"],
                    ct_1_has_flash2=getUtility(foi["ct"]["players"][0]["inventory"])["flash2"],
                    ct_2_hp=foi["ct"]["players"][1]["hp"],
                    ct_2_kevlar=getKevlarType(foi["ct"]["players"][1]["armor"], foi["ct"]["players"][1]["hasHelmet"]).value,
                    ct_2_has_defuser=foi["ct"]["players"][1]["hasDefuse"],
                    ct_2_area_name=foi["ct"]["players"][1]["areaName"],
                    ct_2_weapon=getMainWeapon(foi["ct"]["players"][1]["inventory"])["weapon_name"],
                    ct_2_weapon_type=getMainWeapon(foi["ct"]["players"][1]["inventory"])["weapon_type"],
                    ct_2_has_molotov=getUtility(foi["ct"]["players"][1]["inventory"])["molotov"],
                    ct_2_has_grenade=getUtility(foi["ct"]["players"][1]["inventory"])["grenade"],
                    ct_2_has_smoke=getUtility(foi["ct"]["players"][1]["inventory"])["smoke"],
                    ct_2_has_flash1=getUtility(foi["ct"]["players"][1]["inventory"])["flash1"],
                    ct_2_has_flash2=getUtility(foi["ct"]["players"][1]["inventory"])["flash2"],
                    ct_3_hp=foi["ct"]["players"][2]["hp"],
                    ct_3_kevlar=getKevlarType(foi["ct"]["players"][2]["armor"], foi["ct"]["players"][2]["hasHelmet"]).value,
                    ct_3_has_defuser=foi["ct"]["players"][2]["hasDefuse"],
                    ct_3_area_name=foi["ct"]["players"][2]["areaName"],
                    ct_3_weapon=getMainWeapon(foi["ct"]["players"][2]["inventory"])["weapon_name"],
                    ct_3_weapon_type=getMainWeapon(foi["ct"]["players"][2]["inventory"])["weapon_type"],
                    ct_3_has_molotov=getUtility(foi["ct"]["players"][2]["inventory"])["molotov"],
                    ct_3_has_grenade=getUtility(foi["ct"]["players"][2]["inventory"])["grenade"],
                    ct_3_has_smoke=getUtility(foi["ct"]["players"][2]["inventory"])["smoke"],
                    ct_3_has_flash1=getUtility(foi["ct"]["players"][2]["inventory"])["flash1"],
                    ct_3_has_flash2=getUtility(foi["ct"]["players"][2]["inventory"])["flash2"],
                    ct_4_hp=foi["ct"]["players"][3]["hp"],
                    ct_4_kevlar=getKevlarType(foi["ct"]["players"][3]["armor"], foi["ct"]["players"][3]["hasHelmet"]).value,
                    ct_4_has_defuser=foi["ct"]["players"][3]["hasDefuse"],
                    ct_4_area_name=foi["ct"]["players"][3]["areaName"],
                    ct_4_weapon=getMainWeapon(foi["ct"]["players"][3]["inventory"])["weapon_name"],
                    ct_4_weapon_type=getMainWeapon(foi["ct"]["players"][3]["inventory"])["weapon_type"],
                    ct_4_has_molotov=getUtility(foi["ct"]["players"][3]["inventory"])["molotov"],
                    ct_4_has_grenade=getUtility(foi["ct"]["players"][3]["inventory"])["grenade"],
                    ct_4_has_smoke=getUtility(foi["ct"]["players"][3]["inventory"])["smoke"],
                    ct_4_has_flash1=getUtility(foi["ct"]["players"][3]["inventory"])["flash1"],
                    ct_4_has_flash2=getUtility(foi["ct"]["players"][3]["inventory"])["flash2"],
                    ct_5_hp=foi["ct"]["players"][4]["hp"],
                    ct_5_kevlar=getKevlarType(foi["ct"]["players"][4]["armor"], foi["ct"]["players"][4]["hasHelmet"]).value,
                    ct_5_has_defuser=foi["ct"]["players"][4]["hasDefuse"],
                    ct_5_area_name=foi["ct"]["players"][4]["areaName"],
                    ct_5_weapon=getMainWeapon(foi["ct"]["players"][4]["inventory"])["weapon_name"],
                    ct_5_weapon_type=getMainWeapon(foi["ct"]["players"][4]["inventory"])["weapon_type"],
                    ct_5_has_molotov=getUtility(foi["ct"]["players"][4]["inventory"])["molotov"],
                    ct_5_has_grenade=getUtility(foi["ct"]["players"][4]["inventory"])["grenade"],
                    ct_5_has_smoke=getUtility(foi["ct"]["players"][4]["inventory"])["smoke"],
                    ct_5_has_flash1=getUtility(foi["ct"]["players"][4]["inventory"])["flash1"],
                    ct_5_has_flash2=getUtility(foi["ct"]["players"][4]["inventory"])["flash2"],
                    was_round_t_success=was_round_t_success(round, fop),
                )

                rounds.append(round_object.__dict__)


    df = pd.DataFrame(rounds)
    df.to_csv("data_20/" + file_name + ".csv", index=False)

def was_round_t_success(round, fop):
    vs_eco = round["ctBuyType"] == "Full Eco"
    half_vs_half = round["tBuyType"] == "Semi Eco" and round["ctBuyType"] == "Semi Eco"
    force_and_full_vs_eco_or_half = round["tBuyType"] not in ['Full Eco', 'Semi Eco'] and round["ctBuyType"] in ['Full Eco', 'Semi Eco']
    if round["roundEndReason"] in ['TerroristsWin', 'TargetBombed']:
        return True
    if round["roundEndReason"] == 'TargetSaved':
        return False
    if round["bombPlantTick"] != None:
        if vs_eco or half_vs_half or force_and_full_vs_eco_or_half:
            return False
        if fop['ct']["alivePlayers"] - fop['t']["alivePlayers"] <= 1:
            return True
    return False

data_file_paths = next(walk('./data_20'), (None, None, []))[2]
data_file_names = [x.split('.')[0] for x in data_file_paths if x.endswith('.csv')]
json_file_paths = next(walk('./parsed_demos'), (None, None, []))[2]

for file_path in json_file_paths:
    if file_path.split('.')[0] not in data_file_names:
        extract_data_from_parsed_demo('./parsed_demos/' + file_path, file_path.split('.')[0])
    else:
        print(file_path + ' already processed')
