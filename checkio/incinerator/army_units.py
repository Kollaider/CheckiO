"""Army Units.

URL: https://py.checkio.org/en/mission/army-units/
DESCRIPTION:
        You are the developer of the new strategy game and you need to
    add the soldier creation process to it. Let's start with the 2
    types - AsianArmy and EuropeanArmy (each of them will be a subclass
    of the Army - class with the methods for the creation of soldiers).
    Also there will be 3 types of soldiers in the game - Swordsman,
    Lancer, and Archer (also the classes). Each army has unique names
    for those 3 types. For the EuropeanArmy there are: Knight (for
    Swordsman), Raubritter (for Lancer), and Ranger (for Archer). For
    the AsianArmy: Samurai (for Swordsman), Ronin (for Lancer), and
    Shinobi (for Archer).
        Each army can create all 3 types of the soldiers using the
    next methods:
        train_swordsman(name) - create an instance of the Swordsman.
        train_lancer(name) - create an instance of the Lancer.
        train_archer(name) - create an instance of the Archer.

        All 3 classes (Swordsman, Lancer, and Archer) should have
    the introduce() method, which returns the string that describes
    the soldiers in the following format:
        "'type' 'name', 'army type' 'specialization(basic class)'", for
    example:
        "Raubritter Harold, European lancer"
        "Shinobi Kirigae, Asian archer"

        In this mission you should use the Abstract Factory design pattern.
INPUT/OUTPUT EXAMPLE:
    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    soldier_1.introduce() == "Knight Jaks, European swordsman"
    soldier_2.introduce() == "Raubritter Harold, European lancer"
    soldier_3.introduce() == "Ranger Robin, European archer"

    soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    soldier_6.introduce() == "Shinobi Kirigae, Asian archer"
"""
from abc import ABC, abstractmethod


class Army(ABC):

    def __init__(self, continent):
        self.continent = continent

    @abstractmethod
    def train_swordsman(self, name):
        return Swordsman(name, self.continent)

    @abstractmethod
    def train_lancer(self, name):
        return Lancer(name, self.continent)

    @abstractmethod
    def train_archer(self, name):
        return Archer(name, self.continent)


class KindOfWarrior:

    def __init__(self, name, kind, continent, spec=None):
        self.name = name
        self.kind = kind
        self.continent = continent
        self.spec = spec

    def introduce(self):
        return f'{self.kind.title()} {self.name}, {self.continent} {self.spec}'


class Swordsman(KindOfWarrior):

    def __init__(self, name, kind, continent, spec='swordsman'):
        super().__init__(name, kind, continent, spec)


class Lancer(KindOfWarrior):

    def __init__(self, name, kind, continent, spec='lancer'):
        super().__init__(name, kind, continent, spec)


class Archer(KindOfWarrior):

    def __init__(self, name, kind, continent, spec='archer'):
        super().__init__(name, kind, continent, spec)


class AsianArmy(Army):

    def __init__(self, continent='Asian'):
        super().__init__(continent)

    def train_swordsman(self, name):
        return Swordsman(name, 'Samurai', self.continent)

    def train_lancer(self, name):
        return Lancer(name, 'Ronin', self.continent)

    def train_archer(self, name):
        return Archer(name, 'Shinobi', self.continent)


class EuropeanArmy(Army):

    def __init__(self, continent='European'):
        super().__init__(continent)

    def train_swordsman(self, name):
        return Swordsman(name, 'Knight', self.continent)

    def train_lancer(self, name):
        return Lancer(name, 'Raubritter', self.continent)

    def train_archer(self, name):
        return Archer(name, 'Ranger', self.continent)


def main():
    my_army = EuropeanArmy()
    soldier = my_army.train_swordsman('Jaks')

    print(f'soldier_1.introduce() == {soldier.introduce()}')


if __name__ == '__main__':
    main()
