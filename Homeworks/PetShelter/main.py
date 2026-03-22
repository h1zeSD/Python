import console_service
from cl_pet import Pet
from cl_shelter import Shelter
from cl_volunteer import Volunteer

is_running = True

shelter_title = console_service.input_str("Введите название приюта: ", 2, 30)
volunteer_name = console_service.input_str("Введите имя волонтёра: ", 2, 30)

shelter = Shelter(shelter_title, [Pet("Том", "Кот", 7), Pet("Бобик", "Собака", 11)])
volunteer = Volunteer(volunteer_name, 0)

while is_running:
    console_service.print_devider()
    print(f"Приют для животных {shelter.get_title()}")
    console_service.print_devider()
    print("1 — Показать всех животных")
    print("2 — Добавить животное")
    print("3 — Покормить животное")
    print("4 — Поиграть с животным")
    print("5 — Полечить животное")
    print("6 — Пропустить время")
    print("7 — Показать состояние волонтёра")
    print("8 — Выход")
    console_service.print_devider()

    user_choice = console_service.input_int("Выберите действие в программе(1-8): ", 1, 8)

    if user_choice == 1:
        console_service.clear_console()
        pets = shelter.show_all_pets()
        console_service.print_devider()
        for pet in pets:
            print(pet)
        console_service.check_enter()
    elif user_choice == 2:
        console_service.clear_console()
        name = console_service.input_str("Введите кличку животного: ", 2, 30)
        animal_type = console_service.input_str("Введите тип животного: ", 2, 30)
        age = console_service.input_int("Введите возраст животного: ", 0, 1000)
        shelter.add_pet(Pet(name, animal_type, age))
        console_service.check_enter()
    elif user_choice == 3:
        console_service.clear_console()
        name = console_service.input_str("Введите имя животного: ", 2, 30)
        food_amount = console_service.input_int("Введите количество еды: ", 1, 100)
        volunteer.feed_pet(shelter, name, food_amount)
        console_service.check_enter()
    elif user_choice == 4:
        console_service.clear_console()
        name = console_service.input_str("Введите имя животного: ", 2, 30)
        fun_amount = console_service.input_int("Введите количество веселья: ", 1, 100)
        satiety_cost = console_service.input_int("Введите количество затрат сытости: ", 1, 100)
        volunteer.play_with_pet(shelter, name, fun_amount, satiety_cost)
        console_service.check_enter()
    elif user_choice == 5:
        console_service.clear_console()
        name = console_service.input_str("Введите имя животного: ", 2, 30)
        health_amount = console_service.input_int("Введите количество здоровья: ", 1, 100)
        volunteer.heal_pet(shelter, name, health_amount)
        console_service.check_enter()
    elif user_choice == 6:
        console_service.clear_console()
        shelter.pass_time_for_all()
        console_service.check_enter()
    elif user_choice == 7:
        console_service.clear_console()
        print(volunteer.get_info())
        console_service.check_enter()
    elif user_choice == 8:
        is_running = False
