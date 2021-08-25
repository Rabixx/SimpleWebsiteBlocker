from notifypy import Notify
from datetime import date
import pyfiglet
import os.path
import time
import sys
import os

user_choice = -1
user_choice_block_website = ""
user_choice_unlock_website = ""

win_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"

if os.path.exists("start.tmp"):

    notification = Notify()
                
    notification.application_name = "SimpleWebsiteBlocker"
    notification.title = "First time?"
    notification.message = "we hope you will enjoy our app!"
    notification.icon = "assets/icons/simple_website_blocker_icon.png"

    notification.send()
                
    m = open(win_path,"w")
    m.truncate(0)
    m.close()

    os.remove("start.tmp")

def main(user_choice,user_choice_block_website,user_choice_unlock_website,win_path):
    while user_choice != 6:
        if user_choice == 1:
            try:
                os.system('cls')
                c = open(win_path,"a")
                print("what website u want to block?")
                user_choice_block_website = str(input(">>: "))
                c.writelines("0.0.0.0" + " " + user_choice_block_website + "\n")
                c.close()
                print("website was successfully blocked!")
                time.sleep(1)
                os.system('cls')
            except Exception as ex_1:
                os.system('cls')
                print(f"[ERROR] {ex_1}")
                time.sleep(2)
                os.system('cls')

        if user_choice == 2:
            try:
                os.system('cls')
                print("what website u want to unlock?")
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

        if user_choice == 3:
            try:
                os.system('cls')
                print("all the websites that are currently blocked:")
                print()
                a = open(win_path,"r")
                lines = a.readlines()
                for line in lines:
                    print(line)
                a.close()
            except Exception as ex_3:
                os.system('cls')
                print(f"[ERROR] {ex_3}")
                time.sleep(2)
                os.system('cls')

        if user_choice == 4:
            try:
                os.system('cls')
                print("SimpleWebsiteBlocker",date.today().year,"copyrights")
                print("this app is really simple websiteblocker that can be used")
                print("without any time limits its free and under SimpleWebsiteBlocker license")
                print("you can find more details under this link {}".format("https://github.com/Rabixx/SimpleWebsiteBlocker/"))
                os.system('pause')
                os.system('cls')
            except Exception as ex_4:
                os.system('cls')
                print(f"[ERROR] {ex_4}")
                time.sleep(2)
                os.system('cls')
        
        if user_choice == 5:
            os.system('cls')
            print("Turning program off...")
            time.sleep(2)
            sys.exit()
        
        ascii_banner = pyfiglet.figlet_format("WebsiteBlocker")
        print(ascii_banner)
        print("1. Block website")
        print("2. Unlock website")
        print("3. Show all blocked websites")
        print("4. About app")
        print("5. Exit")
        user_choice = int(input(">>: "))

if __name__ == "__main__":
    main(user_choice,user_choice_block_website,user_choice_unlock_website,win_path)