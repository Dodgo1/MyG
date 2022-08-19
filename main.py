import pygame as pg
import random

LEFT = 150
MIDDLE = 450
RIGHT = 750


class Player:
    def __init__(self, top=450, width=100, height=50, color=(255, 0, 0)):
        self.color = color
        self.left = LEFT - width / 2
        self.top = top
        self.width = width
        self.height = height
        self.rect = pg.rect.Rect(width, width, height, height)

    def handle_keys(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.left = LEFT - self.width / 2
        if key[pg.K_RIGHT]:
            self.left = RIGHT - self.width / 2
        if key[pg.K_UP]:
            self.left = MIDDLE - self.width / 2
        if key[pg.K_DOWN]:
            self.left = MIDDLE - self.width / 2

    def draw(self, surface):
        self.rect.update(self.left, self.top, self.width, self.height)
        pg.draw.rect(surface, self.color, self.rect)

    def check_collision(self, rect):
        return self.rect.colliderect(rect)


class Rock:
    def __init__(self, top=0, width=50, height=50):
        self.left = random.choice([LEFT, MIDDLE, RIGHT]) - width / 2
        self.top = top
        self.width = width
        self.height = height
        self.rect = pg.rect.Rect(width, width, height, height)

    def draw(self, surface):
        self.rect.update(self.left, self.top, self.width, self.height)
        self.top += 15
        pg.draw.rect(surface, (0, 0, 128), self.rect)


pg.init()
pg.display.set_caption('MyG')

clock = pg.time.Clock()
FPS = 30

window = pg.display.set_mode((900, 600))
window.fill(pg.Color('#000000'))

player = Player()
is_running = True
life = 100
enemy_list = [Rock()]
SPAWNENEMY = pg.USEREVENT
pg.time.set_timer(SPAWNENEMY, 300)
while is_running:
    events = pg.event.get()
    keys = pg.key.get_pressed()
    window.fill(pg.Color('#000000'))

    for event in events:
        if event.type == pg.QUIT:
            is_running = False
        if event.type == SPAWNENEMY:
            enemy_list.append(Rock())

    for rock in enemy_list:
        if player.check_collision(rock):
            enemy_list.remove(rock)
            life += -1
        if rock.top > 600:
            enemy_list.remove(rock)

        rock.draw(window)

    player.handle_keys()
    player.draw(window)

    pg.display.update()

    clock.tick(FPS)
    # print(clock.get_fps())
