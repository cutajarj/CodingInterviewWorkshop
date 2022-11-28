import unittest
from coding_puzzles import secret_santa


class TestSecretSanta(unittest.TestCase):
    def test_two_names(self):
        result = secret_santa.gift_paring(["James", "Ruth"])
        self.assertEqual(2, len(result))
        for t in result:
            self.assertNotEqual(t[0], t[1])

    def test_two_names_repeat(self):
        for i in range(1000):
            result = secret_santa.gift_paring(["James", "Ruth"])
            self.assertEqual(2, len(result))
            for t in result:
                self.assertNotEqual(t[0], t[1])

    def test_four_names(self):
        result = secret_santa.gift_paring(["James", "Ruth", "Isabel", "Michelle"])
        self.assertEqual(4, len(result))
        for t in result:
            self.assertNotEqual(t[0], t[1])

    def test_unique_givers_takers(self):
        result = secret_santa.gift_paring(["James", "Ruth", "Isabel", "Michelle", "Luis", "Oliver"])
        self.assertEqual(6, len(result))
        givers = set()
        takers = set()
        for t in result:
            givers.add(t[0])
            takers.add(t[1])
        self.assertEqual(6, len(givers))
        self.assertEqual(6, len(takers))
        self.assertEqual(givers, takers)

