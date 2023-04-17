import pygame as pg

pg.init()

W = 600
H = 400

sc = pg.display.set_mode((W, H))
pg.display.set_caption('Урок 5')

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255,  0, 0)

FPS = 60
clock = pg.time.Clock()

surf = pg.Surface((W, 200))
bita = pg.Surface((50, 10))

surf.fill(blue)
bita.fill(red)

bx, by = 0, 150
x = y = 0

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        
    surf.fill(blue)
    surf.blit(bita, (bx, by))

    if bx < W:
        bx += 5
    else:
        bx = 0
    
    if y < H:
        y += 1
    else:
        y = 0

    sc.fill(white)
    sc.blit(surf, (x, y))
    pg.display.update()
    
    clock.tick(FPS)