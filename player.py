import pygame
from spritesheet import SpriteSheet


class Player:
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.width = 16
        self.height = 16
        self.speed = 2

        self.direction = "down"
        self.frame_index = 0
        self.animation_timer = 0

        self.load_frames()

    def load_frames(self):
        sheet = SpriteSheet("assets/pokecharacters.png", (255, 127, 39))
        self.animations = {
            "down": [
                sheet.get_sprite(26, 34, 15, 15),
                sheet.get_sprite(43, 34, 15, 15),
                sheet.get_sprite(9, 34, 15, 15),
            ],

            "up": [
                sheet.get_sprite(77, 34, 15, 15),
                sheet.get_sprite(94, 34, 15, 15),
                sheet.get_sprite(60, 34, 15, 15),
            ],

            "left": [
                sheet.get_sprite(111, 34, 15, 15),
                sheet.get_sprite(128, 34, 15, 15),
            ],

            "right": [
                sheet.get_sprite(145, 34, 15, 15),
                sheet.get_sprite(162, 34, 15, 15),
            ],
        }


        for direction in self.animations:
            for i in range(len(self.animations[direction])):
                self.animations[direction][i] = pygame.transform.scale(
                    self.animations[direction][i],
                    (self.width, self.height)
                )

    def move(self, keys, mask, is_collision):
    
        moving = False

        old_direction = self.direction

        old_x = self.x
        old_y = self.y

        dx = 0
        dy = 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy -= self.speed
            self.direction = "up"
            moving = True

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += self.speed
            self.direction = "down"
            moving = True

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= self.speed
            self.direction = "left"
            moving = True

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += self.speed
            self.direction = "right"
            moving = True

        if self.direction != old_direction:
            self.frame_index = 0


        self.x += dx

        if is_collision(mask, self.get_rect()):
            self.x = old_x


        self.y += dy

        if is_collision(mask, self.get_rect()):
            self.y = old_y

        if moving:
            self.animate()
        else:
            self.frame_index = 0

    def animate(self):
        self.animation_timer += 1

        if self.animation_timer >= 10:
            self.animation_timer = 0

            self.frame_index += 1

            if self.frame_index >= len(self.animations[self.direction]):
                self.frame_index = 0

    def draw(self, screen, camera_x=0, camera_y=0):
        current_sprite = self.animations[self.direction][self.frame_index]
        screen.blit(current_sprite, (self.x - camera_x, self.y - camera_y))
    
    def get_rect(self):
        return pygame.Rect(
            self.x + 6,
            self.y + 16,
            self.width - 12,
            self.height - 12)