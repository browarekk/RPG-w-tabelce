from enemy import *
#########from RPG import *



def kanaly(score):
    enemy = enemy_kanaly(goblin, rat, spider, big_rat)
    print("groźny", enemy.name, "się pojawił!")
    print("masz 4 opcje...")
    while enemy.health > 0:
        choice = input("1. atak mieczem\n2. atak magiczny\n3. ucieczka i powrót do miasta\n4. Exit\n")

#### atak fizyczny
        if choice == "1":
            print("Zaatakowałeś mieczem", enemy.name + "a")
            hitchance = random.randint(0,15)
            if hitchance >= 3:
                enemy.health = enemy.health - character.strenght
                print("%suderzyłeś wroga, jego aktualne życie to%s" %(fg(3), attr(0)), enemy.health)

                if enemy.health > 0:
                    enemy_hit = enemy.strenght - character.defence
                    if enemy_hit > 0:
                        character.health = character.health - enemy_hit
                        print(enemy.name, "uderzył cię za", enemy_hit, "%s\nZostało tobie%s" % (fg(175), attr(0)), character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                    else:
                        print("Wróg nie przebił się przez twoją obronę")
                    gameOver(character, score)

                else:
                    if enemy.name == "Goblin":
                        enemy.health = 20
                        score = score + 10
                    elif enemy.name == "Szczur":
                        enemy.health = 10
                        score = score + 5
                    elif enemy.name == "Pająk":
                        enemy.health = 20
                        score = score + 10
                    elif enemy.name == "Duży Szczur":
                        enemy.health = 25
                        score = score + 13

                    print("%s%sPokonałeś swojego wroga%s" %(fg(15), bg(3), attr(0)), enemy.name)
                    print("%sWygląda na to, że upuścił jakiś przedmiot,%s" %(fg(2), attr(0)), end = " ")
                    lootDrop = loot()
                    print("%sdostałeś%s" %(fg(2), attr(0)), end = " ")
                    print(lootDrop)
                    lootEffect(lootDrop, character)
                    kanaly(score)
                    return score
                    #return print("masz aktualnie", score, "punktów doświadczenia")
                    #break
            else:
                print("%s%sNie trafiłeś swojego przeciwnika%s" %(fg(1), bg(232), attr(0)))
                print(enemy.name, end = " ")
                print("%s%szadał tobie krytyczne obrażenia%s" %(fg(1), bg(232), attr(0)))
                enemy_crit_hit = 2.5 * (enemy.strenght - character.defence)
                if enemy_crit_hit > 0 :
                    character.health = character.health - enemy_crit_hit
                    print(enemy.name, "uderzył cię za", enemy_crit_hit, "%s\nZostało tobie%s" % (fg(175), attr(0)), character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                else:
                    print("Przyfarciłeś. Wróg nie przebił się przez twoją obronę")
                gameOver(character, score)

#### atak magiczny
        elif choice == "2":
            print("Jebłeś magicznym laserkiem w", enemy.name + "a")
            hitchance = random.randint(0,15)
            if hitchance >= 3:
                enemy.health = enemy.health - character.magic
                print("%suderzyłeś wroga, jego aktualne życie to%s" %(fg(3), attr(0)), enemy.health)
                if enemy.health > 0:
                    enemy_hit = enemy.strenght - character.defence
                    if enemy_hit > 0:
                        character.health = character.health - enemy_hit
                        print(enemy.name, "uderzył cię za", enemy_hit, "%s\nZostało tobie%s" % (fg(175), attr(0)),
                              character.health, "%spunktów życia.%s" % (fg(175), attr(0)))
                    else:
                        print("Wróg nie przebił się przez twoją obronę")
                    gameOver(character, score)

                else:
                    if enemy.name == "Goblin":
                        enemy.health = 20
                        score = score + 10
                    elif enemy.name == "Szczur":
                        enemy.health = 10
                        score = score + 5
                    elif enemy.name == "Pająk":
                        enemy.health = 20
                        score = score + 10
                    elif enemy.name == "Duży Szczur":
                        enemy.health = 25
                        score = score + 13

                    print("%s%sPokonałeś swojego wroga%s" % (fg(15), bg(3), attr(0)), enemy.name)
                    print("%sWygląda na to, że upuścił jakiś przedmiot,%s" % (fg(2), attr(0)), end=" ")
                    lootDrop = loot()
                    print("%sdostałeś%s" % (fg(2), attr(0)), end=" ")
                    print(lootDrop)
                    lootEffect(lootDrop, character)
                    kanaly(score)
                    return score
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
                    print("Przyfarciłeś. Wróg nie przebił się przez twoją obronę")
                gameOver(character, score)

#### ucieczka
        elif choice == "3":
            print("próbujesz uciekać i wrócić do miasta...")
            runchance = random.randint(1, 100)
            if runchance > 15:
                print("udało Ci się uciec...uff...")
                options()
                break
            else:
                print("nie udało Ci się uciec")
                print("próbowałeś się bronić, ale niestety dotałeś pełną bułe za", enemy.strenght, "od wroga")
                character.helath = character.health - enemy.strenght
                print("Pozostało tobie", character.health, "punktów życia")
                gameOver(character, score)
                kanaly(score)

#### exit
        elif choice == "4":
            tak_nie = input("Czy na pewno chcesz wyjść z gry? %s%s(t/n)%s" % (fg(20), bg(7), attr(0)))
            if tak_nie == "t":
                #### dorobić może zapis gry przed wyjsciem?
                sys.exit()
            else:
                kanaly(score)

        else:
            print("Nie ma tego numeru w liście. Wybierz inny numerek.")