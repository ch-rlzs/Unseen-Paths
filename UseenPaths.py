
import time
import os
import json
import sys
from tkinter import *
import tkinter as tk
import sys  
# Global variables
dark = 0
light = 0
Weapon = None
name = ""
hfing = 0

#game=0|TTC=1|PATH=2|FATES=3|WEAPON=4|JOURNEY=5

def reset():
    dark = 0
    light = 0
    Weapon = None
    name = ""
    hfing = 0
    save_data = {
        "dark": dark,
        "light": light,
        "weapon": Weapon,
        "name": name,
        "hfing": hfing,
    
    }
    with open("save_data.json", "w") as save_file:
        json.dump(save_data, save_file)
    print_slow("Game reset successfully!\n")
    load_game()
def savegame():
    global dark, light, Weapon, name, hfing
    save_data = {
        "dark": dark,
        "light": light,
        "weapon": Weapon,
        "name": name,
        "hfing": hfing,
    
    }
    with open("save_data.json", "w") as save_file:
        json.dump(save_data, save_file)
    print_slow("Game saved successfully!\n")

def load_game():
    global dark, light, Weapon, name, hfing
    if os.path.exists("save_data.json"):
        with open("save_data.json", "r") as save_file:
            save_data = json.load(save_file)
        dark = save_data.get("dark", 0)
        light = save_data.get("light", 0)
        Weapon = save_data.get("weapon", None)
        name = save_data.get("name", "")
        hfing = save_data.get("hfing", 0)
        #print(dark, light, Weapon, name, hfing)

    if hfing >=1:  
        print_slow("Game loaded successfully!\n\n")
        
        main()
    else:
        print_slow("No save file found. Starting a new game.\n")

def print_slow(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

def dataload():
    global dark, light, Weapon, name, hfing

    # Load save data if available
    load_game()

    # Initialize defaults if no save data exists
    dark = dark if 'dark' in globals() else 0
    light = light if 'light' in globals() else 0
    Weapon = Weapon if 'Weapon' in globals() else None
    name = name if 'name' in globals() else ""
    hfing = hfing if ', hfing' in globals() else 0
    main()  # Start the game


def game():
    global hfing

    os.system('cls' if os.name == 'nt' else 'clear')
    print_slow('Your story awaits...\n')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print_slow("\nThe world around you is veiled in shadows...\n")
    time.sleep(2)
    print_slow("\nDim light filters through the cracks of an unknown landscape,\n")
    time.sleep(2)
    print_slow("revealing little of where you are or where you should go.\n")
    time.sleep(2)
    print_slow("\nIn the silence, there is a faint presence... something lurking just out of sight.\n")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print_slow("\nDo You feel it now, traveler.\n")
    time.sleep(2)
    print_slow("I have been waiting for you.\n")
    time.sleep(3)
    print_slow("I am The Whisper.\n")
    time.sleep(2)
    print_slow("\nFew have tread these unseen paths, and fewer still have returned.\n")
    time.sleep(3)
    print_slow("But perhaps, you will be different...\n")
    time.sleep(2)
    print_slow("\nCan you feel it? The weight of choices, the gravity of every step.\n")
    time.sleep(4)
    print_slow("Will you be the one to unravel the secrets hidden in the dark,\n")
    time.sleep(3)
    print_slow("or will you fade into the shadows like the rest?\n")
    time.sleep(3)
    print_slow("\nThe path stretches before you. Unseen. Uncertain.\n")
    time.sleep(4)
    print_slow("But remember this: not all paths can be undone.\n")
    time.sleep(5)
    print_slow("\nYour journey begins now.\n")
    time.sleep(3)
    hfing = 1
    savegame()
    TTC()

def TTC():
    global hfing 

    print_slow('The choice lies before you, traveler.\n')
    time.sleep(2)
    print_slow('Two paths, two fates.\n')
    time.sleep(2)
    print_slow('One of light, where the warmth of forgotten hope lingers.\n')
    time.sleep(3)
    print_slow('Another of shadow, where the unknown beckons with secrets untold.\n')
    time.sleep(4)
    print_slow('Each will shape your journey in ways unseen by many others.\n')
    time.sleep(5)
    print_slow('But be warned… not all is as it seems.\n')
    time.sleep(4)
    print_slow('The light may blind, and the darkness may reveal.\n')
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    hfing = 2
    savegame()
    choosepath()

def choosepath():
    global dark, light, hfing

    path_choice = input("Choose your path: Light or Darkness? > ").lower()

    if path_choice == 'light':
        light += 1
        dark = 0
    elif path_choice == 'darkness':
        dark += 1
        light = 0
    else:
        print_slow("\nThis is not the time for hesitation, traveler. Choose wisely...'\n")
        choosepath()
        return

     
    hfing = 3
    savegame()
    fatesdivide()

def fatesdivide():
    global dark, light, Weapon, hfing

    print_slow('You have made a valiant choice\n')
    time.sleep(2)

    if dark >= 1:
        print_slow('Your fate may take a toll for seeking a path so dark\n')
        print_slow('But only time will tell if you made the right decision\n')

    if light >= 1:
        print_slow('A divine light has shone upon your path\n')
        print_slow('But may the gods contain corruption, that is the knowledge you must seek.\n')

    print_slow('Your next choice has come so swiftly.\n')
    print_slow('Many others haven’t even dared come so far.\n')
    print_slow('Your choice is upon which weapon you seek.\n')
    hfing = 4
    weaponselect()

def weaponselect():
    global dark, light, name, Weapon

    if dark >= 1:
        print_slow('Upon being a dark warrior these are your weapon choices..\n')
        time.sleep(2)
        print_slow('1>Void Reaver:\nDamage> 12\nSpeed> 7\n\n')
        print_slow('2>Nightfall Dagger:\nDamage> 3\nSpeed> 13\n\n')
        print_slow('3>Abyssal Scythe:\nDamage> 17\nSpeed> 4\n\n')
        Weapon = input('Your choice> ')
        darknamecreate()

    if light >= 1:
        print_slow('Upon being a light Warrior these are your weapon choices..\n')
        print_slow('1>Radiant Blade:\nDamage> 14\nSpeed> 5\n\n')
        print_slow('2>Gleam Spear:\nDamage> 11\nSpeed> 4\n\n')
        print_slow('3>Aether Bow:\nDamage> 12\nSpeed> 10\nRange> 50\n\n')
        Weapon = input('Your choice> ')
        lightnamecreate()

def lightnamecreate():
    global Weapon, hfing
    if Weapon == '1':
        Weapon = 'Radiant Blade'
    elif Weapon == '2':
        Weapon = 'Gleam Spear'
    elif Weapon == '3':
        Weapon = 'Aether Bow'

    print_slow("Excellent choice...\n")
    time.sleep(1)
    print_slow('What should I call you traveler? \n')
   
    global name
    name = input('--> ')
    while len(name) < 3:
        name = input('--> ')

      # Save progress after weapon selection
    print_slow(f'Ah well {name}, Welcome to the world of Nythra\n')
    hfing = 5
    savegame()
    journeybegins()
   
def darknamecreate():
    global Weapon, hfing
    if Weapon == '1':
        Weapon = 'Void Reaver'
    elif Weapon == '2':
        Weapon = 'Nightfall Dagger'
    elif Weapon == '3':
        Weapon = 'Abyssal Scythe'

    print_slow("Excellent choice...\n")
    time.sleep(1)
    print_slow('What should I call you traveler? \n')
    
    global name
    name = input('--> ')
    while len(name) < 3:
        name = input('--> ')

    savegame()  # Save progress after weapon selection
    print_slow(f'Ah well {name}, Welcome to the world of Nythra\n')
    time.sleep(2)
    hfing = 5
    savegame()
    journeybegins()
    
def journeybegins():
    global dark, light, name, Weapon, hfing, city
    print_slow('You venture near your second choice\n')
    time.sleep(2)
    print_slow('This choice may be greater and deeper affecting than your last\n')
    time.sleep(2)
    print_slow('Your choice may be valiant or it maybe dismal....\n')
    time.sleep(2)
    print_slow('So.. What will you choose next....\n')
    time.sleep(2)
    if light >=1:
        print_slow('Because you chose the path of light\n you get two choices..\n One similar and one different to a darker path\n')
        print_slow('\n\n1> Lumina Celestis- The city of heaven light and succsess\n\n2> Limina- The city between light and dark')
        choose = input('Which will you choose? > ')
        if choose == '1':
            city = 'Lumina_Celestis'
        if choose == '2':
            city = 'Limina'
    if dark >=1:
        print_slow('Because you chose the path of dark..\n\n you get two choices..\n\nOne similar and one different to a lighter path\n')
        print_slow('\n\n1> Noctara- A dismal city though vast \n \n2> Limina- The city between light and dark')
        choose = input('Which will you choose? > ')
        if choose == '1':
            city = 'Noctara'
        if choose == '2':
            city = 'Limina'
    
                   
    #Lumina Celestis
    #Noctara
    #Limina
    print_slow('')
    
    print_slow('')
    
    print_slow('')
    
    print_slow('')
    








    main()


def main():
    global hfing, light, dark
    if hfing >=1:
        print_slow('\nThe path lies before you...\n1> Enter back into the shadows(continue)\n2> Turn back while you still can\n3> Rebirth yourself and start a new life (reset)')

        menu = input("\nWhat will you choose? > ").lower()

        if menu == '1' or menu == 'step into the unknown':
            if hfing == 0:
                game()
            if hfing == 1:  
                TTC()
            if hfing == 2:
                choosepath()
            if hfing == 3:
                fatesdivide()
            if hfing == 4:
                weaponselect()
            if hfing == 5:
                journeybegins()
        elif menu == '2' or menu == 'turn back':
            print_slow("\nThe shadows linger, waiting... perhaps another time.\n")
        elif menu =='3' or menu == 'reset':
            reset()
        elif menu =='cheat':
            print_slow('\nSo you have resort to desperate measures to progress... Only kidding pal heres your options of cheats\n')
            time.sleep(2)
            print_slow('\nYou have 2 options. Technically three but two of them are one or the other\n')
            time.sleep(2)
            print_slow('\n1> Load from a certain point (each chapter)\n2> Force light or dark paths (Auto sets hfing past the choosing a path)\n3> Exit to menu')
            cht = input('Your choice here> ')
            if cht == '1':
                hch = input('1> Start of game(0)\n2> TTC(1)\n3>CHOOSE(2)\n4> FATES(3)\n5> Weapon(4)\n--> ')
                if hch == '0':
                    hfing = 0
                if hch == '1':
                    hfing = 1
                
                if hch == '2':
                    hfing = 2
                

                if hch == '3':
                    hfing = 3
                if hch == '4':
                    hfing = 4
            if cht == '2':
                lod = ('Light or dark?(L/D > ').lower()
                if lod == 'l':
                    dark = 0
                    light += 1
                if lod == 'd':
                    light = 0
                    dark += 1
                

            if cht == '3':
                main()
                
            
                       


            
        else:
            print_slow("\nThat is not a choice, traveler. Decide wisely.\n")
            main()  # Recursively call main to restart the menu if input is invalid
        
    if hfing ==0:
        print_slow('\nThe path lies before you...\n1> Step into the unknown\n2> Turn back while you still can\n')

        menu = input("\nWhat will you choose? > ").lower()
        if menu == '1' or menu == 'step into the unknown':
            game()
        
        elif menu == '2' or menu == 'turn back':
            print_slow("\nThe shadows linger, waiting... perhaps another time.\n")

        elif menu =='cheat':
            print_slow('\nSo you have resort to desperate measures to progress... Only kidding pal heres your options of cheats\n')
            time.sleep(2)
            print_slow('\nYou have 2 options. Technically three but two of them are one or the other\n')
            time.sleep(2)
            print_slow('\n1> Load from a certain point (each chapter)\n2> Force light or dark paths (Auto sets hfing past the choosing a path)\n3> Exit to menu')
            cht = input('\nYour choice here> ')
            if cht == '1':
                hch = input('1> Start of game\n2> TTC\n3>CHOOSE\n4> FATES\n5> Weapon)\n--> ')
                if hch == '1':
                    hfing = 0
                    savegame()
                    main()

                if hch == '2':
                    hfing = 1
                    savegame()
                    main()

                if hch == '3':
                    hfing = 2
                    savegame()
                    main()

                if hch == '4':
                    hfing = 3
                    savegame()
                    main()

                if hch == '5':
                    hfing = 4
                    savegame()
                    main()

            if cht == '2':
                lod = input('Light or dark?(L/D > ').lower()
                if lod == 'l':
                    hfing = 2
                    dark = 0
                    light += 1
                    savegame()
                    main()

                if lod == 'd':
                    hfing = 2
                    light = 0
                    dark += 1
                    savegame()
                    main()


            if cht == '3':
                main()


        else:
            print_slow("\nThat is not a choice, traveler. Decide wisely.\n")
            main()  # Recursively call main to restart the menu if input is invalid

            
# Start the game
dataload()
7
