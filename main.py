import pygame, sys
from pygame.locals import *

screen_width = 600
screen_height = 600

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('BREAKOUT')


# color = (red, green, blue)
bl = (24, 150, 204)
rd = (237, 24, 24)
yl = (242, 230, 5)
back = (71, 71, 63)
white = (255, 255, 255)

screen.fill(back)

rows = 6
coloumns = 8

class brick():
  def __init__(self):
    self.width = screen_width // coloumns

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
    pygame.display.update()

pygame.quit()