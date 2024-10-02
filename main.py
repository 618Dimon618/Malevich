import pygame
import random

pygame.init()

w = 800
h = 600
wr = 300
hr = 200
colsc = (77, 68, 67)
screen = pygame.display.set_mode((w, h))
screen.fill((colsc))
clock = pygame.time.Clock()
malev = pygame.image.load("malev.png")
malevmini = pygame.transform.scale(malev, (wr, hr))

f1 = pygame.font.SysFont('Comic Sans', 70)
text1 = f1.render('Загрузка проекта', 1, (255, 0, 0))
text2 = f1.render('Подожите', 1, (255, 0, 0))

x = 272
y = 129
rec = pygame.Rect((x, y), (wr, hr))
s = "ne"

pointsCount = 0

col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

a = True
while a:
    pointsCount += 1
    if pointsCount > 50:
        pygame.draw.circle(screen, (255, 0, 0), (w // 2 + 160, h // 2 + 75), 5)
    if pointsCount > 100:
        pygame.draw.circle(screen, (255, 0, 0), (w // 2 + 175, h // 2 + 75), 5)
    if pointsCount > 150:
        pygame.draw.circle(screen, (255, 0, 0), (w // 2 + 190, h // 2 + 75), 5)
    if pointsCount == 200:
        pygame.draw.circle(screen, (colsc), (w // 2 + 160, h // 2 + 75), 5)
        pygame.draw.circle(screen, (colsc), (w // 2 + 175, h // 2 + 75), 5)
        pygame.draw.circle(screen, (colsc), (w // 2 + 190, h // 2 + 75), 5)
    if pointsCount == 200:
        pointsCount = 0

    screen.blit(text1, (w // 2 - 280, h // 2 - 100))
    screen.blit(text2, (w // 2 - 200, h // 2))
    if s == "ne":
        x += 1
        y -= 1
    elif s == "se":
        x += 1
        y += 1
    elif s == "sw":
        x -= 1
        y += 1
    elif s == "nw":
        x -= 1
        y -= 1

    if s == "ne" and y == 0:
        s = "se"
        col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif s == "ne" and x == w - wr:
        s = "nw"
        col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif s == "se" and x == w - wr:
        s = "sw"
        col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif s == "se" and y == h - hr:
        s = "ne"
        col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif s == "sw" and y == h - hr:
        s = "nw"
        col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif s == "sw" and x == 0:
        s = "se"
        col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif s == "nw" and x == 0:
        s = "ne"
        col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif s == "nw" and y == 0:
        s = "sw"
        col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.rect(screen, (colsc), rec)
    rec = pygame.Rect((x, y), (wr, hr))
    pygame.draw.rect(screen, col, rec)
    screen.blit(malevmini, (x, y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            a = False
    clock.tick(100)
