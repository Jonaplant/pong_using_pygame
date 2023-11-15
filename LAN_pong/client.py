import pygame
from game import Game

width = 900
height = 600

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)



if __name__ == "__main__":
    main()
