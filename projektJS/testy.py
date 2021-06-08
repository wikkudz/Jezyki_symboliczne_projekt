import random
import logika
import unittest


class testyDoProjektu(unittest.TestCase):

    def test_wrzucania_monet(self):
        # given
        gracz1 = 1
        gracz2 = 2
        gra = logika.cztery_w_rzedzie()

        # when
        for i in range(2):
            gra.wrzuc_monete(i, gracz1)
            gra.wrzuc_monete(i, gracz2)

        wynik = (gra.plansza[0][0] == 1
                        and gra.plansza[0][1] == 1
                        and gra.plansza[1][0] == 2
                        and gra.plansza[1][1] == 2)

        # then
        self.assertTrue(wynik)

    def test_wygrana_pion(self):
        # given
        gracz = 1
        kolumna = random.randint(0, 6)
        gra = logika.cztery_w_rzedzie()

        # when
        for i in range(4):
            gra.wrzuc_monete(kolumna, gracz)
        wynik = gra.czyWygral(gracz)

        # then
        self.assertTrue(wynik)

    def test_wygrana_poziom(self):
        # given
        gracz = 2
        gra = logika.cztery_w_rzedzie()

        # when
        for i in range(4):
            gra.wrzuc_monete(i, gracz)

        wynik = gra.czyWygral(gracz)

        # then
        self.assertTrue(wynik)

    def test_wygrana_skos(self):
        # given
        gracz1 = 1
        gracz2 = 2
        gra = logika.cztery_w_rzedzie()

        # when
        for i in range(1, 4):
            for j in range(i, 4):
                gra.wrzuc_monete(j, gracz1)

        for i in range(4):
            gra.wrzuc_monete(i, gracz2)

            # plansza
            # [[0. 0. 0. 0. 0. 0. 0.]
            #  [0. 0. 0. 0. 0. 0. 0.]
            #  [0. 0. 0. 2. 0. 0. 0.]
            #  [0. 0. 2. 1. 0. 0. 0.]
            #  [0. 2. 1. 1. 0. 0. 0.]
            #  [2. 1. 1. 1. 0. 0. 0.]]

        wynik = gra.czyWygral(gracz2)

        # then
        self.assertTrue(wynik)

    def test_zapelniona_plansza(self):
        # given
        gra = logika.cztery_w_rzedzie()
        gracz1 = 1
        gracz2 = 2

        # when
        for i in [0, 2, 4]:
            for j in range(3):
                gra.wrzuc_monete(i, gracz1)
            for k in range(3):
                gra.wrzuc_monete(i, gracz2)

        for i in [1, 3, 5]:
            for j in range(3):
                gra.wrzuc_monete(i, gracz2)
            for k in range(3):
                gra.wrzuc_monete(i, gracz1)

        for i in range(3):
            gra.wrzuc_monete(6, gracz1)
            gra.wrzuc_monete(6, gracz2)

        # plansza
        #  [[2, 1, 2, 1, 2, 1, 1],
        #   [2, 1, 2, 1, 2, 1, 2],
        #   [2, 1, 2, 1, 2, 1, 1],
        #   [1, 2, 1, 2, 1, 2, 2],
        #   [1, 2, 1, 2, 1, 2, 1],
        #   [1, 2, 1, 2, 1, 2, 2]]

        # then
        wynik = gra.zapelniona_plansza()
        self.assertTrue(wynik)

    def test_wygrana_wiecej_niz_4_w_rzedzie(self):
        # given
        gracz1 = 1
        gracz2 = 2
        gra = logika.cztery_w_rzedzie()

        # when
        for i in range(3):
            gra.wrzuc_monete(i, gracz2)
            gra.wrzuc_monete(i, gracz1)

        for i in range(4,7):
            gra.wrzuc_monete(i, gracz2)
            gra.wrzuc_monete(i, gracz1)

        gra.wrzuc_monete(3, gracz2)
        gra.wyswietl_plansze()
        wynik = gra.czyWygral(gracz2)

        # then
        self.assertTrue(wynik)

    def test_zapelniona_kolumna(self):
        # given
        gracz = random.randint(1, 2)
        kolumna = random.randint(0, 6)
        gra = logika.cztery_w_rzedzie()

        # when
        for i in range(6):
            gra.wrzuc_monete(kolumna, gracz)

        wynik = gra.wrzuc_monete(kolumna, gracz)

        self.assertFalse(wynik)





