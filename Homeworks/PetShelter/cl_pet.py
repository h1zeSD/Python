class Pet:
    __nickname: str
    __animal_type: str
    __age: int
    __satiety_level: int
    __mood: int
    __health: int

    __SATIETY_MIN = 0
    __SATIETY_MAX = 100

    __MOOD_MIN = 0
    __MOOD_MAX = 5

    __HEALTH_MIN = 0
    __HEALTH_MAX = 100

    __MIN_DECREASE = 1
    __MAX_DECREASE = 40

    def __init__(self, nickname: str, animal_type: str, age: int, satiety_level: int, mood: int, health: int) -> None:
        self.__nickname = nickname
        self.__animal_type = animal_type
        self.__age = age
        self.__satiety_level = satiety_level
        self.__mood = mood
        self.__health = health

    def feed(self, food_amount: int) -> None:
        if food_amount > 0:
            self.__satiety_level += food_amount
            if self.__satiety_level > self.__SATIETY_MAX:
                self.__satiety_level = self.__SATIETY_MAX

    def play(self, fun_amount: int, satiety_cost: int) -> None:
        if satiety_cost < 0:
            self.__mood += fun_amount
            if self.__mood > self.__MOOD_MAX:
                self.__mood = self.__MOOD_MAX
            self.__satiety_level -= satiety_cost
            if self.__satiety_level < self.__MOOD_MIN:
                self.__satiety_level = self.__MOOD_MIN

    def heal(self, health_amount: int) -> None:
        if health_amount < 0:
            self.__health += health_amount
            if self.__health > self.__HEALTH_MAX:
                self.__health = self.__HEALTH_MAX