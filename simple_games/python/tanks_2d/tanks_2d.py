import pygame
import math as m
import time
import random

from typing import List

BOARD_X = 1280
BOARD_Y = 960

DEBUG = False


def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    # loc = image.get_rect().center  # rot_image is not defined
    rot_sprite = pygame.transform.rotate(image, angle)
    # rot_sprite.get_rect().center = loc
    return rot_sprite


def remove_obj(objs):
    for obj in objs:
        if not obj.exist:
            d_obj = objs.pop(objs.index(obj))
            del d_obj


class Player:
    @staticmethod
    def get_point_centre_of_tank(x_, y_, w_, h_):
        return int(x_ + w_ / 2), int(y_ + h_ / 2)

    def __init__(self, x, y, name, tank_img, size_tank=50):
        self.name = name
        self.x = x
        self.y = y
        self._size_tank = size_tank
        self._tank_img = tank_img
        self.height = int(self._size_tank * m.sqrt(2))
        self.width = int(self._size_tank * m.sqrt(2))
        self.speed = 10
        self.direction = {'right': 0, 'up': 1, 'left': 0, 'down': 0}

        self.exist = True

        self.centre_x, self.centre_y = self.get_point_centre_of_tank(self.x, self.y, self.width, self.height)

        self.time_prev_shot = 0
        self.gun_reload = 1
        self.gun_ready = True

    def draw(self, scr):
        if self.direction['down'] and self.direction['left']:
            scr.blit(rot_center(self._tank_img, 135), (self.x, self.y))
        elif self.direction['down'] and self.direction['right']:
            scr.blit(rot_center(self._tank_img, 225), (self.x, self.y))
        elif self.direction['up'] and self.direction['left']:
            scr.blit(rot_center(self._tank_img, 45), (self.x, self.y))
        elif self.direction['up'] and self.direction['right']:
            scr.blit(rot_center(self._tank_img, -45), (self.x, self.y))
        elif self.direction['right']:
            scr.blit(rot_center(self._tank_img, -90),
                     (int(self.x + (m.sqrt(2) - 1) / 2 * self._size_tank), int(self.y + (m.sqrt(2) - 1) / 2 * self._size_tank)))
        elif self.direction['left']:
            scr.blit(rot_center(self._tank_img, 90),
                     (int(self.x + (m.sqrt(2) - 1) / 2 * self._size_tank), int(self.y + (m.sqrt(2) - 1) / 2 * self._size_tank)))
        elif self.direction['up']:
            scr.blit(rot_center(self._tank_img, 0),
                     (int(self.x + (m.sqrt(2) - 1) / 2 * self._size_tank), int(self.y + (m.sqrt(2) - 1) / 2 * self._size_tank)))
        elif self.direction['down']:
            scr.blit(rot_center(self._tank_img, 180),
                     (int(self.x + (m.sqrt(2) - 1) / 2 * self._size_tank), int(self.y + (m.sqrt(2) - 1) / 2 * self._size_tank)))

        if DEBUG:
            pygame.draw.rect(scr, (0, 255, 0), (self.x, self.y, self.width, self.height), 1)

    def move(self, keys):
        if keys[pygame.K_s] and keys[pygame.K_a] and self.x > 0 and self.y < BOARD_Y - self.height:
            self.y += int(self.speed / m.sqrt(2))
            self.x -= int(self.speed / m.sqrt(2))
            self.direction['right'], self.direction['left'], self.direction['up'], self.direction['down'] = 0, 1, 0, 1
        elif keys[pygame.K_s] and keys[pygame.K_d] and self.x < BOARD_X - self.width and self.y < BOARD_Y - self.height:
            self.y += int(self.speed / m.sqrt(2))
            self.x += int(self.speed / m.sqrt(2))
            self.direction['right'], self.direction['left'], self.direction['up'], self.direction['down'] = 1, 0, 0, 1
        elif keys[pygame.K_s] and self.y < BOARD_Y - self.height:
            self.y += self.speed
            self.direction['right'], self.direction['left'], self.direction['up'], self.direction['down'] = 0, 0, 0, 1
        elif keys[pygame.K_w] and keys[pygame.K_a] and self.x > 0 and self.y > 0:
            self.y -= int(self.speed / m.sqrt(2))
            self.x -= int(self.speed / m.sqrt(2))
            self.direction['right'], self.direction['left'], self.direction['up'], self.direction['down'] = 0, 1, 1, 0
        elif keys[pygame.K_w] and keys[pygame.K_d] and self.x < BOARD_X - self.width and self.y > 0:
            self.y -= int(self.speed / m.sqrt(2))
            self.x += int(self.speed / m.sqrt(2))
            self.direction['right'], self.direction['left'], self.direction['up'], self.direction['down'] = 1, 0, 1, 0
        elif keys[pygame.K_w] and self.y > 0:
            self.y -= self.speed
            self.direction['right'], self.direction['left'], self.direction['up'], self.direction['down'] = 0, 0, 1, 0
        elif keys[pygame.K_d] and self.x < BOARD_X - self.width:
            self.x += self.speed
            self.direction['right'], self.direction['left'], self.direction['up'], self.direction['down'] = 1, 0, 0, 0
        elif keys[pygame.K_a] and self.x > 0:
            self.x -= self.speed
            self.direction['right'], self.direction['left'], self.direction['up'], self.direction['down'] = 0, 1, 0, 0

        self.centre_x, self.centre_y = self.get_point_centre_of_tank(self.x, self.y, self.width, self.height)

    def recharge(self):
        if int(time.time()) - self.time_prev_shot >= self.gun_reload:
            self.gun_ready = True

    def take_a_shot(self):
        self.time_prev_shot = int(time.time())
        self.gun_ready = False
        return Bullet(self.name, self.centre_x, self.centre_y, self.direction.copy())


class Bullet:
    def __init__(self, source_name, x, y, direction):
        self.source_name = source_name
        self.x = x
        self.y = y
        self.speed = 40
        self.direction = direction
        self.exist = True

    def move(self):
        if self.x < 0 or self.x > BOARD_X or self.y < 0 or self.y > BOARD_Y:
            self.exist = False

        if self.direction['right'] and self.direction['up']:
            self.x += int(self.speed / m.sqrt(2))
            self.y -= int(self.speed / m.sqrt(2))
        elif self.direction['left'] and self.direction['up']:
            self.x -= int(self.speed / m.sqrt(2))
            self.y -= int(self.speed / m.sqrt(2))
        elif self.direction['up']:
            self.y -= self.speed
        elif self.direction['right'] and self.direction['down']:
            self.x += int(self.speed / m.sqrt(2))
            self.y += int(self.speed / m.sqrt(2))
        elif self.direction['left'] and self.direction['down']:
            self.x -= int(self.speed / m.sqrt(2))
            self.y += int(self.speed / m.sqrt(2))
        elif self.direction['down']:
            self.y += self.speed
        elif self.direction['right']:
            self.x += self.speed
        elif self.direction['left']:
            self.x -= self.speed

    def draw(self, scr):
        pygame.draw.circle(scr, (255, 0, 0), (self.x, self.y), 5)


class Enemy(Player):
    def __init__(self, name, tank_img):
        super().__init__(BOARD_X, random.randint(60, BOARD_Y - 60), name, tank_img)

        self.direction = {'right': 0, 'up': 0, 'left': 1, 'down': 0}
        self.gun_reload = 2
        self.speed = 5

    def move(self, keys=None):
        if self.x < 0 or self.x > BOARD_X or self.y < 0 or self.y > BOARD_Y:
            self.exist = False

        self.x -= self.speed
        self.centre_x, self.centre_y = self.get_point_centre_of_tank(self.x, self.y, self.width, self.height)

    def draw(self, scr):
        scr.blit(rot_center(self._tank_img, -90),
                 (int(self.x + (m.sqrt(2) - 1) / 2 * self._size_tank),
                  int(self.y + (m.sqrt(2) - 1) / 2 * self._size_tank)))

        if DEBUG:
            pygame.draw.rect(scr, (0, 255, 0), (self.x, self.y, self.width, self.height), 1)


class ManagerEnemies:
    def __init__(self, number_enemies, respawn_time, tank_img):
        self.tank_img = tank_img
        self.respawn_time = respawn_time
        self.number_enemies = number_enemies
        self.revival = True
        self.time_prev_revival = 0
        self.name_enemies = 0

    def control_populations(self, enemies):
        self.recharge()
        if len(enemies) < self.number_enemies and self.revival:
            self.time_prev_revival = time.time()
            self.revival = False
            enemies.append(Enemy(f"en_{self.name_enemies}", self.tank_img))

    def recharge(self):
        if int(time.time()) - self.time_prev_revival >= self.respawn_time:
            self.revival = True


def draw_window(scr, bg_img, plr: Player, enemies: List[Enemy], bllts: List[Bullet]):
    scr.blit(bg_img, (0, 0))
    plr.draw(scr)

    for enemy in enemies:
        enemy.draw(scr)

    for bllt in bllts:
        bllt.draw(scr)
    pygame.display.update()


def main():
    pygame.init()
    logo = pygame.image.load("data/tank_green.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("tanks_2d")

    screen = pygame.display.set_mode((BOARD_X, BOARD_Y))

    bg_image = pygame.image.load("data/bf.png")
    tank_img = pygame.image.load("data/tank_green.png")
    enemy_img = pygame.image.load("data/tank_red.png")

    _time = 10
    running = True

    player = Player(50, 50, "player_1", tank_img)
    bullets = []

    enemies = []
    manager_enemies = ManagerEnemies(5, 2, enemy_img)

    while running:
        pygame.time.delay(_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and player.gun_ready:
            bullets.append(player.take_a_shot())

        player.move(keys)
        player.recharge()

        print(f"len enemies {len(enemies)}")
        print(f"len bullets {len(bullets)}")

        manager_enemies.control_populations(enemies)

        for enemy in enemies:
            enemy.move()
            enemy.recharge()
            if enemy.gun_ready:
                bullets.append(enemy.take_a_shot())

        for bullet in bullets:
            bullet.move()

        remove_obj(bullets)
        remove_obj(enemies)

        draw_window(screen, bg_image, player, enemies, bullets)


if __name__ == "__main__":
    main()
