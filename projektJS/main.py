import numpy as np

LICZBA_WIERSZY = 6
LICZBA_KOLUMN = 7

def stworz_plansze():
    plansza = np.zeros((LICZBA_WIERSZY, LICZBA_KOLUMN))
    return plansza

plansza = stworz_plansze()
koniec_gry = False
tura = 0

def wrzuc_monete(plansza, wiersz, kolumna, gracz):
    plansza[wiersz][kolumna] = gracz

def zapelniona_kolumna(plansza, kolumna):
    return plansza[LICZBA_WIERSZY - 1][kolumna] == 0

def wolny_wiersz(plansza, kolumna):
    for i in range(LICZBA_WIERSZY):
        if plansza[i][kolumna] == 0:
            return i

def wyswietl_plansze(plansza):
    print(np.flip(plansza, 0))

def wygrany_ruch(plansza, gracz):
    #Sprawdzenie pozycji
    for i in range(LICZBA_KOLUMN):
        for j in range(LICZBA_WIERSZY):
            if plansza[i][j] == gracz and plansza[i][j+1] == gracz and plansza[i][j+2] == gracz and plansza[i][j+3] == gracz:
                return True



while not koniec_gry:
    if tura == 0:
        kolumna = int(input("Tura gracza 1 (0-6): "))
        if zapelniona_kolumna(plansza, kolumna):
            wiersz = wolny_wiersz(plansza, kolumna)
            wrzuc_monete(plansza, wiersz, kolumna, 1)

            # if wygrany_ruch(plansza, 1):
            #     print("Gracz 1 wygrywa")
    else:
        kolumna = int(input("Tura gracza 2 (0-6): "))
        if zapelniona_kolumna(plansza, kolumna):
            wiersz = wolny_wiersz(plansza, kolumna)
            wrzuc_monete(plansza, wiersz, kolumna, 2)
            # if wygrany_ruch(plansza, 2):
            #     print("Gracz 2 wygrywa")

    wyswietl_plansze(plansza)
    tura += 1
    tura = tura % 2
