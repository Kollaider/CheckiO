"""The Warriors.

URL: https://py.checkio.org/en/mission/the-warriors/
DESCRIPTION:
    You need to create the class Warrior , the instances of which will
    have 2 parameters - health (equal to 50 points) and attack (equal
    to 5 points), and 1 property - is_alive, which can be True (if
    warrior's health is > 0) or False (in the other case). In addition
    you have to create the second unit type - Knight, which should be the
    subclass of the Warrior but have the increased attack - 7. Also you have
    to create a function fight() , which will initiate the duel between 2
    warriors and define the strongest of them. The duel occurs according
    to the following principle:
    Every turn, the first warrior will hit the second and this second
    will lose his health in the same value as the attack of the first warrior.
    After that, if he is still alive, the second warrior will do the same
    to the first one.
    The fight ends with the death of one of them. If the first warrior
    is still alive (and thus the other one is not anymore), the function
    should return True , False otherwise.
INPUT/OUTPUT EXAMPLE:
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()

    fight(chuck, bruce) == True
    fight(dave, carl) == False
    chuck.is_alive == True
    bruce.is_alive == False
    carl.is_alive == True
    dave.is_alive == False
"""


class Warrior:

    def __init__(self, health=50, attack=5):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    unit_2.health -= unit_1.attack
    if not unit_2.is_alive:
        return True
    unit_1.health -= unit_2.attack
    if not unit_1.is_alive:
        return False
    return fight(unit_1, unit_2)


def main():
    carl = Knight()
    dave = Warrior()
    print(f'fight(dave, carl) == {fight(dave, carl)}')


if __name__ == '__main__':
    main()
