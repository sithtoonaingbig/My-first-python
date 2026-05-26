import pygame
import random
import sys

# Initialize
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# Player
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 70
player_speed = 7

# Enemy
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = -50
enemy_speed = 6

# Score
score = 0
font = pygame.font.SysFont(None, 40)

# Game loop
running = True

while running:

    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player inside screen
    if player_x < 0:
        player_x = 0

    if player_x > WIDTH - player_size:
        player_x = WIDTH - player_size

    # Enemy movement
    enemy_y += enemy_speed

    # Respawn enemy
    if enemy_y > HEIGHT:
        enemy_y = -50
        enemy_x = random.randint(0, WIDTH - enemy_size)
        score += 1
        enemy_speed += 0.2

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        print("Game Over! Score:", score)
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE,
                     (player_x, player_y, player_size, player_size))

    pygame.draw.rect(screen, RED,
                     (enemy_x, enemy_y, enemy_size, enemy_size))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    # Update display
    pygame.display.update()

pygame.quit()