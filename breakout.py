import pygame, sys
from pygame.locals import *

screen_width = 600
screen_height = 440

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('BREAKOUT')


# color = (red, green, blue)
bl = (24, 150, 204)
rd = (237, 24, 24)
yl = (242, 230, 5)
back = (71, 71, 50)
white = (255, 255, 255)

screen.fill(back)

rows = 6
coloums = 8

class brick():
  def __init__(self):
    self.width = screen_width // coloums
    self.height = 40

  def create_brick(self):
    self.brick = []
    brick_singular = []
    for row in range(rows):
      brick_row = []
      for cols in range(coloums):
        brick_x = coloums * self.width
        brick_y = rows * self.height
        rect = pygame.rect(brick_x, brick_y, self.width, self.height)
        if rows <= 2:
          strength = 3
        elif rows <= 4:
          strength = 2
        elif rows <= 6:
          strength = 1
        brick_singular = [rect, strength]
        brick_row.append(brick_singular)
      self.brick.append(brick_row)
      
  def show_brick(self):
    for row in self.brick:
      for brick in row:
        if brick[1] == 3:
          brick_col = bl
        elif brick[1] == 2: 
          brick_col = yl
        elif brick[1] == 1:
          brick_col = rd
        pygame.draw.rect(screen, brick_col, brick[1])
        pygame.draw.rect(screen.blit, brick[1])


brick = brick()
brick.create_brick()
pass 
    
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
    pygame.display.update()

pygame.quit()