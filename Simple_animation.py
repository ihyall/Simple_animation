import pygame as pg
import random as rd


class drop():
    drops = []
    fl = False

    def __init__(self):
        self.size = rd.randint(2, 10)
        if drop.fl:
            self.rect = pg.rect.Rect(rd.randint(0, 1920), 0, 0, 0)
        else:
            self.rect = pg.rect.Rect(rd.randint(0, 1920), rd.randint(0, 1080), 0, 0)
        self.surface = pg.surface.Surface((self.size*1, self.size*2))
        self.surface.fill((100, 100, 255))
        drop.drops.append(self)

    def gravity(self, gravity=1):
        self.rect.move_ip(0, gravity*self.size/6*10)
        self.surface.get_size()

    def detele(self):
        if self.rect.top >= 1080:
            del self
            drop.fl = True
            return True


width = 1920
height = 1080
FPS = 120

pg.init()
pg.display.init()
clock = pg.time.Clock()
pg.display.set_caption('Rain animation')
screen = pg.display.set_mode((width, height), flags=pg.SCALED)
screen.fill((127, 199, 255))
pg.display.toggle_fullscreen()
n = 2000

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    if len(drop.drops) < n:
        for i in range(n-len(drop.drops)):
            drop()

    for d in drop.drops:
        if d.detele():
            drop.drops.pop(drop.drops.index(d))
            continue

        d.gravity()
        screen.blit(d.surface, d.rect)

    pg.display.update()
    pg.display.flip()
    screen.fill((127, 199, 255))

pg.quit()
