import unittest
from qcm.question import Question

class TestQuestion(unittest.TestCase):
    def test_is_correct(self):
        question = Question("Quel est le plat national du sénégal ?", ["Thiéboudieune", "Mafé", "Athiéké"], "a")
        self.assertTrue(question.is_correct("a"))
        self.assertTrue(question.is_correct("A"))
        self.assertFalse(question.is_correct("b"))

if __name__ == "__main__":
    unittest.main()