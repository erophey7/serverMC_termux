import colorama
import os
import time
import json
import socket


settings = {}


page = "main"


rowAni = (">", " ")
rowAniFrame = 0

colorama.init()


class ui():





    def clear():

        if os.name == 'nt':
             _ = os.system('cls')


        else:
             _ = os.system('clear')

    def main_menu():
        print()
        print(colorama.Fore.GREEN + "                  _________                                 \n",
                                    "   _____   ____  /   _____/ ______________  __ ___________  \n",
                                    "  /     \_/ ___\ \_____  \_/ __ \_  __ \  \/ // __ \_  __ \ \n",
                                    " |  Y Y  \  \___ /        \  ___/|  | \/\   /\  ___/|  | \/ \n",
                                    " |__|_|  /\___  >_______  /\___  >__|    \_/  \___  >__|    \n",
                                    "       \/     \/        \/     \/                 \/        \n")
        print(colorama.Style.RESET_ALL)
        print(" 1 - My servers\n",
              "2 - Create server\n",
              "3 - Delete server\n",
              "4 - Settings\n",
              "5 - Setup required packages\n",
              "6 - Check version\n",
              "0 - Exit \n\n\n\n\n\n")



class func():
    
    def vanilaParser():
        pass


    def getLocalIP():
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip



ui.main_menu()



while True:
    print(func.getLocalIP())
    choice = ""
    print(colorama.Fore.GREEN)
    choice = input("> ")
    print(colorama.Style.RESET_ALL)
    ui.clear()
    time.sleep(0.05)

    if page == "main":
        if choice == "":
            page = "main"
            ui.main_menu()
        
        elif choice == "0":
            exit(0)

