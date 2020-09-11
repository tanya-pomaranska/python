import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500
WIDTH_IMAGE=50
HEIGHT_IMAGE=50

# Call this function so the Pygame library can initialize itself
#pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([WIDTH_DISPLAY, HEIGHT_DISPLAY])

# This sets the name of the window
pygame.display.set_caption('Fly')

clock = pygame.time.Clock()

#обновляємо екран
pygame.display.update()

# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
#background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load(r"F:\Tanya_Python\repository\python\Images\plane.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (WIDTH_IMAGE, HEIGHT_IMAGE))

#Якщо в зображення не має прозорого слою, то щоб його встановити,
#необхідно використати метод set_colorkey() класу Surface:
player_image.set_colorkey(BLACK)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


# Get the current mouse position. This returns the position
    # as a list of two numbers.
#повертає поточну позицію мишки на екрані
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]


    screen.fill((0,0,0))
    # Copy image to screen:
#копіює картинку на екран

    if x > 0:
        x = x
    if x > WIDTH_DISPLAY-WIDTH_IMAGE:
        x = WIDTH_DISPLAY-WIDTH_IMAGE
    if y > 5:
        y = y
    if y>HEIGHT_DISPLAY-HEIGHT_IMAGE:
        y = y-HEIGHT_IMAGE

    screen.blit(player_image, [x, y])

#обновляємо екран
    pygame.display.flip()

    clock.tick(60)


#pygame.quit()