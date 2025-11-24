import unittest

from themes import Duty_list
def testIt():
    #assert len(Duty_list)>10
    assert True is True
    

#test
class TestingDuties(unittest.TestCase):
    
    #check if theres 13 duties 
    def test_there_is_13_duties(self):
        self.assertEqual(len(Duty_list), 13)

if __name__ == "__main__":
    unittest.main()