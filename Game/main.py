import pygame
import sys
import random

# ==========================================
# 1. INITIALIZATION (Must be done first!)
# ==========================================
pygame.init()  # Starts the engine. Do not put font code before this!

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Space Shooter")
clock = pygame.time.Clock()
FPS = 60

# Set up the font safely after pygame.init()
font = pygame.font.SysFont("Arial", 28)

# Colors (R, G, B)
BACKGROUND = (15, 15, 25)
PLAYER_COLOR = (50, 150, 255)
ENEMY_COLOR = (255, 70, 70)
LASER_COLOR = (255, 255, 50)
TEXT_COLOR = (255, 255, 255)


# ==========================================
# 2. SPRITE CLASSES (The Objects)
# ==========================================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()

        # Start at the bottom center
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed = 6

    def update(self):
        # Keyboard movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect()

        # Spawn randomly above the screen
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        # Delete if it falls off the bottom
        if self.rect.top > HEIGHT:
            self.kill()


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((6, 15))
        self.image.fill(LASER_COLOR)
        self.rect = self.image.get_rect()

        # Shoot from the player's position
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -8  # Moves up

    def update(self):
        self.rect.y += self.speed
        # Delete if it flies off the top
        if self.rect.bottom < 0:
            self.kill()


# ==========================================
# 3. GAME SETUP
# ==========================================
# Create groups to hold our objects
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
lasers = pygame.sprite.Group()

# Create the player
player = Player()
all_sprites.add(player)

score = 0
game_over = False
running = True

# ==========================================
# 4. MAIN GAME LOOP
# ==========================================
while running:
    # --- A. Events (Input) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shoot laser on SPACE bar press
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                laser = Laser(player.rect.centerx, player.rect.top)
                all_sprites.add(laser)
                lasers.add(laser)

    # --- B. Game Logic ---
    if not game_over:
        # Spawn enemies randomly (roughly 1-in-40 chance per frame)
        if random.randint(1, 40) == 1:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Move all objects
        all_sprites.update()

        # Check: Did a laser hit an enemy? (True, True deletes both)
        hits = pygame.sprite.groupcollide(enemies, lasers, True, True)
        for hit in hits:
            score += 10

        # Check: Did an enemy hit the player?
        if pygame.sprite.spritecollideany(player, enemies):
            game_over = True

    # --- C. Drawing ---
    screen.fill(BACKGROUND)

    if game_over:
        # Draw "Game Over" screen
        over_text = font.render(f"GAME OVER! Final Score: {score}", True, ENEMY_COLOR)
        text_rect = over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(over_text, text_rect)

        restart_text = font.render("Close window to exit", True, TEXT_COLOR)
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        screen.blit(restart_text, restart_rect)
    else:
        # Draw the game
        all_sprites.draw(screen)
        score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(score_text, (15, 15))

    # --- D. Screen Update ---
    pygame.display.flip()
    clock.tick(FPS)

# ==========================================
# 5. CLEAN EXIT
# ==========================================
pygame.quit()
sys.exit()