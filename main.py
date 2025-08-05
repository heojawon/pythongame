import pygame

pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Pygame Example")

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 채우기
    screen.fill(white)

    # 사각형 그리기
    pygame.draw.rect(screen, blue, [200, 150, 400, 300])

    # 화면 업데이트
    pygame.display.flip()

pygame.quit()