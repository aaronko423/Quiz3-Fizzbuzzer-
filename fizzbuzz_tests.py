from quiz3_Fizzbuzzer import Fizzbuzzer
from unittest import TestCase

class TestFizzBuzz(TestCase):

    def tearDown(self):
        pass
    
    def testDummy(self):
        pass
    
    def testFizzBuzzer(self):
        buzzer = Fizzbuzzer()
        self.assertEqual(buzzer.number, 0, "returns same value of 0")
        buzzer.next()
        self.assertEqual(buzzer.number, 1, "returns same value of 1")
        
    def testFizzBuzzer2(self):
        buzzeragain = Fizzbuzzer(2)
        next_num = buzzeragain.next()
        self.assertEqual(next_num, "fizz", "returns fizz")
        next_next_num = buzzeragain.next()
        self.assertEqual(next_next_num, 4, "returns same value of 4")
