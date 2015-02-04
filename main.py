import pygame
import game
import board
import start_gui_panel
import player
import player_panel
import other_panel

GAME_SCREEN_WIDTH = 1024
GAME_SCREEN_HEIGHT = 768
GAME_SCREEN_COLOR = (200, 200, 200)

def main():
    pygame.init()
    
    game_screen = pygame.display.set_mode((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))
    pygame.display.set_caption("Mage Knight")
    game_engine = game.Game(game_screen)
    start_screen = start_gui_panel.StartGUIPanel(game_screen)
    #start_screen.launch()
    if start_screen.player == player.ARYTHREA:
        game_engine.current_player = player.ARYTHREA
    else:
        game_engine.current_player = player.ARYTHREA
    arythrea = player.Arythrea(game_engine)        
    game_engine.arythrea = arythrea

    game_engine.setup()
    game_board = board.Board(game_screen, game_engine)
    player_board = player_panel.PlayerPanel(game_screen, game_engine, game_board)
    other_board = other_panel.OtherPanel(game_screen, game_engine, game_board)

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
                game_board.check_mousedrag(temp_mousedown_coordinates, pygame.mouse.get_pos())
                
        game_screen.fill(GAME_SCREEN_COLOR)
        game_board.build()
        player_board.paint()
        other_board.paint()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
