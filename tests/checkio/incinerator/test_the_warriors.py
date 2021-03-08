from unittest import TestCase

from checkio.incinerator import the_warriors

chuck = the_warriors.Warrior()
bruce = the_warriors.Warrior()
carl = the_warriors.Knight()
dave = the_warriors.Warrior()
mark = the_warriors.Warrior()


class TheWarriorsTestCase(TestCase):

    def test__unix_max_part_one__valid_result(self):
        self.assertEqual(True, the_warriors.fight(chuck, bruce))
        self.assertEqual(False, the_warriors.fight(dave, carl))
        self.assertEqual(True, chuck.is_alive)
        self.assertEqual(False, bruce.is_alive)
        self.assertEqual(True, carl.is_alive)
        self.assertEqual(False, dave.is_alive)
        self.assertEqual(False, the_warriors.fight(carl, mark))
        self.assertEqual(False, carl.is_alive)
