import random
from colored import fg, bg, attr
from profesions import *
from enemy import *

def loot(enemy):
    loot = ["mikstura", "oręż treningowy", "zbroja treningowa", "śmieć", "kawałek futra", "szczurza korona", "słaby oręż", "słaba zbroja", "srebrny kieł"]
    lootChance = enemy.loot
    lootDrop = loot[lootChance]
    return lootDrop

def lootEffect(lootDrop, character):
    if lootDrop == "mikstura":
        hp_plus = random.randint(3,12)
        if character.health < character.max_health - 12:
            character.health = character.health + hp_plus
            print("%sMiksturka którą wypiłeś, dodała Tobie%s" %(fg(175), attr(0)), hp_plus, "%spunktów życia%s" %(fg(175), attr(0)))
            print("%sTwoje obecne zdrowie to%s" %(fg(175), attr(0)), character.health)
        else:
            print("Wygląda na to że nie trzeba Cię ''leczyć''")
            character.potion = character.potion + 1
            print("%s%sTwój stan mikturek zdrowia:%s" % (fg(170), bg(7), attr(0)), character.potion)
        return character

    elif lootDrop == "oręż treningowy":
        if character.strenght < 17:
            str_plus = random.randint(0,2)
            if character == Wizard:
                character.magic = character.magic + str_plus
                print("%sOręż który znalazłeś, okazał się magiczny. Podniósł twoją magię o %s" %(fg(49), attr(0)), str_plus)
                print("%sTwoja aktualna magia to%s" %(fg(49), attr(0)), character.magic)
                return character
            else:
                character.strenght = character.strenght + str_plus
                print("%sOreż który znalazłeś podniósł twoją siłę o %s" % (fg(4), attr(0)), str_plus)
                print("%sTwoja aktualna siła to%s" % (fg(4), attr(0)), character.strenght)
                return character
        else:
            print("z tego oręża już nic Ci się nie przyda")
            print("zawsze można spróbować to spieniężyć (5)")
            character.cash += 5

    elif lootDrop == "zbroja treningowa":
        if character.defence < 17:
            def_plus = random.randint(0,2)
            character.defence = character.defence + def_plus
            print("%sTarcza którą znalazłeś podniosła twoją obronę o %s" %(fg(6), attr(0)), def_plus)
            print("%sTwioja aktualna obrona to%s" %(fg(6), attr(0)), character.defence)
            return character
        else:
            print("z tej zbroi już nic Ci się nie przyda")
            print("zawsze można spróbować ją spieniężyć (5)")
            character.cash += 5

    elif lootDrop == "śmieć":
        print("Nic ciekawego nie spadło")
        return character

    elif lootDrop == "kawałek futra":
        print("Dodatkowy hajsik (5)")
        character.cash += 5
        return character

    elif lootDrop == "szczurza korona":
        print("Przyfarciłeś, za to dotaniesz niemałą sumkę (100)")
        character.cash += 100
        return character

    elif lootDrop == "słaby oręż":
        if character.strenght < 32:
            str_plus = random.randint(0, 2)
            if character == Wizard:
                character.magic = character.magic + str_plus
                print("%sOręż który znalazłeś, okazał się magiczny. Podniósł twoją magię o %s" % (fg(49), attr(0)),
                      str_plus)
                print("%sTwoja aktualna magia to%s" % (fg(49), attr(0)), character.magic)
                return character
            else:
                character.strenght = character.strenght + str_plus
                print("%sOreż który znalazłeś podniósł twoją siłę o %s" % (fg(4), attr(0)), str_plus)
                print("%sTwoja aktualna siła to%s" % (fg(4), attr(0)), character.strenght)
                return character
        else:
            print("z tego oręża już nic Ci się nie przyda")
            print("zawsze można spróbować to spieniężyć (15)")
            character.cash += 15

    elif lootDrop == "słaba zbroja":
        if character.defence < 32:
            def_plus = random.randint(0,2)
            character.defence = character.defence + def_plus
            print("%sTarcza którą znalazłeś podniosła twoją obronę o %s" %(fg(6), attr(0)), def_plus)
            print("%sTwioja aktualna obrona to%s" %(fg(6), attr(0)), character.defence)
            return character
        else:
            print("z tej zbroi już nic Ci się nie przyda")
            print("zawsze można spróbować ją spieniężyć (15)")
            character.cash += 15
            return character

    elif lootDrop == "srebrny kieł":
        print("Przyfarciłeś, za to dotaniesz niemałą sumkę (500)")
        character.cash += 500
        return character