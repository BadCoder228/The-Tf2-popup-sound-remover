# the "cool style" libraries
from colorama.ansi import AnsiFore
from art import tprint as art
from colorama import Fore

# the "fixers" ones
from os import makedirs, system, remove, removedirs
from sys import exit as leaving
from shutil import copy

# for "data containers"
from json import load, dump

# consts
EXTRA_PATH : str = '/tf/custom/ThePanaceaProject/sound/ui/'

# funcs
def Main() -> None:
    system("cls")

    Banner(Fore.YELLOW, "PANACEA", "The thing, that'll mute the \"exp gained\" sound effect!\n")
    
    action : str = input("1. Fix the sound\n2. Overwrite the game's path\n3. Bring the sound back\n4. Leave\n\n>>> ")
    
    system("cls")

    match(action):
        case "1":
            SoundReplacer()
        case "2":
            PathChanger()
        case "3":
            BringMySoundBack()
        case "4":
            Escape(True)
        case _:
            Main()

def SoundReplacer() -> None:
    panacea_path, tf_path = "sound/mm_xp_chime.wav", Extractor()

    makedirs(tf_path+EXTRA_PATH, exist_ok=True)

    try:
        copy(panacea_path, tf_path+EXTRA_PATH)
        Banner(Fore.GREEN, "Success!", "The sound has been successfully overwritten!")
        Escape(True)

    except Exception as e:
        Banner(Fore.RED, f"Oops!", f"Something went wrong! You just got an error, here's it: {e}")
        Escape()    

def Escape(leave : bool = False) -> None:
    input(f"Press any key to {'close the app' if leave else 'go to the main menu'}\n>>> ")
    leaving() if leave else Main()

def Banner(color : AnsiFore, header : str, subheader : str) -> None:
    print(color)
    art(header)
    print(subheader + Fore.WHITE)

def Extractor() -> str:
    try:
        with open("config.json") as file:
            return load(file)["Path"]
    except:
        return "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2"

def PathChanger() -> None:
    try:
        with open("config.json", "w") as file:
            dump({"Path" : input("Your file path to the \"Team Fortress 2\" folder!\n>>> ")}, file, indent=2)

        file.close()

        system("cls")

        Banner(Fore.GREEN, "Success!", "The game's path has been successfully overwritten!")
        Escape()
    except Exception as e:
        Banner(Fore.RED, f"Oops!", f"Something went wrong! You just got an error, here's it: {e}")
        Escape()   

def BringMySoundBack() -> None:
    try:
        remove(Extractor()+EXTRA_PATH+"mm_xp_chime.wav")
        removedirs(Extractor()+EXTRA_PATH)
        Banner(Fore.GREEN, "Success!", "The \"exp gained\" sound is back!")
        Escape()

    except Exception as e:
        Banner(Fore.RED, f"Oops!", f"Something went wrong! You just got an error, here's it: {e}")
        Escape()   

if __name__ == '__main__':
    Main()