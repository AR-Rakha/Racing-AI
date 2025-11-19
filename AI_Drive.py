import pygame
import math

pygame.init()

class bil:
  def __init__(self,X_pos,Y_pos, angle):
    self.X_pos=X_pos
    self.Y_pos=Y_pos
    self.angle=angle

  def __str__(self):
    pass

  def lagerUpdate(self):
    pass

S_Width=1080

S_Height=1080

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

run=True

#car = pygame.Rect(300,300,50,50)
car = pygame.image.load("Formula_1_car.png")


x_pos=0
y_pos=0
x_vel=0
y_vel=0

acc_multiplier=0.005

angle =0
angle_vel=0
angle_acc_strength=10
angle_de_acc_strength=10

border_bounce_multiplier=1


w, h = pygame.display.get_surface().get_size()


while run:
  
  screen.fill((0,0,0,0.1))

  
  car_rotated=pygame.transform.rotate(car,angle)
  car_rect=car_rotated.get_rect(center=(x_pos,y_pos))
  screen.blit(car_rotated,car_rect)
  #pygame.draw.rect(screen,(255,0,0,0),car)

  key= pygame.key.get_pressed()
  if key[pygame.K_a]:
    angle= angle+1
  elif key[pygame.K_d]:
    angle= angle-1
  
  if key[pygame.K_s]:
    x_vel=x_vel+math.sin(angle*math.pi/180)*acc_multiplier
    y_vel=y_vel+math.cos(angle*math.pi/180)*acc_multiplier
  elif key[pygame.K_w]:
    x_vel=x_vel-math.sin(angle*math.pi/180)*acc_multiplier
    y_vel=y_vel-math.cos(angle*math.pi/180)*acc_multiplier

  x_pos=x_pos+x_vel
  y_pos=y_pos+y_vel

  if x_pos<0:
    x_pos=0
    x_vel=x_vel*-border_bounce_multiplier
  if x_pos>w:
    x_pos=w
    x_vel=x_vel*-border_bounce_multiplier

  if y_pos<0:
    y_pos=0
    y_vel=y_vel*-border_bounce_multiplier
  elif y_pos>h:
    y_pos=h
    y_vel=y_vel*-border_bounce_multiplier

  if key[pygame.K_ESCAPE]:
    run = False

  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      run = False
  pygame.display.update()


pygame.quit()