import pygame
from game import Game
from block import Block
from ball import Ball

width = 900
height = 600

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

game = Game(width, height)
blocks = (Block(0, height/2, 100), Block(width-10, height/2, 100))
ball = Ball(width, height)

score = [0, 0]

def main():
    clock = pygame.time.Clock()
    keys_pressed = [False, False, False, False]

    while True:
        clock.tick(60)

        check_win()
        collect_input(keys_pressed)
        move(keys_pressed)
        move_game_objects()
        draw()

def check_win():
    winner = ball.check_win(width)
    font = pygame.font.Font('freesansbold.ttf', 32)
    if winner == "player 1":
        text = font.render("Player one wins!", True, (255, 0, 0))
        congratulate_winner(text)
        score[0] += 1
    elif winner == "player 2":
        text = font.render("Player two wins!", True, (255, 0, 0))
        congratulate_winner(text)
        score[1] += 1

def congratulate_winner(text):
    pygame.time.wait(500)
    for i in range(5):
        win.fill((0, 0, 0))
        pygame.display.update()
        pygame.time.wait(200)
        win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.wait(300)

    reset_game()

def reset_game():
    ball.x, ball.y = width/2, height/2
    ball.set_random_velocity()
    for block in blocks:
        block.reset(height)

def collect_input(keys_pressed):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys_pressed[0] = True
            if event.key == pygame.K_DOWN:
                keys_pressed[1] = True
            if event.key == pygame.K_w:
                keys_pressed[2] = True
            if event.key == pygame.K_s:
                keys_pressed[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys_pressed[0] = False
            if event.key == pygame.K_DOWN:
                keys_pressed[1] = False
            if event.key == pygame.K_w:
                keys_pressed[2] = False
            if event.key == pygame.K_s:
                keys_pressed[3] = False
    return keys_pressed

def move(keys_pressed):
    if keys_pressed[0]:
        blocks[1].move(True)  # true means it goes up, false it goes down
    if keys_pressed[1]:
        blocks[1].move(False)
    if keys_pressed[2]:
        blocks[0].move(True)
    if keys_pressed[3]:
        blocks[0].move(False)


def draw():
    win.fill((0, 0, 0))
    pygame.draw.line(win, (200, 200, 200), (width/2, 0), (width/2, height))
    ball.draw(win)
    for block in blocks:
        block.draw(win)

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(score), True, (255, 255, 255))
    win.blit(text, (width / 2 - text.get_width() / 2, 50))

    pygame.display.update()


def move_game_objects():
    ball.check_collision(blocks, width)
    ball.bounce(height)
    ball.update()
    for block in blocks:
        block.bounce(height)
        # block.update()


if __name__ == "__main__":
    main()
