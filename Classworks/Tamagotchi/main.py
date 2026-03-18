from tamagotchi_class import Tamagotchi
import console_services

tamagotchi_name = console_services.input_str("Введите имя своего Тамагочи:", 2, 30)
tamagotchi_type_animal = console_services.input_str("Введите тип своего Тамагочи:", 2, 30)
tamagotchi_age = console_services.input_str("Введите возраст своего Тамагочи:", 0, 1000)

is_running = True
current_day = 0

tamagotchi = Tamagotchi("Том", "кот", 2)
tamagotchi.print_status()

while is_running:
    console_services.clear_console()
    current_day += 1

    console_services.print_devider()

    print(f"{current_day} день")

    console_services.print_devider()

    tamagotchi.print_status()

    console_services.print_devider()

    print("Выберите действие")
    print("1 - Покормить")
    print("2 - Поиграть")
    print("3 - Уложить спать")

    action = console_services.input_int("Введите число от 1 до 3: ", 1, 3)

    if action == 1:
        tamagotchi.feed()
    elif action == 2:
        tamagotchi.play()
    elif action == 3:
        tamagotchi.sleep()

    tamagotchi.random_event()

    console_services.check_enter()