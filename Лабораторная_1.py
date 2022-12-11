import doctest

class Family:
    def __init__(self, roles: str):
        """
        Создание и подготовка к работе объекта "Family"
        :param roles: роль в семье
        Примеры:
        >>> family = Family('wife') # инициализация экземпляра класса
        """
        self.names = None
        self.every_names()
        self.roles = None
        self.every_roles(roles)
        ...
    def every_names(self):
        """
        Функция, котоая выводит членов семьи
        :return: возвращает имена
        """
        self.names = "Roman"
        self.names = "Karina"
        ...
    def every_roles(self, roles):
        """
        Функция, котоая определяет роли членов семьи
        :param roles: роли
        :return: возвращает роли
        """
        if not isinstance(roles, str):
            raise TypeError("Роль может иметь только строковый тип")
        self.roles = roles
        ...

class Parrot:
    def __init__(self, food: str, words: int):
        """
        Создание и подготовка к работе объекта "Parrot"
        :param food: еда, которую ест попугай
        :param words: слова, которые говорит попугай
        """
        self.name = "Letun"
        self.weight = 0.3
        self.food = None
        self.init_food(food)
        self.words = None
        self.speak_words(words)
    def init_food(self,food: str):
        """
        Функция, которая выводит название еды попугай
        :param food: еда
        :return: еду
        """
        if not isinstance(food, str):
            raise TypeError("Еда может иметь только строковый тип")
        self.food = food
    def speak_words (self,words: int):
        """
        Функция, которая выводит количество слов, которые произносит попугай
        :param words: слова
        :return: слова
        """
        if not isinstance(words, int):
            raise TypeError("Слова могут иметь только целочисленный тип")
        self.words = words
        
if __name__ == "__main__":
    doctest.testmod()
    family = Family('husband') # не понимаю, как мне ввести и распределить роли
    print(family.names) # не знаю, как вывести, например, два имени
    print(family.roles)
    parrot = Parrot('семечки',20)
    print(parrot.name)
    print(parrot.food)
    print(parrot.words)
    pass
    # TODO работоспособность экземпляров класса проверить с помощью doctest