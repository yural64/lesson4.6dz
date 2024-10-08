# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями
# с различными характеристиками. Игра состоит из раундов, в каждом раунде игроки
# по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
#
# Требования:
# 1. Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# 2. Игра должна быть реализована как консольное приложение.
#
# Классы:
# Класс `Hero`:
# - Атрибуты:
# - Имя (`name`)
# - Здоровье (`health`), начальное значение 100
# - Сила удара (`attack_power`), начальное значение 20
#
# - Методы:
# - `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара
# - `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`
#
# Класс `Game`:
# - Атрибуты:
# - Игрок (`player`), экземпляр класса `Hero`
# - Компьютер (`computer`), экземпляр класса `Hero`
#
# - Методы:
# - `start()`: начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника)
# и объявляет победителя.
#
# Корректировка задания: сила удара при каждом ходе должна рандомно меняться от 0 до 20
# (герои устают, теряют силы, могут промахнуться).

import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
#        damage = self.attack_power
        damage = random.randint(0, 20)  # Случайная сила удара от 0 до 20
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")
        print(f"У {other.name} осталось {other.health} здоровья.\n")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!\n")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player_turn()

            # Проверяем, жив ли компьютер
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

            # Ход компьютера
            self.computer_turn()

            # Проверяем, жив ли игрок
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break

    def player_turn(self):
        input(f"\033[91m{self.player.name}, нажмите Enter для атаки.\033[0m") # использую ANSI код
        # для изменения цвета текста: \033[91m красный цвет, \033[0m сброс цвета
        print()
        self.player.attack(self.computer)

    def computer_turn(self):
        print(f"{self.computer.name} атакует!")
        print()
        self.computer.attack(self.player)


# Запуск игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()