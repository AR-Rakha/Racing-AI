import pygame
import math

import numpy as np



pygame.init()

class bil:
  def __init__(self,X_pos,Y_pos, angle):
    self.X_pos=X_pos
    self.Y_pos=Y_pos
    self.angle=angle

  def __str__(self):
    pass

  

S_Width=1080

S_Height=1080

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

w, h = pygame.display.get_surface().get_size()


run=True

#car = pygame.Rect(300,300,50,50)
car = pygame.image.load("Formula_1_car.png")
car=pygame.transform.scale_by(car,0.5)
track=pygame.image.load("Track.webp")
track_scaled=pygame.transform.scale_by(track,1.4)
track_rect=track_scaled.get_rect(center=(w/2,h/2))

pos=np.array([0,0])
vel=np.array([0,0])

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

air_resistance=1-(0.002)



def getForwardVector(angle):
  return np.array([math.sin(angle*math.pi/180),math.cos(angle*math.pi/180)])
def getRightVector(angle):
  return np.array([math.cos(angle*math.pi/180),-math.sin(angle*math.pi/180)])

def grip(vel,angle,forward_friction_multiplier,sideways_friction_multiplier):
  forward = getForwardVector(angle)
  right = getRightVector(angle)

  forward_comp = np.dot(vel, forward)
  sideways_comp = np.dot(vel, right)

  forward_force = -forward * forward_comp * forward_friction_multiplier
  sideways_force = -right * sideways_comp * sideways_friction_multiplier

  return forward_force + sideways_force
  
  

while run:
  
  screen.fill((0,0,0,0.1))

  
  screen.blit(track_scaled,track_rect)
  
  car_rotated=pygame.transform.rotate(car,angle)
  car_rect=car_rotated.get_rect(center=(pos[0],pos[1]))
  screen.blit(car_rotated,car_rect)

  

  key= pygame.key.get_pressed()
  if key[pygame.K_a]:
    angle= angle+1
  elif key[pygame.K_d]:
    angle= angle-1
  
  if key[pygame.K_s]:
    vel[0]=vel[0]+math.sin(angle*math.pi/180)*acc_multiplier
    vel[1]=vel[1]+math.cos(angle*math.pi/180)*acc_multiplier
  elif key[pygame.K_w]:
    vel[0]=vel[0]-math.sin(angle*math.pi/180)*acc_multiplier
    vel[1]=vel[1]-math.cos(angle*math.pi/180)*acc_multiplier

  pos=np.add(pos,vel)

  if pos[0]<0:
    pos[0]=0
    vel[0]=vel[0]*-border_bounce_multiplier
  if pos[0]>w:
    pos[0]=w
    vel[0]=vel[0]*-border_bounce_multiplier

  if pos[1]<0:
    pos[1]=0
    vel[1]=vel[1]*-border_bounce_multiplier
  elif pos[1]>h:
    pos[1]=h
    vel[1]=vel[1]*-border_bounce_multiplier

  #vel=np.multiply(vel,air_resistance)
  vel=vel+grip(vel,angle,0.001,0.02)

  if key[pygame.K_ESCAPE]:
    run = False

  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      run = False
  pygame.display.update()


pygame.quit()