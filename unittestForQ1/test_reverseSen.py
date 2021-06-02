import unittest
import reverseSen


class TestCase(unittest.TestCase):

    def test_correctResult1(self):
        string1 = "string a is this" 
        self.assertEqual(reverseSen.reverseSentence("this is a string"),string1)

    def test_correctResult2(self):
        string2 = "William is name my"
        self.assertEqual(reverseSen.reverseSentence("my name is William"),string2)

    def test_correctResult3(self):
        string3 = "failed to reverse"
        self.assertEqual(reverseSen.reverseSentence("failed to reverse"),string3)

if __name__ == '__main__':
    unittest.main()
