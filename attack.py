import random

class Attack:
    def __init__(self, name, dmg_percent, success_rate):
        self.name = name
        self.dmg_percent = dmg_percent
        self.success_rate = success_rate
        
    def toString(self):
        return '{} {} {}'.format(self.name, self.dmg_percent, self.success_rate)

    def use(self):
        chance = random.random()
        if(chance < (self.success_rate) ):
            print('Oh no! ', self.name, ' has failed')
            return 0
        else:
            print('Nice ', self.name, ' hits')
            return self.dmg_percent