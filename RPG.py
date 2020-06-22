#import random
import os
import sys
import pickle
from profesions import *
from enemy import *
from items import *
#from locations import *
from kolory import *
from termcolor import colored, cprint
from colored import fg, bg, attr
from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import *



#---------------------------Game Over + best score---------------------------------------
def gameOver(character, score):
    if character.health < 0:
        print("%s%sNie masz już życia, wychodzi na to że się wysypałeś%s" %(fg(0), bg(232), attr(0)))
        print("Zdobyłeś łącznie...", score, "doświadczenia")
        name = input("Wpisz swoje imię...")
        writeScore(score, name)

        file = open("score.txt", "r")

        for line in file:
            # z pliku z punktami oddziela warianty przez znak (",")
            xline = line.split(",")
            print(xline[0], xline[1])
        exit()

def writeScore(score, name):
    file = open("score.txt", "a")
    file.write(str(name))
    file.write(",")
    file.write(str(score))
    file.write(",")
    file.write("\n")
    file.close()

def heroselect():
    print("Wybierz swojego bohatera! (pisz małymi literami)")
    selection = input("1. Wojownik \n2. Mag \n3. łucznik \n4. Wczytaj grę (nie działa)\n")

    if selection == "1" or selection == "wojownik":
        character = Warrior
        print("Siła! to był dobry wybór. Będziesz grać wojownikiem. Oto jego statystyki")
        print("Życie - ", character.health)
        print("Siła - ", character.strenght)
        print("Obrona - ", character.defence)
        print("Magia - ", character.magic)
        return character

    elif selection == "2" or selection == "mag":
        character = Wizard
        print("Intelignecja! Jesteś wyjątkowy. Będziesz grać magiem. Oto jego statystyki:")
        print("Życie - ", character.health)
        print("Siła - ", character.strenght)
        print("Obrona - ", character.defence)
        print("Magia - ", character.magic)
        return character

    elif selection == "3" or selection == "łucznik":
        character = Archer
        print("Zręczność! Balasn między siłą i obroną. Wybrałeś łucznika. Oto są jego statystyki")
        print("Życie - ", character.health)
        print("Siła - ", character.strenght)
        print("Obrona - ", character.defence)
        print("Magia - ", character.magic)
        return character

    elif selection == "4":
        heroselect()
        #data = [character.health, character.strenght, character.defence, character.magic, character.cash, character.potion]
        data = pickle.load(open("save.dat", "rb"))

    elif selection == "7":
        character = Gm
        print("Witaj twórco gry, oto twoje statystyki")
        print("Życie - ", character.health)
        print("Siła - ", character.strenght)
        print("Obrona - ", character.defence)
        print("Magia - ", character.magic)
        return character
    else:
        print("Wpisz 1, 2 albo 3")
        heroselect()

def options():
    choice = input("1. Targowisko\n2. Pokaż aktualne statystyki\n3. Podróż na expowiska\n4. Exit\n5. Zapisz grę (nie działa)\n7. Leczenie się\n")
    if choice == "1":
        print("Czas udać się na targowisko!")
        targowisko()

    elif choice == "2":
        print("%sMasz aktualnie%s" %(fg(175), attr(0)), character.health, "%spunktów życia%s" %(fg(175), attr(0)))
        print("%sTwoja siła wynosi%s" %(fg(4), attr(0)), character.strenght)
        print("%sTwoja obrona wynosi%s" %(fg(6), attr(0)), character.defence)
        print("%sTwoja magia wynosi%s" %(fg(49), attr(0)), character.magic)
        print("%s%sStan twojego konta to:%s" %(fg(11), bg(232), attr(0)), character.cash)
        print("%s%sTwój stan mikturek zdrowia:%s" %(fg(170), bg(7), attr(0)), character.potion)
        options()

    elif choice == "3":
        travel()

    elif choice == "4":
        tak_nie = input("Czy na pewno chcesz wyjść z gry? %s%s(t/n)%s\n" % (fg(20), bg(7), attr(0)))
        if tak_nie == "t" or tak_nie == "1":
            #### dorobić może zapis gry przed wyjsciem?
            sys.exit()
        else:
            options()

    elif choice == "5":
        data = [character.health, character.strenght, character.defence, character.magic, character.cash, character.potion]
        tak_nie = input("Czy na pewno chcesz zapisać grę? %s%s(t/n)%s\n" % (fg(20), bg(7), attr(0)))
        if tak_nie == "t" or tak_nie == "1":
            #### dorobić może zapis gry przed wyjsciem?
            pickle.dump(data, open("save.dat", "wb"))
            print("gra zapisana")
        else:
            options()

    elif choice == "7":
        print("Słabo się czuję, musze se chlupnąć miksturke pana Tadzia <3")
        if character.potion >= 1:
            if character.health < character.max_health - 20:
                character.health = character.health + 20
                print("%sTwój stan zdrowia wynosi obecnie%s" % (fg(175), attr(0)), character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                character.potion = character.potion - 1
                print("%s%sTwój stan mikturek zdrowia:%s" % (fg(170), bg(7), attr(0)), character.potion)
            elif character.health != character.max_health:
                character.health = character.max_health
                character.potion = character.potion - 1
                print("%sTwój stan zdrowia wynosi obecnie%s" % (fg(175), attr(0)), character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                print("%s%sTwój stan mikturek zdrowia:%s" % (fg(170), bg(7), attr(0)), character.potion)
            else:
                print("Jednak napije się kiedy indziej mam pełne życie")
                print("%s%sTwój stan mikturek zdrowia:%s" % (fg(170), bg(7), attr(0)), character.potion)
        else:
            print("O kurde! Pusto! Muszę udać się do Pana Tadzia uzupełnić zapas miksturek")

def targowisko():
    print("Witaj na targowisku!")
    choice = input("1. Pan Tadziu - Potiony życia(20 monet = 1 potion)\n2. Teofil - Kowal(20 monet = +1 do ataku\n3. Andrzej - Płatnerz(20 monet = +1 do obrony)\n4. Tesla - Biblioteka (20 monet = +1 do magi)\n0. Powrót\n")
    if choice == "1":
        if character.cash >= 20:
            character.cash = character.cash - 20
            if character.health < character.max_health - 20:
                character.health = character.health + 20
                print("Pan Tadziu: No to chlusniem... zdrówko!")
                print("%sTwój aktualny stan zdrowia to%s" % (fg(175), attr(0)), character.health)
                print("%s%sZostało tobie%s" % (fg(11), bg(232), attr(0)), character.cash, "%s%smonet%s" % (fg(11), bg(232), attr(0)))
            elif character.health != character.max_health:
                character.health = character.max_health
                print("Pan Tadziu: No to chlusniem... zdrówko!")
                print("%sTwój aktualny stan zdrowia to%s" % (fg(175), attr(0)), character.health)
                print("%s%sZostało tobie%s" % (fg(11), bg(232), attr(0)), character.cash, "%s%smonet%s" % (fg(11), bg(232), attr(0)))
            else:
                character.potion = character.potion +1
                print("Pan Tadziu: Zatankowałeś już pod korek, ale spokojnie oto fla...ee... miksturka na wynos :)")
                print("%s%sTwój stan mikturek zdrowia:%s" %(fg(170), bg(7), attr(0)), character.potion)
                print("%s%sZostało tobie%s" %(fg(11), bg(232), attr(0)), character.cash, "%s%smonet%s" %(fg(11), bg(232), attr(0)))
            targowisko()
        else:
            print("Pan Tadziu: Gościu nie ma siana, nie ma picia!")
            targowisko()

    elif choice == "2":
        if character.cash >= 20:
            character.cash = character.cash - 20
            character.strenght = character.strenght + 2
            print("Teofil: Doskonały nowy oręż...")
            print("%sTwoja siła wynosi%s" %(fg(4), attr(0)), character.strenght)
            print("%s%sZostało tobie%s" % (fg(11), bg(232), attr(0)), character.cash, "%s%smonet%s" %(fg(11), bg(232), attr(0)))
            targowisko()
        else:
            print("Teofil: Mości Panie, jeszcze musisz uzbierać troche drobnych :)")
            targowisko()

    elif choice == "3":
        if character.cash >= 20:
            character.cash = character.cash - 20
            character.defence = character.defence + 2
            print("Andrzej: Do twarzy Ci w tej zbroi...")
            print("%sTwoja obrona wynosi%s" %(fg(6), attr(0)), character.defence)
            print("%s%sZostało tobie%s" % (fg(11), bg(232), attr(0)), character.cash, "%s%smonet%s" %(fg(11), bg(232), attr(0)))
            targowisko()
        else:
            print("Andrzej: Proszę Pana, nie stać Pana na moje usługi!")
            targowisko()

    elif choice == "4":
        if character.cash >= 20:
            character.cash = character.cash - 20
            character.magic = character.magic + 2
            print("Tesla: Nauka to potęgi klucz...")
            print("%sTwoja magia wynosi%s" %(fg(49), attr(0)), character.magic)
            print("%s%sZostało tobie%s" % (fg(11), bg(232), attr(0)), character.cash, "%s%smonet%s" %(fg(11), bg(232), attr(0)))
            targowisko()
        else:
            print("Tesla: Chętnie bym Tobie pomógł, ale to wymaga niestety zapłaty")
            targowisko()

    elif choice == "0":
        options()
    else:
        print("Nie zrozumiałem komendy")
        targowisko()

def travel():
    choice = input("1. Kanały\n2. Mroczny las\n3. Jaskinia nieopodal miasta\n4. Obóz bandytów\n5. Opuszczony zamek\n6. Zaczarowany las\n7. Odległe pola uprawne\n0. Powrót do opcji\n")
    if choice == "1":
        print("Idealne miejsce dla początkujących poszukiwaczy przygów %s%s(lvl 1+)%s" %(fg(11), bg(232), attr(0)))
        tak_nie = input("Chcesz tutaj się udać? %s%s(t/n)%s\n" %(fg(20), bg(7), attr(0)))
        if tak_nie == "t" or tak_nie == "1":
            kanaly(score)
        elif tak_nie == "n" or tak_nie == "2":
            travel()
        else:
            print("Nie zrozumiałem komendy")
            travel()
    elif choice == "2":
        print("W mrocznym lesie mozna spotkać duże pająki, wilki i ogromne żaby %s%s(lvl 5+)%s" %(fg(11), bg(232), attr(0)))
        tak_nie = input("Chcesz tutaj się udać? %s%s(t/n)%s\n" % (fg(20), bg(7), attr(0)))
        if tak_nie == "t" or tak_nie == "1":
            mroczny_las(score)
        elif tak_nie == "n" or tak_nie == "2":
            travel()
        else:
            print("Nie zrozumiałem komendy")
            travel()
    elif choice == "3":
        print("W jaskini żyją niedźwiedzie i ponoć też trole %s%s(lvl 8+)%s" %(fg(11), bg(232), attr(0)))
        tak_nie = input("Chcesz tutaj się udać? %s%s(t/n)%s\n" % (fg(20), bg(7), attr(0)))
        if tak_nie == "t" or tak_nie == "1":
            print("nie ma tego jeszcze!")
            travel()
            #jaskinia_nieopodal_miasta(score)
        elif tak_nie == "n" or tak_nie == "2":
            travel()
        else:
            print("Nie zrozumiałem komendy")
            travel()
    elif choice == "4":
        print("W obozie bandytów jest masa wykolejeńców i złoczyńców, którzy zagrażają naszemu miastu %s%s(lvl 12+)%s" %(fg(11), bg(232), attr(0)))
        tak_nie = input("Chcesz tutaj się udać? %s%s(t/n)%s\n" % (fg(20), bg(7), attr(0)))
        if tak_nie == "t" or tak_nie == "1":
            print("nie ma tego jeszcze!")
            travel()
            #oboz_bandytow(score)
        elif tak_nie == "n" or tak_nie == "2":
            travel()
        else:
            print("Nie zrozumiałem komendy")
            travel()
    elif choice == "5":
        print("W opuszczonym zamku zadomowiły się duchy i inne straszydła %s%s(lvl 18+)%s" %(fg(11), bg(232), attr(0)))
        tak_nie = input("Chcesz tutaj się udać? %s%s(t/n)%s\n" % (fg(20), bg(7), attr(0)))
        if tak_nie == "t" or tak_nie == "1":
            print("nie ma tego jeszcze!")
            travel()
            #opuszczony_zamek(score)
        elif tak_nie == "n" or tak_nie == "2":
            travel()
        else:
            print("Nie zrozumiałem komendy")
            travel()
    elif choice == "6":
        print("W zaczarowanym lesie żyją elfy i skrzaty %s%s(lvl 25+)%s" %(fg(11), bg(232), attr(0)))
        tak_nie = input("Chcesz tutaj się udać? %s%s(t/n)%s\n" % (fg(20), bg(7), attr(0)))
        if tak_nie == "t" or tak_nie == "1":
            print("nie ma tego jeszcze!")
            travel()
            #zaczarowany_las(score)
        elif tak_nie == "n" or tak_nie == "2":
            travel()
        else:
            print("Nie zrozumiałem komendy")
            travel()
    elif choice == "7":
        print("Na odległych polach uprawnych żyją wkur****i rolnicy z powodu wysokich danin, lepiej unikać tego miejsca %s%s(lvl 50+)!!!%s" %(fg(11), bg(232), attr(0)))
        tak_nie = input("Chcesz tutaj się udać? %s%s(t/n)%s\n" % (fg(20), bg(7), attr(0)))
        if tak_nie == "t" or tak_nie == "1":
            print("nie ma tego jeszcze!")
            travel()
            #odlegle_pola_uprawne(score)
        elif tak_nie == "n" or tak_nie == "2":
            travel()
        else:
            print("Nie zrozumiałem komendy")
            travel()
    elif choice == "0":
        options()
    else:
        print("Nie zrozumiałem komendy")
        travel()








def kanaly(score):
    random_enemy = select_enemy(MONSTERS_KANALY)
    enemy = Enemy(random_enemy)
    print(enemy.name, "się pojawił!")
    print("masz 5 opcje...")
    while enemy.health > 0:
        choice = input("1. atak mieczem\n2. atak magiczny\n3. ucieczka i powrót do miasta\n4. Exit\n7. Leczenie się\n")

#### atak fizyczny
        if choice == "1":
            print("Zaatakowałeś mieczem", enemy.name + "a")
            hitchance = random.randint(0,15)
            if hitchance >= 3:
                enemy.health = enemy.health - character.strenght
                if enemy.health < 0:
                    enemy.health = 0
                else:
                    print("%suderzyłeś wroga, jego aktualne życie to%s" %(fg(3), attr(0)), enemy.health)

                if enemy.health > 0:
                    enemy_hit = enemy.strenght - character.defence
                    if enemy_hit > 0:
                        character.health = character.health - enemy_hit
                        print(enemy.name, "uderzył cię za", enemy_hit, "%s\nZostało tobie%s" % (fg(175), attr(0)), character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                    else:
                        print("%sWróg nie przebił się przez twoją obronę%s" %(fg(14), attr(0)))
                    gameOver(character, score)

                else:
                    print("%s%sPokonałeś swojego wroga%s" %(fg(15), bg(3), attr(0)), enemy.name)
                    print("%sWygląda na to, że upuścił jakiś przedmiot,%s" %(fg(2), attr(0)), end = " ")
                    lootDrop = loot(enemy)
                    print("%sdostałeś%s" %(fg(2), attr(0)), end = " ")
                    print(lootDrop)
                    lootEffect(lootDrop, character)
                    print("%s%sotrzymałeś przedmioty o równowartości%s" %(fg(11), bg(232), attr(0)), enemy.money, "%s%smonet%s" %(fg(11), bg(232), attr(0)))
                    character.cash += enemy.money
                    print("%s%smasz aktualnie%s" %(fg(11), bg(232), attr(0)), character.cash, "%s%smonet%s\n" %(fg(11), bg(232), attr(0)))
                    kanaly(score)
                    return score

            else:
                print("%s%sNie trafiłeś swojego przeciwnika%s" %(fg(1), bg(232), attr(0)))
                print(enemy.name, end = " ")
                print("%s%szadał tobie krytyczne obrażenia%s" %(fg(1), bg(232), attr(0)))
                enemy_crit_hit = 2.5 * (enemy.strenght - character.defence)
                if enemy_crit_hit > 0 :
                    character.health = character.health - enemy_crit_hit
                    print(enemy.name, "uderzył cię za", enemy_crit_hit, "%s\nZostało tobie%s" % (fg(175), attr(0)), character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                else:
                    print("%s%sPrzyfarciłeś. Wróg nie przebił się przez twoją obronę%s" %(fg(14), bg(232), attr(0)))
                gameOver(character, score)

#### atak magiczny
        elif choice == "2":
            print("Jebłeś magicznym laserkiem w", enemy.name + "a")
            hitchance = random.randint(0, 15)
            if hitchance >= 3:
                enemy.health = enemy.health - character.magic
                if enemy.health < 0:
                    enemy.health = 0
                else:
                    print("%suderzyłeś wroga, jego aktualne życie to%s" % (fg(3), attr(0)), enemy.health)

                if enemy.health > 0:
                    enemy_hit = enemy.strenght - character.defence
                    if enemy_hit > 0:
                        character.health = character.health - enemy_hit
                        print(enemy.name, "uderzył cię za", enemy_hit, "%s\nZostało tobie%s" % (fg(175), attr(0)),
                              character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                    else:
                        print("%sWróg nie przebił się przez twoją obronę%s" %(fg(14), attr(0)))
                    gameOver(character, score)

                else:
                    print("%s%sPokonałeś swojego wroga%s" % (fg(15), bg(3), attr(0)), enemy.name)
                    print("%sWygląda na to, że upuścił jakiś przedmiot,%s" % (fg(2), attr(0)), end=" ")
                    lootDrop = loot(enemy)
                    print("%sdostałeś%s" % (fg(2), attr(0)), end=" ")
                    print(lootDrop)
                    lootEffect(lootDrop, character)
                    print("%s%sotrzymałeś przedmioty o równowartości%s" % (fg(11), bg(232), attr(0)), enemy.money, "%s%smonet%s" % (fg(11), bg(232), attr(0)))
                    character.cash += enemy.money
                    print("%s%smasz aktualnie%s" % (fg(11), bg(232), attr(0)), character.cash, "%s%smonet%s\n" % (fg(11), bg(232), attr(0)))
                    kanaly(score)
                    return score
                    # return print("masz aktualnie", score, "punktów doświadczenia")
                    # break
            else:
                print("%s%sTwoja laserowa dzida spudłowała%s" % (fg(1), bg(232), attr(0)))
                print(enemy.name, end=" ")
                print("%s%szadał tobie krytyczne obrażenia%s" % (fg(1), bg(232), attr(0)))
                enemy_crit_hit = 2.5 * (enemy.strenght - character.defence)
                if enemy_crit_hit > 0:
                    character.health = character.health - enemy_crit_hit
                    print(enemy.name, "uderzył cię za", enemy_crit_hit, "%s\nZostało tobie%s" % (fg(175), attr(0)),
                          character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                else:
                    print("%s%sPrzyfarciłeś. Wróg nie przebił się przez twoją obronę%s" %(fg(14), bg(232), attr(0)))
                gameOver(character, score)

#### ucieczka
        elif choice == "3":
            print("Próbujesz uciekać i wrócić do miasta")
            runchance = random.randint(1, 100)
            if runchance > 15:
                print("udało Ci się uciec, uff...")
                options()
                break
            else:
                print("nie udało Ci się uciec")
                print("próbowałeś się bronić, ale niestety dotałeś pełną bułe za", enemy.strenght, "od wroga")
                character.health = character.health - enemy.strenght
                print("%sPozostało tobie%s" %(fg(175), attr(0)), character.health, "%spunktów życia%s" %(fg(175), attr(0)))
                gameOver(character, score)
                kanaly(score)

#### leczenie się
        elif choice == "7":
            print("Słabo się czuję, musze se chlupnąć miksturke pana Tadzia <3")
            if character.potion >= 1:
                if character.health < character.max_health - 20:
                    character.health = character.health + 20
                    print("%sTwój stan zdrowia wynosi obecnie%s" % (fg(175), attr(0)), character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                    character.potion = character.potion - 1
                    print("%s%sTwój stan mikturek zdrowia:%s" % (fg(170), bg(7), attr(0)), character.potion)
                elif character.health != character.max_health:
                    character.health = character.max_health
                    character.potion = character.potion - 1
                    print("%sTwój stan zdrowia wynosi obecnie%s" % (fg(175), attr(0)), character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                    print("%s%sTwój stan mikturek zdrowia:%s" % (fg(170), bg(7), attr(0)), character.potion)
                else:
                    print("Jednak napije się kiedy indziej mam pełne życie")
                    print("%s%sTwój stan mikturek zdrowia:%s" % (fg(170), bg(7), attr(0)), character.potion)
            else:
                print("O kurde! Pusto! Muszę udać się do Pana Tadzia uzupełnić zapas miksturek")

#### exit
        elif choice == "4":
            tak_nie = input("Czy na pewno chcesz wyjść z gry? %s%s(t/n)%s\n" % (fg(20), bg(7), attr(0)))
            if tak_nie == "t" or tak_nie == "1":
                #### dorobić może zapis gry przed wyjsciem?
                sys.exit()
            else:
                kanaly(score)

        else:
            print("Nie ma tego numeru w liście. Wybierz inny numerek.")


def mroczny_las(score):
    random_enemy = select_enemy(MONSTERS_MROCZNY_LAS)
    enemy = Enemy(random_enemy)
    print(enemy.name, "się pojawił!")
    print("masz 5 opcje...")
    while enemy.health > 0:
        choice = input("1. atak mieczem\n2. atak magiczny\n3. ucieczka i powrót do miasta\n4. Exit\n7. Leczenie się\n")

        #### atak fizyczny
        if choice == "1":
            print("Zaatakowałeś mieczem", enemy.name + "a")
            hitchance = random.randint(0, 15)
            if hitchance >= 3:
                enemy.health = enemy.health - character.strenght
                if enemy.health < 0:
                    enemy.health = 0
                else:
                    print("%suderzyłeś wroga, jego aktualne życie to%s" % (fg(3), attr(0)), enemy.health)

                if enemy.health > 0:
                    enemy_hit = enemy.strenght - character.defence
                    if enemy_hit > 0:
                        character.health = character.health - enemy_hit
                        print(enemy.name, "uderzył cię za", enemy_hit, "%s\nZostało tobie%s" % (fg(175), attr(0)),
                              character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                    else:
                        print("%sWróg nie przebił się przez twoją obronę%s" % (fg(14), attr(0)))
                    gameOver(character, score)

                else:
                    print("%s%sPokonałeś swojego wroga%s" % (fg(15), bg(3), attr(0)), enemy.name)
                    print("%sWygląda na to, że upuścił jakiś przedmiot,%s" % (fg(2), attr(0)), end=" ")
                    lootDrop = loot(enemy)
                    print("%sdostałeś%s" % (fg(2), attr(0)), end=" ")
                    print(lootDrop)
                    lootEffect(lootDrop, character)
                    print("%s%sotrzymałeś przedmioty o równowartości%s" % (fg(11), bg(232), attr(0)), enemy.money,
                          "%s%smonet%s" % (fg(11), bg(232), attr(0)))
                    character.cash += enemy.money
                    print("%s%smasz aktualnie%s" % (fg(11), bg(232), attr(0)), character.cash,
                          "%s%smonet%s\n" % (fg(11), bg(232), attr(0)))
                    mroczny_las(score)
                    return score

            else:
                print("%s%sNie trafiłeś swojego przeciwnika%s" % (fg(1), bg(232), attr(0)))
                print(enemy.name, end=" ")
                print("%s%szadał tobie krytyczne obrażenia%s" % (fg(1), bg(232), attr(0)))
                enemy_crit_hit = 2.5 * (enemy.strenght - character.defence)
                if enemy_crit_hit > 0:
                    character.health = character.health - enemy_crit_hit
                    print(enemy.name, "uderzył cię za", enemy_crit_hit, "%s\nZostało tobie%s" % (fg(175), attr(0)),
                          character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                else:
                    print("%s%sPrzyfarciłeś. Wróg nie przebił się przez twoją obronę%s" % (fg(14), bg(232), attr(0)))
                gameOver(character, score)

        #### atak magiczny
        elif choice == "2":
            print("Jebłeś magicznym laserkiem w", enemy.name + "a")
            hitchance = random.randint(0, 15)
            if hitchance >= 3:
                enemy.health = enemy.health - character.magic
                if enemy.health < 0:
                    enemy.health = 0
                else:
                    print("%suderzyłeś wroga, jego aktualne życie to%s" % (fg(3), attr(0)), enemy.health)

                if enemy.health > 0:
                    enemy_hit = enemy.strenght - character.defence
                    if enemy_hit > 0:
                        character.health = character.health - enemy_hit
                        print(enemy.name, "uderzył cię za", enemy_hit, "%s\nZostało tobie%s" % (fg(175), attr(0)),
                              character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                    else:
                        print("%sWróg nie przebił się przez twoją obronę%s" % (fg(14), attr(0)))
                    gameOver(character, score)

                else:
                    print("%s%sPokonałeś swojego wroga%s" % (fg(15), bg(3), attr(0)), enemy.name)
                    print("%sWygląda na to, że upuścił jakiś przedmiot,%s" % (fg(2), attr(0)), end=" ")
                    lootDrop = loot(enemy)
                    print("%sdostałeś%s" % (fg(2), attr(0)), end=" ")
                    print(lootDrop)
                    lootEffect(lootDrop, character)
                    print("%s%sotrzymałeś przedmioty o równowartości%s" % (fg(11), bg(232), attr(0)), enemy.money,
                          "%s%smonet%s" % (fg(11), bg(232), attr(0)))
                    character.cash += enemy.money
                    print("%s%smasz aktualnie%s" % (fg(11), bg(232), attr(0)), character.cash,
                          "%s%smonet%s\n" % (fg(11), bg(232), attr(0)))
                    mroczny_las(score)
                    return score
                    # return print("masz aktualnie", score, "punktów doświadczenia")
                    # break
            else:
                print("%s%sTwoja laserowa dzida spudłowała%s" % (fg(1), bg(232), attr(0)))
                print(enemy.name, end=" ")
                print("%s%szadał tobie krytyczne obrażenia%s" % (fg(1), bg(232), attr(0)))
                enemy_crit_hit = 2.5 * (enemy.strenght - character.defence)
                if enemy_crit_hit > 0:
                    character.health = character.health - enemy_crit_hit
                    print(enemy.name, "uderzył cię za", enemy_crit_hit, "%s\nZostało tobie%s" % (fg(175), attr(0)),
                          character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                else:
                    print("%s%sPrzyfarciłeś. Wróg nie przebił się przez twoją obronę%s" % (fg(14), bg(232), attr(0)))
                gameOver(character, score)

        #### ucieczka
        elif choice == "3":
            print("Próbujesz uciekać i wrócić do miasta")
            runchance = random.randint(1, 100)
            if runchance > 15:
                print("udało Ci się uciec, uff...")
                options()
                break
            else:
                print("nie udało Ci się uciec")
                print("próbowałeś się bronić, ale niestety dotałeś pełną bułe za", enemy.strenght, "od wroga")
                character.health = character.health - enemy.strenght
                print("%sPozostało tobie%s" % (fg(175), attr(0)), character.health,
                      "%spunktów życia%s" % (fg(175), attr(0)))
                gameOver(character, score)
                mroczny_las(score)

        #### leczenie się
        elif choice == "7":
            print("Słabo się czuję, musze se chlupnąć miksturke pana Tadzia <3")
            if character.potion >= 1:
                if character.health < character.max_health - 20:
                    character.health = character.health + 20
                    print("%sTwój stan zdrowia wynosi obecnie%s" % (fg(175), attr(0)), character.health,
                          "%spunktów życia.%s" % (fg(175), attr(0)))
                    character.potion = character.potion - 1
                    print("%s%sTwój stan mikturek zdrowia:%s" % (fg(170), bg(7), attr(0)), character.potion)
                elif character.health != character.max_health:
                    character.health = character.max_health
                    character.potion = character.potion - 1
                    print("%sTwój stan zdrowia wynosi obecnie%s" % (fg(175), attr(0)), character.health,
                          "%spunktów życia.%s" % (fg(175), attr(0)))
                    print("%s%sTwój stan mikturek zdrowia:%s" % (fg(170), bg(7), attr(0)), character.potion)
                else:
                    print("Jednak napije się kiedy indziej mam pełne życie")
                    print("%s%sTwój stan mikturek zdrowia:%s" % (fg(170), bg(7), attr(0)), character.potion)
            else:
                print("O kurde! Pusto! Muszę udać się do Pana Tadzia uzupełnić zapas miksturek")

        #### exit
        elif choice == "4":
            tak_nie = input("Czy na pewno chcesz wyjść z gry? %s%s(t/n)%s\n" % (fg(20), bg(7), attr(0)))
            if tak_nie == "t" or tak_nie == "1":
                #### dorobić może zapis gry przed wyjsciem?
                sys.exit()
            else:
                mroczny_las(score)

        else:
            print("Nie ma tego numeru w liście. Wybierz inny numerek.")


character = heroselect()
score = 0
while True:
    options()