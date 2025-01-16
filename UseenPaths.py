import time
import os
import json
import sys
from tkinter import *
import tkinter as tk

# Global variables
dark = 0
light = 0
Weapon = None
name = ""

def save_game():
    global dark, light, Weapon, name
    save_data = {
        "dark": dark,
        "light": light,
        "weapon": Weapon,
        "name": name
    }
    with open("save_data.json", "w") as save_file:
        json.dump(save_data, save_file)
    print("Game saved successfully!")

def load_game():
    global dark, light, Weapon, name
    if os.path.exists("save_data.json"):
        with open("save_data.json", "r") as save_file:
            save_data = json.load(save_file)
        dark = save_data.get("dark", 0)
        light = save_data.get("light", 0)
        Weapon = save_data.get("weapon", None)
        name = save_data.get("name", "")
        print("Game loaded successfully!")
    else:
        print("No save file found. Starting a new game.")

def dataload():
    global dark, light, Weapon, name

    # Load save data if available
    load_game()

    # Initialize defaults if no save data exists
    dark = dark if 'dark' in globals() else 0
    light = light if 'light' in globals() else 0
    Weapon = Weapon if 'Weapon' in globals() else None
    name = name if 'name' in globals() else ""

    main()  # Start the game

def datasave():
    global dark, light, Weapon

    with open('data.txt', 'w') as f:
        f.write(f"{light}\n")
        f.write(f"{dark}\n")
        f.write(f"{Weapon}\n")

# Rest of the game logic

def game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Your story awaits...')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print("\nThe world around you is veiled in shadows...")
    time.sleep(2)
    print("\nDim light filters through the cracks of an unknown landscape,")
    time.sleep(2)
    print("revealing little of where you are or where you should go.")
    time.sleep(2)
    print("\nIn the silence, there is a faint presence... something lurking just out of sight.")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nYou feel it now, traveler.")
    time.sleep(2)
    print("I have been waiting for you.")
    time.sleep(3)
    print("I am The Whisper.")
    time.sleep(2)
    print("\nFew have tread these unseen paths, and fewer still have returned.")
    time.sleep(3)
    print("But perhaps, you will be different...")
    time.sleep(2)
    print("\nCan you feel it? The weight of choices, the gravity of every step.")
    time.sleep(4)
    print("Will you be the one to unravel the secrets hidden in the dark,")
    time.sleep(3)
    print("or will you fade into the shadows like the rest?")
    time.sleep(3)
    print("\nThe path stretches before you. Unseen. Uncertain.")
    time.sleep(4)
    print("But remember this: not all paths can be undone.")
    time.sleep(5)
    print("\nYour journey begins now.")
    time.sleep(3)
    TTC()

def TTC():
    print('The choice lies before you, traveler.')
    time.sleep(2)
    print('Two paths, two fates.')
    time.sleep(2)
    print('One of light, where the warmth of forgotten hope lingers.')
    time.sleep(3)
    print('Another of shadow, where the unknown beckons with secrets untold.')
    time.sleep(4)
    print('Each will shape your journey in ways unseen by many others.')
    time.sleep(5)
    print('But be warned… not all is as it seems.')
    time.sleep(4)
    print('The light may blind, and the darkness may reveal.')
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

    choosepath()

def choosepath():
    global dark, light
    def poL(str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.09)

    path_choice = input("Choose your path: Light or Darkness? > ").lower()

    if path_choice == 'light':
        light += 1
    elif path_choice == 'darkness':
        dark += 1
    else:
        poL("\nThe Whisper: 'This is not the time for hesitation, traveler. Choose wisely...'\n")
        choosepath()
        return

    save_game()  # Save progress after choosing a path
    datasave()
    fatesdivide()

def fatesdivide():
    global dark, light, Weapon

    def printt(str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.03)

    printt('You have made a valiant choice\n')
    time.sleep(2)

    if dark >= 1:
        printt('Your fate may take a toll for seeking a path so dark\n')
        printt('But only time will tell if you made the right decision\n')

    if light >= 1:
        printt('A divine light has shone upon your path\n')
        printt('But may the gods contain corruption, that is the knowledge you must seek.\n')

    printt('Your next choice has come so swiftly.\n')
    printt('Many others haven’t even dared come so far.\n')
    printt('Your choice is upon which weapon you seek.\n')

    weaponselect()

def weaponselect():
    global dark, light, name, Weapon
    def printt(str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.03)

    if dark >= 1:
        printt('Upon being a dark warrior these are your weapon choices..\n')
        time.sleep(2)
        printt('1>Void Reaver:\nDamage> 12\nSpeed> 7\n\n')
        printt('2>Nightfall Dagger:\nDamage> 11\nSpeed> 8\n\n')
        printt('3>Abyssal Scythe:\nDamage> 17\nSpeed> 4\n\n')
        Weapon = input('Your choice> ')
        darknamecreate()

    if light >= 1:
        printt('Upon being a light Warrior these are your weapon choices..\n')
        printt('1>Radiant Blade:\nDamage> 14\nSpeed> 11\n\n')
        printt('2>Gleam Spear:\nDamage> 11\nSpeed> 9\n\n')
        printt('3>Aether Bow:\nDamage> 12\nSpeed> 10\n\n')
        Weapon = input('Your choice> ')
        lightnamecreate()

def lightnamecreate():
    global Weapon
    if Weapon == '1':
        Weapon = 'Radiant Blade'
    elif Weapon == '2':
        Weapon = 'Gleam Spear'
    elif Weapon == '3':
        Weapon = 'Aether Bow'

    print("Excellent choice...")
    time.sleep(1)
    print('What should I call you traveler? ')
    time.sleep(3)
    global name
    name = input('--> ')
    while len(name) < 3:
        name = input('--> ')

    save_game()  # Save progress after weapon selection
    print('Ah well', name, 'Welcome to the world of Nythra')

def darknamecreate():
    global Weapon
    if Weapon == '1':
        Weapon = 'Void Reaver'
    elif Weapon == '2':
        Weapon = 'Nightfall Dagger'
    elif Weapon == '3':
        Weapon = 'Abyssal Scythe'

    print("Excellent choice...")
    time.sleep(1)
    print('What should I call you traveler? ')
    time.sleep(3)
    global name
    name = input('--> ')
    while len(name) < 3:
        name = input('--> ')

    save_game()  # Save progress after weapon selection
    print('Ah well', name, 'Welcome to the world of Nythra')
    time.sleep(2)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

    def print_slowmainmenu(str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.03)

    print_slowmainmenu('\nThe path lies before you...\n1> Step into the unknown\n2> Turn back while you still can')

    menu = input("\nWhat will you choose? > ").lower()

    if menu == '1' or menu == 'step into the unknown':
        game()
    elif menu == '2' or menu == 'turn back':
        print("\nThe shadows linger, waiting... perhaps another time.")
    elif menu == "load":
        load_game()
        main()
    else:
        print("\nThat is not a choice, traveler. Decide wisely.")
        main()  # Recursively call main to restart the menu if input is invalid

# Start the game
dataload()
