import random

class Enemy:
    def __init__(self, name, e_atk, e_def, e_hp, e_ini,e_default_attack_name):
        self.name = name
        self.e_atk = e_atk
        self.e_def = e_def
        self.e_hp = e_hp
        self.e_ini = e_ini
        self.e_default_attack_name = e_default_attack_name

    def toString(self):
        print('Name: ', self.name, '\nHP: ', self.e_hp, '\nAtk: ', self.e_atk,'\nDef: ',self.e_def)

    def defend(self,dmg):
        result_dmg = dmg - self.e_def
        if(result_dmg > 0 ):
            print(f'Enemy {self.name} has received {result_dmg} of damage')
            self.e_hp = self.e_hp - result_dmg
            print(f'Enemy {self.name} has {self.e_hp} of HP')
        else:
            print(f'Enemy {self.name} has blocked the damage')

    def attack(self):
        chance = random.random()
        if(chance < 0.5 ):
            print('Oh no! ', self.e_default_attack_name, ' has failed')
            return 0
        else:
            print('Nice ', self.e_default_attack_name, ' hits')
            return self.e_atk
