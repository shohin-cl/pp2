import pygame


pygame.init()


screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

ball_color = (255, 0, 0)
ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2


clock = pygame.time.Clock()


def move_ball(dx, dy):
    global ball_x, ball_y
    
    ball_x += dx
    ball_y += dy
    
   
    if ball_x < ball_radius:
        ball_x = ball_radius
    elif ball_x > screen_width - ball_radius:
        ball_x = screen_width - ball_radius
    if ball_y < ball_radius:
        ball_y = ball_radius
    elif ball_y > screen_height - ball_radius:
        ball_y = screen_height - ball_radius


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_ball(0, -20)
            elif event.key == pygame.K_DOWN:
                move_ball(0, 20)
            elif event.key == pygame.K_LEFT:
                move_ball(-20, 0)
            elif event.key == pygame.K_RIGHT:
                move_ball(20, 0)
                
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    
    
    clock.tick(60)

pygame.quit()
