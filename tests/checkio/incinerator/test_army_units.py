from unittest import TestCase

from checkio.incinerator import army_units

my_army = army_units.EuropeanArmy()
enemy_army = army_units.AsianArmy()

soldier_1 = my_army.train_swordsman('Jaks')

soldier_2 = my_army.train_lancer('Harold')
soldier_3 = my_army.train_archer('Robin')

soldier_4 = enemy_army.train_swordsman('Kishimoto')
soldier_5 = enemy_army.train_lancer('Ayabusa')
soldier_6 = enemy_army.train_archer('Kirigae')


class ArmyUnitsTestCase(TestCase):

    def test__army_units__valid_result(self):
        self.assertEqual(
            'Knight Jaks, European swordsman', soldier_1.introduce())
        self.assertEqual(
            'Raubritter Harold, European lancer', soldier_2.introduce())
        self.assertEqual(
            'Ranger Robin, European archer', soldier_3.introduce())
        self.assertEqual(
            'Samurai Kishimoto, Asian swordsman', soldier_4.introduce())
        self.assertEqual(
            'Ronin Ayabusa, Asian lancer', soldier_5.introduce())
        self.assertEqual(
            'Shinobi Kirigae, Asian archer', soldier_6.introduce())
