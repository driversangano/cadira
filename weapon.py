class Weapon:
    def __init__(self, name, w_atk, w_def, *attacks):
        self.name = name
        self.w_atk = w_atk
        self.w_def = w_def
        self.attacks = attacks

    def toString(self):
        weapon_details ='Name: {} \nAtk: {} \nDef: {} \n'.format(self.name,self.w_atk,self.w_def) 
        weapon_attacks = 'Attacks:\n'
        for atk in self.attacks:
            weapon_attacks = weapon_attacks + atk.toString() + "\n"
        return weapon_details + weapon_attacks
        