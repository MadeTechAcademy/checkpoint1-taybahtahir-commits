import unittest

from themes import Duty_list
def testIt():
    #assert len(Duty_list)>10
    assert True is True
    

#test
class TestingDuties(unittest.TestCase):
    
    def test_there_is_13_duties(self):
        self.assertEqual(len(Duty_list), 13)
        
    def test_if_all_duties_end_with_a_fullstop(self):
        for duty in Duty_list:
            self.assertTrue(duty.endswith("."))

if __name__ == "__main__":
    unittest.main()