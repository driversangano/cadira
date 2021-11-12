from attack import Attack


class Player:
    def __init__(self, name):
        self.name = name
        self.p_atk = 15
        self.p_def = 15
        self.p_hp = 100
        self.p_ini = 5

    def toString(self):
        print('Name: ', self.name,  '\nHP: ', self.p_hp,'\nAtk: ', self.p_atk,'\nDef: ',self.p_def)
        print(self.weapon.toString())

    def edit_HP(self, val):
        self.p_hp = self.p_hp + val

    def add_weapon(self, weapon):
        self.weapon = weapon
        self.p_atk = self.p_atk + self.weapon.w_atk
        self.p_def = self.p_def + self.weapon.w_def

    def remove_weapon(self):
        self.p_atk = self.p_atk - self.weapon.w_atk
        self.p_def = self.p_def - self.weapon.w_def
        self.weapon = None

    def actual_attacks(self):
        index = 0
        weapon_attacks = ''
        for atk in self.weapon.attacks:
            index += 1
            weapon_attacks = f'{weapon_attacks} + {index} .- {atk.toString()}\n'
        return weapon_attacks

    def attack(self, used_attack_option):
        index = 0
        hit = 0
        for atk in self.weapon.attacks:
            index += 1
            if(used_attack_option == index):
                hit = atk.use()
        return round(hit * self.p_atk,0)

    def defend(self,dmg):
        result_dmg = dmg - self.p_def
        if(result_dmg > 0 ):
            print(f'You received {result_dmg} of damage')
            self.p_hp = self.p_hp - result_dmg
            print(f'You have {self.p_hp} of HP')
        else:
            print(f'You blocked the damage')