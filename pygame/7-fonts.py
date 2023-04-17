import pygame as pg

pg.init()

W, H = 600, 400

sc = pg.display.set_mode((W, H))
pg.display.set_caption('Урок 7')

white = (255, 255, 255)
red = (255,  0, 0)
yellow = (239, 228, 176)

FPS = 60
clock = pg.time.Clock()

# f = pg.font.SysFont('bahnschrift', 24)
# f = pg.font.Font(path, 24)
f = pg.font.Font(None, 48)
sc_text = f.render('Привет мир!', 1, red)
pos = sc_text.get_rect(center=(W//2, H//2))

sc.fill(white)
sc.blit(sc_text, pos)
pg.display.update()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            
    clock.tick(FPS)