from pandas import DataFrame
import pandas as pd
import numpy as np
import ast

def get_team_rifle_amounts_from_data(data_df: DataFrame, side: str):
    rifle_amounts = []
    for _, row in data_df.iterrows():
        rifles = 0
        if row[side + '_1_weapon_type'] == "Rifle":
            rifles += 1
        if row[side + '_2_weapon_type'] == "Rifle":
            rifles += 1
        if row[side + '_3_weapon_type'] == "Rifle":
            rifles += 1
        if row[side + '_4_weapon_type'] == "Rifle":
            rifles += 1
        if row[side + '_5_weapon_type'] == "Rifle":
            rifles += 1
        rifle_amounts.append(rifles)
    return rifle_amounts


def get_team_pistol_amounts_from_data(data_df: DataFrame, side: str):
    pistol_amounts = []
    for _, row in data_df.iterrows():
        pistols = 0
        if row[side + '_1_weapon_type'] == "Pistol":
            pistols += 1
        if row[side + '_2_weapon_type'] == "Pistol":
            pistols += 1
        if row[side + '_3_weapon_type'] == "Pistol":
            pistols += 1
        if row[side + '_4_weapon_type'] == "Pistol":
            pistols += 1
        if row[side + '_5_weapon_type'] == "Pistol":
            pistols += 1
        pistol_amounts.append(pistols)
    return pistol_amounts


def get_team_smoke_amounts_from_data(data_df: DataFrame, side: str):
    smoke_amounts = []
    for _, row in data_df.iterrows():
        smokes = 0
        if row[side + '_1_has_smoke']: smokes += 1
        if row[side + '_2_has_smoke']: smokes += 1
        if row[side + '_3_has_smoke']: smokes += 1
        if row[side + '_4_has_smoke']: smokes += 1
        if row[side + '_5_has_smoke']: smokes += 1
        smoke_amounts.append(smokes)
    return smoke_amounts


def get_team_molotov_amounts_from_data(data_df: DataFrame, side: str):
    molotov_amounts = []
    for _, row in data_df.iterrows():
        molotovs = 0
        if row[side + '_1_has_molotov']: molotovs += 1
        if row[side + '_2_has_molotov']: molotovs += 1
        if row[side + '_3_has_molotov']: molotovs += 1
        if row[side + '_4_has_molotov']: molotovs += 1
        if row[side + '_5_has_molotov']: molotovs += 1
        molotov_amounts.append(molotovs)
    return molotov_amounts


def get_team_grenade_amounts_from_data(data_df: DataFrame, side: str):
    grenade_amounts = []
    for _, row in data_df.iterrows():
        grenades = 0
        if row[side + '_1_has_grenade']: grenades += 1
        if row[side + '_2_has_grenade']: grenades += 1
        if row[side + '_3_has_grenade']: grenades += 1
        if row[side + '_4_has_grenade']: grenades += 1
        if row[side + '_5_has_grenade']: grenades += 1
        grenade_amounts.append(grenades)
    return grenade_amounts


def get_player_locations(data_df: DataFrame, side: str):
    locations_array = []
    for _, row in data_df.iterrows():
        locations = []
        locations.append(row[side + '_1_area_name'])
        locations.append(row[side + '_2_area_name'])
        locations.append(row[side + '_3_area_name'])
        locations.append(row[side + '_4_area_name'])
        locations.append(row[side + '_5_area_name'])
        locations_array.append(locations)
    return locations_array


def is_awp_available(data_df: DataFrame, side: str):
    is_awp_available_array = []
    for _, row in data_df.iterrows():
        is_awp_available = False
        if row[side + '_1_weapon'] == "AWP":
            is_awp_available = True
        if row[side + '_2_weapon'] == "AWP":
            is_awp_available = True
        if row[side + '_3_weapon'] == "AWP":
            is_awp_available = True
        if row[side + '_4_weapon'] == "AWP":
            is_awp_available = True
        if row[side + '_5_weapon'] == "AWP":
            is_awp_available = True
        is_awp_available_array.append(is_awp_available)
    return is_awp_available_array


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


def clean_navi_names(name_df_col):
    names = []
    names_dict = {
        's1mple': 's1mple',
        'Boombl4': 'Boombl4',
        'electronic': 'electronic',
        'electroNic': 'electronic',
        'b1t': 'b1t',
        'B1t': 'b1t',
        'Perfecto': 'Perfecto',
        'flamie': 'flamie',
    }
    for row in name_df_col:
        if row in names_dict:
            names.append(names_dict[row])
        else:
            names.append(row)
    return names


def get_player_data(df, player):
    weapons = []
    has_rifle_array = []
    has_awp = []
    alive_array = []
    for (index, row) in df.iterrows():
        for i in range(1, 6):
            if row['t_' + str(i) + '_name_clean'] == player:
                weapons.append(row['t_' + str(i) + '_weapon'])
                has_rifle_array.append(row['t_' + str(i) + '_weapon_type'] == 'Rifle')
                has_awp.append(row['t_' + str(i) + '_weapon'] == 'AWP')
                alive_array.append(row['t_' + str(i) + '_hp'] > 0)
                break
    df[player + '_weapon'] = weapons
    df[player + '_has_rifle'] = has_rifle_array
    df[player + '_has_awp'] = has_awp
    df[player + '_alive'] = alive_array
    return df


def one_hot_encode_locations(locations, locations_set, side: str):
    import numpy as np
    locations_set = [side + '_pos_' + loc for loc in locations_set]
    df = DataFrame(columns=locations_set)
    for location_list in locations:
        df_term = DataFrame([[0 for _ in range(len(locations_set))]], columns=locations_set)
        for location in np.array(ast.literal_eval(location_list)):
            df_term[side + '_pos_' + location] += 1
        df = pd.concat([df, df_term], ignore_index=True)
    return df
