import unittest

from themes import x2
def testIt():
    #assert len(x2)>10
    assert True is True
    

#test
class TestingDuties(unittest.TestCase):
    def test_duty_numbers(self):
        self.assertEqual(len(x2), 13)

if __name__ == "__main__":
    unittest.main()