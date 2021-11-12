from weapon import Weapon
from enemy import Enemy
from player import Player
from attack import Attack
import actions

name = input('Cual es tu nombre: ')

player = Player(name)
estocada = Attack('Estocada',0.95,0.60)
tajo_rapido = Attack('Tajo_rapido',0.60,0.75)
tajo_horizontal = Attack('Tajo_horizontal',0.55,0.60)
sword = Weapon('Espada',21,1,estocada,tajo_rapido,tajo_horizontal)
player.add_weapon(sword)

enemy = Enemy("Esqueleto", 13,7,60,3,'golpe')

actions.encounter(player,enemy)
