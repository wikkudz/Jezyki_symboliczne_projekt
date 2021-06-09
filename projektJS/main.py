import sys

import logika as l
import pygame


pygame.init()

# ROZMIARY
LICZBA_WIERSZY = 6
LICZBA_KOLUMN = 7
ROZMIAR_KWADRATU = 100
szerokosc = LICZBA_KOLUMN * ROZMIAR_KWADRATU
wysokosc = (LICZBA_WIERSZY+2) * ROZMIAR_KWADRATU
rozmiar = (szerokosc, wysokosc)
RADIUS = int(ROZMIAR_KWADRATU/2 - 5)

# CZCIONKI
czcionka = pygame.font.SysFont('Consolas',  40)
czcionka2 = pygame.font.SysFont('Consolas',  60)

wcisniety = False

pygame.display.set_caption("CZTERY W RZEDZIE")

# Czesto uzywane kolory
COLORS = [
    (255, 255, 255), # 0
    (255, 0, 0), # 1
    (255, 255, 0) # 2
]

class Game():
    kolor_przycisku = (25, 190, 225)
    kolor_tekstu = (255, 255, 255)
    kolor_cienia = (75, 225, 255)
    szerokosc = 50
    wysokosc = 50

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def rysuj_przyciski(self):
        global wcisniety
        action = False
        pos = pygame.mouse.get_pos()

        przycisk = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)

        # sprawdzam czy kursor znajduje się nad przyciskiem
        if przycisk.collidepoint(pos):
            # sprawdzam czy przycisk został wciśnięty i puszczony

            if pygame.mouse.get_pressed()[0] == 1:
                wcisniety = True
                pygame.draw.rect(screen, self.kolor_przycisku, przycisk)
            elif pygame.mouse.get_pressed()[0] == 0 and wcisniety == True:
                wcisniety = False
                action = True
            else:
                pygame.draw.rect(screen, self.kolor_przycisku, przycisk)
        else:
            pygame.draw.rect(screen, self.kolor_cienia, przycisk)

        # obramowanie przycisków
        pygame.draw.line(screen, COLORS[0], (self.x, self.y), (self.x+self.szerokosc, self.y), 2)
        pygame.draw.line(screen, COLORS[0], (self.x, self.y), (self.x, self.wysokosc+self.y), 2)
        pygame.draw.line(screen, (105, 105, 105), (self.x, self.wysokosc+self.y), (self.x + self.szerokosc, self.wysokosc+self.y), 2)
        pygame.draw.line(screen, (105, 105, 105), (self.x+self.szerokosc, self.y), (self.x+ self.szerokosc, self.wysokosc+self.y), 2)

        # tekst na przyciskach
        text_img = czcionka.render(self.text, True, self.kolor_tekstu)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.szerokosc/2) - int(text_len/2), self.y+5))
        return action

    def rysuj_plansze(plansza):
        for i in range(LICZBA_KOLUMN + 1):
            for j in range(LICZBA_WIERSZY):
                pygame.draw.rect(screen, (0, 0, 0), (
                i * ROZMIAR_KWADRATU, j * ROZMIAR_KWADRATU + ROZMIAR_KWADRATU, ROZMIAR_KWADRATU, ROZMIAR_KWADRATU))
                pygame.draw.circle(screen, COLORS[0], (int(i * ROZMIAR_KWADRATU + ROZMIAR_KWADRATU / 2),
                                                       int(j * ROZMIAR_KWADRATU + ROZMIAR_KWADRATU + ROZMIAR_KWADRATU / 2)),
                                   RADIUS)


# tworze przyciski służące do wrzucania monet
przycisk = []
przycisk= [Game(25 + i * 100, 5, str(i + 1)) for i in range(0, LICZBA_KOLUMN + 1)] # LIST COMPREHENSIONS


app = l.cztery_w_rzedzie()
koniec_gry = False
tura = 0

# tworzenie okna
screen = pygame.display.set_mode(rozmiar)
gra = Game
gra.rysuj_plansze(app.plansza)
pygame.display.update()
tekst1 = czcionka.render("WYBIERZ KOLUMNE", True, (255, 255, 255))
screen.blit(tekst1, (0, 70))
mazak = pygame.Rect(0, 700, 450, 120)
alerty = pygame.Rect(100, 300, 500, 120)
mazak2 = pygame.Rect(350, 70, 400, 30)
reset = Game(485, 720, "RESET")
reset.szerokosc = 200
reset.wysokosc = 50

# petla gry
while not koniec_gry:
    pygame.draw.rect(screen, (0, 0, 0), mazak)
    tekst2 = czcionka2.render(f"TURA GRACZA {tura + 1}", True, COLORS[tura +1])
    screen.blit(tekst2, (0, 720))
    kolumna = -1

    for i in range(0, LICZBA_KOLUMN):
        if przycisk[i].rysuj_przyciski():
            kolumna = i

    # sprawdzenie czy przycisk resetu zostal wcisniety
    if reset.rysuj_przyciski():
        var = app.plansza
        app = l.cztery_w_rzedzie()
        tura ^= 1
        screen = pygame.display.set_mode(rozmiar)
        gra.rysuj_plansze(app.plansza)
        screen.blit(tekst1, (0, 70))
        pygame.display.update()

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            sys.exit()

    # sprawdzenie czy plansza jest zapelniona i wyswietlenie komunikatu
    if app.zapelniona_plansza():
        tekst4 = czcionka.render("REMIS", True, COLORS[0])
        pygame.draw.rect(screen, (25, 190, 225), alerty)
        pygame.draw.line(screen, COLORS[0], (100, 300), (600, 300), 2)
        pygame.draw.line(screen, COLORS[0], (100, 300), (100, 420), 2)
        pygame.draw.line(screen, (105, 105, 105), (100, 420), (600, 420), 2)
        pygame.draw.line(screen, (105, 105, 105), (600, 300), (100 + 500, 420), 2)
        screen.blit(tekst4, (300, 340))
        pygame.display.update()
        pygame.time.wait(3000)
        var = app.plansza
        app = l.cztery_w_rzedzie()
        screen = pygame.display.set_mode(rozmiar)
        gra.rysuj_plansze(app.plansza)
        screen.blit(tekst1, (0, 70))
        pygame.display.update()

    if kolumna >= 0:
        if app.zapelniona_kolumna(kolumna):
            wiersz = app.wolny_wiersz(kolumna)
            app.wrzuc_monete(kolumna, tura + 1)
            pygame.draw.circle(screen, COLORS[tura+1], (int(kolumna * ROZMIAR_KWADRATU + ROZMIAR_KWADRATU / 2),int((5-wiersz) * ROZMIAR_KWADRATU + ROZMIAR_KWADRATU + ROZMIAR_KWADRATU / 2)),RADIUS)

            if app.czyWygral(tura + 1):
                pygame.draw.rect(screen, (0, 0, 0), mazak)
                tekst2 = czcionka.render(f"GRACZ {tura + 1} WYGRYWA!", True, (0, 0, 0))
                tekst3 = czcionka.render(f"GRATULACJE!", True, COLORS[tura+1])
                pygame.draw.rect(screen, (25, 190, 225), alerty)
                pygame.draw.line(screen, COLORS[0], (100, 300), (600, 300), 2)
                pygame.draw.line(screen, COLORS[0], (100, 300), (100, 420), 2)
                pygame.draw.line(screen, (105, 105, 105), (100, 420),(600, 420), 2)
                pygame.draw.line(screen, (105, 105, 105), (600, 300),(100 + 500, 420), 2)
                screen.blit(tekst2, (175, 320))
                screen.blit(tekst3, (225, 360))
                pygame.display.update()
                pygame.time.wait(3000)
                var = app.plansza
                app = l.cztery_w_rzedzie()
                screen = pygame.display.set_mode(rozmiar)
                gra.rysuj_plansze(app.plansza)
                screen.blit(tekst1, (0, 70))
                pygame.display.update()

        else:
            tekst5 = czcionka.render("KOLUMNA PELNA", True, (255, 165, 0))
            screen.blit(tekst5, (400, 70))
            pygame.display.update()
            pygame.time.wait(1000)
            pygame.draw.rect(screen, (0, 0, 0), mazak2)
            tura ^= 1

        app.wyswietl_plansze()
        tura ^= 1
    pygame.display.update()



