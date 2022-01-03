from enum import Enum
class Kevlar(Enum):
    NONE = None
    KEVLAR = "kevlar"
    HELMET = "helmet"


class Utiltiy(Enum):
    SMOKE = "smoke"
    DECOY = "decoy"
    FLASH = "flash"
    GRENADE = "grenade"
    MOLOTOV = "molotov"


class Round:
    def __init__(
        self,
        demo_name: str,
        t_team_name: str,
        ct_team_name: str,
        round_number: str,
        was_round_t_success: bool,
        round_end_reason: str,
        bomb_planted: bool,
        bombsite: str,
        t_rifles: int,
        t_pistols: int,
        ct_alive_at_poi: int,
        ct_alive_at_pop: int,
        ct_buy_type: str,
        ct_spend: int,
        t_alive_at_poi: int,
        t_alive_at_pop: int,
        t_buy_type: str,
        t_spend: int,
        t_won: bool,
        t_1_hp: int,
        t_1_kevlar: Kevlar,
        t_1_has_defuser: bool,
        t_1_area_name: str,
        t_1_weapon: str,
        t_1_weapon_type: str,
        t_1_name: str,
        t_1_has_molotov: bool,
        t_1_has_grenade: bool,
        t_1_has_smoke: bool,
        t_1_has_flash1: bool,
        t_1_has_flash2: bool,
        t_2_hp: int,
        t_2_kevlar: Kevlar,
        t_2_has_defuser: bool,
        t_2_area_name: str,
        t_2_weapon: str,
        t_2_weapon_type: str,
        t_2_name: str,
        t_2_has_molotov: bool,
        t_2_has_grenade: bool,
        t_2_has_smoke: bool,
        t_2_has_flash1: bool,
        t_2_has_flash2: bool,
        t_3_hp: int,
        t_3_kevlar: Kevlar,
        t_3_has_defuser: bool,
        t_3_area_name: str,
        t_3_weapon: str,
        t_3_weapon_type: str,
        t_3_name: str,
        t_3_has_molotov: bool,
        t_3_has_grenade: bool,
        t_3_has_smoke: bool,
        t_3_has_flash1: bool,
        t_3_has_flash2: bool,
        t_4_hp: int,
        t_4_kevlar: Kevlar,
        t_4_has_defuser: bool,
        t_4_area_name: str,
        t_4_weapon: str,
        t_4_weapon_type: str,
        t_4_name: str,
        t_4_has_molotov: bool,
        t_4_has_grenade: bool,
        t_4_has_smoke: bool,
        t_4_has_flash1: bool,
        t_4_has_flash2: bool,
        t_5_hp: int,
        t_5_kevlar: Kevlar,
        t_5_has_defuser: bool,
        t_5_area_name: str,
        t_5_weapon: str,
        t_5_weapon_type: str,
        t_5_name: str,
        t_5_has_molotov: bool,
        t_5_has_grenade: bool,
        t_5_has_smoke: bool,
        t_5_has_flash1: bool,
        t_5_has_flash2: bool,
        ct_1_hp: int,
        ct_1_kevlar: Kevlar,
        ct_1_has_defuser: bool,
        ct_1_area_name: str,
        ct_1_weapon: str,
        ct_1_weapon_type: str,
        ct_1_has_molotov: bool,
        ct_1_has_grenade: bool,
        ct_1_has_smoke: bool,
        ct_1_has_flash1: bool,
        ct_1_has_flash2: bool,
        ct_2_hp: int,
        ct_2_kevlar: Kevlar,
        ct_2_has_defuser: bool,
        ct_2_area_name: str,
        ct_2_weapon: str,
        ct_2_weapon_type: str,
        ct_2_has_molotov: bool,
        ct_2_has_grenade: bool,
        ct_2_has_smoke: bool,
        ct_2_has_flash1: bool,
        ct_2_has_flash2: bool,
        ct_3_hp: int,
        ct_3_kevlar: Kevlar,
        ct_3_has_defuser: bool,
        ct_3_area_name: str,
        ct_3_weapon: str,
        ct_3_weapon_type: str,
        ct_3_has_molotov: bool,
        ct_3_has_grenade: bool,
        ct_3_has_smoke: bool,
        ct_3_has_flash1: bool,
        ct_3_has_flash2: bool,
        ct_4_hp: int,
        ct_4_kevlar: Kevlar,
        ct_4_has_defuser: bool,
        ct_4_area_name: str,
        ct_4_weapon: str,
        ct_4_weapon_type: str,
        ct_4_has_molotov: bool,
        ct_4_has_grenade: bool,
        ct_4_has_smoke: bool,
        ct_4_has_flash1: bool,
        ct_4_has_flash2: bool,
        ct_5_hp: int,
        ct_5_kevlar: Kevlar,
        ct_5_has_defuser: bool,
        ct_5_area_name: str,
        ct_5_weapon: str,
        ct_5_weapon_type: str,
        ct_5_has_molotov: bool,
        ct_5_has_grenade: bool,
        ct_5_has_smoke: bool,
        ct_5_has_flash1: bool,
        ct_5_has_flash2: bool,
    ):
        self.demo_name = demo_name
        self.t_team_name = t_team_name
        self.ct_team_name = ct_team_name
        self.round_number = round_number
        self.was_round_t_success = was_round_t_success
        self.round_end_reason = round_end_reason
        self.bomb_planted = bomb_planted
        self.bombsite = bombsite
        self.t_rifles = t_rifles
        self.t_pistols = t_pistols
        self.ct_alive_at_poi = ct_alive_at_poi
        self.ct_alive_at_pop = ct_alive_at_pop
        self.ct_buy_type = ct_buy_type
        self.ct_spend = ct_spend
        self.t_alive_at_poi = t_alive_at_poi
        self.t_alive_at_pop = t_alive_at_pop
        self.t_buy_type = t_buy_type
        self.t_spend = t_spend
        self.t_won = t_won
        self.t_1_hp = t_1_hp
        self.t_1_kevlar = t_1_kevlar
        self.t_1_has_defuser = t_1_has_defuser
        self.t_1_area_name = t_1_area_name
        self.t_1_weapon = t_1_weapon
        self.t_1_weapon_type = t_1_weapon_type
        self.t_1_name = t_1_name
        self.t_1_has_molotov = t_1_has_molotov
        self.t_1_has_grenade = t_1_has_grenade
        self.t_1_has_smoke = t_1_has_smoke
        self.t_1_has_flash1 = t_1_has_flash1
        self.t_1_has_flash2 = t_1_has_flash2
        self.t_2_hp = t_2_hp
        self.t_2_kevlar = t_2_kevlar
        self.t_2_has_defuser = t_2_has_defuser
        self.t_2_area_name = t_2_area_name
        self.t_2_weapon = t_2_weapon
        self.t_2_weapon_type = t_2_weapon_type
        self.t_2_name = t_2_name
        self.t_2_has_molotov = t_2_has_molotov
        self.t_2_has_grenade = t_2_has_grenade
        self.t_2_has_smoke = t_2_has_smoke
        self.t_2_has_flash1 = t_2_has_flash1
        self.t_2_has_flash2 = t_2_has_flash2
        self.t_3_hp = t_3_hp
        self.t_3_kevlar = t_3_kevlar
        self.t_3_has_defuser = t_3_has_defuser
        self.t_3_area_name = t_3_area_name
        self.t_3_weapon = t_3_weapon
        self.t_3_weapon_type = t_3_weapon_type
        self.t_3_name = t_3_name
        self.t_3_has_molotov = t_3_has_molotov
        self.t_3_has_grenade = t_3_has_grenade
        self.t_3_has_smoke = t_3_has_smoke
        self.t_3_has_flash1 = t_3_has_flash1
        self.t_3_has_flash2 = t_3_has_flash2
        self.t_4_hp = t_4_hp
        self.t_4_kevlar = t_4_kevlar
        self.t_4_has_defuser = t_4_has_defuser
        self.t_4_area_name = t_4_area_name
        self.t_4_weapon = t_4_weapon
        self.t_4_weapon_type = t_4_weapon_type
        self.t_4_name = t_4_name
        self.t_4_has_molotov = t_4_has_molotov
        self.t_4_has_grenade = t_4_has_grenade
        self.t_4_has_smoke = t_4_has_smoke
        self.t_4_has_flash1 = t_4_has_flash1
        self.t_4_has_flash2 = t_4_has_flash2
        self.t_5_hp = t_5_hp
        self.t_5_kevlar = t_5_kevlar
        self.t_5_has_defuser = t_5_has_defuser
        self.t_5_area_name = t_5_area_name
        self.t_5_weapon = t_5_weapon
        self.t_5_weapon_type = t_5_weapon_type
        self.t_5_name = t_5_name
        self.t_5_has_molotov = t_5_has_molotov
        self.t_5_has_grenade = t_5_has_grenade
        self.t_5_has_smoke = t_5_has_smoke
        self.t_5_has_flash1 = t_5_has_flash1
        self.t_5_has_flash2 = t_5_has_flash2
        self.ct_1_hp = ct_1_hp
        self.ct_1_kevlar = ct_1_kevlar
        self.ct_1_has_defuser = ct_1_has_defuser
        self.ct_1_area_name = ct_1_area_name
        self.ct_1_weapon = ct_1_weapon
        self.ct_1_weapon_type = ct_1_weapon_type
        self.ct_1_has_molotov = ct_1_has_molotov
        self.ct_1_has_grenade = ct_1_has_grenade
        self.ct_1_has_smoke = ct_1_has_smoke
        self.ct_1_has_flash1 = ct_1_has_flash1
        self.ct_1_has_flash2 = ct_1_has_flash2
        self.ct_2_hp = ct_2_hp
        self.ct_2_kevlar = ct_2_kevlar
        self.ct_2_has_defuser = ct_2_has_defuser
        self.ct_2_area_name = ct_2_area_name
        self.ct_2_weapon = ct_2_weapon
        self.ct_2_weapon_type = ct_2_weapon_type
        self.ct_2_has_molotov = ct_2_has_molotov
        self.ct_2_has_grenade = ct_2_has_grenade
        self.ct_2_has_smoke = ct_2_has_smoke
        self.ct_2_has_flash1 = ct_2_has_flash1
        self.ct_2_has_flash2 = ct_2_has_flash2
        self.ct_3_hp = ct_3_hp
        self.ct_3_kevlar = ct_3_kevlar
        self.ct_3_has_defuser = ct_3_has_defuser
        self.ct_3_area_name = ct_3_area_name
        self.ct_3_weapon = ct_3_weapon
        self.ct_3_weapon_type = ct_3_weapon_type
        self.ct_3_has_molotov = ct_3_has_molotov
        self.ct_3_has_grenade = ct_3_has_grenade
        self.ct_3_has_smoke = ct_3_has_smoke
        self.ct_3_has_flash1 = ct_3_has_flash1
        self.ct_3_has_flash2 = ct_3_has_flash2
        self.ct_4_hp = ct_4_hp
        self.ct_4_kevlar = ct_4_kevlar
        self.ct_4_has_defuser = ct_4_has_defuser
        self.ct_4_area_name = ct_4_area_name
        self.ct_4_weapon = ct_4_weapon
        self.ct_4_weapon_type = ct_4_weapon_type
        self.ct_4_has_molotov = ct_4_has_molotov
        self.ct_4_has_grenade = ct_4_has_grenade
        self.ct_4_has_smoke = ct_4_has_smoke
        self.ct_4_has_flash1 = ct_4_has_flash1
        self.ct_4_has_flash2 = ct_4_has_flash2
        self.ct_5_hp = ct_5_hp
        self.ct_5_kevlar = ct_5_kevlar
        self.ct_5_has_defuser = ct_5_has_defuser
        self.ct_5_area_name = ct_5_area_name
        self.ct_5_weapon = ct_5_weapon
        self.ct_5_weapon_type = ct_5_weapon_type
        self.ct_5_has_molotov = ct_5_has_molotov
        self.ct_5_has_grenade = ct_5_has_grenade
        self.ct_5_has_smoke = ct_5_has_smoke
        self.ct_5_has_flash1 = ct_5_has_flash1
        self.ct_5_has_flash2 = ct_5_has_flash2
