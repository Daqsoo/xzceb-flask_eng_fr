import unittest
from translator import englishToFrench
from translator import frenchToEnglish
class TestFrtoEng (unittest.TestCase):
    def test1(self):
        message = "You should input smth"
        self.assertEqual(None,message)
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')
class TestEngtoFr (unittest.TestCase):
    def test2(self):
        message = "You should input smth"
        self.assertEqual(None,message)
        self.assertEqual(englishtoFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')
if __name__ =='__main__':
    unittest.main()