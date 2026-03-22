class Pet:
    __name: str
    __animal_type: str
    __age: int
    __satiety_level: int
    __mood: int
    __health: int

    __SATIETY_MIN = 0
    __SATIETY_MAX = 100

    __MOOD_MIN = 0
    __MOOD_MAX = 100

    __HEALTH_MIN = 0
    __HEALTH_MAX = 100

    __SATIETY_DECREASE = 20
    __MOOD_DECREASE = 20
    __HEALTH_DECREASE = 20

    __HAPPY_REQUIREMENT = 50

    def __init__(self, name: str, animal_type: str, age: int) -> None:
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        self.__satiety_level = 100
        self.__mood = 100
        self.__health = 100

    def feed(self, food_amount: int) -> None:
        if food_amount > 0:
            self.__satiety_level += food_amount
            if self.__satiety_level > self.__SATIETY_MAX:
                self.__satiety_level = self.__SATIETY_MAX

    def play(self, fun_amount: int, satiety_cost: int) -> None:
        if satiety_cost > 0:
            self.__mood += fun_amount
            if self.__mood > self.__MOOD_MAX:
                self.__mood = self.__MOOD_MAX
            self.__satiety_level -= satiety_cost
            if self.__satiety_level < self.__MOOD_MIN:
                self.__satiety_level = self.__MOOD_MIN

    def heal(self, health_amount: int) -> None:
        if health_amount > 0:
            self.__health += health_amount
            if self.__health > self.__HEALTH_MAX:
                self.__health = self.__HEALTH_MAX

    def pass_time(self) -> None:
        self.__satiety_level -= self.__SATIETY_DECREASE
        self.__mood -= self.__MOOD_DECREASE
        if self.__satiety_level < self.__SATIETY_MIN:
            self.__satiety_level = self.__SATIETY_MIN
            self.__health -= self.__HEALTH_DECREASE
        if self.__health < self.__HEALTH_MIN:
            self.__health = self.__HEALTH_MIN
        if self.__mood < self.__MOOD_MIN:
            self.__mood = self.__MOOD_MIN

    def is_happy(self) -> bool:
        if self.__health >= self.__HAPPY_REQUIREMENT and self.__satiety_level >= self.__HAPPY_REQUIREMENT and self.__mood >= self.__HAPPY_REQUIREMENT/10:
            return True
        else:
            return False

    def get_status(self) -> str:
        return f"{self.__name} ({self.__animal_type}, {self.__age} лет): сытость {self.__satiety_level}, настроение {self.__mood}, здоровье {self.__health}"

    def get_name(self) -> str:
        return self.__name
