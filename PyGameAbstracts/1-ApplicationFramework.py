import pygame as pg

pg.init()

pg.display.set_mode((700, 400), pg.RESIZABLE)  # создание окна нужного размера
pg.display.set_caption('Урок 1')  # изменение названия окна
pg.display.set_icon(pg.image.load('pygame_lofi.png'))  # изменение иконки

clock = pg.time.Clock()  # создаём объект класса Clock
FPS = 60  # создаём переменную с количеством FPS

# создаём главный цикл обработки событий
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        
    clock.tick(60)