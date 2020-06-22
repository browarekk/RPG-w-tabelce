import random


class Enemy(object):

    def __init__(self, enemy):
        self.name = enemy['name']
        self.health = enemy['health']
        self.strenght = enemy['strenght']
        self.defence = enemy['defence']
        self.loot_list = enemy['loot_list']
        self.money = enemy['money']
        self.loot = random.choice(self.loot_list)


MONSTERS_KANALY = {
    "NORMAL": [
        {
            "name": "Goblin",
            "health": 20,
            "strenght": 14,
            "defence": 2,
            "loot_list": [0, 1, 2, 3],
            "money": 5
            #money = random.randint(1, 3)
        },
        {
            "name": "Szczur",
            "health": 10,
            "strenght": 12,
            "defence": 0,
            "loot_list": [0, 3, 4],
            "money": 5
            #money = random.randint(0, 2)
        },
        {
            "name": "Pająk",
            "health": 20,
            "strenght": 13,
            "defence": 1,
            "loot_list": [0, 3],
            "money": 5
            #money = random.randint(0, 3)
        },
        {
            "name": "Duży Szczur",
            "health": 25,
            "strenght": 15,
            "defence": 2,
            "loot_list": [0, 3, 4],
            "money": 5
            #money = random.randint(0, 6)
        }
    ],
    "BOSS": [
        {
            "name": "KRÓL SZCZURÓW",
            "health": 150,
            "strenght": 30,
            "defence": 15,
            "loot_list": [5],
            "money": 10
        }
    ]
}

MONSTERS_MROCZNY_LAS = {
    "NORMAL": [
        {
            "name": "Duży Pająk",
            "health": 50,
            "strenght": 30,
            "defence": 10,
            "loot_list": [0, 3, 4],
            "money": 10
            #money = random.randint(0, 10)
        },
        {
            "name": "Wilk",
            "health": 70,
            "strenght": 45,
            "defence": 8,
            "loot_list": [3, 4],
            "money": 14
            #money = random.randint(0, 14)
        },
        {
            "name": "Ogromna Żaba",
            "health": 100,
            "strenght": 30,
            "defence": 12,
            "loot_list": [0, 3, 4],
            "money": 13
            #money = random.randint(0, 13)
        }
    ],
    "BOSS": [
        {
            "name": "WILCZY KRÓL",
            "health": 350,
            "strenght": 70,
            "defence": 20,
            "loot_list": [8],
            "money": 13
            # money = random.randint(0, 13)
        }
    ]
}

def select_enemy(MONSTERS):
    boss_chance = random.randint(0, 100)
    if boss_chance > 97:
        return random.choice(MONSTERS['BOSS'])
    else:
        return random.choice(MONSTERS['NORMAL'])

# loot = ["mikstura", "oręż treningowy", "zbroja treningowa", "śmieć", "kawałek futra", "szczurza korona", "słaby oręż", "słaba zbroja", "srebrny kieł"]


########## jaskinia nieopodal miasta
class bear(object):
    name = "Niedźwiedź"
    health = 200
    strenght = 60
    defence = 20
    loot = random.randint(10, 25)
    money = random.randint(0, 25)

class black_bear(object):
    name = "Czarny niedźwiedź"
    health = 300
    strenght = 75
    defence = 22
    loot = random.randint(15, 25)
    money = random.randint(0, 25)

class troll(object):
    name = "Trol"
    health = 400
    strenght = 75
    defence = 10
    loot = random.randint(20, 30)
    money = random.randint(10, 30)




########## obozu bandytów
class bandit(object):
    name = "Bandyta"
    health = 500
    strenght = 90
    defence = 20
    loot = random.randint(25, 40)
    money = random.randint(5, 40)

class psycho(object):
    name = "Psychopata"
    health = 1000
    strenght = 150
    defnece = 5
    loot = random.randint(30, 50)
    money = random.randint(0, 100)

class bad_guy(object):
    name = "Wykolejeniec"
    health = 700
    strenght = 105
    defence = 15
    loot = random.randint(30, 45)
    money = random.randint(10, 45)



########## opuszczony zamek


########## zaczarowany las


########## odległe pola uprawne