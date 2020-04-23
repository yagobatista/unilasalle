from l1 import q1, q2, q3, q4, q5, q6
from unittest import TestCase, main


class TestL1(TestCase):

    def test_q1(self):
        self.assertEquals(q1(6), 'Número 6, sucessor 7, antecessor 5')

    def test_q2(self):
        self.assertEquals(
            q2(4), 'Número 4, dobro 8, triplo 12, raiz quadrada 2.0')

    def test_q3(self):
        self.assertEquals(
            q3(1.5), 'Metros 1.5, centimetros 150.0, milimetros 1500.0')

    def test_q4(self):
        self.assertEquals(
            q4(16),
            '16 x 1 = 16\n16 x 2 = 32\n16 x 3 = 48\n16 x 4 = 64\n16 x 5 = 80\n16 x 6 = 96\n16 x 7 = 112\n16 x 8 = 128\n16 x 9 = 144',
        )

    def test_q5(self):
        self.assertEquals(
            q5(150.86),
            'Dinheiro em real 150.86, em dólares 35.91904761904762',
        )

    def test_q6(self):
        self.assertEquals(
            q6(20, 10),
            'Área 200 m², quantidade de tinta necessária 100.0 L',
        )


if __name__ == '__main__':
    main()
