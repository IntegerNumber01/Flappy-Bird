import pygame

pygame.init()
screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption('Flappy Bird')


class Player():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.vel = 0

    def render(self):
        pygame.draw.rect(screen, (77, 184, 225), (self.x, self.y, self.size, self.size))

    def fall(self):
        self.y += self.vel
        if self.vel <= 0.8:  # Maximum velocity
            self.vel += 0.0025  # Gravity

    def jump(self):
        self.vel = -0.9


x = 200
y = 400
size = 50
jumping = False
running = True
player = Player(x, y, size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                jumping = True

    screen.fill('white')

    player.render()

    if jumping:
        player.jump()  # jumping = player.jump() makes the game run smoother.
        jumping = False
    else:
        player.fall()

    pygame.display.flip()

pygame.quit()
