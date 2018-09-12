import unittest

from festival_mames_methods import create_festival_list

class test_word_counter(unittest.TestCase):

    def test_word_count(self):
        self.assertEqual(word_count('./tests/word_count.txt'),8)

    def test_remove_punctuation_and_split(self):
        self.assertEqual(remove_punctuation_and_split("Hello, I'm a string!"),["Hello", "Im", 'a', 'string'])

    def test_most_common_words(self):
        self.assertEqual(ten_most_common_words('./tests/most_common_words.txt'),[('barcelonafc', 10), ('Raptors', 8), ('Torontofc', 6), ('Leafs', 4),('Argonauts', 2)])





if __name__ == '__main__':
    unittest.main()
