""" LIBRARIES """

# the "cool style" libraries
from colorama.ansi import AnsiFore
from art import tprint as art
from colorama import Fore

# the "fixers" ones
from os import makedirs, system, remove, removedirs, path
from sys import exit as leaving
from shutil import copy

# for "data containers"
from json import load, dump

""" VARIABLES """

# consts
EXTRA_PATH : str = '/tf/custom/ThePanaceaProject/sound/ui/'
PANACEA_PATH : str = "sound/mm_xp_chime.wav"

# changeable
tf_path : str = "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2"

""" FUNCTIONS """

# main one
def Main() -> None:
    system("cls")

    Banner(Fore.YELLOW, "PANACEA", "The thing, that'll mute the \"exp gained\" sound effect!\n")
    
    action : str = input("1. Fix the sound\n2. Bring the sound back\n3. Leave\n\n>>> ")
    
    system("cls")

    match(action):
        case "1":
            SoundReplacer()
        case "2":
            SoundRemover()
        case "3":
            Escape(True)
        case _:
            Main()

# creates a banner!
def Banner(color : AnsiFore, header : str, subheader : str) -> None:
    print(color)
    art(header)
    print(subheader + Fore.WHITE)

# removes the original sound
def SoundReplacer() -> None:
    global tf_path

    if path.exists(path.abspath(tf_path)):

        makedirs(tf_path+EXTRA_PATH, exist_ok=True)
        copy(PANACEA_PATH, tf_path+EXTRA_PATH)
        Banner(Fore.GREEN, "Success!", "The sound has been successfully overwritten!")
        Escape()

    else:

        Banner(Fore.LIGHTGREEN_EX, "Path not found", "Please follow the instructions down below!\n\n")
        tf_path = input(f"{Fore.RED}1. Open your Steam client and go to your Library.\n2. Right-click the game you want to check.\n3. Select Properties from the menu, then click on the Installed Files tab\n4. Then click on the \"Browse\" button\n5. Then the file manager will appear, copy the path from the top line and paste it here\n\n{Fore.WHITE}>>> ")
        system("cls")
        SoundReplacer()

# brings the original sound back
def SoundRemover() -> None:
    global tf_path

    if path.exists(path.abspath(tf_path+EXTRA_PATH+"mm_xp_chime.wav")):
            
        remove(tf_path+EXTRA_PATH+"mm_xp_chime.wav")
        removedirs(tf_path+EXTRA_PATH)
        Banner(Fore.GREEN, "Success!", "The \"exp gained\" sound is back!")
        Escape()

    else:

        Banner(Fore.LIGHTGREEN_EX, "Path not found", "Please follow the instructions down below!\n\n")
        tf_path = input(f"{Fore.RED}1. Open your Steam client and go to your Library.\n2. Right-click the game you want to check.\n3. Select Properties from the menu, then click on the Installed Files tab\n4. Then click on the \"Browse\" button\n5. Then the file manager will appear, copy the path from the top line and paste it here\n6. Then go by this path: {EXTRA_PATH} (press '0' if you've noticed, that some of the folders dont exist)\n\n{Fore.WHITE}Or press '0' to leave to the main menu.\n\n>>> ")
        
        if tf_path == "0":
            Escape()
        else:
            system("cls")
            SoundRemover()

# leaves...
def Escape(leave : bool = False) -> None:
    if leave: 
        leaving()
    else:
        input(f"Press any key to {'close the app' if leave else 'go to the main menu'}\n>>> ")
        Main()

""" LAUNCHER """

# the launcher
if __name__ == '__main__':
    Main()

