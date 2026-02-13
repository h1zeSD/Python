import os
import time
from dataclasses import dataclass

@dataclass
class GamingComputer:
    id: int
    fabricator: str
    processor: str
    VRAM: int
    RAM: int
    SSD: int
    weight: int
    price: int
    amount: int
    is_on_sellout: bool

GLOBAL_GAMING_COMPUTER_ID = 0

def clear_console():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


def input_int(min_num, max_num, message):
    is_correct_input = False

    while not is_correct_input:
        try:
            input_data = int(input(f"{message}"))
            if input_data > max_num or input_data < min_num:
                print(f"Ошибка: Введите значение от {min_num} до {max_num}")
                is_correct_input = False
            else: 
                is_correct_input = True
        except:
            print(f"Ошибка: Вы ввели не число")
            is_correct_input = False

    return input_data


def input_str(max_sym, message):
    is_correct_input = False

    while not is_correct_input:
        try:
            input_data = input(f"{message}")
            if len(input_data) > max_sym:
                print(f"Ошибка: Введите меньше {max_sym} символов")
                is_correct_input = False
            else: 
                is_correct_input = True
        except:
            print(f"Ошибка: Вы ввели не строку")
            is_correct_input = False

    return input_data
    

def print_computer_information(computer, message):
    print("-"*120)
    print(message)
    print("-"*120)
    print(
        f"ИД: {computer.id}\nПроизводитель: {computer.fabricator}\nПроцессор: {computer.processor}\nОбъём видеопамяти: {computer.VRAM} ГБ\nОЗУ (ГБ): {computer.RAM} ГБ\nОбъём SSD (ГБ): {computer.SSD} ГБ\nВес (КГ): {computer.weight} КГ\nЦена: {computer.price} рублей\nКоличество на складе: {computer.amount}"
    )
    print("-"*120)


def search_computers(computers):
    print("test")


def sort_computers(computers):
    sort_variant = input_int(1,2, "Выберите способ сортировки(1 - по цене, 2 - по сумме ОЗУ и SSD): ")
    if sort_variant == 1:
        for i in range(len(computers)):
            for j in range(len(computers) - 1):
                if computers[j].price > computers[j+1].price:
                    computers[j], computers[j+1] = computers[j+1], computers[j]
        print("\nКомпьютеры были успешно отсортированы по цене")
    elif sort_variant == 2:
        for i in range(len(computers)):
            for j in range(len(computers) - 1):
                if computers[j].RAM + computers[j].SSD > computers[j+1].RAM + computers[j+1].SSD:
                    computers[j], computers[j+1] = computers[j+1], computers[j]
        print("\nКомпьютеры были успешно отсортированы по сумме ОЗУ + SSD")


def input_computer_data():
    print("Введите данные компьютера\n")

    fabricator = input_str(15, "Производитель: ")
    processor = input_str(20, "Процессор: ")
    VRAM = input_int(0, 999, "Объём видеопамяти (ГБ): ")
    RAM = input_int(0, 999, "ОЗУ (ГБ): ")
    SSD = input_int(0, 999999,"Объём SSD (ГБ): ")
    weight = input_int(0, 99999,"Вес (КГ): ")
    price = input_int(0, 999999999,"Цена: ")
    amount = input_int(0, 999999999,"Количество на складе: ")

    return GamingComputer(
        0, fabricator, processor, VRAM, RAM, SSD, weight, price, amount, False
    )


def add_computer_to_list(computers):
    global GLOBAL_GAMING_COMPUTER_ID
    GLOBAL_GAMING_COMPUTER_ID += 1

    computer = input_computer_data()
    computer.id = GLOBAL_GAMING_COMPUTER_ID

    computers.append(computer)
    print(f"\nУспешно добавлен новый компьютер, которому было присвоено ИД {computer.id}")


def delete_computer(computers):
    computer_id = input_int(1, 99999, "Введите ИД компютера, который вы хотите удалить: ")
    computers.pop([computer_id - 1])
    print(f"\nКомпьютер с ИД {computer_id} был успешно удалён")


def increase_ram(computers):
    computer_id = input_int(0, 99999999999, "Введите ИД компьютера, которому вы хотите увеличить ОЗУ: ")
    computer = computers[computer.id - 1]

    ram = input_int(0, 99999999, "Введите на сколько вы хотите увеличить ОЗУ (ГБ) этому компьютеру: ")

    computer.RAM += ram
    print(f"\nУ компьютера с ИД {computer_id} успешно увеличено ОЗУ (ГБ) с {computer.RAM - ram} ГБ на {computer.RAM} ГБ")


def set_sellout(computers):
    input_int(1, 999, "test")
    print("test")

def print_most_expensive_and_cheapest(computers):
    cheapest_computer = computers[0]
    for i in range(len(computers)):
            for j in range(len(computers) - 1):
                if cheapest_computer.price > computers[j+1].price:
                    cheapest_computer = computers[j+1]

    most_expensive_computer = computers[0]
    for i in range(len(computers)):
            for j in range(len(computers) - 1):
                if most_expensive_computer.price < computers[j+1].price:
                    most_expensive_computer = computers[j+1]
    
    print_computer_information(cheapest_computer, "Самый дешёвый компьютер:")
    print_computer_information(most_expensive_computer, "Самый дорогой компьютер:")


def name():
    print("test")


def print_main_screen():
    print("-"*120)
    print("\nБухгалтерская программа\n")
    print("1 — Поиск компьютеров по нескольким условиям одновременно (например: ОЗУ ≥ 16 и Цена ≤ 150000)")
    print("2 — Сортировка компьютеров по цене или по сумме ОЗУ и SSD")
    print("3 — Добавление нового компьютера")
    print("4 — Удаление компьютера по ИД")
    print("5 — Увеличение объёма ОЗУ у компьютера по ИД")
    print("6 — Пометить компьютер как «распродажа» → автоматически уменьшить цену на 10%")
    print("7 — Вывести самый дорогой и самый дешёвый компьютер")
    print("8 — Вывести компьютеры с видеокартой не слабее указанной")
    print("9 — Выйти из программы\n")
    

def main():

    clear_console()
    print_main_screen()
    user_choice = input_int(1,9, "Выберите действие в программе (1-9): ")

    clear_console()

    print("-"*120)
    print("\n")

    if user_choice == 1:
        search_computers(computers)
        time.sleep(3)
        main()
    elif user_choice == 2:
        sort_computers(computers)
        time.sleep(3)
        main()
    elif user_choice == 3:
        add_computer_to_list(computers)
        time.sleep(3)
        main()
    elif user_choice == 4:
        delete_computer(computers)
        time.sleep(3)
        main()
    elif user_choice == 5:
        increase_ram(computers)
        time.sleep(3)
        main()
    elif user_choice == 6:
        set_sellout(computers)
        time.sleep(3)
        main()
    elif user_choice == 7:
        print_most_expensive_and_cheapest(computers)
        time.sleep(10)
        main()
    elif user_choice == 8:
        name()
        time.sleep(10)
        main()
    elif user_choice == 9:
        quit()


computers = [GamingComputer(1,"22","22",99,22,33,2,999,2,False), GamingComputer(2,"22","22",200,300,999,999,9999,5,False), GamingComputer(1,"22","22",99,22,33,2,999,2,False)] 

main()
