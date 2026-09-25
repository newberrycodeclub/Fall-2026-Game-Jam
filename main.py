import json, os, sys, time

def load_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#changes the room
def change_room(file):
    global room_data
    with open(load_path(f"rooms/{file}"), "r") as f:
        room_data = json.load(f)

#Show some flavor text
def show_text(file):
    print()
    with open(load_path(f"flavor_text/{file}"), "r") as f:
        for line in f.readlines():
            print(line, end="")
    print()
    print()
    input("Press enter to continue")

#We can use a generic resources variable for now.
def subtract_resources(amount):
    global resources
    print()
    print(f"You lost {amount} resources.")
    resources -= amount
    print(f"You have {resources} resources left.")
    input("Press enter to continue.")

#Put your name in the credits.
def roll_credits():
    print("""
Thank you to these wonderful programmers:
            John Name
            Johnny Name

And the person who kept this story on track:
            Abby Griffin

Thank you for playing our game!

""")
    input("Press enter to exit.")

#Titles (Very cinimatic).
print("""
Coding Club Presents...
""")
time.sleep(3)
print("""
The Super Awesome Quest to Kill the Galactic Space Dragon. In Space.
""")
time.sleep(5)

#Actually code for the game.

#Set the starter room
file = "testRoom.json"
global room_data
room_data = ""
change_room(file)
global resources
resources = 50
while True:
    #Clear screen.
    for i in range(50):
        print()
        
    #Give the room description
    print(f"You have entered {room_data['name']}")
    print('--======================--')
    print(room_data["description"])
    print()
    print("You can do the following:")
    
    #List the options
    for i, j in enumerate(room_data["options"]):
        print(f"({i+1}) {j}")
        
    #Get input and run the command associated with it.
    while True:
        try:
            choice = int(input("Pick an option: "))
            eval(room_data["functions"][choice-1])
            break
        except:
            print("You must pick a number that is listed.")