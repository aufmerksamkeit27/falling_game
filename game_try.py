import pygame
import random
import time


pygame.font.init()

# display

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("my first game")

player = pygame.Rect(600, 600, 50, 60)

font = pygame.font.SysFont("arial", 30)

falling_obj = []
falling_gain = []

# speed

player_vel = 20
falling_speed = 1200


# clock

clock = pygame.time.Clock()
start_time = 0


spawn_timer = 0
spawn_delay = 1500

points = 0

# start here

run = True
game_started = False

while run:
    dt = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_started:
                game_started = True
                start_time = time.time()
# player position on each time

    points_gain = font.render(f"Points (Blue) : {points}", True, "yellow")
    keys = pygame.key.get_pressed()

    if game_started:
        elapsed_time = int(time.time() - start_time)

        # keys here

        if keys[pygame.K_RIGHT] and player.x + player.width + player_vel <= WIDTH:
            player.x += player_vel
        if keys[pygame.K_LEFT] and player.x - player_vel >= 0:
            player.x -= player_vel
        if keys[pygame.K_UP] and player.y - player_vel >= 0:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player.height + player_vel <= HEIGHT:
            player.y += player_vel

    # spawing objs increseing

        spawn_timer += dt * 1000

        if spawn_timer >= spawn_delay:

            # white rect

            x = random.randint(0, WIDTH - 20)
            y = random.randint(-150, -20)
            falling_obj.append(pygame.Rect(x, y, 20, 20))

            # blue rect

            x = random.randint(0, WIDTH - 20)
            y = random.randint(-150, -20)
            falling_gain.append(pygame.Rect(x, y, 20, 20))

            spawn_timer = 0

    # falling objs speed

        for i in falling_obj[:]:
            i.y += falling_speed * dt
            if i.y >= HEIGHT:
                falling_obj.remove(i)

            if player.colliderect(i):

                run = False

        for i in falling_gain[:]:
            i.y += falling_speed * dt
            if i.y >= HEIGHT:
                falling_gain.remove(i)

            if player.colliderect(i):
                points += 1
                falling_gain.remove(i)
    else:
        elapsed_time = 0
    # draw here

    screen.fill((0, 0, 0))
    if not game_started:
        start_text = font.render("Start-- SPACE", True, "white")

        rules_text = font.render(
            "  White-- AVOID & Blue -- POINTS", True, "yellow")
        screen.blit(start_text, (WIDTH//2 - start_text.get_width() //
                    2, HEIGHT//2 - start_text.get_height() // 2 - 30))
        screen.blit(rules_text, (WIDTH//2 - start_text.get_width() - 20 //
                    2, HEIGHT//2 - start_text.get_height() // 2 + 30))
        pygame.display.update()

    else:
        pygame.draw.rect(screen, ("red"), player)
        for i in falling_obj:
            pygame.draw.rect(screen, ("white"), i)
        for i in falling_gain:
            pygame.draw.rect(screen, ("blue"), i)
        texture = font.render(f" Time : {elapsed_time}s", True, "yellow")
        screen.blit(texture, (20, 20))

        screen.blit(points_gain, (20, 60))
        pygame.display.update()

pygame.quit()
