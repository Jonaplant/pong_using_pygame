import pygame
import random
import math

class Ball:
    def __init__(self, width, height):
        self.x, self.y = width/2, height/2
        self.radius = 10
        self.color = (255, 255, 255)
        self.velocity_x, self.velocity_y = 0, 0
        self.set_random_velocity()

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def bounce(self, height):
        if self.y <= 0:
            self.y = 1
            self.velocity_y = self.velocity_y * -1
        elif self.y >= height:
            self.y = height-1
            self.velocity_y = self.velocity_y * -1

    def check_collision(self, blocks, screen_width):
        if self.x <= blocks[0].width and blocks[0].y < self.y < blocks[0].y + blocks[0].height:
            self.x = blocks[0].width + 1
            self.velocity_x = self.velocity_x * -1
            self.increase_velocity(0.5)
        if self.x >= screen_width-blocks[1].width and blocks[1].y < self.y < blocks[1].y + blocks[1].height:
            self.x = screen_width - blocks[1].width - 1
            self.velocity_x = self.velocity_x * -1
            self.increase_velocity(0.5)

    def check_win(self, width):
        if self.x < 0:
            return "player 2"
        elif self.x > width:
            return "player 1"
        else:
            return "nobody yet"

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def increase_velocity(self, value):
        if self.velocity_x > 0:
            self.velocity_x += value
        elif self.velocity_x < 0:
            self.velocity_x -= value
        if self.velocity_y > 0:
            self.velocity_y += value
        elif self.velocity_y < 0:
            self.velocity_y -= value

    def set_random_velocity(self):
        #create a vector in a random direction with a set velocity
        total_velocity = 30
        temp_x_sq, temp_y_sq = random.random(), random.random()
        temp_vel_sq = temp_x_sq + temp_y_sq
        x_sq = temp_x_sq/(temp_vel_sq/total_velocity)
        y_sq = temp_y_sq/(temp_vel_sq/total_velocity)

        self.velocity_x = math.sqrt(x_sq) * random.choice([-1, 1])
        self.velocity_y = math.sqrt(y_sq) * random.choice([-1, 1])
