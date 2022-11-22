import unittest
from coding_puzzles import message_decoder


class TestMessageDecoder(unittest.TestCase):

    def test_invalid_100(self):
        self.assertEqual(0, message_decoder.number_of_ways_to_decode("100"))

    def test_11106(self):
        self.assertEqual(2, message_decoder.number_of_ways_to_decode("11106"))

    def test_19173(self):
        self.assertEqual(4, message_decoder.number_of_ways_to_decode("19173"))

    def test_11(self):
        self.assertEqual(2, message_decoder.number_of_ways_to_decode("11"))

    def test_216(self):
        self.assertEqual(3, message_decoder.number_of_ways_to_decode("216"))

    def test_316(self):
        self.assertEqual(2, message_decoder.number_of_ways_to_decode("316"))

    def test_9999(self):
        self.assertEqual(1, message_decoder.number_of_ways_to_decode("9999"))

    def test_large(self):
        self.assertEqual(102334155, message_decoder.number_of_ways_to_decode("111111111111111111111111111111111111111"))


