class Warrior(object):
    max_health = 150
    health = 150
    strenght = 10
    defence = 10
    magic = 1
    cash = 0
    potion = 0

    @property
    def name(self):
        return "Siła! to był dobry wybór. Będziesz grać wojownikiem.\n"


class Wizard(object):
    max_health = 120
    health = 120
    strenght = 7
    defence = 7
    magic = 10
    cash = 0
    potion = 0

    @property
    def name(self):
        return "Intelignecja! Jesteś wyjątkowy. Będziesz grać magiem.\n"

class Archer(object):
    max_health = 120
    health = 120
    strenght = 13
    defence = 7
    magic = 5
    cash = 0
    potion = 0

    @property
    def name(self):
        return "Zręczność! Balasn między siłą i obroną. Wybrałeś łucznika.\n"

class Gm(object):
    max_health = 1000000
    health = 1000000
    strenght = 10000
    defence = 10000
    magic = 10000
    cash = 10000
    potion = 100

    @property
    def name(self):
        return "Witaj twórco gry.\n"