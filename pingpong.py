import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
BALL_SPEED = 5
PADDLE_SPEED = 10
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong Game")

ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

player1_x, player2_x = 50, WIDTH - 50
player1_y, player2_y = HEIGHT // 2, HEIGHT // 2
paddle_height = 100
paddle_width = 10
player1_dy, player2_dy = 0, 0

score1, score2 = 0, 0
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_dy = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                player1_dy = PADDLE_SPEED

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1_dy = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2_dy = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                player2_dy = PADDLE_SPEED
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2_dy = 0

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_dy *= -1

    if (
        (ball_x <= player1_x + paddle_width and player1_y <= ball_y <= player1_y + paddle_height) or
        (ball_x >= player2_x - paddle_width and player2_y <= ball_y <= player2_y + paddle_height)
    ):
        ball_dx *= -1

    if ball_x <= 0:
        score2 += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx *= -1
    elif ball_x >= WIDTH:
        score1 += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx *= -1

    player1_y += player1_dy
    player2_y += player2_dy

    player1_y = max(0, min(HEIGHT - paddle_height, player1_y))
    player2_y = max(0, min(HEIGHT - paddle_height, player2_y))

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (player2_x - paddle_width, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x - 10, ball_y - 10, 20, 20))

    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 40, 20))

    pygame.display.flip()

    pygame.time.Clock().tick(60)