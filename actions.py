import inspect
from player import Player
from enemy import Enemy

def combat(first, second):
    if(isinstance(first, Player)):
        print(first.actual_attacks())
        option = int(input('Select an attack: '))
        total_dmg_first = first.attack(option)
        second.defend(total_dmg_first)
        total_dmg_second = second.attack()
        first.defend(total_dmg_second)
    else:
        first.p_hp = 0
        


def encounter(player, enemy):
    while (player.p_hp > 0 and enemy.e_hp > 0 ):
        if(player.p_ini >= enemy.e_ini ):
            combat(player,enemy)
        else:
            combat(enemy,player)
