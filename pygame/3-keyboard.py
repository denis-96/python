import pygame as pg

pg.init()

W, H = 600, 400

sc = pg.display.set_mode((W, H))
pg.display.set_caption('Урок 3')
pg.display.set_icon(pg.image.load('pygame_lofi.png'))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255,  0, 0)

FPS = 60
clock = pg.time.Clock()

x = W // 2
y = H // 2
speed = 5

rect_w, rect_h = 10, 20

# простой способ

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x != 0:
        x -= speed
    elif keys[pg.K_RIGHT] and x + rect_w != W:
        x += speed
    elif keys[pg.K_UP] and y != 0:
        y -= speed
    elif keys[pg.K_DOWN] and y + rect_h != H:
        y += speed 
        

    sc.fill(WHITE)
    pg.draw.rect(sc, BLUE, (x, y, rect_w, rect_h))
    pg.display.update()

    clock.tick(FPS)



# сложный способ

# flLeft = flRight = False
# flUp = flDown = False

# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             exit()
#         elif event.type == pg.KEYDOWN:
#             if event.key == pg.K_LEFT:
#                 flLeft = True
#             elif event.key == pg.K_RIGHT:
#                 flRight = True
#             elif event.key == pg.K_UP:
#                 flUp = True
#             elif event.key == pg.K_DOWN:
#                 flDown = True
#         elif event.type == pg.KEYUP:
#             if event.key in (pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN):
#                 flLeft = flRight = flUp = flDown = False

#     if flLeft and x != 0:
#          x -= speed
#     elif flRight and x + rect_w != W:
#         x += speed
#     elif flUp and y != 0:
#         y -= speed
#     elif flDown and y + rect_h != H:
#         y += speed

#     sc.fill(WHITE)
#     pg.draw.rect(sc, BLUE, (x, y, rect_w, rect_h))
#     pg.display.update()

#     clock.tick(FPS)
