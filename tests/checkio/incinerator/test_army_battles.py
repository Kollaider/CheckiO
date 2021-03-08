from unittest import TestCase

from checkio.incinerator import army_battles

chuck = army_battles.Warrior()
bruce = army_battles.Warrior()
carl = army_battles.Knight()
dave = army_battles.Warrior()
mark = army_battles.Warrior()


class TheWarriorsTestCase(TestCase):

    def test__the_warriors__valid_result(self):
        self.assertEqual(True, army_battles.fight(chuck, bruce))
        self.assertEqual(False, army_battles.fight(dave, carl))
        self.assertEqual(True, chuck.is_alive)
        self.assertEqual(False, bruce.is_alive)
        self.assertEqual(True, carl.is_alive)
        self.assertEqual(False, dave.is_alive)
        self.assertEqual(False, army_battles.fight(carl, mark))
        self.assertEqual(False, carl.is_alive)


my_army = army_battles.Army()
my_army.add_units(army_battles.Knight, 3)

enemy_army = army_battles.Army()
enemy_army.add_units(army_battles.Warrior, 3)

army_3 = army_battles.Army()
army_3.add_units(army_battles.Warrior, 20)
army_3.add_units(army_battles.Knight, 5)

army_4 = army_battles.Army()
army_4.add_units(army_battles.Warrior, 30)

battle = army_battles.Battle()


class ArmyBattlesTestCase(TestCase):

    def test_army_battles__valid_result(self):
        self.assertEqual(True, battle.fight(my_army, enemy_army))
        self.assertEqual(False, battle.fight(army_3, army_4))
