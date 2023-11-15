from ball import Ball


class Game:
    def __init__(self, width, height):
        self.ready = False
        self.score = [0, 0]

    def point_has_been_made(self, winner):
        self.score[winner] += 1

    def reset_game(self, width, height):
        # self.ball.x, self.ball.y = width/2, height/2
        pass


