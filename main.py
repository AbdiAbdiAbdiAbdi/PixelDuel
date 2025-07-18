import pygame
from fighter import Fighter
# from effects import HitEffect  # Uncomment if you have this

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blob Battles")

# Load background image
try:
    bg_img = pygame.image.load("assets/background.jpg").convert_alpha()
    scale_bg = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Background loaded successfully!")
except Exception as e:
    print(f"Error loading background image: {e}")
    scale_bg = None

clock = pygame.time.Clock()

YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

font = pygame.font.SysFont('arialblack', 24)

effects = []  # Placeholder for effects list

def draw_bg():
    if scale_bg:
        screen.blit(scale_bg, (0, 0))
    else:
        screen.fill((30, 30, 40))

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, GREY, (x - 5, y + 2, 410, 35))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

def draw_attack_text(text, x, y):
    render = font.render(text, True, WHITE)
    screen.blit(render, (x, y))

# Controls for red blob
controls1 = {
    'left': pygame.K_a,
    'right': pygame.K_d,
    'jump': pygame.K_w,
    'attack_punch': pygame.K_f,
    'attack_special': pygame.K_g
}

# Controls for blue blob
controls2 = {
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'jump': pygame.K_UP,
    'attack_punch': pygame.K_SLASH,
    'attack_special': pygame.K_PERIOD
}

fighter1 = Fighter(200, 400, (255, 0, 0), controls1)
fighter2 = Fighter(700, 400, (0, 0, 255), controls2)

run = True
while run:
    clock.tick(60)
    attack1_text = ""
    attack2_text = ""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Attack text for red blob
    if keys[controls1['attack_punch']]:
        attack1_text = "Red: Punch!"
    elif keys[controls1['attack_special']]:
        attack1_text = "Red: Special Attack!"

    # Attack text for blue blob
    if keys[controls2['attack_punch']]:
        attack2_text = "Blue: Punch!"
    elif keys[controls2['attack_special']]:
        attack2_text = "Blue: Special Attack!"

    draw_bg()
    # Title removed here, no draw_title()

    draw_health_bar(fighter1.health, 20, 20)
    draw_health_bar(fighter2.health, 580, 20)

    fighter1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter2, effects)
    fighter2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter1, effects)

    fighter1.draw(screen)
    fighter2.draw(screen)

    # Effects update/draw code if any

    if attack1_text:
        draw_attack_text(attack1_text, 20, 70)
    if attack2_text:
        draw_attack_text(attack2_text, 580, 70)

    pygame.display.update()

pygame.quit()
