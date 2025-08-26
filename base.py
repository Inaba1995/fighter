from abc import ABC, abstractmethod


# Абстрактный класс оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def get_weapon_name(self):
        pass


# Конкретные реализации оружия
class Sword(Weapon):
    def attack(self):
        return "наносит мощный удар мечом"

    def get_weapon_name(self):
        return "меч"


class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"

    def get_weapon_name(self):
        return "лук"


class Axe(Weapon):
    def attack(self):
        return "размахивает топором"

    def get_weapon_name(self):
        return "топор"


# Класс бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.get_weapon_name()}")

    def attack_monster(self, monster):
        if self.weapon:
            attack_description = self.weapon.attack()
            print(f"{self.name} {attack_description}")
            monster.take_damage(10)  # Базовый урон
            if monster.is_defeated():
                print("Монстр побежден!")
            else:
                print("Монстр еще жив!")
        else:
            print(f"{self.name} не может атаковать без оружия!")


# Класс монстра
class Monster:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_defeated(self):
        return self.health <= 0


# Демонстрация работы
def main():
    # Создаем персонажей
    fighter = Fighter("Рыцарь Артур")
    monster = Monster("Злобный гоблин")

    # Бой с мечом
    fighter.change_weapon(Sword())
    fighter.attack_monster(monster)

    # Бой с луком
    fighter.change_weapon(Bow())
    fighter.attack_monster(monster)

    # Бой с топором
    fighter.change_weapon(Axe())
    fighter.attack_monster(monster)


if __name__ == "__main__":
    main()
