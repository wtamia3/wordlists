import unittest
from utils import load_wordlist, suggest_corrections

class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.wordlist = {"apple", "banana", "orange", "grape"}

    def test_correct_spelling(self):
        self.assertIn("apple", self.wordlist)

    def test_suggest_corrections(self):
        self.assertEqual(suggest_corrections("bpple", self.wordlist), "apple")

    def test_no_suggestions(self):
        self.assertIsNone(suggest_corrections("aappple", self.wordlist))

if __name__ == "__main__":
    unittest.main()