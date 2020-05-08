from av1 import *
from unittest import TestCase, main


class TestL1(TestCase):

    def test_q1(self):
        self.assertEquals(q1(6), 'Número 6, sucessor 7, antecessor 5')
