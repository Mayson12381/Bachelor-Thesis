from pandas import DataFrame
import pandas as pd
import numpy as np
import ast

def get_team_rifle_amounts_from_data(data_df: DataFrame):
    rifle_amounts = []
    for _, row in data_df.iterrows():
        rifles = 0
        if row['t_1_weapon_type'] == "Rifle":
            rifles += 1
        if row['t_2_weapon_type'] == "Rifle":
            rifles += 1
        if row['t_3_weapon_type'] == "Rifle":
            rifles += 1
        if row['t_4_weapon_type'] == "Rifle":
            rifles += 1
        if row['t_5_weapon_type'] == "Rifle":
            rifles += 1
        rifle_amounts.append(rifles)
    return rifle_amounts


def get_team_pistol_amounts_from_data(data_df: DataFrame):
    pistol_amounts = []
    for _, row in data_df.iterrows():
        pistols = 0
        if row['t_1_weapon_type'] == "Pistol":
            pistols += 1
        if row['t_2_weapon_type'] == "Pistol":
            pistols += 1
        if row['t_3_weapon_type'] == "Pistol":
            pistols += 1
        if row['t_4_weapon_type'] == "Pistol":
            pistols += 1
        if row['t_5_weapon_type'] == "Pistol":
            pistols += 1
        pistol_amounts.append(pistols)
    return pistol_amounts


def get_team_smoke_amounts_from_data(data_df: DataFrame):
    smoke_amounts = []
    for _, row in data_df.iterrows():
        smokes = 0
        if row['t_1_has_smoke']: smokes += 1
        if row['t_2_has_smoke']: smokes += 1
        if row['t_3_has_smoke']: smokes += 1
        if row['t_4_has_smoke']: smokes += 1
        if row['t_5_has_smoke']: smokes += 1
        smoke_amounts.append(smokes)
    return smoke_amounts


def get_team_molotov_amounts_from_data(data_df: DataFrame):
    molotov_amounts = []
    for _, row in data_df.iterrows():
        molotovs = 0
        if row['t_1_has_molotov']: molotovs += 1
        if row['t_2_has_molotov']: molotovs += 1
        if row['t_3_has_molotov']: molotovs += 1
        if row['t_4_has_molotov']: molotovs += 1
        if row['t_5_has_molotov']: molotovs += 1
        molotov_amounts.append(molotovs)
    return molotov_amounts


def get_team_grenade_amounts_from_data(data_df: DataFrame):
    grenade_amounts = []
    for _, row in data_df.iterrows():
        grenades = 0
        if row['t_1_has_grenade']: grenades += 1
        if row['t_2_has_grenade']: grenades += 1
        if row['t_3_has_grenade']: grenades += 1
        if row['t_4_has_grenade']: grenades += 1
        if row['t_5_has_grenade']: grenades += 1
        grenade_amounts.append(grenades)
    return grenade_amounts


def get_player_locations(data_df: DataFrame):
    locations_array = []
    for _, row in data_df.iterrows():
        locations = []
        locations.append(row['t_1_area_name'])
        locations.append(row['t_2_area_name'])
        locations.append(row['t_3_area_name'])
        locations.append(row['t_4_area_name'])
        locations.append(row['t_5_area_name'])
        locations_array.append(locations)
    return locations_array


def get_correct_team_names(name_df_col):
    names = []
    names_dict = {
        "NAVI GGBET": "NAVI",
        'Natus Vincere': 'NAVI',
        'NAVI GG.BET': 'NAVI',
        'NAVI 2020': 'NAVI',
        'Team Vitality': 'Vitality',
        'TeamVitality': 'Vitality',
        'G2 Esports': 'G2',
        'G2 ESPORTS': 'G2',
        'Virtus.pro': 'VP',
        'Virtus.pro Parimatch': 'VP',
        'Virtus pro': 'VP',
        'VP Parimatch': 'VP',
        'VP x Parimatch': 'VP',
        'Vp-': 'VP',
        'Team Spirit': 'Spirit',
        'Team Spirit x Parimatch': 'Spirit',
        'Evil Geniuses': 'EG',
        'OGEsports': 'OG',
        'OG Esports': 'OG',
        'Heroic GGBET': 'Heroic',
        'HEROIC': 'Heroic',
        'FaZe Clan': 'Faze',
        'Ninjas in Pyjamas': 'NIP',
        'Gambit Esports': 'Gambit',
        'Gambit.VulkanBET': 'Gambit',
        'Gambit.VulkanBet': 'Gambit',
        'Team Liquid': 'Liquid',
        'FURIA eSports': 'Furia',
        'BIG Clan': 'BIG',
        'Nemiga Gaming': 'Nemiga',
        'compLexity': 'Complexity',
        'SINNERS Esports': 'Sinners',
        'SINNERS': 'Sinners',
        'FNATIC': 'Fnatic',
    }
    for row in name_df_col:
        if row in names_dict:
            names.append(names_dict[row])
        else:
            names.append(row)
    return names


def one_hot_encode_locations(locations, locations_set):
    import numpy as np
    df = DataFrame(columns=locations_set)
    for location_list in locations:
        df_term = DataFrame([[0 for _ in range(len(locations_set))]], columns=locations_set)
        for location in np.array(ast.literal_eval(location_list)):
            df_term[location] += 1
        df = pd.concat([df, df_term], ignore_index=True)
    return df
