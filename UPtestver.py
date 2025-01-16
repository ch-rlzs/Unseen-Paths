import time
import os
import json
import sys
from tkinter import *
from tkinter import scrolledtext

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
    update_message("Game saved successfully!\n")

def load_game():
    global dark, light, Weapon, name
    if os.path.exists("save_data.json"):
        with open("save_data.json", "r") as save_file:
            save_data = json.load(save_file)
        dark = save_data.get("dark", 0)
        light = save_data.get("light", 0)
        Weapon = save_data.get("weapon", None)
        name = save_data.get("name", "")
        update_message("Game loaded successfully!\n")
    else:
        update_message("No save file found. Starting a new game.\n")

def update_message(text):
    message_area.config(state=NORMAL)
    message_area.insert(END, text + "\n")
    message_area.see(END)
    message_area.config(state=DISABLED)

def start_game():
    update_message("Your story awaits...")
    time.sleep(1)
    update_message("\nThe world around you is veiled in shadows...\n")
    TTC()

def TTC():
    update_message('The choice lies before you, traveler.\n')
    update_message('Two paths, two fates.\n')
    update_message('One of light, where the warmth of forgotten hope lingers.\n')
    update_message('Another of shadow, where the unknown beckons with secrets untold.\n')
    update_message('Each will shape your journey in ways unseen by many others.\n')
    update_message('But be warned... not all is as it seems.\n')
    update_message('The light may blind, and the darkness may reveal.\n')
    show_choices(["Light", "Darkness"], choosepath)

def choosepath(choice):
    global dark, light

    if choice == 'Light':
        light += 1
    elif choice == 'Darkness':
        dark += 1
    save_game()
    fatesdivide()

def fatesdivide():
    global dark, light

    update_message('You have made a valiant choice\n')

    if dark >= 1:
        update_message('Your fate may take a toll for seeking a path so dark\n')
        update_message('But only time will tell if you made the right decision\n')

    if light >= 1:
        update_message('A divine light has shone upon your path\n')
        update_message('But may the gods contain corruption, that is the knowledge you must seek.\n')

    update_message('Your next choice has come so swiftly.\n')
    update_message('Many others haven’t even dared come so far.\n')
    update_message('Your choice is upon which weapon you seek.\n')
    weaponselect()

def weaponselect():
    global dark, light

    if dark >= 1:
        update_message('Upon being a dark warrior these are your weapon choices..\n')
        show_choices(["Void Reaver", "Nightfall Dagger", "Abyssal Scythe"], darknamecreate)

    if light >= 1:
        update_message('Upon being a light Warrior these are your weapon choices..\n')
        show_choices(["Radiant Blade", "Gleam Spear", "Aether Bow"], lightnamecreate)

def lightnamecreate(choice):
    global Weapon
    Weapon = choice
    update_message(f"Excellent choice... You chose {Weapon}\n")
    ask_name()

def darknamecreate(choice):
    global Weapon
    Weapon = choice
    update_message(f"Excellent choice... You chose {Weapon}\n")
    ask_name()

def ask_name():
    update_message('What should I call you, traveler?')
    name_entry.pack(pady=5)
    name_button.pack()

def save_name():
    global name
    name = name_entry.get()
    if len(name) < 3:
        update_message("Name must be at least 3 characters long.")
        return

    name_entry.pack_forget()
    name_button.pack_forget()
    save_game()
    update_message(f'Ah well {name}, Welcome to the world of Nythra\n')

def show_choices(options, callback):
    for button in choice_buttons:
        button.pack_forget()

    for option in options:
        btn = Button(root, text=option, command=lambda opt=option: callback(opt), bg="#2E3B4E", fg="white", font=("Helvetica", 12, "bold"), relief="groove", padx=10, pady=5)
        btn.pack(pady=5)
        choice_buttons.append(btn)

def main_menu():
    update_message("The path lies before you...")
    for button in choice_buttons:
        button.pack_forget()

    start_button.pack(pady=10)
    load_button.pack(pady=10)
    exit_button.pack(pady=10)

# Initialize Tkinter GUI
root = Tk()
root.title("Unseen Paths")
root.geometry("800x500")
root.config(bg="#1F1F1F")

# Style settings
message_area = scrolledtext.ScrolledText(root, wrap=WORD, state=DISABLED, width=80, height=20, bg="#121212", fg="white", font=("Courier", 12), relief="flat", bd=0)
message_area.pack(pady=10, padx=20)

start_button = Button(root, text="Start Game", command=start_game, bg="#2E3B4E", fg="white", font=("Helvetica", 14, "bold"), relief="ridge", padx=10, pady=5)
load_button = Button(root, text="Load Game", command=load_game, bg="#2E3B4E", fg="white", font=("Helvetica", 14, "bold"), relief="ridge", padx=10, pady=5)
exit_button = Button(root, text="Exit", command=root.quit, bg="#C0392B", fg="white", font=("Helvetica", 14, "bold"), relief="ridge", padx=10, pady=5)

name_entry = Entry(root, font=("Helvetica", 12), bg="#2E3B4E", fg="white", insertbackground="white", relief="flat", width=30)
name_button = Button(root, text="Submit", command=save_name, bg="#27AE60", fg="white", font=("Helvetica", 12, "bold"), relief="ridge", padx=10, pady=5)

choice_buttons = []

main_menu()
root.mainloop()
