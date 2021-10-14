from enum import Enum


class Round:
    def __init__(
        self,
        bomb_planted: bool,
        ct_alive_at_plant: int,
        ct_buy_type: str,
        ct_players: list,
        ct_spend: int,
        t_alive_at_plant: int,
        t_buy_type: str,
        t_players: list,
        t_spend: int,
        t_won: bool,
    ):
        self.bomb_planted = bomb_planted
        self.ct_alive_at_plant = ct_alive_at_plant
        self.ct_buy_type = ct_buy_type
        self.ct_players = ct_players
        self.ct_spend = ct_spend
        self.t_alive_at_plant = t_alive_at_plant
        self.t_buy_type = t_buy_type
        self.t_players = t_players
        self.t_spend = t_spend
        self.t_won = t_won


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


class Player:
    def __init__(
        self,
        hp: int,
        kevlar: Kevlar,
        has_defuser: bool,
        area_name: str,
        weapon: str,
        utility: list[Utiltiy]
    ):
        self.hp = hp
        self.kevlar = kevlar
        self.has_defuser = has_defuser
        self.area_name = area_name
        self.weapon = weapon
        self.utility = utility

    def is_player_dead(self):
        return self.hp <= 0