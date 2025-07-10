import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

#load background image
bg_img = pygame.image.load("assets/background/backdrop.jpg").convert_alpha()
#scale background to screen
scale_bg = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
#Set up clock
clock = pygame.time.Clock()

#define colors (some might not be used)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)


#draw background image func
def draw_bg():
    screen.blit(scale_bg, (0, 0))

#func to draw health bars
def draw_health_bar(health, x, y):
    ratio_of_vitality = health / 100
    pygame.draw.rect(screen, GREY, (x-5, y+2, 410, 35))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio_of_vitality, 30))


#instatiate two fighters
fighter1 = Fighter(200, 400)
fighter2 = Fighter(700, 400)


run = True

while run:
    #Caps framerate at 60FPS
    clock.tick(60)

    

    #event handeler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run  = False

    draw_bg()

    #show players health
    draw_health_bar(fighter1.health, 20, 20)
    draw_health_bar(fighter2.health, 580, 20)


    #move fighters
    fighter1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter2)
    #fighter2.move(SCREEN_WIDTH)

    #draw fighters
    fighter1.draw(screen)
    fighter2.draw(screen)


    #updates screen
    pygame.display.update()
    



#exit pygame

pygame.quit()

