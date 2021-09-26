from datetime import datetime
from notifypy import Notify
from colorama import Fore
import pyfiglet
import colorama
import requests
import logging
import os.path
import dotenv
import time
import sys
import os

colorama.init()

logging.basicConfig(level=logging.INFO,format='%(asctime)s : %(levelname)s : %(message)s')

config_path = "assets/config.env"
dotenv.load_dotenv(config_path)

COLOR = os.environ.get("COLOR")

user_choice = -1
user_choice_block_website = ""
user_choice_unlock_website = ""
user_confirm_choice = ""
user_choice_settings = -1
user_choice_settings_confirm_color = -1
user_choice_settings_confirm_clear = -1
user_choice_settings_choice_list = ""

current_version = "1.4"

version_url = "https://raw.githubusercontent.com/Rabixx/updater/main/version.txt"

win_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"

def on_start():
    if os.path.exists("start.tmp"):
        try:
            notification = Notify()

            notification.application_name = "SimpleWebsiteBlocker"
            notification.title = "First time?"
            notification.message = "Hello {} we hope you will enjoy our app!".format(os.getlogin())
            notification.icon = "assets/icons/simple_website_blocker_icon.png"

            notification.send()

            with open(win_path,"w") as m:
                m.truncate(0)

            os.remove("start.tmp")

            CONFIG_COLOR = getattr(Fore, COLOR)
            print(CONFIG_COLOR)
            os.system('cls')
        except PermissionError:
            logging.warning("Access denied please run SimpleWebsiteBlocker with admin permissions!")
            os.system('pause')
            sys.exit()

def load_config():
    CONFIG_COLOR = getattr(Fore, COLOR)
    print(CONFIG_COLOR)
    os.system('cls')

def main(user_choice,user_choice_block_website,user_choice_unlock_website,win_path,version_url,current_version,user_confirm_choice,user_choice_settings,user_choice_settings_confirm_clear,user_choice_settings_confirm_color,config_path,COLOR,user_choice_settings_choice_list):
    while user_choice != 7:
        if user_choice == 1:
            try:
                os.system('cls')
                print("what website u want to block?")
                print()
                print("to cancel hold CTRL + C in the same moment")
                print()
                user_choice_block_website = str(input(">>: "))
                
                with open(win_path,"a") as c:
                    c.writelines("0.0.0.0" + " " + user_choice_block_website + "\n")
                
                print("website was successfully blocked!")
                time.sleep(1)
                os.system('cls')
            except Exception as ex_1:
                os.system('cls')
                print(f"[ERROR] {ex_1}")
                time.sleep(2)
                os.system('cls')
            except KeyboardInterrupt:
                os.system('cls')

        if user_choice == 2:
            try:
                os.system('cls')
                print("what website u want to unlock?")
                print()
                print("to cancel hold CTRL + C in the same moment")
                print()
                user_choice_unlock_website = str(input(">>: "))
                with open(win_path, 'r') as file:
                    lines = file.readlines()

                content = f'0.0.0.0 {user_choice_unlock_website}'
                with open(win_path, 'w') as file:
                    for line in lines:
                        if line.strip("\n") != content:
                            file.write(line)
                
                print("website was successfully unlocked!")
                time.sleep(1)
                os.system('cls')
            except Exception as ex_2:
                os.system('cls')
                print(f"[ERROR] {ex_2}")
                time.sleep(2)
                os.system('cls')
            except KeyboardInterrupt:
                os.system('cls')
        
        if user_choice == 3:
            try:
                os.system('cls')
                print("all the websites that are currently blocked:")
                print()
                with open(win_path,"r") as a:
                    lines = a.readlines()
                
                for line in lines:
                    print(line)

            except Exception as ex_3:
                os.system('cls')
                print(f"[ERROR] {ex_3}")
                time.sleep(2)
                os.system('cls')
        
        if user_choice == 4:
            try:
                os.system('cls')

                url = requests.get(version_url)

                version = url.text
                
                if float(version) > float(current_version):
                    os.system('cls')
                    
                    print("New version {}is avaliable do you want to download it?".format(version))
                    print()
                    
                    user_confirm_choice = str(input("(yes,no): "))

                    if user_confirm_choice == "yes":
                        os.system('start https://cutt.ly/wWoOWvb')
                        os.system('cls')
                    elif user_confirm_choice == "no":
                        os.system('cls')
                else:
                    print("Great no updates were found!")
                    time.sleep(2)
                    os.system('cls')
            except Exception as ex_4:
                os.system('cls')
                print(f"[ERROR] {ex_4}")
                time.sleep(2)
                os.system('cls')
            except KeyboardInterrupt:
                os.system('cls')

        if user_choice == 5:
            try:
                os.system('cls')
            
                print("1. Change app color")
                print("2. Reset all blocked websites")
                print("3. About app")
                print("4. Inject list to block")
                print()
                print("to cancel hold CTRL + C in the same moment")
                print()
                user_choice_settings = int(input(">>: "))

                if user_choice_settings == 1:
                    os.system('cls')
                    
                    print(f"Current color: {COLOR}")
                    print()
                    print("1. Red")
                    print("2. Green")
                    print("3. Yellow")
                    print("4. Blue")
                    print("5. Magenta")
                    print("6. Cyan")
                    print("7. Reset color")
                    print()
                    print("to cancel hold CTRL + C in the same moment")
                    print()
                    user_choice_settings_confirm_color = int(input(">>: "))

                    if user_choice_settings_confirm_color == 1:
                        os.system('cls')
                                    
                        os.environ["COLOR"] = "RED"

                        dotenv.set_key(config_path,"COLOR",os.environ["COLOR"])

                        print("Changed color to red!")
                        print()
                        print("To see changes you have to restart the app")
                        time.sleep(3)
                        os.system('cls')

                    elif user_choice_settings_confirm_color == 2:
                        os.system('cls')
                                        
                        os.environ["COLOR"] = "GREEN"

                        dotenv.set_key(config_path,"COLOR",os.environ["COLOR"])

                        print("Changed color to green!")
                        print()
                        print("To see changes you have to restart the app")
                        time.sleep(3)
                        os.system('cls')
                    
                    elif user_choice_settings_confirm_color == 3:
                            os.system('cls')
                                        
                            os.environ["COLOR"] = "YELLOW"

                            dotenv.set_key(config_path,"COLOR",os.environ["COLOR"])

                            print("Changed color to yellow!")
                            print()
                            print("To see changes you have to restart the app")
                            time.sleep(3)
                            os.system('cls')

                    elif user_choice_settings_confirm_color == 4:
                        os.system('cls')
                                        
                        os.environ["COLOR"] = "BLUE"

                        dotenv.set_key(config_path,"COLOR",os.environ["COLOR"])

                        print("Changed color to blue!")
                        print()
                        print("To see changes you have to restart the app")
                        time.sleep(3)
                        os.system('cls')
                    
                    elif user_choice_settings_confirm_color == 5:
                        os.system('cls')
                                        
                        os.environ["COLOR"] = "MAGENTA"

                        dotenv.set_key(config_path,"COLOR",os.environ["COLOR"])

                        print("Changed color to magenta!")
                        print()
                        print("To see changes you have to restart the app")
                        time.sleep(3)
                        os.system('cls')

                    elif user_choice_settings_confirm_color == 6:
                        os.system('cls')
                                        
                        os.environ["COLOR"] = "CYAN"

                        dotenv.set_key(config_path,"COLOR",os.environ["COLOR"])

                        print("Changed color to cyan!")
                        print()
                        print("To see changes you have to restart the app")
                        time.sleep(3)
                        os.system('cls')

                    elif user_choice_settings_confirm_color == 7:   
                        os.system('cls')
                                        
                        os.environ["COLOR"] = "WHITE"

                        dotenv.set_key(config_path,"COLOR",os.environ["COLOR"])

                        print("Changed color to deafult!")
                        print()
                        print("To see changes you have to restart the app")
                        time.sleep(3)
                        os.system('cls')
                        
                if user_choice_settings == 2:
                    os.system('cls')
                    print("Are you sure to reset all blocked websites?")
                    print()
                    print("to cancel hold CTRL + C in the same moment")
                    print()
                    user_choice_settings_confirm_clear = str(input("(yes,no): "))

                    if user_choice_settings_confirm_clear == "yes":
                        with open(win_path,"w") as clear_file:
                            clear_file.truncate(0)

                        print("All websites were unlocked!")
                        time.sleep(1)
                        os.system('cls')
                    else:
                        os.system('cls')

                if user_choice_settings == 3:
                    os.system('cls')
                    print(f"> SimpleWebsiteBlocker {datetime.today().year} copyrights (C)")
                    print()
                    print("> the SimpleWebsiteBlocker as it says is simple app to block")
                    print("> unwanted or annoying websites also SimpleWebsiteBlocker")
                    print("> is free and under SimpleWebsiteBlocker(SBW) license you can use")
                    print("> it without any time limits for more details visit {}".format("https://github.com/Rabixx/SimpleWebsiteBlocker"))
                    print()
                    os.system('pause')
                    os.system('cls')

                if user_choice_settings == 4:
                    os.system('cls')
                    
                    files = os.listdir("assets\\lists\\")
                    
                    print("Which list you want to inject?")
                    print()
                    for file in files:
                        if file.endswith(".txt"):
                            print(">>",file)
                    print()
                    print("To cancel hold Ctrl + C in the same moment")
                    print()
                    user_choice_settings_choice_list = str(input(">>: "))

                    os.system('cls')

                    with open(f"assets\\lists\\{user_choice_settings_choice_list}","r+") as list_to_block:
                        with open(win_path,"w") as win_block:
                            for item in list_to_block:
                                win_block.writelines("0.0.0.0 " + item.strip() + "\n")

                    print(f"List {file} successfully injected!")
                    
                    time.sleep(2)

                    os.system('cls')

            except Exception as ex_5:
                os.system('cls')
                print(f"[ERROR] {ex_5}")
                time.sleep(2)
                os.system('cls')
            except KeyboardInterrupt:
                os.system('cls')

        if user_choice == 6:
            os.system('cls')
            print("Turning program off...")
            time.sleep(2)
            sys.exit()
        
        ascii_banner = pyfiglet.figlet_format("WebsiteBlocker")
        print(ascii_banner)
        print("1. Block website")
        print("2. Unlock website")
        print("3. Show all blocked websites")
        print("4. Check for updates")
        print("5. Settings")
        print("6. Exit")
        user_choice = int(input(">>: "))

if __name__ == "__main__":
    if sys.platform.startswith("win"):
        on_start()
        load_config()
        main(user_choice,user_choice_block_website,user_choice_unlock_website,win_path,version_url,current_version,user_confirm_choice,user_choice_settings,user_choice_settings_confirm_clear,user_choice_settings_confirm_color,config_path,COLOR,user_choice_settings_choice_list)
    else:
        logging.warning("SimpleWebsiteBlocker works only on Windows operating system!")
        os.system('pause')
        sys.exit()