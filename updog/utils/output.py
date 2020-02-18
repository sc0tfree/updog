import sys
from colorama import Fore, Style


def info(string):
    preface = "[*] "
    print(Fore.BLUE + preface + string + Style.RESET_ALL)


def error(string):
    preface = "[!] "
    print(Fore.RED + preface + string + Style.RESET_ALL)
    sys.exit(1)


def warn(string):
    preface = "[-] "
    print(Fore.YELLOW + preface + string + Style.RESET_ALL)


def success(string):
    preface = "[+] "
    print(Fore.GREEN + preface + string + Style.RESET_ALL)


def heading(string):
    armor = '----'
    spacing = ' '
    print('')
    print(Fore.GREEN + armor + spacing + string + spacing + armor + Style.RESET_ALL)