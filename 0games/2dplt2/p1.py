import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5
isJump = False 
run = True
jumpCount = 10 

class player:
    pass

class enemy():
    pass 
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    
    if not (isJump):
        if keys[pygame.K_UP]:
            y -= vel

        if keys[pygame.K_DOWN]:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True 
    else:
        if jumpCount>= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount **2) * 0.5 * neg
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height)) 
    pygame.draw.rect(win,(255,255,0),(90,90,width,height))  
    pygame.draw.rect(win,(255,255,255),(140,140,width,height))
    pygame.draw.rect(win,(0,0,255),(140,140,width,height))
    pygame.display.update() 
    
pygame.quit()