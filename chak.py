class Character:
    def __init__(self, health):
        self.__health = health  # приватный атрибут

    def get_health(self):
        return self.__health

    def set_health(self, value):
        self.__health = value

    def perform_action(self):
        print("Персонаж что-то делает")


class Warrior(Character):
    def perform_action(self):
        print("Воин наносит удар мечом!")


class Mage(Character):
    def perform_action(self):
        print("Маг использует заклинание!")


class Healer(Character):
    def perform_action(self):
        print("Лекарь восстанавливает здоровье!")


# Проверка
characters = [
    Warrior(100),
    Mage(80),
    Healer(90)
]

for c in characters:
    c.perform_action()
