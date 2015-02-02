import pygame
import game
import board

MAP_SCREEN_WIDTH = 1024
MAP_SCREEN_HEIGHT = 768

def main():
    pygame.init()
    
    map_screen = pygame.display.set_mode((MAP_SCREEN_WIDTH, MAP_SCREEN_HEIGHT))
    pygame.display.set_caption("Mage Knight: Map")
    mage_knight = game.Game(map_screen)
    map_board = board.Board(map_screen, mage_knight)

    done = False
    clock = pygame.time.Clock()

    temp_mousedown_coordinates = None
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                temp_mousedown_coordinates = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                map_board.check_mousedrag(temp_mousedown_coordinates, pygame.mouse.get_pos())
                
                
        map_board.build()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
