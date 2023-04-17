import pygame as pg

pg.init()

W = 600
H = 400

sc = pg.display.set_mode((W, H))
pg.display.set_caption('Урок 4')


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255,  0, 0)

FPS = 60
clock = pg.time.Clock()

sp = None

sc.fill(WHITE)
pg.display.update()

pg.mouse.set_visible(False)

while 1:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    sc.fill(WHITE)

    pos = pg.mouse.get_pos()
    if pg.mouse.get_focused():
        pg.draw.circle(sc, BLUE, pos, 2)

    pressed = pg.mouse.get_pressed()

    if pressed[0]:

        if sp is None:
            sp = pos


        width = abs(pos[0] - sp[0])
        height = abs(pos[1] - sp[1])

        if sp[0] <= pos[0] and sp[1] <= pos[1]:
            rectangle = pg.Rect(sp[0], sp[1], width, height)
        else:
            rectangle = pg.Rect(pos[0], pos[1], width, height)

        sc.fill(WHITE)
        pg.draw.rect(sc, RED, rectangle)
        
        
    else: 
        sp = None

    pg.display.update()

    clock.tick(FPS)