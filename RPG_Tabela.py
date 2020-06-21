from tkinter import *
from profesions import *
import random

class Aplikacja:
    def __init__(self, master):
        """
        self.character = ''
        self.health = 0
        self.strenght = 0
        self.defence = 0
        self.magic = 0
        self.cash = 0
        self.potion = 0
        """
        self.character = None
        frame_G = Frame(master)
        frame_G.pack(side = TOP)
        frame_D = Frame(master)
        frame_D.pack(side = BOTTOM)

        # Górna Ramka
        frame_GR = Label(frame_G, width=150, height=30, bd=3, relief="groove")
        frame_GR.pack()

        #Dolna Ramka
        frame_DR = Label(frame_D, width=150, height=12, bd=3, relief="groove")
        frame_DR.pack()

        # Lewa górna ramka #tu beda obrazki się wyświetlać (lokacji i potworów)
        frame_GRL = Frame(frame_GR, width=822, height=452, bd=3, relief="groove")
        frame_GRL.place(relx = 0.00, rely = 0.00, anchor = NW)

        # Prawa górna ramka #tu będą ikonki z życiem statystykami itd
        frame_GRP = Frame(frame_GR, width=231, height=452, bd=3, relief="groove")
        frame_GRP.place(relx = 0.78, rely = 0.00, anchor = NW)

        # Dolna ramka prawa ale jakoś nie jest prawa przez "Output" jest w ogóle potrzbena
        #self.D_RP = Frame(self.D_R, width=188, height=214, bd=3, relief="groove")
        #self.D_RP.place(relx = 0.314, rely = 0.00, anchor = NW)

        # Dolna ramka lewa
        frame_DRL = Frame(frame_DR, width=350, height=182, bd=3, relief="groove")
        frame_DRL.place(relx = 0.00, rely = 0.00, anchor = NW)
        frame_DRLL = Frame(frame_DRL, width=175, height=182)
        frame_DRLL.pack(side = LEFT)
        frame_DRLP = Frame(frame_DRL, width=175, height=182)
        frame_DRLP.pack(side = RIGHT)

        #### koncepcja z przyciskaniem przyciskow
        self.BTN1 = Entry(frame_DRLL, width=28)
        self.BTN1.bind('<Return>', self.get)
        self.BTN1.pack()
        self.BTN2 = Button(frame_DRLP, text="Heroselect", width=23, command=self.hero_select)
        self.BTN2.pack()
        self.BTN3 = Button(frame_DRLL, text="BTN3", width=23)
        self.BTN3.pack()
        self.BTN4 = Button(frame_DRLP, text="BTN4", width=24)
        self.BTN4.pack()
        self.BTN5 = Button(frame_DRLL, text="BTN5", width=23)
        self.BTN5.pack()
        self.BTN6 = Button(frame_DRLP, text="BTN6", width=24)
        self.BTN6.pack()
        self.BTN7 = Button(frame_DRLL, text="BTN7", width=23)
        self.BTN7.pack()
        self.BTN8 = Button(frame_DRLP, text="BTN8", width=24)
        self.BTN8.pack()
        self.BTN9 = Button(frame_DRLL, text="BTN9", width=23)
        self.BTN9.pack()
        self.BTN10 = Button(frame_DRLP, text="BTN10", width=24)
        self.BTN10.pack()
        self.BTN11 = Button(frame_DRLL, text="BTN11", width=23)
        self.BTN11.pack()
        self.BTN12 = Button(frame_DRLP, text="EXIT", width=24, command=self.exituj)
        self.BTN12.pack()
        self.BTN13 = Button(frame_DRLL, text="pisz comand", width=23, command=self.pisz)
        self.BTN13.pack()
        self.BTN14 = Button(frame_DRLP, text="Czyść okno", width=24, command=self.clear_output)
        self.BTN14.pack()

        #### koncepcja z wpisywaniem wartości, trzeba dopracować
        #self.inputval = StringVar()
        #self.inputentry = Entry(self.D_RL, textvariable=self.inputval).grid(column=1, row=1)

        #Output
        self.Output = Text(frame_DR, width=87, height=11, wrap=WORD, bg="#c2d6d6")
        self.Output.place(relx = 0.335, rely = 0.00, anchor = NW)
        # print(Output)
        # Output.config(yscrollcomands=SCRL.set)

        # ---------------------------TK dodatki---------------------------------------
        #### Scroll
        # SCRL = Scrollbar(D_R2)
        # SCRL.pack(side = RIGHT, fill = Y)
        # SCRL.config(command = Output.yview)

        self.health = IntVar()
        # ---------------------------Odwołanie do obrazków---------------------------------------
        cont = Canvas(frame_GRL, width=812, height=442)
        cont.place(relx = 0.00, rely = 0.00, anchor = NW)
        image1 = PhotoImage(file="images/obrazy/bg1.png") # rozmiar 822x452
        image = cont.create_image(100, 100, image=image1)



        self.health_ikon = PhotoImage(file=r"images/health_iko.png")  # rozmiar 32x32
        self.strenght_ikon = PhotoImage(file=r"images/strenght_iko.png")  # rozmiar 32x32
        self.defence_ikon = PhotoImage(file=r"images/defence_iko.png")  # rozmiar 32x32
        self.magic_ikon = PhotoImage(file=r"images/magic_iko.png")  # rozmiar 32x32
        self.cash_ikon = PhotoImage(file=r"images/cash_iko.png")  # rozmiar 32x32
        self.potion_ikon = PhotoImage(file=r"images/potion_iko.png")  # rozmiar 32x32

        self.heroselect_image = PhotoImage(file=r"images/obrazy/heroselect2.png") #rozmiar 1024x576

        # ---------------------------Labele---------------------------------------
        self.Health_LBL = Label(frame_GRP, image=self.health_ikon, compound=LEFT, text='Zdrowie:', font=('arial', 10, 'bold'), width=130, height=32, anchor=W).place(relx=0.0, rely=0.00, anchor=NW)
        self.Health_LBL2 = Label(frame_GRP, textvariable=self.health, font=('arial', 10, 'bold'))
        self.Health_LBL2.place(relx=0.42, rely=0.015, anchor=NW)
        # Health_LBL2['text'] = character.health

        self.Strenght_LBL = Label(frame_GRP, image=self.strenght_ikon, compound=LEFT, text='Siła:', font=('arial', 10, 'bold'), width=130, height=32, anchor=W).place(relx=0.0, rely=0.07, anchor=NW)
        self.Strenght_LBL2 = Label(frame_GRP, text='abc', font=('arial', 10, 'bold')).place(relx=0.31, rely=0.085, anchor=NW)

        self.Defence_LBL = Label(frame_GRP, image=self.defence_ikon, compound=LEFT, text='Obrona:', font=('arial', 10, 'bold'), width=130, height=32, anchor=W).place(relx=0.0, rely=0.14, anchor=NW)
        self.Defence_LBL2 = Label(frame_GRP, text='abc', font=('arial', 10, 'bold')).place(relx=0.40, rely=0.155, anchor=NW)

        self.Magic_LBL = Label(frame_GRP, image=self.magic_ikon, compound=LEFT, text='Magia:', font=('arial', 10, 'bold'), width=130, height=32, anchor=W).place(relx=0.0, rely=0.21, anchor=NW)
        self.Magic_LBL2 = Label(frame_GRP, text='abc', font=('arial', 10, 'bold')).place(relx=0.37, rely=0.225, anchor=NW)

        self.Cash_LBL = Label(frame_GRP, image=self.cash_ikon, compound=LEFT, text='Stan konta:', font=('arial', 10, 'bold'), width=130, height=32, anchor=W).place(relx=0.0, rely=0.28, anchor=NW)
        self.Cash_LBL2 = Label(frame_GRP, text='abc', font=('arial', 10, 'bold')).place(relx=0.49, rely=0.295, anchor=NW)

        self.Potion_LBL = Label(frame_GRP, image=self.potion_ikon, compound=LEFT, text='Stan miksturek:', font=('arial', 10, 'bold'), width=130, height=32, anchor=W).place(relx=0.0, rely=0.35, anchor=NW)
        self.Potion_LBL2 = Label(frame_GRP, text='abc', font=('arial', 10, 'bold')).place(relx=0.61, rely=0.365, anchor=NW)

    def get(event):
        print(event.get())
        #self.Output.insert(END, "Wcisnąłeś 'Enter'")

        pass

    def clear_output(self):
        self.Output.delete(0.0, END)

    def pisz(self):
        self.Output.insert(END, "testuje pisanie\n")
        self.Output.insert(END, do_pisania)

    def exituj(self):
        self.Output.insert(END, "na pewno wyjść?")
        sys.exit()

    def hero_select(self):
        #image = cont.create_image(140, 105, image = self.heroselect_image)
        #image_heroes = Frame(master, image=self.heroselect_image)
        #image_heroes.place(relx=0.00, rely=0.00, anchor=NW)
        self.Output.insert(END, "Wybierz swojego bohatera!\n")
        self.Output.insert(END, "Wojownik \nMag \nłucznik \nWczytaj grę (nie działa jeszcze)\n")
        #selection = input

        #self.BTN2.configure(text="Wojownik", command=self.warrior)
        #self.BTN2.configure(text="Wojownik")
        self.BTN2['text'] = "Wojownik"
        self.BTN2['command'] = lambda: self.create_character(Warrior())
        self.BTN3['text'] = "Mag"
        self.BTN3['command'] = lambda: self.create_character(Wizard())
        self.BTN4['text'] = "łucznik"
        self.BTN5['text'] = "GM"
        self.BTN6['text'] = " "
        self.BTN7['text'] = " "
        self.BTN8['text'] = " "
        self.BTN9['text'] = " "
        self.BTN10['text'] = " "
        self.BTN11['text'] = " "

    def create_character(self, character):
        self.character = character
        self.Output.insert(END, "Wybrales {}".format(self.character.name))
        self.update_char_attributes()

        #selection = self.Output.insert(END, input("1. Wojownik \n2. Mag \n3. łucznik \n4. Wczytaj grę (nie działa)\n"))
        #selection = input("1. Wojownik \n2. Mag \n3. łucznik \n4. Wczytaj grę (nie działa)\n")
    def update_char_attributes(self):
        self.health.set(self.character.health)

    def game_load():
        self.Output.insert(END, "Ta funkcja jeszcze nie działa")
        # nie działa
        #data = [character.health, character.strenght, character.defence, character.magic, character.cash, character.potion]
        #data = pickle.load(open("save.dat", "rb"))



do_pisania = "witaj\n"

root = Tk()
root.title("Text RPG w tkinter od podstaw")
root.iconbitmap("images/ikony/0ikona6.ico")
#root.geometry("1280x714+300+150")
app = Aplikacja(root)
root.mainloop()



