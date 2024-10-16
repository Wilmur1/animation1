import pygame
import sys
import time
pygame.init()
screen = pygame.display.set_mode((1520,780))
pygame.display.set_caption("animation")

image1 = pygame.image.load("animation/Images/Image1.jpg")
resize1 = pygame.transform.scale(image1,(1520,780))
image2 = pygame.image.load("animation/Images/Image2.jpg")
resize2 = pygame.transform.scale(image2,(1520,780))   
image3 = pygame.image.load("animation/Images/Image3.jpg")
resize3 = pygame.transform.scale(image3,(1520,780))

font = pygame.font.SysFont("arial",50)

while True:
    screen.blit(resize1,(0,0))
    text = font.render("Happy Birthday",False,"blue")
    screen.blit(text,(100,100))
    pygame.display.update()
    time.sleep(2)
    
    screen.blit(resize2,(0,0))
    text = font.render("Have a good day",True,"blue")
    screen.blit(text,(100,100))
    pygame.display.update()
    time.sleep(2)
    
    screen.blit(resize3,(0,0))
    text = font.render("From William",True,"blue")
    screen.blit(text,(700,370))
    pygame.display.update()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    