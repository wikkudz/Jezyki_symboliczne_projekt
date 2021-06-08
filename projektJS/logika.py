import numpy as np

# ROZMIARY
LICZBA_WIERSZY = 6
LICZBA_KOLUMN = 7

class cztery_w_rzedzie:
    def __init__(self):
        self.plansza = np.zeros((LICZBA_WIERSZY, LICZBA_KOLUMN))


    def zapelniona_kolumna(self, kolumna1):
        return self.plansza[LICZBA_WIERSZY - 1][kolumna1] == 0

    def zapelniona_plansza(self):
        counter = 0
        for i in range(LICZBA_KOLUMN):
            if not self.plansza[LICZBA_WIERSZY - 1][i] == 0:
                counter +=1
        if counter == 7:
            print("Kolumna zapelniona, REMIS")
            return True
        return False

    def wolny_wiersz(self, kolumna1):
        for i in range(LICZBA_WIERSZY):
            if self.plansza[i][kolumna1] == 0:
                return i

    def wrzuc_monete(self, kolumna1, gracz):
        if self.zapelniona_kolumna(kolumna1):
            self.plansza[self.wolny_wiersz(kolumna1)][kolumna1] = gracz
        else:
            print("KOLUMNA ZAPELNIONA, WYBIERZ INNA")
            return False

    def wyswietl_plansze(self):
        print(np.flip(self.plansza, 0))

    def czyWygral(self, gracz):
        # poziome pozycje
        for kol in range(LICZBA_KOLUMN - 3):
            for wier in range(LICZBA_WIERSZY):
                if self.plansza[wier][kol] == gracz and self.plansza[wier][kol + 1] == gracz and self.plansza[wier][kol + 2] == gracz and self.plansza[wier][kol + 3] == gracz:
                    print(f"GRATULACJE GRACZ {gracz} WYGRAL")
                    return True

        # pionowe pozycje
        for kol in range(LICZBA_KOLUMN):
            for wier in range(LICZBA_WIERSZY - 3):
                if self.plansza[wier][kol] == gracz and self.plansza[wier + 1][kol] == gracz and self.plansza[wier + 2][kol] == gracz and self.plansza[wier + 3][kol] == gracz:
                    print(f"GRATULACJE GRACZ {gracz} WYGRAL")
                    return True

        # pozycje ukośna
        for kol in range(LICZBA_KOLUMN - 3):
            for wier in range(LICZBA_WIERSZY - 3):
                if self.plansza[wier][kol] == gracz and self.plansza[wier + 1][kol + 1] == gracz and \
                        self.plansza[wier + 2][kol + 2] == gracz and self.plansza[wier + 3][kol + 3] == gracz:
                    print(f"GRATULACJE GRACZ {gracz} WYGRAL")
                    return True
        for kol in range(LICZBA_KOLUMN - 3):
            for wier in range(3, LICZBA_WIERSZY):
                if self.plansza[wier][kol] == gracz and self.plansza[wier - 1][kol + 1] == gracz and \
                        self.plansza[wier - 2][kol + 2] == gracz and self.plansza[wier - 3][kol + 3] == gracz:
                    print(f"GRATULACJE GRACZ {gracz} WYGRAL")
                    return True

