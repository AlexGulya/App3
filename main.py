import os
from person import Person
os.system('cls')

list = []


def info_list(list):
    for i in list:
        i.get_info()

def append_person(list):
    name = input("Name: ")
    age = int(input("age: "))
    list.append(Person(name,age))
    print("hfbjksdf")


while(True):
    os.system('cls')
    print("\t\t\t\tmeny\n1. Добавить\n2. Просмотр\n3. Выход")
    meny = int(input())
    if meny == 1:
        os.system('cls')
        append_person(list)
        input()
    elif meny == 2:
        os.system('cls')
        info_list(list)
        input()
    elif meny==3: break

