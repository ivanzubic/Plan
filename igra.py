import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("F1 Images")

clock = pygame.time.Clock()

# UČITAVANJE SLIKA
player_img = pygame.image.load("image.png")
enemy_img = pygame.image.load("protivnik.png")

# Resize (važan!)
player_img = pygame.transform.scale(player_img, (60, 100))
enemy_img = pygame.transform.scale(enemy_img, (60, 100))

pygame.mixer.init()

engine_sound = pygame.mixer.Sound("engine.wav")
engine_sound.set_volume(0.3)
engine_sound.play(-1)

# Igrač
player = pygame.Rect(250, 500, 40, 70)
speed = 5

# Protivnici
enemies = []

# Score
score = 0
font = pygame.font.SysFont(None, 36)

scroll_y = 0
started = False
engine_playing = False

def draw():
    win.fill((34, 139, 34))

    # Cesta
    pygame.draw.rect(win, (50, 50, 50), (100, 0, 300, HEIGHT))

    # Linije
    for i in range(-40, HEIGHT, 40):
        pygame.draw.rect(win, (255, 255, 255), (240, i + scroll_y, 20, 20))

    # Igrač (SLIKA)
    win.blit(player_img, (player.x, player.y))

    # Protivnici (SLIKE)
    for e in enemies:
        win.blit(enemy_img, (e.x, e.y))

    # Score
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(text, (10, 10))

    pygame.display.update()

def main():
    global scroll_y, score, started, engine_playing
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x > 100:
            player.x -= speed
        if keys[pygame.K_RIGHT] and player.x < 360:
            player.x += speed
        if keys[pygame.K_UP]:
            started = True
            scroll_y += 10
            score += 1
            if not engine_playing:
                engine_sound.play(-1)
                engine_playing = True
                
        if keys[pygame.K_DOWN]:
            scroll_y += 3

        if scroll_y > 40:
            scroll_y = 0

        # Spawn
        if random.randint(1, 25) == 1:
            x = random.randint(120, 340)
            enemies.append(pygame.Rect(x, -80, 40, 70))

        # Kretanje
        for e in enemies[:]:
            if started:
                e.y += 6

            if player.colliderect(e):
                print("GAME OVER")
                pygame.quit()
                return

            if e.y > HEIGHT:
                enemies.remove(e)
                score += 5

        draw()
 
    pygame.quit()

main()