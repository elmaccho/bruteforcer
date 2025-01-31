from art import text2art
from termcolor import colored

import os, os.path

target = ""
dictionary = ""
errorMessage = ""

def clearconsole():
    os.system("cls || clear")

def displaytext():
    global errorMessage
    appname = text2art("BForcer", font="slant")

    print(colored(appname, "blue"), end="")
    print(colored("------------------< by elmaccho >------------------", "light_blue"))

    if errorMessage:
        print(colored("------------------" + errorMessage +  "------------------", "red"))


def target_ip():
    global target

    clearconsole()
    displaytext()

    set_target = input("Wprowadź IP: ")

    target = set_target

    select_attack()


def dictionary_file():
    global dictionary, errorMessage

    clearconsole()
    displaytext()

    print("By uzyc pliku " + colored("rockyou.txt", "red")+" wpisz 0")
    set_dictionary = input("Wprowadź sciezke do pliku: ")

    if set_dictionary == "0":
        dictionary = os.path.join(os.getcwd(), 'assets', 'rockyou.txt')
        set_dictionary = dictionary

    if os.path.isfile(set_dictionary):
        dictionary = set_dictionary
        errorMessage = ""
        select_attack()
    else:
        errorMessage = "Plik nie istnieje"
        dictionary_file()



def select_attack():
    global errorMessage
    global target
    global dictionary

    clearconsole()
    displaytext()



    if target or dictionary:
        print(colored("---------------------------------------------------", "light_yellow"))
        print(colored("IP: ", "yellow") + target)
        print(colored("Plik: ", "yellow") + dictionary)
        print(colored("---------------------------------------------------", "light_yellow"))


    print(colored("[1]", "yellow") + "\tHTTP")
    print(colored("[2]", "yellow") + "\tSSH")
    print(colored("[3]", "yellow") + "\tIP celu")
    print(colored("[4]", "yellow") + "\tPlik z haslami")
    print(colored("[5]", "yellow") + "\tZakończ")

    set_attack = int(input("Wybierz opcje: "))

    if set_attack == 1:
        errorMessage = ""
    elif set_attack == 2:
        errorMessage = ""
    elif set_attack == 3:
        errorMessage = ""
        target_ip()
    elif set_attack == 4:
        errorMessage = ""
        dictionary_file()
    elif set_attack == 5:
        errorMessage = ""
        print(colored("Adios!", "magenta"))
        exit()
    else:
        errorMessage = "Niepoprawna opcja!"
        select_attack()


def start():
    displaytext()
    select_attack()

if __name__ == '__main__':
    start()