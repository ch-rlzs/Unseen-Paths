import time
import os
from tkinter import *
import tkinter as tk
import sys

def dataload():
    global dark, light, Weapon
    
    if os.path.exists("data.txt"):
        with open('data.txt', 'r') as f:
            # Read the variables from the file
            light = int(f.readline().strip())  # First line for light
            dark = int(f.readline().strip())   # Second line for dark
            Weapon = f.readline().strip()      # Third line for Weapon (as a string)
    else:
        # Create the file if it doesn't exist
        with open('data.txt', 'x'):
            pass  # Just creating the file, no need to write anything yet
    
    main()  # Assuming this is a function defined elsewhere in your code
def datasave():
    global dark, light, Weapon
    
    # Open the file in write mode to overwrite existing content
    with open('data.txt', 'w') as f:
        f.write(f"{light}\n")   # Save 'light' on the first line
        f.write(f"{dark}\n")    # Save 'dark' on the second line
        f.write(f"{Weapon}\n")  # Save 'Weapon' on the third line

print('''
 █    ██  ███▄    █   ██████ ▓█████ ▓█████ ███▄    █     ██▓███   ▄▄▄     ▄▄▄█████▓ ██░ ██   ██████ 
 ██  ▓██▒ ██ ▀█   █ ▒██    ▒ ▓█   ▀ ▓█   ▀ ██ ▀█   █    ▓██░  ██▒▒████▄   ▓  ██▒ ▓▒▓██░ ██▒▒██    ▒ 
▓██  ▒██░▓██  ▀█ ██▒░ ▓██▄   ▒███   ▒███  ▓██  ▀█ ██▒   ▓██░ ██▓▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░░ ▓██▄   
▓▓█  ░██░▓██▒  ▐▌██▒  ▒   ██▒▒▓█  ▄ ▒▓█  ▄▓██▒  ▐▌██▒   ▒██▄█▓▒ ▒░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██   ▒   ██▒
▒▒█████▓ ▒██░   ▓██░▒██████▒▒░▒████▒░▒████▒██░   ▓██░   ▒██▒ ░  ░ ▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓▒██████▒▒
░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░░ ▒░ ░ ▒░   ▒ ▒    ▒▓▒░ ░  ░ ▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒▒ ▒▓▒ ▒ ░
░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░▒  ░ ░ ░ ░  ░ ░ ░  ░ ░░   ░ ▒░   ░▒ ░       ▒   ▒▒ ░   ░     ▒ ░▒░ ░░ ░▒  ░ ░
 ░░░ ░ ░    ░   ░ ░ ░  ░  ░     ░      ░     ░   ░ ░    ░░         ░   ▒    ░       ░  ░░ ░░  ░  ░  
   ░              ░       ░     ░  ░   ░  ░        ░                   ░  ░         ░  ░  ░      ░  
                                                                                                    
                                                                                                                                                      
''')
time.sleep(2)
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
     #TTC stands for The Twilight Crossing
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
    printt('Many others havnt even dared come so far.\n')
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
        printt('Upon being a light Warror these are your weapon choices..\n')
        printt('1>Radiant Blade:\nDamage> 14\nSpeed> 11\n\n')
        printt('2>Gleam Spear:\nDamage> 11\nSpeed> 9\n\n')
        printt('3>Aether Bow:\nDamage> 12\nSpeed> 10\n\n')
        Weapon = input('Your choice> ')
        lightnamecreate()
def lightnamecreate():
    global Weapon
    if Weapon == '1':
            Weapon = 'Radiant Blade'
            print("Exelent choice...")
            time.sleep(1)
            print('What should i call you traveller? ')
            time.sleep(3)
            name = input('--> ')
            while len(name) < 3:
                name = input('--> ')
    if Weapon == '2':
            Weapon = 'Gleam Spear'
            print("Exelent choice...")
            time.sleep(1)
            print('What should i call you traveller? ')
            time.sleep(3)
            name = input('--> ')
            while len(name) < 3:
                name = input('--> ')
    if Weapon == '3':
            Weapon = 'Aether Bow'
            print("Exelent choice...")
            time.sleep(1)
            print('What should i call you traveller? ')
            time.sleep(3)
            name = input('--> ')
            while len(name) < 3:
                name = input('--> ')
    
    print('Ah well', name, 'Welcome to the world of Nythra')
def darknamecreate():
    global Weapon
    if Weapon == '1':
            Weapon = 'Void Reaver'
            print("Exelent choice...")
            time.sleep(1)
            print('What should i call you traveller? ')
            time.sleep(3)
            name = input('--> ')
            while len(name) < 3:
                name = input('--> ')
    if Weapon == '2':
            Weapon = 'Nightfall Dagger'
            print("Exelent choice...")
            time.sleep(1)
            print('What should i call you traveller? ')
            time.sleep(3)
            name = input('--> ')
            while len(name) < 3:
                name = input('--> ')
    if Weapon == '3':
            Weapon = 'Abyssal Scythe'
            print("Exelent choice...")
            time.sleep(1)
            print('What should i call you traveller? ')
            time.sleep(3)
            name = input('--> ')
            while len(name) < 3:
                name = input('--> ')
    datasave()
    print('Ah well', name, 'Welcome to the world of Nythra')
    time.sleep(2)


def test():
     global Weapon
     print(Weapon)
     input(' ')














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
    if menu == "skip1":
        TTC()
    if menu == "skip2":
        choosepath()
    if menu == "skip3":
        fatesdivide()
    if menu == "skip4":
        weaponselect()
    if menu == "test":
         test()
    
    
    elif menu == '2' or menu == 'turn back':
        print("\nThe shadows linger, waiting... perhaps another time.")
    else:
        print("\nThat is not a choice, traveler. Decide wisely.")
        main()  # Recursively call main to restart the menu if input is invalid


    
dataload()
