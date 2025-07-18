import pygame

class Fighter:
    def __init__(self, x, y, color, controls):
        self.rect = pygame.Rect(x, y, 80, 80)  # Blob size (80x80)
        self.color = color
        self.controls = controls
        self.vel_y = 0
        self.jump = False
        self.health = 100
        self.attacking = False
        self.speed = 8
        self.gravity = 2

    def move(self, screen_width, screen_height, surface, target, effects):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()

        if not self.attacking:
            if keys[self.controls['left']]:
                dx = -self.speed
            if keys[self.controls['right']]:
                dx = self.speed

            if keys[self.controls['jump']] and not self.jump:
                self.vel_y = -30
                self.jump = True

            if keys[self.controls['attack_punch']]:
                self.attack(surface, target, effects, "punch")
            elif keys[self.controls['attack_special']]:
                self.attack(surface, target, effects, "special")

        self.vel_y += self.gravity
        dy += self.vel_y

        # Stay on screen horizontally
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        # Stay on floor vertically
        floor = screen_height - 50
        if self.rect.bottom + dy > floor:
            dy = floor - self.rect.bottom
            self.vel_y = 0
            self.jump = False

        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target, effects, attack_type):
        self.attacking = True
        attack_rect = pygame.Rect(self.rect.centerx - 40, self.rect.y, 80, 80)
        if attack_rect.colliderect(target.rect):
            target.health -= 5 if attack_type == "punch" else 10
            # Add hit effect, sounds etc here
        # Reset attacking after small delay (simple example)
        pygame.time.set_timer(pygame.USEREVENT + 1, 300)

    def draw(self, surface):
        center = self.rect.center
        radius = self.rect.width // 2

        pygame.draw.circle(surface, self.color, center, radius)

        # Subtle highlight for 3D effect
        highlight_color = (
            min(self.color[0] + 60, 255),
            min(self.color[1] + 60, 255),
            min(self.color[2] + 60, 255),
        )
        highlight_pos = (center[0] - radius // 3, center[1] - radius // 3)
        pygame.draw.circle(surface, highlight_color, highlight_pos, radius // 2)
