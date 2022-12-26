import pygame as pg

pg.init()

W = 600
H = 400

sc = pg.display.set_mode((W, H))
pg.display.set_caption('Урок 6')

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255,  0, 0)

FPS = 60
clock = pg.time.Clock()

ground = H-70
jump_force = 20
move = jump_force+1

hero = pg.Surface((40, 50))
hero.fill(blue)
rect = hero.get_rect(centerx=W//2)
rect.bottom = ground

rect_update = pg.Rect(rect.x, 0, rect.width, ground)
sc.fill(white)
pg.display.update()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and ground == rect.bottom:
                move = -jump_force
        
    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move += 1
        else:
            rect.bottom = ground
            move = jump_force+1
                
    sc.fill(white)
    sc.blit(hero, rect)
    pg.display.update(rect_update)
        
    clock.tick(FPS)