import numpy as np
from tkinter import *

LICZBA_WIERSZY = 6
LICZBA_KOLUMN = 7


class cztery_w_rzedzie:
    def __init__(self):
        self.wiersze = 6
        self.kolumny = 7
        self.plansza = np.zeros((LICZBA_WIERSZY, LICZBA_KOLUMN))

    def wrzuc_monete(self, wiersz1, kolumna1, gracz):
        self.plansza[wiersz1][kolumna1] = gracz

    def zapelniona_kolumna(self, kolumna1):
        return self.plansza[LICZBA_WIERSZY - 1][kolumna1] == 0

    def wolny_wiersz(self, kolumna1):
        for i in range(LICZBA_WIERSZY):
            if self.plansza[i][kolumna1] == 0:
                return i

    def wyswietl_plansze(self):
        print(np.flip(self.plansza, 0))

    def wygrany_ruch(self, gracz):
        # poziome pozycje
        for kol in range(LICZBA_KOLUMN - 3):
            for wier in range(LICZBA_WIERSZY):
                if self.plansza[wier][kol] == gracz and self.plansza[wier][kol + 1] == gracz and self.plansza[wier][
                    kol + 2] == gracz and self.plansza[wier][kol + 3] == gracz:
                    return True

        # pionowe pozycje
        for kol in range(LICZBA_KOLUMN):
            for wier in range(LICZBA_WIERSZY - 3):
                if self.plansza[wier][kol] == gracz and self.plansza[wier + 1][kol] == gracz and self.plansza[wier + 2][
                    kol] == gracz and self.plansza[wier + 3][kol] == gracz:
                    return True

        # pozycje ukośna
        for kol in range(LICZBA_KOLUMN - 3):
            for wier in range(LICZBA_WIERSZY - 3):
                if self.plansza[wier][kol] == gracz and self.plansza[wier + 1][kol + 1] == gracz and \
                        self.plansza[wier + 2][kol + 2] == gracz and self.plansza[wier + 3][kol + 3] == gracz:
                    return True
        for kol in range(LICZBA_KOLUMN - 3):
            for wier in range(3, LICZBA_WIERSZY):
                if self.plansza[wier][kol] == gracz and self.plansza[wier - 1][kol + 1] == gracz and \
                        self.plansza[wier - 2][kol + 2] == gracz and self.plansza[wier - 3][kol + 3] == gracz:
                    return True


gra = cztery_w_rzedzie()
koniec_gry = False
tura = 0

while not koniec_gry:
    if tura == 0:
        kolumna = int(input("Tura gracza 1 (0-6): "))

        if gra.zapelniona_kolumna(kolumna):
            wiersz = gra.wolny_wiersz(kolumna)
            gra.wrzuc_monete(wiersz, kolumna, 1)

            if gra.wygrany_ruch(1):
                print("Gracz 1 wygrywa")
                koniec_gry = True

    else:
        kolumna = int(input("Tura gracza 2 (0-6): "))
        if gra.zapelniona_kolumna(kolumna):
            wiersz = gra.wolny_wiersz(kolumna)
            gra.wrzuc_monete(wiersz, kolumna, 2)

            if gra.wygrany_ruch(2):
                print("Gracz 2 wygrywa")
                koniec_gry = True

    gra.wyswietl_plansze()
    tura += 1
    tura = tura % 2
