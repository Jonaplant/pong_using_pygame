import pygame

class Block:
    def __init__(self, x, y, height):
        self.width, self.height = 10, height
        self.x, self.y = x, y - self.height/2
        # self.velocity = 0
        # self.acceleration = 0
        self.color = (255, 255, 255)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move(self, direction_is_up):
        if direction_is_up:
            # self.acceleration -= 0.1 + 1 * self.acceleration
            self.y -= 5

        else:
            # self.acceleration += 0.1 - 1 * self.acceleration
            self.y += 5

    def bounce(self, height):
        if self.y <= 0:
            self.y = 1
            # self.velocity = self.velocity * -0.5
            # self.acceleration = 0
        if self.y >= height - self.height:
            self.y = height - self.height - 1
            # self.velocity = self.velocity * -0.5
            # self.acceleration = 0

    # def update(self):
    #     self.y += self.velocity
    #     self.velocity += self.acceleration
    #     if self.acceleration > 0:
    #         self.acceleration -= 0.001
    #     if self.acceleration < 0:
    #         self.acceleration += 0.001

    def reset(self, screen_height):
        self.y = screen_height/2 - self.height/2
        # self.velocity = 0
        # self.acceleration = 0

