import pygame

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

car = pygame.Rect(300,300,50,50)

while run:
  
  screen.fill((0,0,0,0.1))

  pygame.draw.rect(screen,(255,0,0,0),car)

  key= pygame.key.get_pressed()
  if key[pygame.K_a]:
    car.move_ip(-1,0)
  elif key[pygame.K_d]:
    car.move_ip(1,0)
  
  if key[pygame.K_s]:
    car.move_ip(0,1)
  elif key[pygame.K_w]:
    car.move_ip(0,-1)

  if key[pygame.K_ESCAPE]:
    run = False

  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      run = False
  pygame.display.update()


pygame.quit()