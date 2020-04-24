from l2 import *
from unittest import TestCase


class TestL2(TestCase):
    def test_q1(self):
        self.assertEquals(q1(100), 95)
        self.assertEquals(q1(50), 47.5)

    def test_q2(self):
        self.assertEquals(q2(1000), 1150)
        self.assertEquals(q2(5000), 5750)

    def test_q3(self):
        self.assertEquals(q3(10), 50)
        self.assertEquals(q3(25), 77)
        self.assertEquals(q3(39), 102.2)

    def test_q4(self):
        self.assertEquals(q4(120, 1), 78)
        self.assertEquals(q4(240, 2), 156)
        self.assertEquals(q4(220, 1), 93)
        self.assertEquals(q4(440, 2), 186)
        self.assertEquals(q4(1500, 4), 465)

    def test_q5a(self):
        self.assertEquals(q5a1("Foo Fooo fo Fo"), "foo fooo fo fo")
        self.assertEquals(q5a2("Foo Fooo fo Fo"), "FOO FOOO FO FO")

    def test_q5b(self):
        self.assertEquals(q5b("Foo Fooo fo Fo"), 11)
        self.assertEquals(q5b("Fooo Fo Fo"), 8)

    def test_q5c(self):
        self.assertEquals(q5c("Foo Fooo fo Fo"), 3)
        self.assertEquals(q5c("Fooo Fo Fo"), 4)

    def test_q6(self):
        self.assertEquals(q6(1000), ["1", "0", "0", "0"])
        self.assertEquals(q6(101), ["1", "0", "1"])
        self.assertEquals(q6(99), ["9", "9"])
        self.assertEquals(q6(9), ["9"])

    def test_q8(self):
        self.assertEquals(q8(40), 0)
        self.assertEquals(q8(60), 0)
        self.assertEquals(q8(80), 0)
        self.assertEquals(q8(81), 7)
        self.assertEquals(q8(90), 70)
        self.assertEquals(q8(101), 147)
        self.assertEquals(q8(120), 280)

    def test_q9(self):
        self.assertEquals(q9(100), 50)
        self.assertEquals(q9(150), 75)
        self.assertEquals(q9(200), 100)
        self.assertEquals(q9(201), 90.45)
        self.assertEquals(q9(250), 112.5)
        self.assertEquals(q9(300), 135)

    def test_q10(self):
        self.assertEquals(q10(2015), False)
        self.assertEquals(q10(2016), True)

    def test_q11(self):
        self.assertEquals(q11(4, 2, 3), 4)
        self.assertEquals(q11(4, 5, 3), 5)
        self.assertEquals(q11(4, 5, 10), 10)

    def test_q12(self):
        self.assertEquals(q12(1000), 1150)
        self.assertEquals(q12(1250), 1437.5)
        self.assertEquals(q12(2000), 2200)

    def test_q12(self):
        self.assertEquals(q12(1000), 1150)
        self.assertEquals(q12(1250), 1437.5)
        self.assertEquals(q12(2000), 2200)

    def test_q13(self):
        self.assertEquals(q13(5, 2, 1), False)
        self.assertEquals(q13(5, 4, 3), True)
