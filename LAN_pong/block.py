class Block:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.velocity, self.acceleration = 0, 0
        width = 10
        height = 20
        color = (255, 255, 255)

    def draw(self):
        pass

    def move(self, direction_is_up):
        if direction_is_up:
            self.acceleration -= 5
        else:
            self.acceleration += 5

    def bounce(self, height):
        if self.y <= 0 or self.y >= height:
            self.velocity = self.velocity * -0.9
            self.acceleration = 0

    def update(self):
        self.y += self.velocity
        self.velocity += self.acceleration



