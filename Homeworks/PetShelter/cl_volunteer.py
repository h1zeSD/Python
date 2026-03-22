from cl_shelter import Shelter

class Volunteer:
    __name: str
    __actions_performed: int

    def __init__(self, name: str, actions_performed: int):
        self.__name = name
        self.__actions_performed = actions_performed

    def feed_pet(self, shelter: Shelter, name: str, food_amount: int) -> bool:
        try:
            shelter.feed_pet(name, food_amount)
            self.__actions_performed += 1
            return True
        except:
            return False

    def play_with_pet(self, shelter: Shelter, name: str, fun_amount: int, satiety_cost: int) -> bool:
        try:
            shelter.play_with_pet(name, fun_amount, satiety_cost)
            self.__actions_performed += 1
            return True
        except:
            return False

    def heal_pet(self, shelter: Shelter, name: str, health_amount: int) -> bool:
        try:
            shelter.heal_pet(name, health_amount)
            self.__actions_performed += 1
            return True
        except:
            return False

    def get_info(self) -> str:
        return f"Волонтёр {self.__name}. Выполнено действий: {self.__actions_performed}"
