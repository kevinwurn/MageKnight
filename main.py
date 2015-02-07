import pygame
import game
import board
import gui_start_panel
import player
import panel_player
import panel_other
import panel_offers

GAME_SCREEN_WIDTH = 1024
GAME_SCREEN_HEIGHT = 768
GAME_SCREEN_COLOR = (200, 200, 200)
MAGNIFY_FACTOR = 3.5  

def main():
    pygame.init()
    
    game_screen = pygame.display.set_mode((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))
    pygame.display.set_caption("Mage Knight")
    game_engine = game.Game(game_screen)
    start_screen = gui_start_panel.GUIStartPanel(game_screen)
    start_screen.launch()
    if start_screen.player == player.ARYTHREA:
        game_engine.chosen_player = player.ARYTHREA
        arythrea = player.Arythrea(game_engine)
        arythrea.load()
        game_engine.magnify_collection.append(arythrea)
        game_engine.player_group.add(arythrea)
        game_engine.arythrea = arythrea
    else:
        game_engine.chosen_player = player.ARYTHREA
        arythrea = player.Arythrea(game_engine)
        game_engine.arythrea = arythrea
        arythrea.load()
        game_engine.magnify_collection.append(arythrea)
        game_engine.player_group.add(arythrea)
        game_engine.arythrea = arythrea
    game_engine.setup()
    game_board = board.Board(game_screen, game_engine)
    player_board = panel_player.PanelPlayer(game_screen, game_engine, game_board)
    other_board = panel_other.PanelOther(game_screen, game_engine, game_board)
    offers_board = panel_offers.PanelOffers(game_screen, game_engine, game_board)

    done = False
    clock = pygame.time.Clock()
    temp_mousedown_coordinates = None
    magnify_sprites = []
    magnify_sprite = pygame.sprite.GroupSingle()
    magnify_image_original_width = 0
    magnify_image_original_height = 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                temp_mousedown_coordinates = pygame.mouse.get_pos()
                player_board.check_btn_start_round_clicked(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                game_board.check_mousedrag(temp_mousedown_coordinates, pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    for s in game_engine.magnify_collection:
                        if s.rect.collidepoint(pygame.mouse.get_pos()):
                            magnify_sprites.append(s)
                    if magnify_sprites:
                        # create new image that is much larger - save original dimensions
                        magnify_image_original_width = magnify_sprites[0].rect.width
                        magnify_image_original_height = magnify_sprites[0].rect.height
                        can_magnify = True
                        try:
                            magnify_sprites[0].image = pygame.image.load(magnify_sprites[0].relative_path_filename).convert_alpha()
                        except AttributeError:
                            magnify_sprites = []
                            can_magnify = False
                            print("can't magnify")
                        if can_magnify:
                            magnify_sprites[0].image = pygame.transform.smoothscale(magnify_sprites[0].image, (int(magnify_image_original_width*MAGNIFY_FACTOR), int(magnify_image_original_height*MAGNIFY_FACTOR)))
                            magnify_sprite.add(magnify_sprites[0])
            elif event.type == pygame.KEYUP:
                if magnify_sprites:
                        magnify_sprites[0].image = pygame.image.load(magnify_sprites[0].relative_path_filename).convert_alpha()
                        magnify_sprites[0].image = pygame.transform.smoothscale(magnify_sprites[0].image, (magnify_image_original_width, magnify_image_original_height))
                        magnify_sprite.add(magnify_sprites[0])
                        magnify_sprites = []

        game_screen.fill(GAME_SCREEN_COLOR)
        game_board.build()
        player_board.paint()
        other_board.paint()
        offers_board.paint()
        magnify_sprite.draw(game_screen) 
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    
if __name__ == "__main__":
    main()
