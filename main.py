from art import text2art
from termcolor import colored

import os, os.path

target = ""
dictionary = ""
errorMessage = ""
formMethod = ""
usernames = ""
username = ""

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

def set_form_method():
    global formMethod
    global errorMessage
    clearconsole()
    displaytext()

    print("Wybierz metode formularza: ")

    print(colored("[1]", "yellow") + "\tPOST")
    print(colored("[2]", "yellow") + "\tGET")
    print(colored("[3]", "yellow") + "\tWroc do menu")

    set_method = int(input("Wybierz opcje: "))

    if set_method == 1:
        errorMessage = ""
        formMethod = "POST"
    elif set_method == 2:
        errorMessage = ""
        formMethod = "GET"
    elif set_method == 3:
        errorMessage = ""
        select_attack()
    else:
        errorMessage = "Niepoprawna opcja!"
        set_form_method()

def set_username():
    global username, usernames, errorMessage

    username = ""
    usernames = ""

    clearconsole()
    displaytext()

    username = input("Wprowadz nazwe uzytkownika: ")

    if username == "":
        errorMessage = "Wprowadz poprawne dane"
        set_username()
    else:
        errorMessage = ""
        select_attack()

def set_users_file():
    global username, usernames, errorMessage

    username = ""
    usernames = ""

    clearconsole()
    displaytext()

    usernames = input("Wprowadz sciezke do pliku z nazwami uzytkownikow: ")

    if os.path.isfile(usernames):
        errorMessage = ""
        select_attack()
    elif usernames == "":
        errorMessage = "Wprowadz poprawne dane"
        set_users_file()
    else:
        errorMessage = "Plik nie istnieje"
        set_users_file()

def choose_username():
    global errorMessage

    clearconsole()
    displaytext()

    print(colored("[1]", "yellow") + "\tPlik usernames")
    print(colored("[2]", "yellow") + "\tPojedynczy user")
    print(colored("[3]", "yellow") + "\tWroc do menu")

    set_method = int(input("Wybierz opcje: "))

    if set_method == 1:
        errorMessage = ""
        set_users_file()
    elif set_method == 2:
        errorMessage = ""
        set_username()
    elif set_method == 3:
        errorMessage = ""
        select_attack()
    else:
        errorMessage = "Niepoprawna opcja!"
        choose_username()

def select_attack():
    global errorMessage
    global target
    global dictionary
    global username
    global usernames

    clearconsole()
    displaytext()



    if target or dictionary or username or usernames:
        print(colored("---------------------------------------------------", "light_yellow"))
        if target:
            print(colored("IP: ", "yellow") + target)
        if dictionary:
            print(colored("Plik: ", "yellow") + dictionary)
        if username:
            print(colored("Username: ", "yellow") + username)
        if usernames:
            print(colored("Usernames: ", "yellow") + usernames)
        print(colored("---------------------------------------------------", "light_yellow"))


    if target == "" or dictionary == "":
        print(colored("[1]", "red") + "\tHTTP")
        print(colored("[2]", "red") + "\tSSH")
    else:
        print(colored("[1]", "light_green") + "\tHTTP")
        print(colored("[2]", "light_green") + "\tSSH")


    if target == "":
        print(colored("[3]", "yellow") + "\tIP celu" + "\t" + colored("[!]", "light_yellow"))
    else:
        print(colored("[3]", "green") + "\tIP celu")

    if dictionary == "":
        print(colored("[4]", "yellow") + "\tPlik z haslami" + "\t" + colored("[!]", "light_yellow"))
    else:
        print(colored("[4]", "green") + "\tPlik z haslami")

    if username == "" and usernames == "":
        print(colored("[5]", "yellow") + "\tUżytkownik" + "\t" + colored("[!]", "light_yellow"))
    else:
        print(colored("[5]", "green") + "\tUżytkownik")

    print(colored("[6]", "yellow") + "\tZakończ")

    set_attack = int(input("Wybierz opcje: "))

    if set_attack == 1:
        if target == "" or dictionary == "":
            errorMessage = "Uzupelnij dane!"
            select_attack()
        else:
            errorMessage = ""
            set_form_method()
    elif set_attack == 2:
        if target == "" or dictionary == "":
            errorMessage = "Uzupelnij dane!"
            select_attack()
        else:
            errorMessage = ""
    elif set_attack == 3:
        errorMessage = ""
        target_ip()
    elif set_attack == 4:
        errorMessage = ""
        dictionary_file()
    elif set_attack == 5:
        errorMessage = ""
        choose_username()
    elif set_attack == 6:
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