

class Ball:
    def __init__(self, width, height):
        self.x, self.y = width/2, height/2
        self.velocity_x, self.velocity_y = 0, 0
        self.acceleration_x, self.acceleration_y = 0, 0
        self.radius = 10
        self.color = (255, 255, 255)


    def draw(self):
        pass

    def move(self):
        pass

