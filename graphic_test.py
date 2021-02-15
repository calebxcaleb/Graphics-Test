# Simple pygame program

# Import and initialize the pygame library
import pygame
import random

pygame.init()

# Set up the drawing window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Show Text')

x = 250
y = 250
r = 25
r_max = 35
r_min = 15
w_min = 6
w_max = r
r_speed = 0.01
col = (r - r_min) / (r_max - r_min) * 255
w = (r - r_min) / (r_max - r_min) * w_max + w_min
speed = 0.1

AI_r = 15
AI_x = random.randint(AI_r, screen_width-AI_r)
AI_y = random.randint(AI_r, screen_height-AI_r)
AI_x_speed = 0
AI_y_speed = 0
AI_speed = 0.05
AI_count = 0
AI_max_count = 1000

R = random.randint(0, 255)
G = random.randint(0, 255)
B = random.randint(0, 255)

count = 0

font1 = pygame.font.Font('freesansbold.ttf', 256)
text = font1.render(str(count), True, (255-R, 255-G, 255-B), (R, G, B))
textRect = text.get_rect()
textRect.center = (screen_width // 2, screen_height // 2)

# Run until the user asks to quit
running = True
while running:

    text = font1.render(str(count), True, (255-R, 255-G, 255-B), (R, G, B))
    textRect = text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 2)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((R, G, B))
    screen.blit(text, textRect)
    pygame.draw.rect(screen, (255 - R, 255 - G, 255 - B), (25, 25, screen_width - 50, screen_height - 50), 3)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        y -= speed
    if pressed[pygame.K_s]:
        y += speed
    if pressed[pygame.K_a]:
        x -= speed
    if pressed[pygame.K_d]:
        x += speed

    if x + r > screen_width:
        x = screen_width - r
    if x - r < 0:
        x = r
    if y + r > screen_height:
        y = screen_height - r
    if y - r < 0:
        y = r

    AI_count += 1

    if AI_count >= AI_max_count:
        AI_count = 0
        AI_x_speed = AI_speed * random.randint(-1, 1)
        AI_y_speed = AI_speed * random.randint(-1, 1)

    AI_x += AI_x_speed
    AI_y += AI_y_speed

    if AI_x + AI_r > screen_width:
        AI_x = screen_width - AI_r
    if AI_x - AI_r < 0:
        AI_x = AI_r
    if AI_y + AI_r > screen_height:
        AI_y = screen_height - AI_r
    if AI_y - AI_r < 0:
        AI_y = AI_r

    if r >= r_max and r_speed > 0:
        r_speed *= -1
    if r <= r_min and r_speed < 0:
        r_speed *= -1

    r += r_speed
    col = (r - r_min) / (r_max - r_min) * 255
    w = (1 - (r - r_min) / (r_max - r_min)) * w_max + w_min

    if x - r < AI_x + AI_r and x + r > AI_x - AI_r and y - r < AI_y + AI_r and y + r > AI_y - AI_r:
        AI_x = random.randint(AI_r, screen_width - AI_r)
        AI_y = random.randint(AI_r, screen_height - AI_r)
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        count += 1

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (255 - R, 255 - G, 255 - B), (AI_x, AI_y), AI_r)
    pygame.draw.circle(screen, (col, col, col), (x, y), r, int(w))
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 25)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()