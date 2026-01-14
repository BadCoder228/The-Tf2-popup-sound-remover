""" LIBRARIES """

# the "cool style" libraries
from colorama.ansi import AnsiFore
from art import tprint as art
from colorama import Fore

# the "fixers" ones
from os import system, path
from sys import exit as leaving

# for "data containers"
from json import load, dump

""" VARIABLES """

# consts
COMMAND : str = 'tf_mainmenu_match_panel_type "8"\n'

# changeable
tf_path : str = "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/cfg/config.cfg"

""" FUNCTIONS """

# main one
def Main() -> None:
    system("cls")

    Banner(Fore.YELLOW, "PANACEA", "The thing, that'll mute the \"exp gained\" sound effect!\n")
    
    action : str = input("1. Fix the sound\n2. Leave\n\n>>> ")
    
    system("cls")

    match(action):
        case "1":
            ConfigChanger()
        case "2":
            Escape(True)
        case _:
            Main()

# creates a banner!
def Banner(color : AnsiFore, header : str, subheader : str) -> None:
    print(color)
    art(header)
    print(subheader + Fore.WHITE)

# removes the original sound
def ConfigChanger() -> None:
    global tf_path

    if path.exists(path.abspath(tf_path)):

        with open(tf_path) as file:
            data = file.readlines()


        with open(tf_path, "w+") as file:
            for i in data:
                if i.startswith("tf_mainmenu_match_panel_type"):
                    data[data.index(i)] = COMMAND
                    break
            else:
                data.append(COMMAND)

            file.write("".join(data))
        
            file.close()

        Banner(Fore.GREEN, "Success!", "The \"exp gained\" sound is back!")
        Escape()

    else:

        Banner(Fore.LIGHTGREEN_EX, "Path not found", "Please follow the instructions down below!\n\n")
        tf_path = input(f"{Fore.RED}1. Open your Steam client and go to your Library.\n2. Right-click the game you want to check.\n3. Select Properties from the menu, then click on the Installed Files tab\n4. Then click on the \"Browse\" button\n5. Then the file manager will appear\nAfter copy the path from the top line and paste it here\n\n{Fore.WHITE}>>> ").replace("\\", "/") + '/tf/cfg/config.cfg'
        system("cls")
        ConfigChanger()

# leaves...
def Escape(leave : bool = False) -> None:
    if leave: 
        leaving()
    else:
        input(f"Press 'enter' to {'close the app' if leave else 'go to the main menu'}\n>>> ")
        Main()

""" LAUNCHER """

# the launcher
if __name__ == '__main__':
    Main()