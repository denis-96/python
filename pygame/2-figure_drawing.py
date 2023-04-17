import pygame as pg
pg.init()

FPS = 60

W, H = 600, 400
clock = pg.time.Clock()

sc = pg.display.set_mode((600, 400), pg.RESIZABLE)
pg.display.set_caption('Урок 2')
pg.display.set_icon(pg.image.load('pygame_lofi.png'))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255,  0, 0)

pg.draw.rect(sc, WHITE, (10, 10, 50, 100), 2)

pg.draw.line(sc, GREEN, (200, 20), (350, 50), 5)
pg.draw.aaline(sc, GREEN, (200, 40), (350, 70))

pg.draw.lines(sc, RED, True, [(200, 80), (250, 80), (300, 200)], 5)
pg.draw.aalines(sc, RED, True, [(300, 80), (350, 80), (400, 200)])

pg.draw.polygon(sc, WHITE, [(150, 210), (180, 250), (90, 290), (30, 230)])
pg.draw.polygon(sc, WHITE, [(150, 310), (180, 350), (90, 390), (30, 330)], 1)

pg.draw.circle(sc, BLUE, (300, 250), 40)
pg.draw.ellipse(sc, BLUE, (300, 300, 100, 50), 1)

pi = 3.14
pg.draw.arc(sc, RED, (450, 30, 50, 150), pi, 2*pi, 5)

pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        
    clock.tick(60)