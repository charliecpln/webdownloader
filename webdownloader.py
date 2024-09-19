#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coded by      @charliecpln
# Discord:      @charliecpln
# Telegram:     @charliecpln
# Github:       @charliecpln

import os
import time

try:
    def sil():
        name = os.name
        if name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    sil()

    def installation():
        try:
            print("Libraries checking...")
            from bs4 import BeautifulSoup
            import requests
            import webbrowser
            from colorama import Fore, Back, Style, init
            sil()
        except ImportError:
            print("Libraries are auto dowloading...")
            os.system("pip install beautifulsoup4 requests webbrowser colorama")
            sil()
    installation()

    import requests
    from bs4 import BeautifulSoup
    import webbrowser
    from colorama import Fore, Back, Style, init

    init(autoreset=True)

    banner = Fore.LIGHTRED_EX + Style.BRIGHT + """
 █     █▓█████ ▄▄▄▄      ▓█████▄ ▒█████  █     ████▄    █ ██▓    ▒█████  ▄▄▄     ▓█████▄▓█████ ██▀███  
▓█░ █ ░█▓█   ▀▓█████▄    ▒██▀ ██▒██▒  ██▓█░ █ ░███ ▀█   █▓██▒   ▒██▒  ██▒████▄   ▒██▀ ██▓█   ▀▓██ ▒ ██▒
▒█░ █ ░█▒███  ▒██▒ ▄██   ░██   █▒██░  ██▒█░ █ ░▓██  ▀█ ██▒██░   ▒██░  ██▒██  ▀█▄ ░██   █▒███  ▓██ ░▄█ ▒
░█░ █ ░█▒▓█  ▄▒██░█▀     ░▓█▄   ▒██   ██░█░ █ ░▓██▒  ▐▌██▒██░   ▒██   ██░██▄▄▄▄██░▓█▄   ▒▓█  ▄▒██▀▀█▄  
░░██▒██▓░▒████░▓█  ▀█▓   ░▒████▓░ ████▓▒░░██▒██▒██░   ▓██░██████░ ████▓▒░▓█   ▓██░▒████▓░▒████░██▓ ▒██▒
░ ▓░▒ ▒ ░░ ▒░ ░▒▓███▀▒    ▒▒▓  ▒░ ▒░▒░▒░░ ▓░▒ ▒░ ▒░   ▒ ▒░ ▒░▓  ░ ▒░▒░▒░ ▒▒   ▓▒█░▒▒▓  ▒░░ ▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░  ░ ░  ▒░▒   ░     ░ ▒  ▒  ░ ▒ ▒░  ▒ ░ ░░ ░░   ░ ▒░ ░ ▒  ░ ░ ▒ ▒░  ▒   ▒▒ ░░ ▒  ▒ ░ ░  ░ ░▒ ░ ▒░
  ░   ░    ░   ░    ░     ░ ░  ░░ ░ ░ ▒   ░   ░   ░   ░ ░  ░ ░  ░ ░ ░ ▒   ░   ▒   ░ ░  ░   ░    ░░   ░ 
    ░      ░  ░░            ░       ░ ░     ░           ░    ░  ░   ░ ░       ░  ░  ░      ░  ░  ░     
                    ░     ░                                                       ░                    
                                       [github.com/charliecpln]                            @charliecpln

                    """
    print(banner,"\n")
    url = input(Fore.LIGHTYELLOW_EX + Style.DIM + "[?] Please enter the target URL address: ").strip().lower()

    if not url.startswith("http"):
        if url.startswith("www."):
            url = "https://" + url
        else:
            url = "https://www." + url

    sil()
    print(Fore.LIGHTMAGENTA_EX + f"[*] Retrying connection to: {url}")
    cikti = requests.get(url)
    print(Fore.LIGHTGREEN_EX + f"[+] Connection sucsesfull")
    time.sleep(1.5)

    htmlkodu = cikti.text
    soup = BeautifulSoup(htmlkodu, "html.parser")
    formattedhtml = soup.prettify()
    sil()
    print(formattedhtml)

    def websitesiac():
        dosyaad = input(Fore.LIGHTYELLOW_EX + "Please enter a file name (default: 'webpage.html'): ").lower().strip() or "webpage.html"
        if not dosyaad.endswith(".html"):
            dosyaad = dosyaad + ".html"

        with open(dosyaad, "w", encoding="utf-8") as webpage:
            webpage.write(htmlkodu)
        print(Fore.LIGHTCYAN_EX + f"\n[+] File opened was {dosyaad} and code writed!")
        webbrowser.open(dosyaad)

    while True:
        sor = input(Fore.LIGHTYELLOW_EX + "Do you wanna open this code (y/n): ").lower().strip()

        if sor in ["y","n"]:
            if sor == "y":
                websitesiac()

            elif sor == "n":
                print(Fore.LIGHTWHITE_EX + "\n[-] Exiting...")
                quit()

        else:
            print(Fore.LIGHTRED_EX + "\n[X] Error: Exiting the program...")
            sil()
            quit()

        input(Fore.LIGHTYELLOW_EX + "\nPress 'enter' to exit...\n")
        sil()
        quit()

except Exception as e:
    input(f"Error: {e}\nPress 'enter' to exit...\n")
    sil()
    quit()
