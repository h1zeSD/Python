from classes import *
import os

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

warehouse = Warehouse()
GLOBAL_PRODUCT_CODE = 3
warehouse.add_product(Product("Молоко", 1, 1734, 79))
warehouse.add_product(Product("Хлеб", 2, 3951, 69))
# warehouse.print_all_products()

def print_main_screen():
    print("-"*120)
    print()
    print("Учёт товаров на складе")
    print()
    print("-"*120)
    print()
    print("1 - Вывод всех товаров")
    print("2 - Добавление товара на склад")
    print("3 - Удаление товара по коду")
    print("4 - Обновление количества товара на складе по коду")
    print("5 - Обновление цены товара по коду")
    print("6 - Выход из программы\n")

is_running = True

while is_running:
    clear_console()

    print_main_screen()
    user_choice = input_int(1, 6, "Выберите действие в программе (1-6): ")
    print()

    if user_choice == 1:
        clear_console()

        warehouse.print_all_products()
        input("\nЧтобы продолжить нажмите Enter: ")
    elif user_choice == 2:
        clear_console()

        print("Введите данные товара:\n")
        name = input("Название: ")
        quantity = input_int(1, 9999999, "Количество: ")
        price = input_int(1, 9999999, "Цена: ")
        warehouse.add_product(Product(name, GLOBAL_PRODUCT_CODE, quantity, price))
        GLOBAL_PRODUCT_CODE += 1
    elif user_choice == 3:
        clear_console()

        code = int(input("Введите код товара: "))
        warehouse.remove_product_by_code(code)
        input("\nЧтобы продолжить нажмите Enter: ")
    elif user_choice == 4:
        clear_console()

        code = int(input("Введите код товара: "))
        quantity = int(input("Введите количество: "))
        try:
            warehouse.get_product_by_code(code).update_price(quantity)
        except AttributeError:
            print("Ошибка. Товара с таким кодом не существует")

        input("\nЧтобы продолжить нажмите Enter: ")
    elif user_choice == 5:
        clear_console()

        code = int(input("Введите код товара: "))
        price = int(input("Введите цену: "))
        try:
            warehouse.get_product_by_code(code).update_price(price)
        except AttributeError:
            print("Ошибка. Товара с таким кодом не существует")

        input("\nЧтобы продолжить нажмите Enter: ")
    elif user_choice == 6:
        is_running = False