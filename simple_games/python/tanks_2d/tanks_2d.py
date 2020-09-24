import pygame
import math as m
import time
import random

from typing import List, Union

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

    def set_points_collision_model(self):
        self.collision_model_x = (self.centre_x - self._size_tank // 2, self.centre_x + self._size_tank // 2)
        self.collision_model_y = (self.centre_y - self._size_tank // 2, self.centre_y + self._size_tank // 2)

    def __init__(self, x, y, name, tank_img, size_tank=50):
        self.name = name
        self.x = x
        self.y = y
        self.score = 0
        self._size_tank = size_tank
        self._tank_img = tank_img
        self.height = int(self._size_tank * m.sqrt(2))
        self.width = int(self._size_tank * m.sqrt(2))
        self.speed = 10
        self.direction = {'right': 0, 'up': 1, 'left': 0, 'down': 0}

        self.exist = True

        self.centre_x, self.centre_y = self.get_point_centre_of_tank(self.x, self.y, self.width, self.height)
        self.collision_model_x = (self.centre_x - self._size_tank // 2, self.centre_x + self._size_tank // 2)
        self.collision_model_y = (self.centre_y - self._size_tank // 2, self.centre_y + self._size_tank // 2)

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
                     (int(self.x + (m.sqrt(2) - 1) / 2 * self._size_tank),
                      int(self.y + (m.sqrt(2) - 1) / 2 * self._size_tank)))
        elif self.direction['left']:
            scr.blit(rot_center(self._tank_img, 90),
                     (int(self.x + (m.sqrt(2) - 1) / 2 * self._size_tank),
                      int(self.y + (m.sqrt(2) - 1) / 2 * self._size_tank)))
        elif self.direction['up']:
            scr.blit(rot_center(self._tank_img, 0),
                     (int(self.x + (m.sqrt(2) - 1) / 2 * self._size_tank),
                      int(self.y + (m.sqrt(2) - 1) / 2 * self._size_tank)))
        elif self.direction['down']:
            scr.blit(rot_center(self._tank_img, 180),
                     (int(self.x + (m.sqrt(2) - 1) / 2 * self._size_tank),
                      int(self.y + (m.sqrt(2) - 1) / 2 * self._size_tank)))

        if DEBUG:
            pygame.draw.rect(scr, (0, 255, 0), (self.x, self.y, self.width, self.height), 1)
            pygame.draw.circle(scr, (255, 0, 0), (self.collision_model_x[0], self.collision_model_y[0]), 3)
            pygame.draw.circle(scr, (255, 0, 0), (self.collision_model_x[1], self.collision_model_y[1]), 3)
            pygame.draw.circle(scr, (255, 0, 0), (self.collision_model_x[0], self.collision_model_y[1]), 3)
            pygame.draw.circle(scr, (255, 0, 0), (self.collision_model_x[1], self.collision_model_y[0]), 3)

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
        self.set_points_collision_model()

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
        if self.x < -self._size_tank or self.x > BOARD_X or self.y < 0 or self.y > BOARD_Y:
            self.exist = False

        self.x -= self.speed
        self.centre_x, self.centre_y = self.get_point_centre_of_tank(self.x, self.y, self.width, self.height)
        self.set_points_collision_model()

    def draw(self, scr):
        scr.blit(rot_center(self._tank_img, -90),
                 (int(self.x + (m.sqrt(2) - 1) / 2 * self._size_tank),
                  int(self.y + (m.sqrt(2) - 1) / 2 * self._size_tank)))

        if DEBUG:
            pygame.draw.rect(scr, (0, 255, 0), (self.x, self.y, self.width, self.height), 1)
            pygame.draw.circle(scr, (255, 0, 0), (self.collision_model_x[0], self.collision_model_y[0]), 3)
            pygame.draw.circle(scr, (255, 0, 0), (self.collision_model_x[1], self.collision_model_y[1]), 3)
            pygame.draw.circle(scr, (255, 0, 0), (self.collision_model_x[0], self.collision_model_y[1]), 3)
            pygame.draw.circle(scr, (255, 0, 0), (self.collision_model_x[1], self.collision_model_y[0]), 3)


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
            self.name_enemies += 1

    def recharge(self):
        if int(time.time()) - self.time_prev_revival >= self.respawn_time:
            self.revival = True


class ManagerCollisions:
    def __init__(self):
        pass

    @staticmethod
    def get_collision_between_tanks(player_: Player, enemies_: List[Enemy]):
        pl_x_l, pl_x_r = player_.collision_model_x
        pl_y_u, pl_y_d = player_.collision_model_y
        for enemy_ in enemies_:
            en_x_l, en_x_r = enemy_.collision_model_x
            en_y_d, en_y_u = enemy_.collision_model_y
            if (en_x_r >= pl_x_r >= en_x_l and en_y_d <= pl_y_d <= en_y_u or
                    en_x_r >= pl_x_r >= en_x_l and en_y_d <= pl_y_u <= en_y_u or
                    en_x_r >= pl_x_l >= en_x_l and en_y_d <= pl_y_d <= en_y_u or
                    en_x_r >= pl_x_l >= en_x_l and en_y_d <= pl_y_u <= en_y_u):
                player_.exist = False
                enemy_.exist = False
                break

    @staticmethod
    def get_collision_tank_with_bullets(tank_: Union[Player, Enemy], bullets_):
        t_x_l, t_x_r = tank_.collision_model_x
        t_y_d, t_y_u = tank_.collision_model_y
        for bullet in bullets_:
            b_x, b_y = bullet.x, bullet.y
            if t_x_l <= b_x <= t_x_r and t_y_d <= b_y <= t_y_u and tank_.name != bullet.source_name:
                tank_.exist = False
                bullet.exist = False


def end_game(scr):
    scr.fill((0, 0, 0))
    f1 = pygame.font.SysFont('serif', 30)
    f2 = pygame.font.SysFont('serif', 48)
    text1 = f2.render("GAME OVER!", 10, (180, 180, 0))
    text2 = f1.render("Press Space to Quit", 10, (180, 180, 0))
    scr.blit(text1, (BOARD_X // 2 - 200, BOARD_Y // 2 - 200))
    scr.blit(text2, (BOARD_X // 2 - 200, BOARD_Y // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            break

    return False


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

    manager_collisions = ManagerCollisions()

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

        manager_enemies.control_populations(enemies)

        for enemy in enemies:
            enemy.move()
            enemy.recharge()
            if enemy.gun_ready:
                bullets.append(enemy.take_a_shot())

            manager_collisions.get_collision_tank_with_bullets(enemy, bullets)

        for bullet in bullets:
            bullet.move()

        manager_collisions.get_collision_tank_with_bullets(player, bullets)
        manager_collisions.get_collision_between_tanks(player, enemies)

        remove_obj(bullets)
        remove_obj(enemies)

        draw_window(screen, bg_image, player, enemies, bullets)

        if not player.exist:
            running = end_game(screen)


if __name__ == "__main__":
    main()
