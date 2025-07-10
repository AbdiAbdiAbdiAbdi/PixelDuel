import pygame

class Fighter():
    #init func
    def __init__(self,x,y):
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.num_of_jumps = 0
        self.attack_type = 0
        self.attacking = False
        self.health = 100
    
    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        # d = delta (change in axis)
        dx = 0
        dy = 0


        #get keypress
        key = pygame.key.get_pressed()

        #can only do the following if not attacing
        if self.attacking == False:
            #movement keys
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED
            
            #jump
            #TODO add Double Jump
            if key[pygame.K_k] and self.jump == False:
                self.vel_y = -40
                self.jump = True
            
            #attack key
            if key[pygame.K_j]:
                self.attack_type = 1
                self.attack(surface, target)
            


        #applyin gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #make sure play stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left

        if self.rect.right + dx > 1000:
            dx = screen_width - self.rect.right
        
        if self.rect.bottom + dy > screen_height - 21:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 21 - self.rect.bottom

        #make sure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False

        else:
            self.flip = True

        #update player postion
        self.rect.x += dx
        self.rect.y += dy

    
    #attack func
    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)

        if attacking_rect.colliderect(target.rect):
            print("Hit!")
            target.health -= 5

        



        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    #draw func
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

