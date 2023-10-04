from pybraille import convertText
import pygame

print("hello", convertText("hello"))

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Segoeui', 30)
print(pygame.font.get_fonts())

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption('Braille Rendering Tester')

background_color = (30,30,30)
screen.fill(background_color)


running = True
while running:
    
    pygame.display.flip()

    textsurface = myfont.render(convertText('Hello'), False, (255,255,255))
    screen.blit(textsurface, (0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False