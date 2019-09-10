import pygame.freetype  # Import the freetype module.

pygame.init()
screen = pygame.display.set_mode((800, 600))
GAME_FONT = pygame.freetype.Font('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 24)
ONE_PLAYER_FONT = pygame.freetype.Font('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 24)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    GAME_FONT.render_to(screen, (300, 150), "Cartões Malucos!", (0, 0, 0))
    GAME_FONT.render_to(screen, (300, 250), "One Player", (0, 0, 0))
    ONE_PLAYER_FONT.render("One Player", (255, 255, 255), (0, 0, 0))
    one_player_font_rect = ONE_PLAYER_FONT.get_rect("bla")
    one_player_font_rect.right = 300
    one_player_font_rect.height = 250
    pygame.display.flip()

pygame.quit()
