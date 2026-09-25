import json, os, sys

def load_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def change_room(file):
    global room_data
    with open(load_path(f"rooms/{file}"), "r") as f:
        room_data = json.load(f)

def show_text(file):
    print()
    with open(load_path(f"flavor_text/{file}"), "r") as f:
        for line in f.readlines():
            print(line, end="")
    print()
    print()
    input("Press enter to continue")

def subtract_resources(amount):
    global resources
    print()
    print(f"You lost {amount} resources.")
    resources -= amount
    print(f"You have {resources} resources left.")
    input("Press enter to continue.")

file = "testRoom.json"
global room_data
room_data = ""
change_room(file)
global resources
resources = 50
while True:
    for i in range(50):
        print()
        
    print(f"You have entered {room_data['name']}")
    print('--======================--')
    print(room_data["description"])
    print()
    print("You can do the following:")
    
    for i, j in enumerate(room_data["options"]):
        print(f"({i+1}) {j}")
        
    while True:
        try:
            choice = int(input("Pick an option: "))
            break
        except:
            print("You must pick a number.")
    
    eval(room_data["functions"][choice-1])