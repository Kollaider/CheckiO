"""Army battles. Part II from the series: The Warriors.

URL: https://py.checkio.org/en/mission/army-battles/
DESCRIPTION:
    In this mission your task is to add new classes and functions
    to the existing ones. The new class should be the Army and have
    the method add_units() - for adding the chosen amount of units
    to the army. The first unit added will be the first to go to
    fight, the second will be the second, ...
    Also you need to create a Battle() class with a fight() function,
    which will determine the strongest army.
    The battles occur according to the following principles:
    at first, there is a duel between the first warrior of the first
    army and the first warrior of the second army. As soon as one of
    them dies - the next warrior from the army that lost the fighter
    enters the duel, and the surviving warrior continues to fight with
    his current health. This continues until all the soldiers of one
    of the armies die. In this case, the fight() function should return
    True , if the first army won, or False , if the second one was stronger.
    Note that army 1 have the advantage to start every fight!
INPUT/OUTPUT EXAMPLE:
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    battle.fight(my_army, enemy_army) == True
    battle.fight(army_3, army_4) == False
"""


class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


class Army:

    def __init__(self):
        self.units = []

    def add_units(self, unit, amount):
        self.units.extend(unit() for i in range(amount))


class Battle:

    def fight(self, army1, army2):
        while len(army1.units) > 0 and len(army2.units) > 0:
            if fight(army1.units[0], army2.units[0]):
                army2.units.pop(0)
            else:
                army1.units.pop(0)
        return len(army1.units) > 0


def fight(unit_1, unit_2):
    unit_2.health -= unit_1.attack
    if not unit_2.is_alive:
        return True
    unit_1.health -= unit_2.attack
    if not unit_1.is_alive:
        return False
    return fight(unit_1, unit_2)


def main():
    my_army = Army()
    my_army.add_units(Knight, 3)
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)
    battle = Battle()
    print(
        f'assert battle.fight(my_army, enemy_army) == '
        f'{battle.fight(my_army, enemy_army)}')


if __name__ == '__main__':
    main()
