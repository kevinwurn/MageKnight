import pygame
import board

MAP_SCREEN_WIDTH = 1024
MAP_SCREEN_HEIGHT = 768

def main():
    pygame.init()
    
    map_screen = pygame.display.set_mode((MAP_SCREEN_WIDTH, MAP_SCREEN_HEIGHT))
    pygame.display.set_caption("Mage Knight: Map")
    map_board = board.Board(map_screen, board.BOARD_TYPE_WEDGE)

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                map_board.click_board_zone(pygame.mouse.get_pos())
                
        map_board.build()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
