from cl_pet import Pet

class Shelter:
    __title: str
    __pets_list: list[Pet]

    def __init__(self, title: str, pet_list: list[Pet]) -> None:
        self.__title = title
        self.__pets_list = pet_list

    def add_pet(self, pet: Pet) -> None:
        self.__pets_list.append(pet)

    def show_all_pets(self) -> list[str]:
        pets = []
        for pet in self.__pets_list:
            pets.append(pet.get_status())
        return pets

    def find_pet_by_name(self, name: str) -> Pet | None:
        return [pet for pet in self.__pets_list if pet.get_name().lower() == name.lower()][0]
        is_found = False
        pet = None
        for pet in self.__pets_list:
            if is_found:
                break
            if pet.get_name().lower() == name.lower():
                pet = pet
                is_found = True
        if is_found:
            return pet
        else:
            return None

    def feed_pet(self, name: str, food_amount: int) -> bool:
        pet = self.find_pet_by_name(name)
        try:
            pet.feed(food_amount)
            return True
        except:
            return False

    def play_with_pet(self, name: str, fun_amount: int, satiety_cost: int) -> bool:
        pet = self.find_pet_by_name(name)
        try:
            pet.play(fun_amount, satiety_cost)
            return True
        except:
            return False

    def heal_pet(self, name: str, health_amount: int) -> bool:
        pet = self.find_pet_by_name(name)
        try:
            pet.heal(health_amount)
            return True
        except:
            return False

    def pass_time_for_all(self) -> None:
        for pet in self.__pets_list:
            pet.pass_time()

    def get_title(self) -> str:
        return self.__title
