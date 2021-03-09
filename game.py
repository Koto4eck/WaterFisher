import pygame
import random
import winsound

class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish, self).__init__()
        self.image = pygame.image.load("C:/Users/badiw/Desktop/Game Top By badi and andriy/New folder/fish1.png")
        self.rect = self.image.get_rect()
        y = random.randint(120, 710)
        self.rect.center = (100, y)

    def update(self):
        self.rect.x += 1
        if self.rect.x == 1920:
            fish = Fish()
            seafood.add(fish)


    def is_caught(self, sprite):
        return self.rect.colliderect(sprite.rect)

def spawn():
    fish = Fish()
    seafood.add(fish)

class Shark(pygame.sprite.Sprite):
    def __init__(self):
        super(Shark, self).__init__()
        self.image = pygame.image.load(
            "C:/Users/badiw/Desktop/Game Top By badi and andriy/New folder/Shark1.png")
        self.rect = self.image.get_rect()
        y = random.randint(120, 710)
        self.rect.center = (100, y)

    def update(self):
        self.rect.x += 1
        if self.rect.x == 2020:
            shark = Shark()
            sharks.add(shark)



class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super(Cat, self).__init__()
        self.image = pygame.image.load("C:/Users/badiw/Desktop/Game Top By badi and andriy/New folder/cat1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (1500, 710)

    def move(self, direction):
        if direction == 1:
            if self.rect.y < 710:
                self.rect.y += 50
        else:
            if self.rect.y > 120:
                self.rect.y -= 50

seafood = pygame.sprite.Group()
sharks = pygame.sprite.Group()
cats = pygame.sprite.Group()

cat = Cat()
cats.add(cat)

fish = Fish()
seafood.add(fish)
#shark = Shark()
#sharks.add(shark)

pygame.init()
screen = pygame.display.set_mode([1900, 1080])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                cat.move(0)
            if event.key == pygame.K_DOWN:
                cat.move(1)

    screen.fill((0, 255, 255))
    seafood.update()
    sharks.update()
    catch = pygame.sprite.spritecollide(cat, seafood, dokill=True)
    if catch:

        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 10  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        fish = Fish()

        seafood.add(fish)
    seafood.draw(screen)
    cats.draw(screen)
    pygame.display.flip()

pygame.quit()
#120 710