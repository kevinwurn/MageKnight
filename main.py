import pygame
import board

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

def main():
    pygame.init()
    board_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mage Knight")
    game_board = board.Board(board_screen, board.BOARD_TYPE_WEDGE)

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_board.check_board_zone(pygame.mouse.get_pos())
                
        game_board.build()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
