import pygame.draw

from _thread import *

from meta import *
from button import Button
from player import Player
from dice import Dice
from server import start_server, check_server
from network import Network


D4 = Dice(4, D4_IMAGES)
D6 = Dice(6, D6_IMAGES)
D6_2 = Dice(6, D6_IMAGES)
D8 = Dice(8, D8_IMAGES)
D8_2 = Dice(8, D8_IMAGES)
D10 = Dice(10, D10_IMAGES)
D10_2 = Dice(10, D10_IMAGES)
D12 = Dice(12, D12_IMAGES)
D12_2 = Dice(12, D12_IMAGES)
D20 = Dice(20, D20_IMAGES)
D20_2 = Dice(20, D20_IMAGES)
D20_3 = Dice(20, D20_IMAGES)


pygame.display.set_caption("Tyche's Game")


def draw_window():
    if Meta.CURRENT_STATE == ScreenState.START:  # Start Menu
        WINDOW.fill(GREEN)
        draw_game_image(GAME_TITLE, (960, 90), 1)
        quit_button = Button("Quit", 960, 610, 60)
        if quit_button.check_click():
            pygame.quit()
        new_game_button = Button("Single Device", 960, 470, 60)
        if new_game_button.check_click():
            Meta.CURRENT_STATE = ScreenState.NEW_MENU
        local_multiplayer_button = Button("Local Multiplayer", 960, 540, 60)
        if local_multiplayer_button.check_click():
            Meta.IS_MULTIPLAYER = True
            Meta.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
    elif Meta.CURRENT_STATE == ScreenState.JOIN_LOCAL_GAME:  # Join/Create a Local Game
        WINDOW.fill(GREEN)
        if Meta.HAS_SERVER:
            draw_text("Server Active", SMALL_FONT, ORANGE, (960, 200))
        draw_text("Enter Server IP Address:", SMALL_FONT, ORANGE, (960, 350))
        draw_text_input()
        join_server_button = Button("Join Server", 960, 500, 60)
        if join_server_button.check_click():
            Meta.NETWORK = Network(Meta.USER_TEXT)
            Meta.USER_TEXT = ""
            if Meta.NETWORK.success:
                Meta.CURRENT_STATE = ScreenState.NAME_LOCAL_PLAYER
        create_server_button = Button("Create Server", 960, 590, 60)
        if create_server_button.check_click():
            Meta.CURRENT_STATE = ScreenState.CREATE_SERVER
            Meta.CAN_TEXT_INPUT = False
        quit_button = Button("Quit", 960, 690, 60)
        if quit_button.check_click():
            pygame.quit()
    elif Meta.CURRENT_STATE == ScreenState.CREATE_SERVER:  # Sets Player Count for the Server
        WINDOW.fill(GREEN)
        draw_text("How many players?", BIG_FONT, ORANGE, (960, 100))
        quit_button = Button("Quit", 1060, 600, 60)
        if quit_button.check_click():
            pygame.quit()
        back_button = Button("Back", 860, 600, 60)
        if back_button.check_click():
            Meta.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
        two_player_button = Button("Two Players", 820, 300, 60, BLUE, ORANGE, SMALL_FONT, 220)
        three_player_button = Button("Three Players", 1100, 300, 60, BLUE, ORANGE, SMALL_FONT, 220)
        four_player_button = Button("Four Players", 820, 400, 60, BLUE, ORANGE, SMALL_FONT, 220)
        five_player_button = Button("Five Players", 1100, 400, 60, BLUE, ORANGE, SMALL_FONT, 220)
        if two_player_button.check_click():
            if check_server(Meta.USER_TEXT):
                Meta.HAS_SERVER = True
                start_new_thread(start_server, (2, Meta.USER_TEXT, Meta.BOARD_SQUARES, Meta.RED_DRAW_DECK, Meta.BLUE_DRAW_DECK))
                Meta.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
        elif three_player_button.check_click():
            if check_server(Meta.USER_TEXT):
                Meta.HAS_SERVER = True
                start_new_thread(start_server, (3, Meta.USER_TEXT, Meta.BOARD_SQUARES, Meta.RED_DRAW_DECK, Meta.BLUE_DRAW_DECK))
                Meta.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
        elif four_player_button.check_click():
            if check_server(Meta.USER_TEXT):
                Meta.HAS_SERVER = True
                start_new_thread(start_server, (4, Meta.USER_TEXT, Meta.BOARD_SQUARES, Meta.RED_DRAW_DECK, Meta.BLUE_DRAW_DECK))
                Meta.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
        elif five_player_button.check_click():
            if check_server(Meta.USER_TEXT):
                Meta.HAS_SERVER = True
                start_new_thread(start_server, (5, Meta.USER_TEXT, Meta.BOARD_SQUARES, Meta.RED_DRAW_DECK, Meta.BLUE_DRAW_DECK))
                Meta.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
    elif Meta.CURRENT_STATE == ScreenState.NAME_LOCAL_PLAYER:  # Names the Player in a Local Game
        WINDOW.fill(GREEN)
        quit_button = Button("Quit", 960, 600, 60)
        if quit_button.check_click():
            pygame.quit()
        draw_text("Enter your Player Name", MEDIUM_FONT, ORANGE, (960, 69))
        draw_text_input()
        if Meta.PLAYER_NUMBER == 69:
            if Meta.TEXT_CONFIRMED:
                data = ("Name", Meta.USER_TEXT)
                response = Meta.NETWORK.send(data)
                Meta.PLAYER_NUMBER = response[0]
                Meta.PLAYER_COUNT = response[1]
                Meta.TEXT_CONFIRMED = False
                Meta.CAN_TEXT_INPUT = False
        else:
            network_response = Meta.NETWORK.send("?")
            if network_response is not False:
                Meta.PLAYERS = network_response[0]
                for x in range(len(Meta.PLAYERS)):
                    Meta.BOARD_SQUARES[0].players.append(Meta.PLAYERS[x])
                Meta.RED_DRAW_DECK = network_response[1]
                Meta.BLUE_DRAW_DECK = network_response[2]
                Meta.CURRENT_STATE = ScreenState.PLAYING_LOCAL_GAME
    elif Meta.CURRENT_STATE == ScreenState.NEW_MENU:  # New Game Menu
        WINDOW.fill(GREEN)
        draw_text("How many players?", BIG_FONT, ORANGE, (960, 100))
        quit_button = Button("Quit", 1060, 600, 60)
        if quit_button.check_click():
            pygame.quit()
        back_button = Button("Back", 860, 600, 60)
        if back_button.check_click():
            Meta.CURRENT_STATE = ScreenState.START
        two_player_button = Button("Two Players", 820, 300, 60, BLUE, ORANGE, SMALL_FONT, 220)
        three_player_button = Button("Three Players", 1100, 300, 60, BLUE, ORANGE, SMALL_FONT, 220)
        four_player_button = Button("Four Players", 820, 400, 60, BLUE, ORANGE, SMALL_FONT, 220)
        five_player_button = Button("Five Players", 1100, 400, 60, BLUE, ORANGE, SMALL_FONT, 220)
        if two_player_button.check_click():
            Meta.PLAYER_COUNT = 2
        elif three_player_button.check_click():
            Meta.PLAYER_COUNT = 3
        elif four_player_button.check_click():
            Meta.PLAYER_COUNT = 4
        elif five_player_button.check_click():
            Meta.PLAYER_COUNT = 5
        if Meta.PLAYER_COUNT is not None:
            Meta.CAN_TEXT_INPUT = True
            Meta.CURRENT_STATE = ScreenState.PLAYER_NAMING
    elif Meta.CURRENT_STATE == ScreenState.PLAYER_NAMING:  # Player Naming Menu
        WINDOW.fill(GREEN)
        quit_button = Button("Quit", 960, 600, 60)
        if quit_button.check_click():
            pygame.quit()
        elif Meta.CURRENT_PLAYER == Meta.PLAYER_COUNT:
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_ONE
            Meta.CURRENT_PLAYER = 0
            random.shuffle(Meta.PLAYERS)
        else:
            match Meta.CURRENT_PLAYER:  # Draw Screen Title
                case 0:
                    draw_text("Enter Player One's Name", MEDIUM_FONT, ORANGE, (960, 69))
                case 1:
                    draw_text("Enter Player Two's Name", MEDIUM_FONT, ORANGE, (960, 69))
                case 2:
                    draw_text("Enter Player Three's Name", MEDIUM_FONT, ORANGE, (960, 69))
                case 3:
                    draw_text("Enter Player Four's Name", MEDIUM_FONT, ORANGE, (960, 69))
                case 4:
                    draw_text("Enter Player Five's Name", MEDIUM_FONT, ORANGE, (960, 69))
            draw_text_input()
            if Meta.TEXT_CONFIRMED:
                Meta.PLAYERS.append(Player(Meta.CURRENT_PLAYER, Meta.USER_TEXT))
                Meta.USER_TEXT = ""
                Meta.CURRENT_PLAYER += 1
                Meta.TEXT_CONFIRMED = False
    elif Meta.CURRENT_STATE == ScreenState.GAME_INTRO_ONE:
        WINDOW.fill((30, 100, 150))
        quit_button = Button("Quit", 200, 600, 60)
        if quit_button.check_click():
            pygame.quit()
        draw_text("Welcome to Tyche's Game", BIG_FONT, ORANGE, (960, 69))
        page_background = pygame.Rect((460, 150), (1000, 850))
        pygame.draw.rect(WINDOW, PASTEL_GREEN, page_background, 0, 5)
        draw_text("Scenario", MEDIUM_FONT, ORANGE, (960, 190))
        draw_text("Tyche, the Goddess of Chance, has had enough of humanity", SMALL_FONT, BLACK, (960, 250))
        draw_text("blaming Luck for their own errors, so she has decided to", SMALL_FONT, BLACK, (960, 290))
        draw_text("entrap some humans in her game to show them what Luck", SMALL_FONT, BLACK, (960, 330))
        draw_text("truly means.", SMALL_FONT, BLACK, (960, 370))
        draw_text("However, Tyche's game isn't all about Luck and Chance. There's", SMALL_FONT, BLACK, (960, 490))
        draw_text("also a degree of human skill involved in the process. This skill", SMALL_FONT, BLACK, (960, 530))
        draw_text("comes in several different forms, which you will learn of in time.", SMALL_FONT, BLACK, (960, 570))
        draw_text("You find yourselves in a dark room containing just an empty table.", SMALL_FONT, BLACK, (960, 690))
        next_button = Button(">", 1420, 760, 70, WHITE, BLACK, MEDIUM_FONT)
        if next_button.check_click() or Meta.RIGHT_ARROW_DOWN:
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
    elif Meta.CURRENT_STATE == ScreenState.GAME_INTRO_TWO:
        WINDOW.fill((30, 100, 150))
        quit_button = Button("Quit", 200, 600, 60)
        if quit_button.check_click():
            pygame.quit()
        draw_text("Welcome to Tyche's Game", BIG_FONT, ORANGE, (960, 69))
        page_background = pygame.Rect((460, 150), (1000, 850))
        pygame.draw.rect(WINDOW, PASTEL_GREEN, page_background, 0, 5)
        draw_text("Understanding the Game", MEDIUM_FONT, ORANGE, (960, 190))
        draw_text("Tyche's game is visually similar to Snakes & Ladders with", SMALL_FONT, BLACK, (960, 250))
        draw_text("the fact that you need to ascend the board to win. However,", SMALL_FONT, BLACK, (960, 290))
        draw_text("there are also two decks of playing cards that are in play. These", SMALL_FONT, BLACK, (960, 330))
        draw_text("change the way the game is played somewhat with the Blue being", SMALL_FONT, BLACK, (960, 370))
        draw_text("positive and the Red being negative. You can click below to see", SMALL_FONT, BLACK, (960, 410))
        draw_text("the effect each card has on the game.", SMALL_FONT, BLACK, (960, 450))
        draw_text("The board will contain symbols that determine what type of space", SMALL_FONT, BLACK, (960, 570))
        draw_text("you'd be in. There is a guide below to help you understand it.", SMALL_FONT, BLACK, (960, 610))
        back_button = Button("<", 500, 760, 70, WHITE, BLACK, MEDIUM_FONT)
        blue_guide_button = Button("Blue Card Guide", 800, 690, 60, WHITE, BLACK, SMALL_FONT)
        red_guide_button = Button("Red Card Guide", 1120, 690, 60, WHITE, BLACK, SMALL_FONT)
        board_guide_button = Button("Board Symbols Guide", 950, 790, 60, WHITE, BLACK, SMALL_FONT)
        play_game_button = Button("Play Game", 1360, 760, 60, WHITE, BLACK, SMALL_FONT)
        if back_button.check_click() or Meta.LEFT_ARROW_DOWN:
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_ONE
        elif blue_guide_button.check_click():
            Meta.CURRENT_STATE = ScreenState.BLUE_CARD_GUIDE
        elif red_guide_button.check_click():
            Meta.CURRENT_STATE = ScreenState.RED_CARD_GUIDE
        elif board_guide_button.check_click():
            Meta.CURRENT_STATE = ScreenState.BOARD_SYMBOLS_GUIDE
        elif play_game_button.check_click():
            Meta.CURRENT_STATE = ScreenState.PLAYING_GAME
            for x in range(len(Meta.PLAYERS)):
                Meta.BOARD_SQUARES[0].players.append(Meta.PLAYERS[x])
    elif Meta.CURRENT_STATE == ScreenState.BLUE_CARD_GUIDE:
        WINDOW.fill(PASTEL_GREEN)
        draw_text("Blue Card Guide", MEDIUM_FONT, ORANGE, (960, 69))
        quit_button = Button("Quit", 1280, 950, 60)
        back_button = Button("Back", 640, 950, 60)
        if quit_button.check_click():
            pygame.quit()
        elif back_button.check_click():
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
        draw_card(BLUE_ACE_OF_HEARTS, (320, 270), 2)
        draw_card(BLUE_TWO_OF_HEARTS, (640, 270), 2)
        draw_card(BLUE_THREE_OF_HEARTS, (960, 270), 2)
        draw_card(BLUE_FOUR_OF_HEARTS, (1280, 270), 2)
        draw_card(BLUE_FIVE_OF_HEARTS, (1600, 270), 2)
        draw_card(BLUE_SIX_OF_HEARTS, (320, 540), 2)
        draw_card(BLUE_SEVEN_OF_HEARTS, (640, 540), 2)
        draw_card(BLUE_EIGHT_OF_HEARTS, (960, 540), 2)
        draw_card(BLUE_NINE_OF_HEARTS, (1280, 540), 2)
        draw_card(BLUE_TEN_OF_HEARTS, (1600, 540), 2)
        draw_card(BLUE_JACK_OF_HEARTS, (320, 810), 2)
        draw_card(BLUE_KING_OF_HEARTS, (640, 810), 2)
        draw_card(BLUE_QUEEN_OF_HEARTS, (960, 810), 2)
        draw_card(BLUE_RED_JOKER, (1280, 810), 2)
        draw_card(BLUE_BLACK_JOKER, (1600, 810), 2)
        check_hover_boxes()
    elif Meta.CURRENT_STATE == ScreenState.RED_CARD_GUIDE:
        WINDOW.fill(PASTEL_GREEN)
        draw_text("Red Card Guide", MEDIUM_FONT, ORANGE, (960, 69))
        quit_button = Button("Quit", 1280, 950, 60)
        back_button = Button("Back", 640, 950, 60)
        if quit_button.check_click():
            pygame.quit()
        elif back_button.check_click():
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
        draw_card(RED_ACE_OF_HEARTS, (320, 270), 2)
        draw_card(RED_TWO_OF_HEARTS, (640, 270), 2)
        draw_card(RED_THREE_OF_HEARTS, (960, 270), 2)
        draw_card(RED_FOUR_OF_HEARTS, (1280, 270), 2)
        draw_card(RED_FIVE_OF_HEARTS, (1600, 270), 2)
        draw_card(RED_SIX_OF_HEARTS, (320, 540), 2)
        draw_card(RED_SEVEN_OF_HEARTS, (640, 540), 2)
        draw_card(RED_EIGHT_OF_HEARTS, (960, 540), 2)
        draw_card(RED_NINE_OF_HEARTS, (1280, 540), 2)
        draw_card(RED_TEN_OF_HEARTS, (1600, 540), 2)
        draw_card(RED_JACK_OF_HEARTS, (320, 810), 2)
        draw_card(RED_KING_OF_HEARTS, (640, 810), 2)
        draw_card(RED_QUEEN_OF_HEARTS, (960, 810), 2)
        draw_card(RED_RED_JOKER, (1280, 810), 2)
        draw_card(RED_BLACK_JOKER, (1600, 810), 2)
        check_hover_boxes()
    elif Meta.CURRENT_STATE == ScreenState.BOARD_SYMBOLS_GUIDE:
        WINDOW.fill(PASTEL_GREEN)
        draw_text("Board Symbols Guide", MEDIUM_FONT, ORANGE, (960, 69))
        quit_button = Button("Quit", 1280, 950, 60)
        back_button = Button("Back", 640, 950, 60)
        if quit_button.check_click():
            pygame.quit()
        elif back_button.check_click():
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
        draw_game_image(BLUE_CARD_SYMBOL, (320, 270), 2, True, WHITE, (330, 80),
                        "Blue Card", "", "Draw 1 from the Blue Draw Deck")
        draw_game_image(RED_CARD_SYMBOL, (640, 270), 2, True, WHITE, (330, 80),
                        "Red Card", "", "Draw 1 from the Red Draw Deck")
        draw_game_image((MISS_TURN, (89, 89)), (960, 270), 2, True, WHITE, (330, 80),
                        "Miss a Turn", "", "Landing here traps you for a turn")
        draw_game_image((BACK_8, (89, 89)), (1280, 270), 2, True, WHITE, (270, 80),
                        "Back 8", "", "Roll d8 to Move Backwards")
        draw_game_image((GO_BACK, (89, 89)), (1600, 270), 2, True, WHITE, (260, 80),
                        "From Whence You Came", "", "Sends you backwards")
        draw_game_image((TWO_BLUE, (89, 89)), (320, 540), 2, True, WHITE, (330, 80),
                        "Two Blue Cards", "", "Draw 2 from the Blue Draw Deck")
        draw_game_image((TWO_RED, (89, 89)), (640, 540), 2, True, WHITE, (330, 80),
                        "Two Red Cards", "", "Draw 2 from the Red Draw Deck")
        draw_game_image((BLUE_RED, (89, 89)), (960, 540), 2, True, WHITE, (330, 80),
                        "Blue Card, Red Card", "", "Draw 1 from each Draw Deck")
        draw_game_image((ROLL_8, (89, 89)), (1280, 540), 2, True, WHITE, (260, 80),
                        "Roll 8", "", "Roll d8 to Move Forwards")
        draw_game_image((REDO, (89, 89)), (1600, 540), 2, True, WHITE, (260, 80),
                        "Double Up", "", "Sends you forwards again")
        draw_game_image((UP_KEY, (89, 89)), (320, 810), 2, True, WHITE, (240, 80),
                        "Up Key", "", "Move up a row")
        draw_game_image((DOWN_KEY, (89, 89)), (640, 810), 2, True, WHITE, (240, 80),
                        "Down Key", "", "Move down a row")
        draw_game_image((MONSTER, (89, 89)), (960, 810), 2, True, WHITE, (330, 80),
                        "Monster", "", "This square contains a Monster")
        draw_game_image((BACK_10, (89, 89)), (1280, 810), 2, True, WHITE, (280, 80),
                        "Back 10", "", "Roll d10 to move Backwards")
        draw_game_image((ROLL_10, (89, 89)), (1600, 810), 2, True, WHITE, (270, 80),
                        "Roll 10", "", "Roll d10 to move Forwards")
        check_hover_boxes()
    elif Meta.CURRENT_STATE == ScreenState.PLAYING_LOCAL_GAME:
        WINDOW.fill(WHITE)
        Meta.BUTTONS_ENABLED = True
        if Meta.SHOW_HAND is None and Meta.CHOOSE_DICE is None and Meta.CHOOSE_PLAYERS is None and Meta.CHOOSE_SQUARE is None and not Meta.SQUARE_VOTE:
            quit_button = Button("Quit", 360, 450, 60)
            if quit_button.check_click():
                pygame.quit()
        check_server_updates()
        current_player = Meta.PLAYERS[Meta.CURRENT_PLAYER]
        is_your_turn = Meta.CURRENT_PLAYER == Meta.PLAYER_NUMBER
        if is_your_turn:
            draw_text("Your Turn", SMALL_FONT, PLAYER_TO_COLOUR[current_player.playerNumber], (960, 30))
        else:
            draw_text(current_player.playerName + "'s Turn", SMALL_FONT, PLAYER_TO_COLOUR[current_player.playerNumber], (960, 30))
        game_board = pygame.Rect((480, 60), (960, 960))
        pygame.draw.rect(WINDOW, BLUE, game_board)
        roll_background = pygame.Rect((1460, 100), (440, 700))
        pygame.draw.rect(WINDOW, PASTEL_GREEN, roll_background, 0, 20)
        if not is_your_turn:
            draw_text("Waiting for your Turn", SMALL_FONT, BLACK, (1680, 240))
            for event in range(len(Meta.EVENT_LIST)):
                draw_text(Meta.EVENT_LIST[event], TINY_FONT, BLACK, (10, 10 + (20 * event)), False)
        else:
            draw_game_image(BLUE_CARD_SYMBOL, (360, 250), 3, True, PASTEL_GREEN, (170, 75),
                            "Blue Draw Pile", "", "Current Size: " + str(len(Meta.BLUE_DRAW_DECK)))
            draw_game_image(RED_CARD_SYMBOL, (360, 650), 3, True, PASTEL_GREEN, (170, 75),
                            "Red Draw Pile", "", "Current Size: " + str(len(Meta.RED_DRAW_DECK)))
        if is_your_turn:
            if len(current_player.blueDeck) != 0:
                turned_blue_deck_image = pygame.transform.rotate(BLUE_CARD_SYMBOL[0], -90)
                turned_blue_deck_image = pygame.transform.scale(turned_blue_deck_image, (
                BLUE_CARD_SYMBOL[1][1] * 3, BLUE_CARD_SYMBOL[1][0] * 3))
                WINDOW.blit(turned_blue_deck_image, (95, 835))
                if Meta.CARD_HANDS_ACTIVE: Meta.HOVER_BOXES.append(("board symbol", ["Your Blue Card Hand"],
                                                                    turned_blue_deck_image, (95, 835), (215, 35),
                                                                    PASTEL_GREEN))
                blue_hand_rect = turned_blue_deck_image.get_rect()
                blue_hand_rect.topleft = (95, 835)
                if blue_hand_rect.collidepoint(
                        pygame.mouse.get_pos()) and Meta.LEFT_MOUSE_RELEASED and Meta.CARD_HANDS_ACTIVE:
                    Meta.SHOW_HAND = CardType.BLUE
                    Meta.CARD_HANDS_ACTIVE = False
                    if Meta.TURN_STAGE == TurnStage.DRAW_CARDS:
                        if Meta.DISPLAYING_CARD:
                            Meta.CARDS_TO_DRAW.pop(0)
                            Meta.DISPLAYING_CARD = False
            if len(current_player.redDeck) != 0:
                turned_red_deck_image = pygame.transform.rotate(RED_CARD_SYMBOL[0], 90)
                turned_red_deck_image = pygame.transform.scale(turned_red_deck_image,
                                                               (RED_CARD_SYMBOL[1][1] * 3, RED_CARD_SYMBOL[1][0] * 3))
                WINDOW.blit(turned_red_deck_image, (1530, 835))
                if Meta.CARD_HANDS_ACTIVE: Meta.HOVER_BOXES.append(("board symbol", ["Your Red Card Hand"],
                                                                    turned_red_deck_image, (1530, 835), (215, 35),
                                                                    PASTEL_GREEN))
                red_hand_rect = turned_red_deck_image.get_rect()
                red_hand_rect.topleft = (1530, 835)
                if red_hand_rect.collidepoint(
                        pygame.mouse.get_pos()) and Meta.LEFT_MOUSE_RELEASED and Meta.CARD_HANDS_ACTIVE:
                    Meta.SHOW_HAND = CardType.RED
                    Meta.CARD_HANDS_ACTIVE = False
                    if Meta.TURN_STAGE == TurnStage.DRAW_CARDS:
                        if Meta.DISPLAYING_CARD:
                            Meta.CARDS_TO_DRAW.pop(0)
                            Meta.DISPLAYING_CARD = False
        draw_squares()
        if is_your_turn:
            if Meta.SQUARE_VOTE:
                Meta.HOVER_BOXES.clear()
                WINDOW.fill(PASTEL_GREEN)
                draw_text("Waiting for the Square Vote to Conclude", MEDIUM_FONT, ORANGE, (960, 69))
                Meta.BUTTONS_ENABLED = False
            elif Meta.SHOW_HAND == CardType.BLUE:
                Meta.HOVER_BOXES.clear()
                WINDOW.fill(PASTEL_GREEN)
                draw_text(current_player.playerName + "'s Blue Card Hand", MEDIUM_FONT, ORANGE, (960, 69))
                back_button = Button("Back", 960, 950, 60)
                if back_button.check_click():
                    Meta.SHOW_HAND = None
                    Meta.CARD_HANDS_ACTIVE = True
                for x in range(len(current_player.blueDeck)):
                    draw_card(current_player.blueDeck[x], CARD_TO_POSITION[x], 2)
                Meta.BUTTONS_ENABLED = False
                check_hover_boxes()
            elif Meta.SHOW_HAND == CardType.RED:
                Meta.HOVER_BOXES.clear()
                WINDOW.fill(PASTEL_GREEN)
                draw_text(current_player.playerName + "'s Red Card Hand", MEDIUM_FONT, ORANGE, (960, 69))
                back_button = Button("Back", 960, 950, 60)
                if back_button.check_click():
                    Meta.SHOW_HAND = None
                    Meta.CARD_HANDS_ACTIVE = True
                for x in range(len(current_player.redDeck)):
                    draw_card(current_player.redDeck[x], CARD_TO_POSITION[x], 2)
                Meta.BUTTONS_ENABLED = False
                check_hover_boxes()
            elif Meta.CHOOSE_PLAYERS is not None:
                Meta.HOVER_BOXES.clear()
                WINDOW.fill(PASTEL_GREEN)
                draw_text("Choose a Player:", MEDIUM_FONT, ORANGE, (960, 69))
                player = None
                for x in range(len(Meta.PLAYERS)):
                    if Meta.PLAYERS[x] != current_player:
                        if Meta.CHOOSE_PLAYERS == "Red Five":
                            if Meta.PLAYERS[x].setPlayerRoll is None:
                                button = Button(Meta.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                                if button.check_click():
                                    player = Meta.PLAYERS[x]
                        elif Meta.CHOOSE_PLAYERS == "Blue Five":
                            if Meta.PLAYERS[x].setNextRoll is None:
                                button = Button(Meta.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                                if button.check_click():
                                    player = Meta.PLAYERS[x]
                        else:
                            button = Button(Meta.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                            if button.check_click():
                                player = Meta.PLAYERS[x]
                if player is not None:
                    if Meta.CHOOSE_PLAYERS == "Blue Three":
                        event_data = []
                        for x in range(len(Meta.PLAYERS)):
                            if Meta.PLAYERS[x] != player and Meta.PLAYERS[x] != current_player:
                                red_card = Meta.RED_DRAW_DECK.pop()
                                Meta.PLAYERS[x].redDeck.append(red_card)
                                event_data.append(Meta.PLAYERS[x].playerName + " drew the " + red_card.displayName)
                        Meta.NETWORK.send(("PlayersRedEvents", Meta.PLAYERS, Meta.RED_DRAW_DECK, event_data))
                        Meta.CHOOSE_PLAYERS = None
                    elif Meta.CHOOSE_PLAYERS == "Red Three":
                        event_data = []
                        for x in range(len(Meta.PLAYERS)):
                            if Meta.PLAYERS[x] != player and Meta.PLAYERS[x] != current_player:
                                blue_card = Meta.BLUE_DRAW_DECK.pop()
                                Meta.PLAYERS[x].blueDeck.append(blue_card)
                                event_data.append(Meta.PLAYERS[x].playerName + " drew the " + blue_card.displayName)
                        Meta.NETWORK.send(("PlayersBlueEvents", Meta.PLAYERS, Meta.BLUE_DRAW_DECK, event_data))
                        Meta.CHOOSE_PLAYERS = None
                    elif Meta.CHOOSE_PLAYERS == "Blue Five":
                        Meta.CHOOSE_PLAYERS = None
                        Meta.CHOOSE_DICE = player
                    elif Meta.CHOOSE_PLAYERS == "Red Five":
                        Meta.CHOOSE_PLAYERS = None
                        player.setPlayerRoll = current_player
                        Meta.NETWORK.send(("PlayerEvents", player, [player.playerName + " will set a dice roll for " + current_player.playerName]))
                Meta.BUTTONS_ENABLED = False
            elif Meta.CHOOSE_DICE is not None:
                Meta.HOVER_BOXES.clear()
                WINDOW.fill(PASTEL_GREEN)
                draw_text("Choose a Dice Value:", MEDIUM_FONT, ORANGE, (960, 69))
                one_d6 = Dice(1, D6_IMAGES)
                two_d6 = Dice(2, D6_IMAGES)
                three_d6 = Dice(3, D6_IMAGES)
                four_d6 = Dice(4, D6_IMAGES)
                five_d6 = Dice(5, D6_IMAGES)
                six_d6 = Dice(6, D6_IMAGES)
                draw_dice(one_d6, CARD_TO_POSITION[0], 2)
                draw_dice(two_d6, CARD_TO_POSITION[1], 2)
                draw_dice(three_d6, CARD_TO_POSITION[2], 2)
                draw_dice(four_d6, CARD_TO_POSITION[3], 2)
                draw_dice(five_d6, CARD_TO_POSITION[4], 2)
                draw_dice(six_d6, CARD_TO_POSITION[5], 2)
                if one_d6.check_click(False):
                    Meta.CHOOSE_DICE.setNextRoll = 1
                    Meta.NETWORK.send(("PlayerEvents", Meta.CHOOSE_DICE, [current_player.playerName + " set " + Meta.CHOOSE_DICE.playerName + " to Roll a One"]))
                    Meta.CHOOSE_DICE = None
                if two_d6.check_click(False):
                    Meta.CHOOSE_DICE.setNextRoll = 2
                    Meta.NETWORK.send(("PlayerEvents", Meta.CHOOSE_DICE, [current_player.playerName + " set " + Meta.CHOOSE_DICE.playerName + " to Roll a Two"]))
                    Meta.CHOOSE_DICE = None
                if three_d6.check_click(False):
                    Meta.CHOOSE_DICE.setNextRoll = 3
                    Meta.NETWORK.send(("PlayerEvents", Meta.CHOOSE_DICE, [current_player.playerName + " set " + Meta.CHOOSE_DICE.playerName + " to Roll a Three"]))
                    Meta.CHOOSE_DICE = None
                if four_d6.check_click(False):
                    Meta.CHOOSE_DICE.setNextRoll = 4
                    Meta.NETWORK.send(("PlayerEvents", Meta.CHOOSE_DICE, [current_player.playerName + " set " + Meta.CHOOSE_DICE.playerName + " to Roll a Four"]))
                    Meta.CHOOSE_DICE = None
                if five_d6.check_click(False):
                    Meta.CHOOSE_DICE.setNextRoll = 5
                    Meta.NETWORK.send(("PlayerEvents", Meta.CHOOSE_DICE, [current_player.playerName + " set " + Meta.CHOOSE_DICE.playerName + " to Roll a Five"]))
                    Meta.CHOOSE_DICE = None
                if six_d6.check_click(False):
                    Meta.CHOOSE_DICE.setNextRoll = 6
                    Meta.NETWORK.send(("PlayerEvents", Meta.CHOOSE_DICE, [current_player.playerName + " set " + Meta.CHOOSE_DICE.playerName + " to Roll a Six"]))
                    Meta.CHOOSE_DICE = None
                Meta.BUTTONS_ENABLED = False
            elif Meta.CHOOSE_SQUARE is not None:
                Meta.HOVER_BOXES.clear()
                WINDOW.fill(PASTEL_GREEN)
                draw_text("Choose a Square:", MEDIUM_FONT, ORANGE, (960, 30))
                draw_squares()
                square_clicked = check_squares_clicked()
                if square_clicked is not None and Meta.BOARD_SQUARES.index(square_clicked) != 99 and Meta.BOARD_SQUARES.index(square_clicked) != 0:
                    if Meta.CHOOSE_SQUARE == "Blue Nine":
                        if not square_clicked.hasBarrier:
                            square_clicked.hasBarrier = True
                            Meta.NETWORK.send(("SquareEvents", (Meta.BOARD_SQUARES.index(square_clicked), square_clicked), [current_player.playerName +
                                               " placed a Magic Barrier"]))
                            Meta.CHOOSE_SQUARE = None
                    else:
                        if not square_clicked.hasBarrier:
                            Meta.NETWORK.send(("SquareVote", Meta.BOARD_SQUARES.index(square_clicked), [Meta.PLAYERS[Meta.PLAYER_NUMBER].playerName +
                                               " voted for Square " + str(Meta.BOARD_SQUARES.index(square_clicked))]))
                            Meta.CHOOSE_SQUARE = None
                Meta.BUTTONS_ENABLED = False
            elif Meta.TURN_STAGE == TurnStage.START_TURN:
                if current_player.missNextTurn:
                    draw_text("You don't get to take this turn", SMALL_FONT, BLACK, (1680, 240))
                    continue_button = Button("Continue", 1680, 600, 60)
                    if continue_button.check_click():
                        current_player.missNextTurn = False
                        Meta.NETWORK.send(("PlayerEvents", current_player, [current_player.playerName + " Missed their Turn"]))
                        end_turn()
                else:
                    if current_player.setPlayerRoll is not None:
                        draw_text("Set " + current_player.setPlayerRoll.playerName + "'s", SMALL_FONT, BLACK,
                                  (1680, 230))
                        draw_text("Next Dice Roll", SMALL_FONT, BLACK, (1680, 260))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            Meta.CHOOSE_DICE = current_player.setPlayerRoll
                            current_player.setPlayerRoll = None
                            Meta.NETWORK.send(("Player", current_player))
                    else:
                        if Meta.FORCED_CARD is None:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.THREE:
                                    Meta.FORCED_CARD = CardValue.THREE
                                    break
                                if card.cardValue == CardValue.FIVE:
                                    Meta.FORCED_CARD = CardValue.FIVE
                                    break
                                if card.cardValue == CardValue.NINE:
                                    Meta.FORCED_CARD = CardValue.NINE
                                    break
                        if Meta.FORCED_CARD == CardValue.THREE:
                            draw_text("Use your Red Three Card!", SMALL_FONT, BLACK, (1680, 240))
                        elif Meta.FORCED_CARD == CardValue.FIVE:
                            draw_text("Use your Red Five Card!", SMALL_FONT, BLACK, (1680, 240))
                        elif Meta.FORCED_CARD == CardValue.NINE:
                            draw_text("Use your Red Nine Card!", SMALL_FONT, BLACK, (1680, 240))
                        elif Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth > 0:
                            D20.enabled = True
                            D20_2.enabled = True
                            D20_3.enabled = True
                            Meta.SUCCEEDED_DEFENCE = None
                            Meta.TURN_STAGE = TurnStage.MONSTER_ATTACK
                        else:  # Roll Dice
                            Meta.TOP_DICE = [D6]
                            Meta.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            draw_dice_sets()
                            D6.enabled = True
                            D6_2.enabled = True
                            Meta.TURN_STAGE = TurnStage.ROLL_DICE
            elif Meta.TURN_STAGE == TurnStage.MONSTER_ATTACK:  # Monster Attacks
                if Meta.SUCCEEDED_DEFENCE is None: draw_text("Defend against the Monster!", SMALL_FONT, BLACK, (1680, 240))
                if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                    for card in current_player.redDeck:
                        if card.cardValue == CardValue.TWO:
                            Meta.FORCED_CARD = CardValue.TWO
                if Meta.FORCED_CARD is None and Meta.SUCCEEDED_DEFENCE:
                    for card in current_player.redDeck:
                        if card.cardValue == CardValue.EIGHT:
                            Meta.FORCED_CARD = CardValue.EIGHT
                if Meta.FORCED_CARD == CardValue.TWO:
                    draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                elif Meta.FORCED_CARD == CardValue.EIGHT:
                    draw_text("Use your Red Eight Card!", SMALL_FONT, BLACK, (1680, 240))
                else:
                    if D20_3.enabled:
                        D20_3.sideFacing = random.randrange(1, 21)
                        D20_3.enabled = False
                    draw_dice(D20_3, (1680, 330), 2)
                    if Meta.ROLLING_WITH_ADVANTAGE:
                        Meta.TOP_DICE = [D20, D20_2]
                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                        Meta.BOTTOM_DICE = [D10, D10_2, D12, D12_2, D4]
                        D20.check_click()
                        D20_2.check_click()
                        if not D20.enabled and not D20_2.enabled and Meta.SUCCEEDED_DEFENCE is None:
                            Meta.SUCCEEDED_DEFENCE = max(D20.sideFacing, D20_2.sideFacing) >= D20_3.sideFacing
                            if not Meta.SUCCEEDED_DEFENCE:
                                for card in current_player.blueDeck:
                                    if card.cardValue == CardValue.EIGHT:
                                        Meta.CARD_TO_REMOVE = (current_player.blueDeck, card)
                                        Meta.DISCARD_PILE.append(card)
                                        Meta.NETWORK.send(("DiscardEvents", Meta.DISCARD_PILE, [current_player.playerName + " used the " + card.displayName]))
                                        Meta.SHIELD_ACTIVE = True
                                        break
                    elif Meta.ROLLING_WITH_DISADVANTAGE:
                        Meta.TOP_DICE = [D20, D20_2]
                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                        Meta.BOTTOM_DICE = [D10, D10_2, D12, D12_2, D4]
                        D20.check_click()
                        D20_2.check_click()
                        if not D20.enabled and not D20_2.enabled and Meta.SUCCEEDED_DEFENCE is None:
                            Meta.SUCCEEDED_DEFENCE = min(D20.sideFacing, D20_2.sideFacing) >= D20_3.sideFacing
                            if not Meta.SUCCEEDED_DEFENCE:
                                for card in current_player.blueDeck:
                                    if card.cardValue == CardValue.EIGHT:
                                        Meta.CARD_TO_REMOVE = (current_player.blueDeck, card)
                                        Meta.DISCARD_PILE.append(card)
                                        Meta.NETWORK.send(("DiscardEvents", Meta.DISCARD_PILE, [current_player.playerName + " used the " + card.displayName]))
                                        Meta.SHIELD_ACTIVE = True
                                        break
                    else:
                        Meta.TOP_DICE = [D20]
                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                        Meta.BOTTOM_DICE = [D10_2, D12, D12_2, D20_2, D4]
                        if D20.check_click():
                            Meta.SUCCEEDED_DEFENCE = D20.sideFacing >= D20_3.sideFacing
                            if not Meta.SUCCEEDED_DEFENCE:
                                for card in current_player.blueDeck:
                                    if card.cardValue == CardValue.EIGHT:
                                        Meta.CARD_TO_REMOVE = (current_player.blueDeck, card)
                                        Meta.DISCARD_PILE.append(card)
                                        Meta.NETWORK.send(("DiscardEvents", Meta.DISCARD_PILE, [current_player.playerName + " used the " + card.displayName]))
                                        Meta.SHIELD_ACTIVE = True
                                        break
                    draw_dice_sets(500)
                    if Meta.SUCCEEDED_DEFENCE is not None:
                        if not Meta.SUCCEEDED_DEFENCE:  # Player Loses
                            if Meta.SHIELD_ACTIVE:
                                draw_text("Your Shield saved you", SMALL_FONT, BLACK, (1680, 230))
                                draw_text("You survived the encounter", SMALL_FONT, BLACK, (1680, 260))
                                continue_button = Button("Continue", 1680, 600, 60)
                                if continue_button.check_click():
                                    Meta.ROLLING_WITH_ADVANTAGE = False
                                    Meta.ROLLING_WITH_DISADVANTAGE = False
                                    Meta.TOP_DICE = [D12]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                    Meta.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                    Meta.TURN_STAGE = TurnStage.ATTACK_MONSTER
                                    D12.enabled = True
                                    D12_2.enabled = True
                                    Meta.SHIELD_ACTIVE = False
                            else:
                                draw_text("You Failed your Defence Roll", SMALL_FONT, BLACK, (1680, 200))
                                draw_text("The Monster will knock you", SMALL_FONT, BLACK, (1680, 230))
                                draw_text("back 4 spaces", SMALL_FONT, BLACK, (1680, 260))
                                continue_button = Button("Continue", 1680, 600, 60)
                                if continue_button.check_click():
                                    Meta.ROLLING_WITH_ADVANTAGE = False
                                    Meta.ROLLING_WITH_DISADVANTAGE = False
                                    updated_squares = []
                                    Meta.BOARD_SQUARES[current_player.currentSquare].players.remove(current_player)
                                    updated_squares.append((current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]))
                                    current_player.currentSquare -= 4
                                    Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    updated_squares.append((current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]))
                                    Meta.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [current_player.playerName + " Failed their Defence"]))
                                    Meta.TURN_STAGE = TurnStage.START_TURN
                        else:
                            draw_text("You defended yourself", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Meta.ROLLING_WITH_ADVANTAGE = False
                                Meta.ROLLING_WITH_DISADVANTAGE = False
                                Meta.TOP_DICE = [D12]
                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                Meta.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                Meta.TURN_STAGE = TurnStage.ATTACK_MONSTER
                                D12.enabled = True
                                D12_2.enabled = True
            elif Meta.TURN_STAGE == TurnStage.ATTACK_MONSTER:  # Attacking a Monster
                if Meta.FORCED_CARD is None and not Meta.TAKING_FOUR and not Meta.TAKEN_FOUR:
                    for card in current_player.redDeck:
                        if card.cardValue == CardValue.FOUR:
                            Meta.FORCED_CARD = CardValue.FOUR
                if Meta.FORCED_CARD == CardValue.FOUR:
                    draw_text("Use your Red Four!", SMALL_FONT, BLACK, (1680, 240))
                else:
                    if Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth <= 0:
                        draw_text("Congratulations!", SMALL_FONT, BLACK, (1680, 200))
                        draw_text("You have killed the Monster!", SMALL_FONT, BLACK, (1680, 230))
                        draw_text("You can roll movement now", SMALL_FONT, BLACK, (1680, 260))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            Meta.TURN_STAGE = TurnStage.START_TURN
                            Meta.ADDING_FOUR = False
                            Meta.TAKING_FOUR = False
                            Meta.TAKEN_FOUR = False
                            Meta.ROLLING_WITH_ADVANTAGE = False
                            Meta.BOARD_SQUARES[current_player.currentSquare].monsterAwake = False
                            Meta.NETWORK.send(("SquareEvents", (current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]), [current_player.playerName + " killed the Monster"]))
                    elif not D12.enabled and not D12_2.enabled:
                        if Meta.ADDING_FOUR:
                            draw_text("Add a d4 to the Attack:", SMALL_FONT, BLACK, (1680, 240))
                            Meta.TOP_DICE = [D4]
                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                            Meta.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                            draw_dice_sets()
                            if D4.check_click():
                                Meta.ADDING_FOUR = False
                                Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= D4.sideFacing
                                Meta.NETWORK.send(("SquareEvents", (current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]),
                                                   [current_player.playerName + " hit the Monster for " + str(D4.sideFacing)]))
                        elif Meta.TAKING_FOUR and not Meta.TAKEN_FOUR:
                            draw_text("Take a d4 from the Attack:", SMALL_FONT, BLACK, (1680, 240))
                            Meta.TOP_DICE = [D4]
                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                            Meta.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                            draw_dice_sets()
                            if D4.check_click():
                                Meta.TAKEN_FOUR = True
                                Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth += D4.sideFacing
                                Meta.NETWORK.send(("SquareEvents", (current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]),
                                                   [current_player.playerName + " healed the Monster for " + str(D4.sideFacing)]))
                        else:
                            draw_text("You did not kill the Monster", SMALL_FONT, BLACK, (1680, 240))
                            end_turn_button = Button("End Turn", 1680, 600, 60)
                            if end_turn_button.check_click():
                                end_turn()
                                Meta.TAKEN_FOUR = False
                                Meta.TAKING_FOUR = False
                                Meta.ROLLING_WITH_ADVANTAGE = False
                    else:
                        draw_text("Attack the Monster:", SMALL_FONT, BLACK, (1680, 240))
                        if Meta.ROLLING_WITH_ADVANTAGE:
                            Meta.TOP_DICE = [D12, D12_2]
                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                            Meta.BOTTOM_DICE = [D10, D10_2, D20, D20_2, D4]
                        if not Meta.ROLLING_WITH_ADVANTAGE:
                            if D12.check_click():
                                D12_2.enabled = False
                                Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= D12.sideFacing
                                Meta.NETWORK.send(("SquareEvents", (current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]),
                                                   [current_player.playerName + " hit the Monster for " + str(D12.sideFacing)]))
                        else:
                            D12.check_click()
                            D12_2.check_click()
                            if not D12.enabled and not D12_2.enabled:
                                Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= max(D12.sideFacing, D12_2.sideFacing)
                                Meta.NETWORK.send(("SquareEvents", (current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]),
                                                   [current_player.playerName + " hit the Monster for " + str(max(D12.sideFacing, D12_2.sideFacing))]))
                    draw_dice_sets()
            elif Meta.TURN_STAGE == TurnStage.ROLL_DICE:  # Rolling the Movement Dice
                if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                    for card in current_player.redDeck:
                        if card.cardValue == CardValue.TWO:
                            Meta.FORCED_CARD = CardValue.TWO
                if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_FOUR:
                    for card in current_player.redDeck:
                        if card.cardValue == CardValue.JACK:
                            Meta.FORCED_CARD = CardValue.JACK
                if Meta.FORCED_CARD == CardValue.TWO:
                    draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                elif Meta.FORCED_CARD == CardValue.JACK:
                    draw_text("Use your Red Jack Card!", SMALL_FONT, BLACK, (1680, 240))
                else:
                    if Meta.ROLLING_WITH_FOUR:
                        Meta.TOP_DICE = [D4]
                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                        Meta.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                        draw_text("Roll d4 to move:", SMALL_FONT, BLACK, (1680, 240))
                        draw_dice_sets()
                        if D4.check_click():
                            Meta.ROLLING_WITH_FOUR = False
                            Meta.SQUARES_TO_MOVE = D4.sideFacing
                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                    elif Meta.ROLLING_WITH_ADVANTAGE and Meta.DICE_ROLLED == 2:
                        draw_text("Pick a dice to use:", SMALL_FONT, BLACK, (1680, 240))
                        draw_dice_sets()
                        if D6.check_click(False):
                            Meta.ROLLING_WITH_ADVANTAGE = False
                            Meta.DICE_ROLLED = 0
                            Meta.SQUARES_TO_MOVE = D6.sideFacing
                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                            Meta.TOP_DICE = [D6]
                            Meta.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                        if D6_2.check_click(False):
                            Meta.ROLLING_WITH_ADVANTAGE = False
                            Meta.DICE_ROLLED = 0
                            Meta.SQUARES_TO_MOVE = D6_2.sideFacing
                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                            Meta.TOP_DICE = [D6_2]
                            Meta.MIDDLE_DICE = [D6, D8, D8_2, D10, D10_2]
                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                    else:
                        draw_text("Roll d6 to move:", SMALL_FONT, BLACK, (1680, 240))
                        if not Meta.ROLLING_WITH_ADVANTAGE and not Meta.ROLLING_DOUBLE and not Meta.ROLLING_WITH_DISADVANTAGE:
                            draw_dice_sets()
                            if D6.check_click():
                                Meta.TURN_STAGE = TurnStage.MOVEMENT
                                Meta.SQUARES_TO_MOVE = D6.sideFacing
                        elif Meta.ROLLING_WITH_ADVANTAGE:
                            Meta.TOP_DICE = [D6, D6_2]
                            Meta.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            draw_dice_sets()
                            if D6.check_click():
                                Meta.DICE_ROLLED += 1
                            if D6_2.check_click():
                                Meta.DICE_ROLLED += 1
                            if Meta.DICE_ROLLED == 2:
                                D6.enabled = True
                                D6_2.enabled = True
                        elif Meta.ROLLING_WITH_DISADVANTAGE:
                            Meta.TOP_DICE = [D6, D6_2]
                            Meta.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            draw_dice_sets()
                            D6.check_click()
                            D6_2.check_click()
                            if not D6.enabled and not D6_2.enabled:
                                Meta.SQUARES_TO_MOVE = min(D6.sideFacing, D6_2.sideFacing)
                                if D6.sideFacing > D6_2.sideFacing:
                                    Meta.TOP_DICE = [D6_2]
                                    Meta.MIDDLE_DICE = [D6, D8, D8_2, D10, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                else:
                                    Meta.TOP_DICE = [D6]
                                    Meta.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                Meta.TURN_STAGE = TurnStage.MOVEMENT
                                Meta.ROLLING_WITH_DISADVANTAGE = False
                        elif Meta.ROLLING_DOUBLE:
                            Meta.TOP_DICE = [D6, D6_2]
                            Meta.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            draw_dice_sets()
                            D6.check_click()
                            D6_2.check_click()
                            if not D6.enabled and not D6_2.enabled:
                                Meta.SQUARES_TO_MOVE = D6.sideFacing + D6_2.sideFacing
                                Meta.TURN_STAGE = TurnStage.MOVEMENT
                                Meta.ROLLING_DOUBLE = False
            elif Meta.TURN_STAGE == TurnStage.MOVEMENT:  # Moving the Current Player
                draw_dice_sets()
                for x in range(Meta.SQUARES_TO_MOVE):
                    if Meta.BOARD_SQUARES[current_player.currentSquare + x].hasBarrier and x != 0:
                        has_ten = False
                        for card in current_player.blueDeck:
                            if card.cardValue == CardValue.TEN:
                                Meta.CARD_TO_REMOVE = (current_player.blueDeck, card)
                                Meta.DISCARD_PILE.append(card)
                                Meta.NETWORK.send(("DiscardEvents", Meta.DISCARD_PILE, [current_player.playerName + " used the " + card.displayName]))
                                has_ten = True
                                break
                        if not has_ten:
                            Meta.SQUARES_TO_MOVE = x
                            Meta.BOARD_SQUARES[current_player.currentSquare + x].hasBarrier = False
                            break
                    elif Meta.BOARD_SQUARES[current_player.currentSquare + x].monsterAwake:
                        Meta.SQUARES_TO_MOVE = x
                        break
                player_to_remove = None
                for player in Meta.BOARD_SQUARES[current_player.currentSquare].players:
                    if player.playerNumber == current_player.playerNumber:
                        player_to_remove = player
                Meta.BOARD_SQUARES[current_player.currentSquare].players.remove(player_to_remove)
                updated_squares = [(current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare])]
                current_player.currentSquare = min(99, current_player.currentSquare + Meta.SQUARES_TO_MOVE)
                Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                updated_squares.append((current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]))
                Meta.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [current_player.playerName + " moved " + str(Meta.SQUARES_TO_MOVE)]))
                Meta.TURN_STAGE = TurnStage.SQUARE_ACTION
                Meta.CAN_PROGRESS = False
                if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                    Meta.FORCED_MOVEMENT = True
                    D10.enabled = True
                    D10_2.enabled = True
                    D8.enabled = True
                    D8_2.enabled = True
                elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                    Meta.BONUS_MOVEMENT = True
                    D10.enabled = True
                    D10_2.enabled = True
                    D8.enabled = True
                    D8_2.enabled = True
            elif Meta.TURN_STAGE == TurnStage.SQUARE_ACTION:  # Doing what the Square wants
                draw_dice_sets()
                current_square = Meta.BOARD_SQUARES[current_player.currentSquare]
                if current_player.currentSquare == 99:
                    Meta.TURN_STAGE = TurnStage.GAME_WON
                else:
                    if current_square.symbol == "OneBlue":
                        Meta.TURN_STAGE = TurnStage.DRAW_CARDS
                        Meta.CARDS_TO_DRAW.append(CardType.BLUE)
                    elif current_square.symbol == "OneRed":
                        Meta.TURN_STAGE = TurnStage.DRAW_CARDS
                        Meta.CARDS_TO_DRAW.append(CardType.RED)
                    elif current_square.symbol == "TwoRed":
                        Meta.TURN_STAGE = TurnStage.DRAW_CARDS
                        Meta.CARDS_TO_DRAW.append(CardType.RED)
                        Meta.CARDS_TO_DRAW.append(CardType.RED)
                    elif current_square.symbol == "TwoBlue":
                        Meta.TURN_STAGE = TurnStage.DRAW_CARDS
                        Meta.CARDS_TO_DRAW.append(CardType.BLUE)
                        Meta.CARDS_TO_DRAW.append(CardType.BLUE)
                    elif current_square.symbol == "BlueRed":
                        Meta.TURN_STAGE = TurnStage.DRAW_CARDS
                        Meta.CARDS_TO_DRAW.append(CardType.BLUE)
                        Meta.CARDS_TO_DRAW.append(CardType.RED)
                    elif current_square.symbol == "Roll10":
                        if Meta.FORCED_CARD is None and Meta.BONUS_MOVEMENT:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.SIX:
                                    Meta.FORCED_CARD = CardValue.SIX
                        if Meta.FORCED_CARD == CardValue.SIX:
                            draw_text("Use your Red Six Card!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Meta.BONUS_MOVEMENT:
                                draw_text("You don't get this benefit", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                                    for card in current_player.redDeck:
                                        if card.cardValue == CardValue.TWO:
                                            Meta.FORCED_CARD = CardValue.TWO
                                if Meta.FORCED_CARD == CardValue.TWO:
                                    draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                                else:
                                    draw_text("Roll d10 to Move:", SMALL_FONT, BLACK, (1680, 240))
                                    if Meta.ROLLING_WITH_ADVANTAGE:
                                        Meta.TOP_DICE = [D10, D10_2]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        D10.check_click()
                                        D10_2.check_click()
                                        if not D10.enabled and not D10_2.enabled:
                                            Meta.BONUS_MOVEMENT = False
                                            if D10.sideFacing >= D10_2.sideFacing:
                                                Meta.TOP_DICE = [D10]
                                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Meta.SQUARES_TO_MOVE = D10.sideFacing
                                            else:
                                                Meta.TOP_DICE = [D10_2]
                                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Meta.SQUARES_TO_MOVE = D10_2.sideFacing
                                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                                    elif Meta.ROLLING_WITH_DISADVANTAGE:
                                        Meta.TOP_DICE = [D10, D10_2]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        D10.check_click()
                                        D10_2.check_click()
                                        if not D10.enabled and not D10_2.enabled:
                                            Meta.BONUS_MOVEMENT = False
                                            if D10.sideFacing <= D10_2.sideFacing:
                                                Meta.TOP_DICE = [D10]
                                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Meta.SQUARES_TO_MOVE = D10.sideFacing
                                            else:
                                                Meta.TOP_DICE = [D10_2]
                                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Meta.SQUARES_TO_MOVE = D10_2.sideFacing
                                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                                    else:
                                        Meta.TOP_DICE = [D10]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        if D10.check_click():
                                            Meta.BONUS_MOVEMENT = False
                                            Meta.TOP_DICE = [D10]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Meta.SQUARES_TO_MOVE = D10.sideFacing
                                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                    elif current_square.symbol == "Roll8":
                        if Meta.FORCED_CARD is None and Meta.BONUS_MOVEMENT:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.SIX:
                                    Meta.FORCED_CARD = CardValue.SIX
                        if Meta.FORCED_CARD == CardValue.SIX:
                            draw_text("Use your Red Six Card!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Meta.BONUS_MOVEMENT:
                                draw_text("You don't get this benefit", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                                    for card in current_player.redDeck:
                                        if card.cardValue == CardValue.TWO:
                                            Meta.FORCED_CARD = CardValue.TWO
                                if Meta.FORCED_CARD == CardValue.TWO:
                                    draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                                else:
                                    draw_text("Roll d8 to Move:", SMALL_FONT, BLACK, (1680, 240))
                                    if Meta.ROLLING_WITH_ADVANTAGE:
                                        Meta.TOP_DICE = [D8, D8_2]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        D8.check_click()
                                        D8_2.check_click()
                                        if not D8.enabled and not D8_2.enabled:
                                            Meta.BONUS_MOVEMENT = False
                                            if D8.sideFacing >= D8_2.sideFacing:
                                                Meta.TOP_DICE = [D8]
                                                Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Meta.SQUARES_TO_MOVE = D8.sideFacing
                                            else:
                                                Meta.TOP_DICE = [D8_2]
                                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Meta.SQUARES_TO_MOVE = D8_2.sideFacing
                                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                                    elif Meta.ROLLING_WITH_DISADVANTAGE:
                                        Meta.TOP_DICE = [D8, D8_2]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        D8.check_click()
                                        D8_2.check_click()
                                        if not D8.enabled and not D8_2.enabled:
                                            Meta.BONUS_MOVEMENT = False
                                            if D8.sideFacing <= D8_2.sideFacing:
                                                Meta.TOP_DICE = [D8]
                                                Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Meta.SQUARES_TO_MOVE = D8.sideFacing
                                            else:
                                                Meta.TOP_DICE = [D8_2]
                                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Meta.SQUARES_TO_MOVE = D8_2.sideFacing
                                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                                    else:
                                        Meta.TOP_DICE = [D8]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        if D8.check_click():
                                            Meta.BONUS_MOVEMENT = False
                                            Meta.TOP_DICE = [D8]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Meta.SQUARES_TO_MOVE = D8.sideFacing
                                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                    elif current_square.symbol == "Back10":
                        if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.TWO:
                                    Meta.FORCED_CARD = CardValue.TWO
                        if Meta.FORCED_CARD == CardValue.TWO:
                            draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Meta.FORCED_MOVEMENT:
                                draw_text("You are safe for now", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                draw_text("Roll d10 to go Back:", SMALL_FONT, BLACK, (1680, 240))
                                if Meta.ROLLING_WITH_ADVANTAGE:
                                    Meta.TOP_DICE = [D10, D10_2]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D10.check_click()
                                    D10_2.check_click()
                                    if not D10.enabled and not D10_2.enabled:
                                        Meta.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        if D10.sideFacing <= D10_2.sideFacing:
                                            Meta.TOP_DICE = [D10]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D10.sideFacing
                                        else:
                                            Meta.TOP_DICE = [D10_2]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D10_2.sideFacing
                                        Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.current_square, Meta.BOARD_SQUARES[current_player.currentSquare]))
                                        Meta.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [current_player.playerName + " moved backward"]))
                                        if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Meta.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Meta.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                elif Meta.ROLLING_WITH_DISADVANTAGE:
                                    Meta.TOP_DICE = [D10, D10_2]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D10.check_click()
                                    D10_2.check_click()
                                    if not D10.enabled and not D10_2.enabled:
                                        Meta.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        if D10.sideFacing >= D10_2.sideFacing:
                                            Meta.TOP_DICE = [D10]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D10.sideFacing
                                        else:
                                            Meta.TOP_DICE = [D10_2]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D10_2.sideFacing
                                        Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]))
                                        Meta.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [current_player.playerName + " moved backward"]))
                                        if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Meta.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Meta.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                else:
                                    Meta.TOP_DICE = [D10]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    if D10.check_click():
                                        Meta.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        Meta.TOP_DICE = [D10]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D10.sideFacing
                                        Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]))
                                        Meta.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [current_player.playerName + " moved backward"]))
                                        if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Meta.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Meta.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                    elif current_square.symbol == "Back8":
                        if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.TWO:
                                    Meta.FORCED_CARD = CardValue.TWO
                        if Meta.FORCED_CARD == CardValue.TWO:
                            draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Meta.FORCED_MOVEMENT:
                                draw_text("You are safe for now", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                draw_text("Roll d8 to go Back:", SMALL_FONT, BLACK, (1680, 240))
                                if Meta.ROLLING_WITH_ADVANTAGE:
                                    Meta.TOP_DICE = [D8, D8_2]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D8.check_click()
                                    D8_2.check_click()
                                    if not D8.enabled and not D8_2.enabled:
                                        Meta.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        if D8.sideFacing <= D8_2.sideFacing:
                                            Meta.TOP_DICE = [D8]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D8.sideFacing
                                        else:
                                            Meta.TOP_DICE = [D8_2]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D8_2.sideFacing
                                        Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]))
                                        Meta.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [current_player.playerName + " moved backward"]))
                                        if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Meta.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Meta.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                elif Meta.ROLLING_WITH_DISADVANTAGE:
                                    Meta.TOP_DICE = [D8, D8_2]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D8.check_click()
                                    D8_2.check_click()
                                    if not D8.enabled and not D8_2.enabled:
                                        Meta.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        if D8.sideFacing >= D8_2.sideFacing:
                                            Meta.TOP_DICE = [D8]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D8.sideFacing
                                        else:
                                            Meta.TOP_DICE = [D8_2]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D8_2.sideFacing
                                        Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]))
                                        Meta.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [current_player.playerName + " moved backward"]))
                                        if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Meta.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Meta.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                else:
                                    Meta.TOP_DICE = [D8]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    if D8.check_click():
                                        Meta.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        Meta.TOP_DICE = [D8]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D8.sideFacing
                                        Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]))
                                        Meta.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [current_player.playerName + " moved backward"]))
                                        if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Meta.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Meta.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                    elif current_square.symbol == "DownKey":
                        if not Meta.FORCED_MOVEMENT:
                            draw_text("You gain common sense", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("The key unlocks a door", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("Use the door to go South", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Meta.FORCED_MOVEMENT = False
                                current_square.players.remove(current_player)
                                updated_squares = [(current_player.currentSquare, current_square)]
                                current_player.currentSquare = current_square.keyLocation
                                Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                updated_squares.append((current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]))
                                Meta.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [current_player.playerName + " moved down"]))
                    elif current_square.symbol == "GoBack":
                        if not Meta.FORCED_MOVEMENT:
                            draw_text("You beat fate this time", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("You are going back", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("from whence you came", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Meta.FORCED_MOVEMENT = False
                                current_square.players.remove(current_player)
                                updated_squares = [(current_player.currentSquare, current_square)]
                                current_player.currentSquare -= Meta.SQUARES_TO_MOVE
                                Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                updated_squares.append((current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]))
                                Meta.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [current_player.playerName + " moved back from whence they came"]))
                                if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                    Meta.FORCED_MOVEMENT = True
                                    D10.enabled = True
                                    D10_2.enabled = True
                                    D8.enabled = True
                                    D8_2.enabled = True
                                elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                    Meta.BONUS_MOVEMENT = True
                                    D10.enabled = True
                                    D10_2.enabled = True
                                    D8.enabled = True
                                    D8_2.enabled = True
                    elif current_square.symbol == "UpKey":
                        if Meta.FORCED_CARD is None and Meta.BONUS_MOVEMENT:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.SIX:
                                    Meta.FORCED_CARD = CardValue.SIX
                        if Meta.FORCED_CARD == CardValue.SIX:
                            draw_text("Use your Red Six!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Meta.BONUS_MOVEMENT:
                                draw_text("You don't get to move", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                draw_text("You find a key", SMALL_FONT, BLACK, (1680, 230))
                                draw_text("Use the key to go North", SMALL_FONT, BLACK, (1680, 260))
                                continue_button = Button("Continue", 1680, 600, 60)
                                if continue_button.check_click():
                                    Meta.BONUS_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    updated_squares = [(current_player.currentSquare, current_square)]
                                    current_player.currentSquare = current_square.keyLocation
                                    Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    updated_squares.append((current_player.currentSquare, Meta.BOARD_SQUARES[current_player.currentSquare]))
                                    Meta.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [current_player.playerName + " moved up"]))
                    elif current_square.symbol == "Redo":
                        if Meta.FORCED_CARD is None and Meta.BONUS_MOVEMENT:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.SIX:
                                    Meta.FORCED_CARD = CardValue.SIX
                        if Meta.FORCED_CARD == CardValue.SIX:
                            draw_text("Use your Red Six!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Meta.BONUS_MOVEMENT:
                                draw_text("You don't get to move", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                draw_text("You get Double Movement", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("Continue", 1680, 600, 60)
                                if continue_button.check_click():
                                    Meta.BONUS_MOVEMENT = False
                                    Meta.TURN_STAGE = TurnStage.MOVEMENT
                    elif current_square.symbol == "MissTurn":
                        draw_text("You Miss your Next Turn", SMALL_FONT, BLACK, (1680, 240))
                        current_player.missNextTurn = True
                        Meta.NETWORK.send(("Player", current_player))
                        continue_button = Button("End Turn", 1680, 600, 60)
                        if continue_button.check_click():
                            end_turn()
                    elif current_square.symbol == "Monster":
                        if current_square.monsterHealth > 0:
                            if not current_square.monsterAwake:
                                draw_text("You have awoken a Monster!", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("Fight!", 1680, 600, 60)
                                if continue_button.check_click():
                                    current_square.monsterAwake = True
                                    Meta.NETWORK.send(("SquareEvents", (current_player.currentSquare, current_square), [current_player.playerName + " woke a Monster"]))
                                    D12.enabled = True
                                    D12_2.enabled = True
                                    Meta.TOP_DICE = [D12]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                    Meta.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                    Meta.TURN_STAGE = TurnStage.ATTACK_MONSTER
                            else:
                                draw_text("You join a Monster fight!", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("Fight!", 1680, 600, 60)
                                if continue_button.check_click():
                                    Meta.NETWORK.send(("Events", [current_player.playerName + " joined a Monster Fight"]))
                                    D12.enabled = True
                                    D12_2.enabled = True
                                    Meta.TOP_DICE = [D12]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                    Meta.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                    Meta.TURN_STAGE = TurnStage.ATTACK_MONSTER
                        else:
                            Meta.CAN_PROGRESS = True
                    elif current_square.symbol is None:
                        Meta.CAN_PROGRESS = True
                    if Meta.CAN_PROGRESS:
                        Meta.TURN_STAGE = TurnStage.END_TURN
            elif Meta.TURN_STAGE == TurnStage.DRAW_CARDS:
                if Meta.FORCED_CARD is None and len(Meta.CARDS_TO_DRAW) > 0:
                    for card_type in Meta.CARDS_TO_DRAW:
                        if card_type == CardType.BLUE:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.QUEEN:
                                    Meta.FORCED_CARD = CardValue.QUEEN
                            break
                if Meta.FORCED_CARD == CardValue.QUEEN:
                    draw_text("Use your Red Queen Card!", SMALL_FONT, BLACK, (1680, 240))
                else:
                    if len(Meta.CARDS_TO_DRAW) == 0:
                        Meta.TURN_STAGE = TurnStage.END_TURN
                    else:
                        draw_dice_sets()
                        if Meta.CARDS_TO_DRAW[0] == CardType.BLUE:
                            if not Meta.DISPLAYING_CARD:
                                draw_text("Draw a Blue Card:", SMALL_FONT, BLACK, (1680, 240))
                                check_get_card(CardType.BLUE)
                            else:
                                draw_card(current_player.blueDeck[len(current_player.blueDeck) - 1], (1680, 380), 3)
                                if len(Meta.CARDS_TO_DRAW) == 1:
                                    text = "End Turn"
                                else:
                                    text = "Continue"
                                continue_button = Button(text, 1680, 600, 60)
                                if continue_button.check_click():
                                    Meta.DISPLAYING_CARD = False
                                    Meta.CARDS_TO_DRAW.pop(0)
                                    if len(Meta.CARDS_TO_DRAW) == 0:
                                        end_turn()
                        else:
                            if not Meta.DISPLAYING_CARD:
                                draw_text("Draw a Red Card:", SMALL_FONT, BLACK, (1680, 240))
                                check_get_card(CardType.RED)
                            else:
                                draw_card(current_player.redDeck[len(current_player.redDeck) - 1], (1680, 380), 3)
                                if len(Meta.CARDS_TO_DRAW) == 1:
                                    text = "End Turn"
                                else:
                                    text = "Continue"
                                continue_button = Button(text, 1680, 600, 60)
                                if continue_button.check_click():
                                    Meta.DISPLAYING_CARD = False
                                    Meta.CARDS_TO_DRAW.pop(0)
                                    if len(Meta.CARDS_TO_DRAW) == 0:
                                        end_turn()
            elif Meta.TURN_STAGE == TurnStage.END_TURN:
                draw_dice_sets()
                continue_button = Button("End Turn", 1680, 600, 60)
                if continue_button.check_click():
                    end_turn()
            elif Meta.TURN_STAGE == TurnStage.GAME_WON:
                draw_text(current_player.playerName + " has Won!!", SMALL_FONT, BLACK, (1680, 240))
            if Meta.SHOW_HAND is None and Meta.CHOOSE_DICE is None and Meta.CHOOSE_PLAYERS is None and Meta.CHOOSE_SQUARE is None:
                quit_button = Button("Quit", 360, 450, 60)
                if quit_button.check_click():
                    pygame.quit()
            check_hover_boxes()
    elif Meta.CURRENT_STATE == ScreenState.PLAYING_GAME:
        WINDOW.fill(WHITE)
        Meta.BUTTONS_ENABLED = True
        current_player = Meta.PLAYERS[Meta.CURRENT_PLAYER]
        draw_text(current_player.playerName + "'s Turn", SMALL_FONT, PLAYER_TO_COLOUR[current_player.playerNumber], (960, 30))
        game_board = pygame.Rect((480, 60), (960, 960))
        pygame.draw.rect(WINDOW, BLUE, game_board)
        roll_background = pygame.Rect((1460, 100), (440, 700))
        pygame.draw.rect(WINDOW, PASTEL_GREEN, roll_background, 0, 20)
        draw_game_image(BLUE_CARD_SYMBOL, (360, 250), 3, True, PASTEL_GREEN, (170, 75),
                        "Blue Draw Pile", "", "Current Size: " + str(len(Meta.BLUE_DRAW_DECK)))
        draw_game_image(RED_CARD_SYMBOL, (360, 650), 3, True, PASTEL_GREEN, (170, 75),
                        "Red Draw Pile", "", "Current Size: " + str(len(Meta.RED_DRAW_DECK)))
        if len(current_player.blueDeck) != 0:
            turned_blue_deck_image = pygame.transform.rotate(BLUE_CARD_SYMBOL[0], -90)
            turned_blue_deck_image = pygame.transform.scale(turned_blue_deck_image, (BLUE_CARD_SYMBOL[1][1] * 3, BLUE_CARD_SYMBOL[1][0] * 3))
            WINDOW.blit(turned_blue_deck_image, (95, 835))
            if Meta.CARD_HANDS_ACTIVE: Meta.HOVER_BOXES.append(("board symbol", ["Your Blue Card Hand"], turned_blue_deck_image, (95, 835), (215, 35), PASTEL_GREEN))
            blue_hand_rect = turned_blue_deck_image.get_rect()
            blue_hand_rect.topleft = (95, 835)
            if blue_hand_rect.collidepoint(pygame.mouse.get_pos()) and Meta.LEFT_MOUSE_RELEASED and Meta.CARD_HANDS_ACTIVE:
                Meta.SHOW_HAND = CardType.BLUE
                Meta.CARD_HANDS_ACTIVE = False
                if Meta.TURN_STAGE == TurnStage.DRAW_CARDS:
                    if Meta.DISPLAYING_CARD:
                        Meta.CARDS_TO_DRAW.pop(0)
                        Meta.DISPLAYING_CARD = False
        if len(current_player.redDeck) != 0:
            turned_red_deck_image = pygame.transform.rotate(RED_CARD_SYMBOL[0], 90)
            turned_red_deck_image = pygame.transform.scale(turned_red_deck_image, (RED_CARD_SYMBOL[1][1] * 3, RED_CARD_SYMBOL[1][0] * 3))
            WINDOW.blit(turned_red_deck_image, (1530, 835))
            if Meta.CARD_HANDS_ACTIVE: Meta.HOVER_BOXES.append(("board symbol", ["Your Red Card Hand"], turned_red_deck_image, (1530, 835), (215, 35), PASTEL_GREEN))
            red_hand_rect = turned_red_deck_image.get_rect()
            red_hand_rect.topleft = (1530, 835)
            if red_hand_rect.collidepoint(pygame.mouse.get_pos()) and Meta.LEFT_MOUSE_RELEASED and Meta.CARD_HANDS_ACTIVE:
                Meta.SHOW_HAND = CardType.RED
                Meta.CARD_HANDS_ACTIVE = False
                if Meta.TURN_STAGE == TurnStage.DRAW_CARDS:
                    if Meta.DISPLAYING_CARD:
                        Meta.CARDS_TO_DRAW.pop(0)
                        Meta.DISPLAYING_CARD = False
        draw_squares()
        if Meta.SHOW_HAND == CardType.BLUE:
            Meta.HOVER_BOXES.clear()
            WINDOW.fill(PASTEL_GREEN)
            draw_text(current_player.playerName + "'s Blue Card Hand", MEDIUM_FONT, ORANGE, (960, 69))
            back_button = Button("Back", 960, 950, 60)
            if back_button.check_click():
                Meta.SHOW_HAND = None
                Meta.CARD_HANDS_ACTIVE = True
            for x in range(len(current_player.blueDeck)):
                draw_card(current_player.blueDeck[x], CARD_TO_POSITION[x], 2)
            Meta.BUTTONS_ENABLED = False
            check_hover_boxes()
        elif Meta.SHOW_HAND == CardType.RED:
            Meta.HOVER_BOXES.clear()
            WINDOW.fill(PASTEL_GREEN)
            draw_text(current_player.playerName + "'s Red Card Hand", MEDIUM_FONT, ORANGE, (960, 69))
            back_button = Button("Back", 960, 950, 60)
            if back_button.check_click():
                Meta.SHOW_HAND = None
                Meta.CARD_HANDS_ACTIVE = True
            for x in range(len(current_player.redDeck)):
                draw_card(current_player.redDeck[x], CARD_TO_POSITION[x], 2)
            Meta.BUTTONS_ENABLED = False
            check_hover_boxes()
        elif Meta.CHOOSE_PLAYERS is not None:
            Meta.HOVER_BOXES.clear()
            WINDOW.fill(PASTEL_GREEN)
            draw_text("Choose a Player:", MEDIUM_FONT, ORANGE, (960, 69))
            player = None
            for x in range(len(Meta.PLAYERS)):
                if Meta.PLAYERS[x] != current_player:
                    if Meta.CHOOSE_PLAYERS == "Red Five":
                        if Meta.PLAYERS[x].setPlayerRoll is None:
                            button = Button(Meta.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                            if button.check_click():
                                player = Meta.PLAYERS[x]
                    elif Meta.CHOOSE_PLAYERS == "Blue Five":
                        if Meta.PLAYERS[x].setNextRoll is None:
                            button = Button(Meta.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                            if button.check_click():
                                player = Meta.PLAYERS[x]
                    else:
                        button = Button(Meta.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                        if button.check_click():
                            player = Meta.PLAYERS[x]
            if player is not None:
                if Meta.CHOOSE_PLAYERS == "Blue Three":
                    for x in range(len(Meta.PLAYERS)):
                        if Meta.PLAYERS[x] != player and Meta.PLAYERS[x] != current_player:
                            Meta.PLAYERS[x].redDeck.append(Meta.RED_DRAW_DECK.pop())
                    Meta.CHOOSE_PLAYERS = None
                elif Meta.CHOOSE_PLAYERS == "Red Three":
                    for x in range(len(Meta.PLAYERS)):
                        if Meta.PLAYERS[x] != player and Meta.PLAYERS[x] != current_player:
                            Meta.PLAYERS[x].blueDeck.append(Meta.BLUE_DRAW_DECK.pop())
                    Meta.CHOOSE_PLAYERS = None
                elif Meta.CHOOSE_PLAYERS == "Blue Five":
                    Meta.CHOOSE_PLAYERS = None
                    Meta.CHOOSE_DICE = player
                elif Meta.CHOOSE_PLAYERS == "Red Five":
                    Meta.CHOOSE_PLAYERS = None
                    player.setPlayerRoll = current_player
            Meta.BUTTONS_ENABLED = False
        elif Meta.CHOOSE_DICE is not None:
            Meta.HOVER_BOXES.clear()
            WINDOW.fill(PASTEL_GREEN)
            draw_text("Choose a Dice Value:", MEDIUM_FONT, ORANGE, (960, 69))
            one_d6 = Dice(1, D6_IMAGES)
            two_d6 = Dice(2, D6_IMAGES)
            three_d6 = Dice(3, D6_IMAGES)
            four_d6 = Dice(4, D6_IMAGES)
            five_d6 = Dice(5, D6_IMAGES)
            six_d6 = Dice(6, D6_IMAGES)
            draw_dice(one_d6, CARD_TO_POSITION[0], 2)
            draw_dice(two_d6, CARD_TO_POSITION[1], 2)
            draw_dice(three_d6, CARD_TO_POSITION[2], 2)
            draw_dice(four_d6, CARD_TO_POSITION[3], 2)
            draw_dice(five_d6, CARD_TO_POSITION[4], 2)
            draw_dice(six_d6, CARD_TO_POSITION[5], 2)
            if one_d6.check_click(False):
                Meta.CHOOSE_DICE.setNextRoll = 1
                Meta.CHOOSE_DICE = None
            if two_d6.check_click(False):
                Meta.CHOOSE_DICE.setNextRoll = 2
                Meta.CHOOSE_DICE = None
            if three_d6.check_click(False):
                Meta.CHOOSE_DICE.setNextRoll = 3
                Meta.CHOOSE_DICE = None
            if four_d6.check_click(False):
                Meta.CHOOSE_DICE.setNextRoll = 4
                Meta.CHOOSE_DICE = None
            if five_d6.check_click(False):
                Meta.CHOOSE_DICE.setNextRoll = 5
                Meta.CHOOSE_DICE = None
            if six_d6.check_click(False):
                Meta.CHOOSE_DICE.setNextRoll = 6
                Meta.CHOOSE_DICE = None
            Meta.BUTTONS_ENABLED = False
        elif Meta.CHOOSE_SQUARE is not None:
            Meta.HOVER_BOXES.clear()
            WINDOW.fill(PASTEL_GREEN)
            draw_text("Choose a Square:", MEDIUM_FONT, ORANGE, (960, 30))
            draw_squares()
            square_clicked = check_squares_clicked()
            if square_clicked is not None and Meta.BOARD_SQUARES.index(square_clicked) != 99 and Meta.BOARD_SQUARES.index(square_clicked) != 0:
                if Meta.CHOOSE_SQUARE == "Blue Nine" or Meta.CHOOSE_SQUARE == "Red Nine":
                    if not square_clicked.hasBarrier:
                        square_clicked.hasBarrier = True
                        Meta.CHOOSE_SQUARE = None
            Meta.BUTTONS_ENABLED = False
        elif Meta.TURN_STAGE == TurnStage.START_TURN:  # Calculations at the start of all turns
            D8.enabled = True
            D8_2.enabled = True
            D10.enabled = True
            D10_2.enabled = True
            if current_player.missNextTurn:  # Miss a Turn
                draw_text("You don't get to take this turn", SMALL_FONT, BLACK, (1680, 240))
                continue_button = Button("Continue", 1680, 600, 60)
                if continue_button.check_click():
                    current_player.missNextTurn = False
                    end_turn()
            else:
                if current_player.setPlayerRoll is not None:
                    draw_text("Set " + current_player.setPlayerRoll.playerName + "'s", SMALL_FONT, BLACK, (1680, 230))
                    draw_text("Next Dice Roll", SMALL_FONT, BLACK, (1680, 260))
                    continue_button = Button("Continue", 1680, 600, 60)
                    if continue_button.check_click():
                        Meta.CHOOSE_DICE = current_player.setPlayerRoll
                        current_player.setPlayerRoll = None
                else:
                    if Meta.FORCED_CARD is None:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.THREE:
                                Meta.FORCED_CARD = CardValue.THREE
                                break
                            if card.cardValue == CardValue.FIVE:
                                Meta.FORCED_CARD = CardValue.FIVE
                                break
                            if card.cardValue == CardValue.NINE:
                                Meta.FORCED_CARD = CardValue.NINE
                                break
                    if Meta.FORCED_CARD == CardValue.THREE:
                        draw_text("Use your Red Three Card!", SMALL_FONT, BLACK, (1680, 240))
                    elif Meta.FORCED_CARD == CardValue.FIVE:
                        draw_text("Use your Red Five Card!", SMALL_FONT, BLACK, (1680, 240))
                    elif Meta.FORCED_CARD == CardValue.NINE:
                        draw_text("Use your Red Nine Card!", SMALL_FONT, BLACK, (1680, 240))
                    elif Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth > 0:
                        D20.enabled = True
                        D20_2.enabled = True
                        D20_3.enabled = True
                        Meta.SUCCEEDED_DEFENCE = None
                        Meta.TURN_STAGE = TurnStage.MONSTER_ATTACK
                    else:  # Roll Dice
                        Meta.TOP_DICE = [D6]
                        Meta.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                        draw_dice_sets()
                        D6.enabled = True
                        D6_2.enabled = True
                        Meta.TURN_STAGE = TurnStage.ROLL_DICE
        elif Meta.TURN_STAGE == TurnStage.MONSTER_ATTACK:  # Monster Attacks
            if Meta.SUCCEEDED_DEFENCE is None: draw_text("Defend against the Monster!", SMALL_FONT, BLACK, (1680, 240))
            if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                for card in current_player.redDeck:
                    if card.cardValue == CardValue.TWO:
                        Meta.FORCED_CARD = CardValue.TWO
            if Meta.FORCED_CARD is None and Meta.SUCCEEDED_DEFENCE:
                for card in current_player.redDeck:
                    if card.cardValue == CardValue.EIGHT:
                        Meta.FORCED_CARD = CardValue.EIGHT
            if Meta.FORCED_CARD == CardValue.TWO:
                draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
            elif Meta.FORCED_CARD == CardValue.EIGHT:
                draw_text("Use your Red Eight Card!", SMALL_FONT, BLACK, (1680, 240))
            else:
                if D20_3.enabled:
                    D20_3.sideFacing = random.randrange(1, 21)
                    D20_3.enabled = False
                draw_dice(D20_3, (1680, 330), 2)
                if Meta.ROLLING_WITH_ADVANTAGE:
                    Meta.TOP_DICE = [D20, D20_2]
                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                    Meta.BOTTOM_DICE = [D10, D10_2, D12, D12_2, D4]
                    D20.check_click()
                    D20_2.check_click()
                    if not D20.enabled and not D20_2.enabled and Meta.SUCCEEDED_DEFENCE is None:
                        Meta.SUCCEEDED_DEFENCE = max(D20.sideFacing, D20_2.sideFacing) >= D20_3.sideFacing
                        if not Meta.SUCCEEDED_DEFENCE:
                            for card in current_player.blueDeck:
                                if card.cardValue == CardValue.EIGHT:
                                    Meta.CARD_TO_REMOVE = (current_player.blueDeck, card)
                                    Meta.DISCARD_PILE.append(card)
                                    Meta.SHIELD_ACTIVE = True
                                    break
                elif Meta.ROLLING_WITH_DISADVANTAGE:
                    Meta.TOP_DICE = [D20, D20_2]
                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                    Meta.BOTTOM_DICE = [D10, D10_2, D12, D12_2, D4]
                    D20.check_click()
                    D20_2.check_click()
                    if not D20.enabled and not D20_2.enabled and Meta.SUCCEEDED_DEFENCE is None:
                        Meta.SUCCEEDED_DEFENCE = min(D20.sideFacing, D20_2.sideFacing) >= D20_3.sideFacing
                        if not Meta.SUCCEEDED_DEFENCE:
                            for card in current_player.blueDeck:
                                if card.cardValue == CardValue.EIGHT:
                                    Meta.CARD_TO_REMOVE = (current_player.blueDeck, card)
                                    Meta.DISCARD_PILE.append(card)
                                    Meta.SHIELD_ACTIVE = True
                                    break
                else:
                    Meta.TOP_DICE = [D20]
                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                    Meta.BOTTOM_DICE = [D10_2, D12, D12_2, D20_2, D4]
                    if D20.check_click():
                        Meta.SUCCEEDED_DEFENCE = D20.sideFacing >= D20_3.sideFacing
                        if not Meta.SUCCEEDED_DEFENCE:
                            for card in current_player.blueDeck:
                                if card.cardValue == CardValue.EIGHT:
                                    Meta.CARD_TO_REMOVE = (current_player.blueDeck, card)
                                    Meta.DISCARD_PILE.append(card)
                                    Meta.SHIELD_ACTIVE = True
                                    break
                draw_dice_sets(500)
                if Meta.SUCCEEDED_DEFENCE is not None:
                    if not Meta.SUCCEEDED_DEFENCE:  # Player Loses
                        if Meta.SHIELD_ACTIVE:
                            draw_text("Your Shield saved you", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("You survived the encounter", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Meta.ROLLING_WITH_ADVANTAGE = False
                                Meta.ROLLING_WITH_DISADVANTAGE = False
                                Meta.TOP_DICE = [D12]
                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                Meta.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                Meta.TURN_STAGE = TurnStage.ATTACK_MONSTER
                                D12.enabled = True
                                D12_2.enabled = True
                                Meta.SHIELD_ACTIVE = False
                        else:
                            draw_text("You failed your Defence Roll", SMALL_FONT, BLACK, (1680, 200))
                            draw_text("The Monster will knock you", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("back 4 spaces", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Meta.ROLLING_WITH_ADVANTAGE = False
                                Meta.ROLLING_WITH_DISADVANTAGE = False
                                Meta.BOARD_SQUARES[current_player.currentSquare].players.remove(current_player)
                                current_player.currentSquare -= 4
                                Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                Meta.TURN_STAGE = TurnStage.START_TURN
                    else:
                        draw_text("You defended yourself", SMALL_FONT, BLACK, (1680, 240))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            Meta.ROLLING_WITH_ADVANTAGE = False
                            Meta.ROLLING_WITH_DISADVANTAGE = False
                            Meta.TOP_DICE = [D12]
                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                            Meta.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                            Meta.TURN_STAGE = TurnStage.ATTACK_MONSTER
                            D12.enabled = True
                            D12_2.enabled = True
        elif Meta.TURN_STAGE == TurnStage.ATTACK_MONSTER:  # Attacking a Monster
            if Meta.FORCED_CARD is None and not Meta.TAKING_FOUR and not Meta.TAKEN_FOUR:
                for card in current_player.redDeck:
                    if card.cardValue == CardValue.FOUR:
                        Meta.FORCED_CARD = CardValue.FOUR
            if Meta.FORCED_CARD == CardValue.FOUR:
                draw_text("Use your Red Four!", SMALL_FONT, BLACK, (1680, 240))
            else:
                if Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth <= 0:
                    draw_text("Congratulations!", SMALL_FONT, BLACK, (1680, 200))
                    draw_text("You have killed the Monster!", SMALL_FONT, BLACK, (1680, 230))
                    draw_text("You can roll movement now", SMALL_FONT, BLACK, (1680, 260))
                    continue_button = Button("Continue", 1680, 600, 60)
                    if continue_button.check_click():
                        Meta.TURN_STAGE = TurnStage.START_TURN
                        Meta.ADDING_FOUR = False
                        Meta.TAKING_FOUR = False
                        Meta.TAKEN_FOUR = False
                        Meta.ROLLING_WITH_ADVANTAGE = False
                        Meta.BOARD_SQUARES[current_player.currentSquare].monsterAwake = False
                elif not D12.enabled and not D12_2.enabled:
                    if Meta.ADDING_FOUR:
                        draw_text("Add a d4 to the Attack:", SMALL_FONT, BLACK, (1680, 240))
                        Meta.TOP_DICE = [D4]
                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                        Meta.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                        draw_dice_sets()
                        if D4.check_click():
                            Meta.ADDING_FOUR = False
                            Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= D4.sideFacing
                    elif Meta.TAKING_FOUR and not Meta.TAKEN_FOUR:
                        draw_text("Take a d4 from the Attack:", SMALL_FONT, BLACK, (1680, 240))
                        Meta.TOP_DICE = [D4]
                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                        Meta.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                        draw_dice_sets()
                        if D4.check_click():
                            Meta.TAKEN_FOUR = True
                            Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth += D4.sideFacing
                    else:
                        draw_text("You did not kill the Monster", SMALL_FONT, BLACK, (1680, 240))
                        end_turn_button = Button("End Turn", 1680, 600, 60)
                        if end_turn_button.check_click():
                            end_turn()
                            Meta.TAKEN_FOUR = False
                            Meta.TAKING_FOUR = False
                            Meta.ROLLING_WITH_ADVANTAGE = False
                else:
                    draw_text("Attack the Monster:", SMALL_FONT, BLACK, (1680, 240))
                    if Meta.ROLLING_WITH_ADVANTAGE:
                        Meta.TOP_DICE = [D12, D12_2]
                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                        Meta.BOTTOM_DICE = [D10, D10_2, D20, D20_2, D4]
                    if not Meta.ROLLING_WITH_ADVANTAGE:
                        if D12.check_click():
                            D12_2.enabled = False
                            Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= D12.sideFacing
                    else:
                        D12.check_click()
                        D12_2.check_click()
                        if not D12.enabled and not D12_2.enabled:
                            Meta.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= max(D12.sideFacing, D12_2.sideFacing)
                draw_dice_sets()
        elif Meta.TURN_STAGE == TurnStage.ROLL_DICE:  # Rolling the Movement Dice
            if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                for card in current_player.redDeck:
                    if card.cardValue == CardValue.TWO:
                        Meta.FORCED_CARD = CardValue.TWO
            if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_FOUR:
                for card in current_player.redDeck:
                    if card.cardValue == CardValue.JACK:
                        Meta.FORCED_CARD = CardValue.JACK
            if Meta.FORCED_CARD == CardValue.TWO:
                draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
            elif Meta.FORCED_CARD == CardValue.JACK:
                draw_text("Use your Red Jack Card!", SMALL_FONT, BLACK, (1680, 240))
            else:
                if Meta.ROLLING_WITH_FOUR:
                    Meta.TOP_DICE = [D4]
                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                    Meta.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                    draw_text("Roll d4 to move:", SMALL_FONT, BLACK, (1680, 240))
                    draw_dice_sets()
                    if D4.check_click():
                        Meta.ROLLING_WITH_FOUR = False
                        Meta.SQUARES_TO_MOVE = D4.sideFacing
                        Meta.TURN_STAGE = TurnStage.MOVEMENT
                elif Meta.ROLLING_WITH_ADVANTAGE and Meta.DICE_ROLLED == 2:
                    draw_text("Pick a dice to use:", SMALL_FONT, BLACK, (1680, 240))
                    draw_dice_sets()
                    if D6.check_click(False):
                        Meta.ROLLING_WITH_ADVANTAGE = False
                        Meta.DICE_ROLLED = 0
                        Meta.SQUARES_TO_MOVE = D6.sideFacing
                        Meta.TURN_STAGE = TurnStage.MOVEMENT
                        Meta.TOP_DICE = [D6]
                        Meta.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                    if D6_2.check_click(False):
                        Meta.ROLLING_WITH_ADVANTAGE = False
                        Meta.DICE_ROLLED = 0
                        Meta.SQUARES_TO_MOVE = D6_2.sideFacing
                        Meta.TURN_STAGE = TurnStage.MOVEMENT
                        Meta.TOP_DICE = [D6_2]
                        Meta.MIDDLE_DICE = [D6, D8, D8_2, D10, D10_2]
                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                else:
                    draw_text("Roll d6 to move:", SMALL_FONT, BLACK, (1680, 240))
                    if not Meta.ROLLING_WITH_ADVANTAGE and not Meta.ROLLING_DOUBLE and not Meta.ROLLING_WITH_DISADVANTAGE:
                        draw_dice_sets()
                        if D6.check_click():
                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                            Meta.SQUARES_TO_MOVE = D6.sideFacing
                    elif Meta.ROLLING_WITH_ADVANTAGE:
                        Meta.TOP_DICE = [D6, D6_2]
                        Meta.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                        draw_dice_sets()
                        if D6.check_click():
                            Meta.DICE_ROLLED += 1
                        if D6_2.check_click():
                            Meta.DICE_ROLLED += 1
                        if Meta.DICE_ROLLED == 2:
                            D6.enabled = True
                            D6_2.enabled = True
                    elif Meta.ROLLING_WITH_DISADVANTAGE:
                        Meta.TOP_DICE = [D6, D6_2]
                        Meta.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                        draw_dice_sets()
                        D6.check_click()
                        D6_2.check_click()
                        if not D6.enabled and not D6_2.enabled:
                            Meta.SQUARES_TO_MOVE = min(D6.sideFacing, D6_2.sideFacing)
                            if D6.sideFacing > D6_2.sideFacing:
                                Meta.TOP_DICE = [D6_2]
                                Meta.MIDDLE_DICE = [D6, D8, D8_2, D10, D10_2]
                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            else:
                                Meta.TOP_DICE = [D6]
                                Meta.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                            Meta.ROLLING_WITH_DISADVANTAGE = False
                    elif Meta.ROLLING_DOUBLE:
                        Meta.TOP_DICE = [D6, D6_2]
                        Meta.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                        draw_dice_sets()
                        D6.check_click()
                        D6_2.check_click()
                        if not D6.enabled and not D6_2.enabled:
                            Meta.SQUARES_TO_MOVE = D6.sideFacing + D6_2.sideFacing
                            Meta.TURN_STAGE = TurnStage.MOVEMENT
                            Meta.ROLLING_DOUBLE = False
        elif Meta.TURN_STAGE == TurnStage.MOVEMENT:  # Moving the Current Player
            draw_dice_sets()
            for x in range(Meta.SQUARES_TO_MOVE):
                if Meta.BOARD_SQUARES[current_player.currentSquare + x].hasBarrier and x != 0:
                    has_ten = False
                    for card in current_player.blueDeck:
                        if card.cardValue == CardValue.TEN:
                            Meta.CARD_TO_REMOVE = (current_player.blueDeck, card)
                            Meta.DISCARD_PILE.append(card)
                            has_ten = True
                            break
                    if not has_ten:
                        Meta.SQUARES_TO_MOVE = x
                        Meta.BOARD_SQUARES[current_player.currentSquare + x].hasBarrier = False
                        break
                elif Meta.BOARD_SQUARES[current_player.currentSquare + x].monsterAwake:
                    Meta.SQUARES_TO_MOVE = x
                    break
            Meta.BOARD_SQUARES[current_player.currentSquare].players.remove(current_player)
            current_player.currentSquare = min(99, current_player.currentSquare + Meta.SQUARES_TO_MOVE)
            Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
            Meta.TURN_STAGE = TurnStage.SQUARE_ACTION
            Meta.CAN_PROGRESS = False
            if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                Meta.FORCED_MOVEMENT = True
                D10.enabled = True
                D10_2.enabled = True
                D8.enabled = True
                D8_2.enabled = True
            elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                Meta.BONUS_MOVEMENT = True
                D10.enabled = True
                D10_2.enabled = True
                D8.enabled = True
                D8_2.enabled = True
        elif Meta.TURN_STAGE == TurnStage.SQUARE_ACTION:  # Doing what the Square wants
            draw_dice_sets()
            current_square = Meta.BOARD_SQUARES[current_player.currentSquare]
            if current_player.currentSquare == 99:
                Meta.TURN_STAGE = TurnStage.GAME_WON
            else:
                if current_square.symbol == "OneBlue":
                    Meta.TURN_STAGE = TurnStage.DRAW_CARDS
                    Meta.CARDS_TO_DRAW.append(CardType.BLUE)
                elif current_square.symbol == "OneRed":
                    Meta.TURN_STAGE = TurnStage.DRAW_CARDS
                    Meta.CARDS_TO_DRAW.append(CardType.RED)
                elif current_square.symbol == "TwoRed":
                    Meta.TURN_STAGE = TurnStage.DRAW_CARDS
                    Meta.CARDS_TO_DRAW.append(CardType.RED)
                    Meta.CARDS_TO_DRAW.append(CardType.RED)
                elif current_square.symbol == "TwoBlue":
                    Meta.TURN_STAGE = TurnStage.DRAW_CARDS
                    Meta.CARDS_TO_DRAW.append(CardType.BLUE)
                    Meta.CARDS_TO_DRAW.append(CardType.BLUE)
                elif current_square.symbol == "BlueRed":
                    Meta.TURN_STAGE = TurnStage.DRAW_CARDS
                    Meta.CARDS_TO_DRAW.append(CardType.BLUE)
                    Meta.CARDS_TO_DRAW.append(CardType.RED)
                elif current_square.symbol == "Roll10":
                    if Meta.FORCED_CARD is None and Meta.BONUS_MOVEMENT:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.SIX:
                                Meta.FORCED_CARD = CardValue.SIX
                    if Meta.FORCED_CARD == CardValue.SIX:
                        draw_text("Use your Red Six Card!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Meta.BONUS_MOVEMENT:
                            draw_text("You don't get this benefit", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                                for card in current_player.redDeck:
                                    if card.cardValue == CardValue.TWO:
                                        Meta.FORCED_CARD = CardValue.TWO
                            if Meta.FORCED_CARD == CardValue.TWO:
                                draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                            else:
                                draw_text("Roll d10 to Move:", SMALL_FONT, BLACK, (1680, 240))
                                if Meta.ROLLING_WITH_ADVANTAGE:
                                    Meta.TOP_DICE = [D10, D10_2]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D10.check_click()
                                    D10_2.check_click()
                                    if not D10.enabled and not D10_2.enabled:
                                        Meta.BONUS_MOVEMENT = False
                                        if D10.sideFacing >= D10_2.sideFacing:
                                            Meta.TOP_DICE = [D10]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Meta.SQUARES_TO_MOVE = D10.sideFacing
                                        else:
                                            Meta.TOP_DICE = [D10_2]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Meta.SQUARES_TO_MOVE = D10_2.sideFacing
                                        Meta.TURN_STAGE = TurnStage.MOVEMENT
                                elif Meta.ROLLING_WITH_DISADVANTAGE:
                                    Meta.TOP_DICE = [D10, D10_2]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D10.check_click()
                                    D10_2.check_click()
                                    if not D10.enabled and not D10_2.enabled:
                                        Meta.BONUS_MOVEMENT = False
                                        if D10.sideFacing <= D10_2.sideFacing:
                                            Meta.TOP_DICE = [D10]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Meta.SQUARES_TO_MOVE = D10.sideFacing
                                        else:
                                            Meta.TOP_DICE = [D10_2]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Meta.SQUARES_TO_MOVE = D10_2.sideFacing
                                        Meta.TURN_STAGE = TurnStage.MOVEMENT
                                else:
                                    Meta.TOP_DICE = [D10]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    if D10.check_click():
                                        Meta.BONUS_MOVEMENT = False
                                        Meta.TOP_DICE = [D10]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        Meta.SQUARES_TO_MOVE = D10.sideFacing
                                        Meta.TURN_STAGE = TurnStage.MOVEMENT
                elif current_square.symbol == "Roll8":
                    if Meta.FORCED_CARD is None and Meta.BONUS_MOVEMENT:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.SIX:
                                Meta.FORCED_CARD = CardValue.SIX
                    if Meta.FORCED_CARD == CardValue.SIX:
                        draw_text("Use your Red Six Card!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Meta.BONUS_MOVEMENT:
                            draw_text("You don't get this benefit", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                                for card in current_player.redDeck:
                                    if card.cardValue == CardValue.TWO:
                                        Meta.FORCED_CARD = CardValue.TWO
                            if Meta.FORCED_CARD == CardValue.TWO:
                                draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                            else:
                                draw_text("Roll d8 to Move:", SMALL_FONT, BLACK, (1680, 240))
                                if Meta.ROLLING_WITH_ADVANTAGE:
                                    Meta.TOP_DICE = [D8, D8_2]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D8.check_click()
                                    D8_2.check_click()
                                    if not D8.enabled and not D8_2.enabled:
                                        Meta.BONUS_MOVEMENT = False
                                        if D8.sideFacing >= D8_2.sideFacing:
                                            Meta.TOP_DICE = [D8]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Meta.SQUARES_TO_MOVE = D8.sideFacing
                                        else:
                                            Meta.TOP_DICE = [D8_2]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Meta.SQUARES_TO_MOVE = D8_2.sideFacing
                                        Meta.TURN_STAGE = TurnStage.MOVEMENT
                                elif Meta.ROLLING_WITH_DISADVANTAGE:
                                    Meta.TOP_DICE = [D8, D8_2]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D8.check_click()
                                    D8_2.check_click()
                                    if not D8.enabled and not D8_2.enabled:
                                        Meta.BONUS_MOVEMENT = False
                                        if D8.sideFacing <= D8_2.sideFacing:
                                            Meta.TOP_DICE = [D8]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Meta.SQUARES_TO_MOVE = D8.sideFacing
                                        else:
                                            Meta.TOP_DICE = [D8_2]
                                            Meta.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                            Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Meta.SQUARES_TO_MOVE = D8_2.sideFacing
                                        Meta.TURN_STAGE = TurnStage.MOVEMENT
                                else:
                                    Meta.TOP_DICE = [D8]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    if D8.check_click():
                                        Meta.BONUS_MOVEMENT = False
                                        Meta.TOP_DICE = [D8]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        Meta.SQUARES_TO_MOVE = D8.sideFacing
                                        Meta.TURN_STAGE = TurnStage.MOVEMENT
                elif current_square.symbol == "Back10":
                    if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.TWO:
                                Meta.FORCED_CARD = CardValue.TWO
                    if Meta.FORCED_CARD == CardValue.TWO:
                        draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Meta.FORCED_MOVEMENT:
                            draw_text("You are safe for now", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("Roll d10 to go Back:", SMALL_FONT, BLACK, (1680, 240))
                            if Meta.ROLLING_WITH_ADVANTAGE:
                                Meta.TOP_DICE = [D10, D10_2]
                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                D10.check_click()
                                D10_2.check_click()
                                if not D10.enabled and not D10_2.enabled:
                                    Meta.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    if D10.sideFacing <= D10_2.sideFacing:
                                        Meta.TOP_DICE = [D10]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D10.sideFacing
                                    else:
                                        Meta.TOP_DICE = [D10_2]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D10_2.sideFacing
                                    Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Meta.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Meta.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                            elif Meta.ROLLING_WITH_DISADVANTAGE:
                                Meta.TOP_DICE = [D10, D10_2]
                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                D10.check_click()
                                D10_2.check_click()
                                if not D10.enabled and not D10_2.enabled:
                                    Meta.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    if D10.sideFacing >= D10_2.sideFacing:
                                        Meta.TOP_DICE = [D10]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D10.sideFacing
                                    else:
                                        Meta.TOP_DICE = [D10_2]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D10_2.sideFacing
                                    Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Meta.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Meta.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                            else:
                                Meta.TOP_DICE = [D10]
                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                if D10.check_click():
                                    Meta.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    Meta.TOP_DICE = [D10]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    current_player.currentSquare -= D10.sideFacing
                                    Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Meta.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Meta.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                elif current_square.symbol == "Back8":
                    if Meta.FORCED_CARD is None and not Meta.ROLLING_WITH_DISADVANTAGE:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.TWO:
                                Meta.FORCED_CARD = CardValue.TWO
                    if Meta.FORCED_CARD == CardValue.TWO:
                        draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Meta.FORCED_MOVEMENT:
                            draw_text("You are safe for now", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("Roll d8 to go Back:", SMALL_FONT, BLACK, (1680, 240))
                            if Meta.ROLLING_WITH_ADVANTAGE:
                                Meta.TOP_DICE = [D8, D8_2]
                                Meta.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                D8.check_click()
                                D8_2.check_click()
                                if not D8.enabled and not D8_2.enabled:
                                    Meta.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    if D8.sideFacing <= D8_2.sideFacing:
                                        Meta.TOP_DICE = [D8]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D8.sideFacing
                                    else:
                                        Meta.TOP_DICE = [D8_2]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D8_2.sideFacing
                                    Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Meta.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Meta.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                            elif Meta.ROLLING_WITH_DISADVANTAGE:
                                Meta.TOP_DICE = [D8, D8_2]
                                Meta.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                D8.check_click()
                                D8_2.check_click()
                                if not D8.enabled and not D8_2.enabled:
                                    Meta.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    if D8.sideFacing >= D8_2.sideFacing:
                                        Meta.TOP_DICE = [D8]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D8.sideFacing
                                    else:
                                        Meta.TOP_DICE = [D8_2]
                                        Meta.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                        Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D8_2.sideFacing
                                    Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Meta.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Meta.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                            else:
                                Meta.TOP_DICE = [D8]
                                Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                if D8.check_click():
                                    Meta.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    Meta.TOP_DICE = [D8]
                                    Meta.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                    Meta.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    current_player.currentSquare -= D8.sideFacing
                                    Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Meta.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Meta.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                elif current_square.symbol == "DownKey":
                    if not Meta.FORCED_MOVEMENT:
                        draw_text("You gain common sense", SMALL_FONT, BLACK, (1680, 240))
                        continue_button = Button("End Turn", 1680, 600, 60)
                        if continue_button.check_click(): end_turn()
                    else:
                        draw_text("The key unlocks a door", SMALL_FONT, BLACK, (1680, 230))
                        draw_text("Use the door to go South", SMALL_FONT, BLACK, (1680, 260))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            Meta.FORCED_MOVEMENT = False
                            current_square.players.remove(current_player)
                            current_player.currentSquare = current_square.keyLocation
                            Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                elif current_square.symbol == "GoBack":
                    if not Meta.FORCED_MOVEMENT:
                        draw_text("You beat fate this time", SMALL_FONT, BLACK, (1680, 240))
                        continue_button = Button("End Turn", 1680, 600, 60)
                        if continue_button.check_click(): end_turn()
                    else:
                        draw_text("You are going back", SMALL_FONT, BLACK, (1680, 230))
                        draw_text("from whence you came", SMALL_FONT, BLACK, (1680, 260))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            Meta.FORCED_MOVEMENT = False
                            current_square.players.remove(current_player)
                            current_player.currentSquare -= Meta.SQUARES_TO_MOVE
                            Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                            if Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                Meta.FORCED_MOVEMENT = True
                                D10.enabled = True
                                D10_2.enabled = True
                                D8.enabled = True
                                D8_2.enabled = True
                            elif Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Meta.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                Meta.BONUS_MOVEMENT = True
                                D10.enabled = True
                                D10_2.enabled = True
                                D8.enabled = True
                                D8_2.enabled = True
                elif current_square.symbol == "UpKey":
                    if Meta.FORCED_CARD is None and Meta.BONUS_MOVEMENT:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.SIX:
                                Meta.FORCED_CARD = CardValue.SIX
                    if Meta.FORCED_CARD == CardValue.SIX:
                        draw_text("Use your Red Six!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Meta.BONUS_MOVEMENT:
                            draw_text("You don't get to move", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("You find a key", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("Use the key to go North", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Meta.BONUS_MOVEMENT = False
                                current_square.players.remove(current_player)
                                current_player.currentSquare = current_square.keyLocation
                                Meta.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                elif current_square.symbol == "Redo":
                    if Meta.FORCED_CARD is None and Meta.BONUS_MOVEMENT:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.SIX:
                                Meta.FORCED_CARD = CardValue.SIX
                    if Meta.FORCED_CARD == CardValue.SIX:
                        draw_text("Use your Red Six!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Meta.BONUS_MOVEMENT:
                            draw_text("You don't get to move", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("You get Double Movement", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Meta.BONUS_MOVEMENT = False
                                Meta.TURN_STAGE = TurnStage.MOVEMENT
                elif current_square.symbol == "MissTurn":
                    draw_text("You Miss your Next Turn", SMALL_FONT, BLACK, (1680, 240))
                    current_player.missNextTurn = True
                    continue_button = Button("End Turn", 1680, 600, 60)
                    if continue_button.check_click():
                        end_turn()
                elif current_square.symbol == "Monster":
                    if current_square.monsterHealth > 0:
                        if not current_square.monsterAwake:
                            draw_text("You have awoken a Monster!", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("Fight!", 1680, 600, 60)
                            if continue_button.check_click():
                                current_square.monsterAwake = True
                                D12.enabled = True
                                D12_2.enabled = True
                                Meta.TOP_DICE = [D12]
                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                Meta.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                Meta.TURN_STAGE = TurnStage.ATTACK_MONSTER
                        else:
                            draw_text("You join a Monster fight!", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("Fight!", 1680, 600, 60)
                            if continue_button.check_click():
                                D12.enabled = True
                                D12_2.enabled = True
                                Meta.TOP_DICE = [D12]
                                Meta.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                Meta.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                Meta.TURN_STAGE = TurnStage.ATTACK_MONSTER
                    else:
                        Meta.CAN_PROGRESS = True
                elif current_square.symbol is None:
                    Meta.CAN_PROGRESS = True
                if Meta.CAN_PROGRESS:
                    Meta.TURN_STAGE = TurnStage.END_TURN
        elif Meta.TURN_STAGE == TurnStage.DRAW_CARDS:
            if Meta.FORCED_CARD is None and len(Meta.CARDS_TO_DRAW) > 0:
                for card_type in Meta.CARDS_TO_DRAW:
                    if card_type == CardType.BLUE:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.QUEEN:
                                Meta.FORCED_CARD = CardValue.QUEEN
                        break
            if Meta.FORCED_CARD == CardValue.QUEEN:
                draw_text("Use your Red Queen Card!", SMALL_FONT, BLACK, (1680, 240))
            else:
                if len(Meta.CARDS_TO_DRAW) == 0:
                    Meta.TURN_STAGE = TurnStage.END_TURN
                else:
                    draw_dice_sets()
                    if Meta.CARDS_TO_DRAW[0] == CardType.BLUE:
                        if not Meta.DISPLAYING_CARD:
                            draw_text("Draw a Blue Card:", SMALL_FONT, BLACK, (1680, 240))
                            check_get_card(CardType.BLUE)
                        else:
                            draw_card(current_player.blueDeck[len(current_player.blueDeck) - 1], (1680, 380), 3)
                            if len(Meta.CARDS_TO_DRAW) == 1:
                                text = "End Turn"
                            else:
                                text = "Continue"
                            continue_button = Button(text, 1680, 600, 60)
                            if continue_button.check_click():
                                Meta.DISPLAYING_CARD = False
                                Meta.CARDS_TO_DRAW.pop(0)
                                if len(Meta.CARDS_TO_DRAW) == 0:
                                    end_turn()
                    else:
                        if not Meta.DISPLAYING_CARD:
                            draw_text("Draw a Red Card:", SMALL_FONT, BLACK, (1680, 240))
                            check_get_card(CardType.RED)
                        else:
                            draw_card(current_player.redDeck[len(current_player.redDeck) - 1], (1680, 380), 3)
                            if len(Meta.CARDS_TO_DRAW) == 1:
                                text = "End Turn"
                            else:
                                text = "Continue"
                            continue_button = Button(text, 1680, 600, 60)
                            if continue_button.check_click():
                                Meta.DISPLAYING_CARD = False
                                Meta.CARDS_TO_DRAW.pop(0)
                                if len(Meta.CARDS_TO_DRAW) == 0:
                                    end_turn()
        elif Meta.TURN_STAGE == TurnStage.END_TURN:
            draw_dice_sets()
            continue_button = Button("End Turn", 1680, 600, 60)
            if continue_button.check_click():
                end_turn()
        elif Meta.TURN_STAGE == TurnStage.GAME_WON:
            draw_text(current_player.playerName + " has Won!!", SMALL_FONT, BLACK, (1680, 240))
        if Meta.SHOW_HAND is None and Meta.CHOOSE_DICE is None and Meta.CHOOSE_PLAYERS is None and Meta.CHOOSE_SQUARE is None:
            quit_button = Button("Quit", 360, 450, 60)
            if quit_button.check_click():
                pygame.quit()
        check_hover_boxes()


def check_server_updates():
    network_response = Meta.NETWORK.send("!")
    if network_response:
        if "curr_player" in network_response:
            Meta.CURRENT_PLAYER = network_response["curr_player"]
            if Meta.CURRENT_PLAYER == Meta.PLAYER_NUMBER:
                Meta.EVENT_LIST.clear()
        if "players" in network_response:
            Meta.PLAYERS = network_response["players"]
        if "board" in network_response:
            Meta.BOARD_SQUARES = network_response["board"]
        if "discard" in network_response:
            Meta.DISCARD_PILE = network_response["discard"]
        if "red" in network_response:
            Meta.RED_DRAW_DECK = network_response["red"]
        if "blue" in network_response:
            Meta.BLUE_DRAW_DECK = network_response["blue"]
        if "events" in network_response:
            for event in network_response["events"]:
                Meta.EVENT_LIST.append(event)
        if "square_vote" in network_response:
            Meta.CHOOSE_SQUARE = "Red Nine"


def draw_dice_sets(top_height = 330):
    if len(Meta.TOP_DICE) == 1:
        draw_dice(Meta.TOP_DICE[0], (1680, top_height), 2)
    else:
        draw_dice(Meta.TOP_DICE[0], (1628, top_height), 2)
        draw_dice(Meta.TOP_DICE[1], (1732, top_height), 2)
    for x in range(len(Meta.MIDDLE_DICE)):
        draw_dice(Meta.MIDDLE_DICE[x], (1550 + (60 * x), 690), 1)
    for x in range(len(Meta.BOTTOM_DICE)):
        draw_dice(Meta.BOTTOM_DICE[x], (1550 + (60 * x), 760), 1)


def end_turn():
    if Meta.IS_MULTIPLAYER:
        Meta.CURRENT_PLAYER = Meta.NETWORK.send("End Turn")
    else:
        if Meta.CURRENT_PLAYER == Meta.PLAYER_COUNT - 1:
            Meta.CURRENT_PLAYER = 0
        else:
            Meta.CURRENT_PLAYER += 1
    Meta.TURN_STAGE = TurnStage.START_TURN
    if Meta.ROLLING_DOUBLE: Meta.ROLLING_DOUBLE = False


def draw_squares():
    for x in range(len(Meta.BOARD_SQUARES)):
        square = Meta.BOARD_SQUARES[x]
        square_rect = pygame.Rect((square.center[0] - 44, square.center[1] - 44), (89, 89))
        pygame.draw.rect(WINDOW, WHITE, square_rect)
        if square.symbol is not None:
            if square.symbol == "Monster":
                if square.monsterHealth > 0:
                    draw_game_image((ID_TO_SYMBOLS[square.symbol], (89, 89)), square.center, 1)
                    draw_text(str(square.monsterHealth) + "hp", TINY_FONT, BLUE,
                              (square.center[0] - 10, square.center[1] + 20), False)
            else:
                draw_game_image((ID_TO_SYMBOLS[square.symbol], (89, 89)), square.center, 1)
        if square.hasBarrier:
            if Meta.BOARD_SQUARES[x + 1].center[0] > square.center[0]:
                barrier_rect = pygame.Rect((square.center[0] + 34, square.center[1] - 39), (5, 79))
            elif Meta.BOARD_SQUARES[x + 1].center[0] < square.center[0]:
                barrier_rect = pygame.Rect((square.center[0] - 39, square.center[1] - 39), (5, 79))
            else:
                barrier_rect = pygame.Rect((square.center[0] - 39, square.center[1] - 39), (79, 5))
            pygame.draw.rect(WINDOW, PASTEL_GREEN, barrier_rect)
        if x == 0:  # Start Square
            draw_text("START", TINY_FONT, BLUE, square.center)
        elif x == 99:  # Finish Square
            draw_text("FINISH", TINY_FONT, BLUE, square.center)
        else:
            draw_text(str(x), TINY_FONT, BLUE, (square.center[0] - 30, square.center[1] + 35))
        for i in range(len(square.players)):
            player_image = PLAYER_TO_PIECE[square.players[i].playerNumber]
            WINDOW.blit(player_image, ((square.center[0] + PLAYER_TO_POSITION[i][0]) - 14,
                                       (square.center[1] + PLAYER_TO_POSITION[i][1]) - 14))


def draw_text(text, font, colour, location, center = True):  # Draws text centered on a location
    text_surface = font.render(text, True, colour)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    if center:
        WINDOW.blit(text_surface, (location[0] - (text_width/2), location[1] - (text_height/2)))
    else:
        WINDOW.blit(text_surface, location)


def draw_text_input(location = (960, 400), max_length = 300):  # Creates Text Input Visuals
    text_surface = SMALL_FONT.render(Meta.USER_TEXT, True, ORANGE)
    if text_surface.get_width() >= max_length:
        Meta.CAN_TEXT_INPUT = False
    else:
        Meta.CAN_TEXT_INPUT = True
    input_rect_width = max(text_surface.get_width() + 10, 200)
    input_rect = pygame.Rect(location[0] - (input_rect_width / 2), location[1], input_rect_width, 60)
    pygame.draw.rect(WINDOW, BLUE, input_rect, 5, 5)
    WINDOW.blit(text_surface, ((input_rect.x + (input_rect.width / 2)) - (text_surface.get_width() / 2), (input_rect.y + (input_rect.height / 2)) -
    text_surface.get_height() / 2))


def draw_card(card, location, scale, hover_box = True):
    card_image = pygame.image.load(card.imagePath)
    card_width = CARD_SIZE[0] * scale
    card_height = CARD_SIZE[1] * scale
    card_image = pygame.transform.scale(card_image, (card_width, card_height))
    new_location = (location[0] - (card_width/2), location[1] - (card_height/2))
    if hover_box:
        card_usable = False
        if Meta.SHOW_HAND is not None and check_card_usable(card):
            card_usable = True
            card_rect = card_image.get_rect()
            card_rect.topleft = new_location
            if card_rect.collidepoint(pygame.mouse.get_pos()) and Meta.LEFT_MOUSE_RELEASED:
                perform_card_action(card)
        Meta.HOVER_BOXES.append(("card", card, card_image, new_location, card_usable))
    WINDOW.blit(card_image, new_location)


def draw_dice(dice, location, scale):
    dice_width = dice.valueToImage[dice.sideFacing][1][0] * scale
    dice_height = dice.valueToImage[dice.sideFacing][1][1] * scale
    dice_image = dice.valueToImage[dice.sideFacing][0]
    dice_image = pygame.transform.scale(dice_image, (dice_width, dice_height))
    new_location = (location[0] - (dice_width/2), location[1] - (dice_height/2))
    dice.currentRect = pygame.Rect(new_location, (dice_width, dice_height))
    WINDOW.blit(dice_image, new_location)


def draw_game_image(symbol, location, scale, hover_box = False, colour = WHITE, desc_size = (0, 0), *desc_lines):
    image_width = symbol[1][0] * scale
    image_height = symbol[1][1] * scale
    image = symbol[0]
    image = pygame.transform.scale(image, (image_width, image_height))
    new_location = (location[0] - (image_width/2), location[1] - (image_height/2))
    if hover_box:
        Meta.HOVER_BOXES.append(("board symbol", desc_lines, image, new_location, desc_size, colour))
    WINDOW.blit(image, new_location)


def check_get_card(card_colour):
    mouse_pos = pygame.mouse.get_pos()
    if card_colour == CardType.BLUE:
        if BLUE_DRAW_DECK_RECT.collidepoint(mouse_pos) and Meta.LEFT_MOUSE_RELEASED:
            card = Meta.BLUE_DRAW_DECK.pop()
            Meta.PLAYERS[Meta.CURRENT_PLAYER].blueDeck.append(card)
            if Meta.IS_MULTIPLAYER:
                Meta.NETWORK.send(("PlayerBlueEvents", Meta.PLAYERS[Meta.CURRENT_PLAYER], Meta.BLUE_DRAW_DECK, [Meta.PLAYERS[Meta.CURRENT_PLAYER].playerName +
                                   " drew the " + card.displayName]))
            Meta.DISPLAYING_CARD = True
            return True
    else:
        if RED_DRAW_DECK_RECT.collidepoint(mouse_pos) and Meta.LEFT_MOUSE_RELEASED:
            card = Meta.RED_DRAW_DECK.pop()
            Meta.PLAYERS[Meta.CURRENT_PLAYER].redDeck.append(card)
            if Meta.IS_MULTIPLAYER:
                Meta.NETWORK.send(("PlayerRedEvents", Meta.PLAYERS[Meta.CURRENT_PLAYER], Meta.RED_DRAW_DECK, [Meta.PLAYERS[Meta.CURRENT_PLAYER].playerName +
                                   " drew the " + card.displayName]))
            Meta.DISPLAYING_CARD = True
            return True
    return False


def check_card_usable(card):
    if Meta.PLAYERS[Meta.CURRENT_PLAYER].missNextTurn: return False
    if card.cardType == CardType.BLUE:
        if Meta.FORCED_CARD is not None: return False
        match card.cardValue:
            case CardValue.ACE:  # True if there is a non-Joker and non-Ace Card in the Discard Pile
                for card in Meta.DISCARD_PILE:
                    if card.cardValue != CardValue.JOKER and card.cardValue != CardValue.ACE:
                        return True
            case CardValue.TWO:  # True anytime you need to roll a dice but not when in disadvantage or being controlled
                if (((Meta.TURN_STAGE == TurnStage.ROLL_DICE and Meta.PLAYERS[Meta.CURRENT_PLAYER].setNextRoll is None) or
                     (Meta.TURN_STAGE == TurnStage.MONSTER_ATTACK and Meta.SUCCEEDED_DEFENCE is None) or
                     (Meta.TURN_STAGE == TurnStage.SQUARE_ACTION and Meta.BOARD_SQUARES[Meta.PLAYERS[Meta.CURRENT_PLAYER].currentSquare].symbol == "Back8" and
                     Meta.FORCED_MOVEMENT) or
                     (Meta.TURN_STAGE == TurnStage.ATTACK_MONSTER and D12.enabled)) and
                        (not Meta.ROLLING_WITH_DISADVANTAGE and not Meta.ROLLING_WITH_ADVANTAGE and not Meta.ROLLING_DOUBLE)):
                    return True
            case CardValue.THREE:  # Always True
                return True
            case CardValue.FOUR:  # True anytime you are about to roll for damage
                if Meta.TURN_STAGE == TurnStage.ATTACK_MONSTER and D12.enabled and D12_2.enabled and not Meta.TAKING_FOUR:
                    return True
            case CardValue.FIVE:  # Always True
                return True
            case CardValue.SIX:  # True when about to force movement
                return Meta.FORCED_MOVEMENT
            case CardValue.SEVEN:
                return True
            case CardValue.EIGHT:  # Never True, Uses Automatically
                return False
            case CardValue.NINE:  # True before movement
                if Meta.TURN_STAGE == TurnStage.ROLL_DICE:
                    return True
            case CardValue.TEN:  # Never True (Card Uses Automatically)
                return False
            case CardValue.JACK:  # True anytime you are about to roll for movement but not when in advantage or disadvantage
                if Meta.TURN_STAGE == TurnStage.ROLL_DICE and not Meta.ROLLING_WITH_ADVANTAGE and not Meta.ROLLING_WITH_DISADVANTAGE:
                    return True
            case CardValue.KING:
                return True
            case CardValue.QUEEN:  # True anytime you need to draw Red Cards
                for card_type in Meta.CARDS_TO_DRAW:
                    if card_type == CardType.RED:
                        return True
            case CardValue.JOKER:
                return True
    else:
        match card.cardValue:
            case CardValue.ACE:
                return True
            case CardValue.TWO:
                return Meta.FORCED_CARD == CardValue.TWO
            case CardValue.THREE:
                return Meta.FORCED_CARD == CardValue.THREE
            case CardValue.FOUR:
                return Meta.FORCED_CARD == CardValue.FOUR
            case CardValue.FIVE:
                return Meta.FORCED_CARD == CardValue.FIVE
            case CardValue.SIX:
                return Meta.FORCED_CARD == CardValue.SIX
            case CardValue.SEVEN:
                return True
            case CardValue.EIGHT:
                return Meta.FORCED_CARD == CardValue.EIGHT
            case CardValue.NINE:
                return Meta.FORCED_CARD == CardValue.NINE
            case CardValue.TEN:
                return True
            case CardValue.JACK:
                return Meta.FORCED_CARD == CardValue.JACK
            case CardValue.KING:
                return True
            case CardValue.QUEEN:
                return Meta.FORCED_CARD == CardValue.QUEEN
            case CardValue.JOKER:
                return True
    return False


def perform_card_action(card):
    current_player = Meta.PLAYERS[Meta.CURRENT_PLAYER]
    event_data = [current_player.playerName + " Used the " + card.displayName]
    if card.cardType == CardType.BLUE:
        match card.cardValue:
            case CardValue.ACE:  # Swaps with the last non-Joker and non-Ace card in the Discard Pile
                for x in range(len(Meta.DISCARD_PILE)):
                    if Meta.DISCARD_PILE[len(Meta.DISCARD_PILE) - (x + 1)].cardValue != CardValue.JOKER and Meta.DISCARD_PILE[len(Meta.DISCARD_PILE) - (x + 1)].cardValue != CardValue.ACE:
                        new_card = Meta.DISCARD_PILE.pop()
                        if new_card.cardType == CardType.BLUE:
                            current_player.blueDeck.append(new_card)
                        else:
                            current_player.redDeck.append(new_card)
                        if Meta.IS_MULTIPLAYER:
                            event_data.append([current_player.playerName + " got the " + new_card.displayName])
                        break
            case CardValue.TWO:  # Rolls dice with advantage
                Meta.ROLLING_WITH_ADVANTAGE = True
            case CardValue.THREE:  # Open menu for choosing another player and give all others a Red Card
                if Meta.PLAYER_COUNT > 3: Meta.CHOOSE_PLAYERS = "Blue Three"
                else:
                    player_cards = []
                    for player in Meta.PLAYERS:
                        if player != Meta.PLAYERS[Meta.CURRENT_PLAYER]:
                            new_card = Meta.RED_DRAW_DECK.pop()
                            player.redDeck.append(new_card)
                            player_cards.append((player, new_card))
                    if Meta.IS_MULTIPLAYER:
                        for player_card in player_cards:
                            event_data.append(player_card[0].playerName + " got the " + player_card[1].displayName)
                        Meta.NETWORK.send(("PlayersRed", Meta.PLAYERS, Meta.RED_DRAW_DECK))
            case CardValue.FOUR:
                Meta.ADDING_FOUR = True
                D4.enabled = True
            case CardValue.FIVE:
                Meta.CHOOSE_PLAYERS = "Blue Five"
            case CardValue.SIX:
                Meta.FORCED_MOVEMENT = False
            case CardValue.SEVEN:
                print("Card Used: " + card.displayName)
            case CardValue.EIGHT:
                print("Card Used: " + card.displayName)
            case CardValue.NINE:  # Tells the player to click on a square and place a magic barrier there
                Meta.CHOOSE_SQUARE = "Blue Nine"
            case CardValue.TEN:
                print("Card Used: " + card.displayName)
            case CardValue.JACK:
                Meta.ROLLING_DOUBLE = True
            case CardValue.KING:
                print("Card Used: " + card.displayName)
            case CardValue.QUEEN:  # Removes the need to draw any Red Cards
                while CardType.RED in Meta.CARDS_TO_DRAW:
                    Meta.CARDS_TO_DRAW.remove(CardType.RED)
                print("Card Used: " + card.displayName)
            case CardValue.JOKER:
                print("Card Used: " + card.displayName)
        Meta.CARD_TO_REMOVE = (current_player.blueDeck, card)
    else:
        match card.cardValue:
            case CardValue.ACE:
                print("Card Used: " + card.displayName)
            case CardValue.TWO:
                Meta.FORCED_CARD = None
                Meta.ROLLING_WITH_DISADVANTAGE = True
                print("Card Used: " + card.displayName)
            case CardValue.THREE:
                Meta.FORCED_CARD = None
                if Meta.PLAYER_COUNT > 3: Meta.CHOOSE_PLAYERS = "Red Three"
                else:
                    player_cards = []
                    for player in Meta.PLAYERS:
                        if player != Meta.PLAYERS[Meta.CURRENT_PLAYER]:
                            new_card = Meta.BLUE_DRAW_DECK.pop()
                            player.blueDeck.append(new_card)
                            player_cards.append((player, new_card))
                    if Meta.IS_MULTIPLAYER:
                        for player_card in player_cards:
                            event_data.append(player_card[0].playerName + " got the " + player_card[1].displayName)
                        Meta.NETWORK.send(("PlayersBlue", Meta.PLAYERS, Meta.BLUE_DRAW_DECK))
            case CardValue.FOUR:
                Meta.FORCED_CARD = None
                Meta.TAKING_FOUR = True
                D4.enabled = True
            case CardValue.FIVE:
                Meta.FORCED_CARD = None
                Meta.CHOOSE_PLAYERS = "Red Five"
            case CardValue.SIX:
                Meta.FORCED_CARD = None
                Meta.BONUS_MOVEMENT = False
            case CardValue.SEVEN:
                print("Card Used: " + card.displayName)
            case CardValue.EIGHT:
                Meta.FORCED_CARD = None
                Meta.SUCCEEDED_DEFENCE = False
            case CardValue.NINE:
                Meta.FORCED_CARD = None
                if Meta.IS_MULTIPLAYER:
                    Meta.SQUARE_VOTE = Meta.NETWORK.send("StartSquareVote")
                else:
                    Meta.CHOOSE_SQUARE = "Red Nine"
            case CardValue.TEN:
                print("Card Used: " + card.displayName)
            case CardValue.JACK:
                Meta.FORCED_CARD = None
                Meta.ROLLING_WITH_FOUR = True
                D4.enabled = True
            case CardValue.KING:
                print("Card Used: " + card.displayName)
            case CardValue.QUEEN:
                Meta.FORCED_CARD = None
                while CardType.BLUE in Meta.CARDS_TO_DRAW:
                    Meta.CARDS_TO_DRAW.remove(CardType.BLUE)
            case CardValue.JOKER:
                print("Card Used: " + card.displayName)
        Meta.CARD_TO_REMOVE = (current_player.redDeck, card)
    Meta.DISCARD_PILE.append(card)
    Meta.NETWORK.send(("DiscardEvents", Meta.DISCARD_PILE, event_data))
    Meta.SHOW_HAND = None
    Meta.CARD_HANDS_ACTIVE = True


def check_hover_boxes():
    for hover_box in Meta.HOVER_BOXES:
        if hover_box[0] == "card":
            card_rect = hover_box[2].get_rect()
            card_rect.topleft = hover_box[3]
            mouse_pos = pygame.mouse.get_pos()
            if card_rect.collidepoint(mouse_pos):
                rect_size = hover_box[1].descRectSize
                desc_lines = hover_box[1].descLines
                if Meta.SHOW_HAND is not None:
                    if hover_box[4]:
                        rect_size = (hover_box[1].descRectSize[0], hover_box[1].descRectSize[1] + 35)
                        desc_lines = desc_lines + ("", "Click to Use Card")
                if mouse_pos[0] <= 960:  # Card Desc. Horizontal Positioning
                    rect_left_position = mouse_pos[0] + 5
                else:
                    rect_left_position = mouse_pos[0] - rect_size[0]
                if mouse_pos[1] <= 540:
                    rect_top_position = mouse_pos[1] + 5
                else:
                    rect_top_position = mouse_pos[1] - rect_size[1]
                # Draw Card Name and Description
                card_desc_rect = pygame.Rect((rect_left_position, rect_top_position), rect_size)
                pygame.draw.rect(WINDOW, WHITE, card_desc_rect, 0, 5)
                draw_text(hover_box[1].displayName, TINY_FONT, BLACK, (rect_left_position + 5, rect_top_position + 5), False)
                for x in range(len(desc_lines)):
                    draw_text(desc_lines[x], TINY_FONT, BLACK, (rect_left_position + 5, rect_top_position + (20 * (x + 2))), False)
        elif hover_box[0] == "board symbol":
            card_rect = hover_box[2].get_rect()
            card_rect.topleft = hover_box[3]
            mouse_pos = pygame.mouse.get_pos()
            if card_rect.collidepoint(mouse_pos):
                if mouse_pos[0] <= 960:  # Card Back Desc. Horizontal Positioning
                    rect_left_position = mouse_pos[0] + 5
                else:
                    rect_left_position = mouse_pos[0] - hover_box[4][0]
                if mouse_pos[1] <= 540:
                    rect_top_position = mouse_pos[1] + 5
                else:
                    rect_top_position = mouse_pos[1] - hover_box[4][1]
                card_desc_rect = pygame.Rect((rect_left_position, rect_top_position), hover_box[4])
                pygame.draw.rect(WINDOW, hover_box[5], card_desc_rect, 0, 5)
                for x in range(len(hover_box[1])):
                    draw_text(hover_box[1][x], TINY_FONT, BLACK, (rect_left_position + 5, rect_top_position + ((20 * x) + 5)), False)


def check_squares_clicked():
    for square in Meta.BOARD_SQUARES:
        if square.currentRect.collidepoint(pygame.mouse.get_pos()) and Meta.LEFT_MOUSE_RELEASED:
            return square
    return None


def display_debug_info():
    if DEBUG_MODE:
        for x in range(len(Meta.DEBUG_INFO)):
            draw_text(Meta.DEBUG_INFO[x][0], TINY_FONT, Meta.DEBUG_INFO[x][1], (10, 10 + (20 * x)), False)


def main():  # Game Loop
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        Meta.HOVER_BOXES.clear()
        Meta.DEBUG_INFO.clear()
        if Meta.CURRENT_STATE == ScreenState.PLAYING_GAME:
            Meta.DEBUG_INFO.append((str(Meta.TURN_STAGE), BLACK))
            Meta.DEBUG_INFO.append(("Rolling with Advantage: " + str(Meta.ROLLING_WITH_ADVANTAGE), BLACK))
            Meta.DEBUG_INFO.append(("Rolling with Disadvantage: " + str(Meta.ROLLING_WITH_DISADVANTAGE), BLACK))
            Meta.DEBUG_INFO.append(("Rolling Double: " + str(Meta.ROLLING_DOUBLE), BLACK))
            Meta.DEBUG_INFO.append(("Adding Four: " + str(Meta.ADDING_FOUR), BLACK))
            Meta.DEBUG_INFO.append(("Taking Four: " + str(Meta.TAKING_FOUR), BLACK))
            Meta.DEBUG_INFO.append(("Shield Active: " + str(Meta.SHIELD_ACTIVE), BLACK))
            Meta.DEBUG_INFO.append(("Forced Movement: " + str(Meta.FORCED_MOVEMENT), BLACK))
            Meta.DEBUG_INFO.append(("D4: " + str(D4.enabled), BLACK))
            Meta.DEBUG_INFO.append(("D6 One: " + str(D6.enabled), BLACK))
            Meta.DEBUG_INFO.append(("D6 Two: " + str(D6_2.enabled), BLACK))
            Meta.DEBUG_INFO.append(("D12 One: " + str(D12.enabled), BLACK))
            Meta.DEBUG_INFO.append(("D12 Two: " + str(D12_2.enabled), BLACK))
            Meta.DEBUG_INFO.append(("D20 One: " + str(D20.enabled), BLACK))
            Meta.DEBUG_INFO.append(("D20 Two: " + str(D20_2.enabled), BLACK))
            Meta.DEBUG_INFO.append(("Dice Rolled: " + str(Meta.DICE_ROLLED), BLACK))
            Meta.DEBUG_INFO.append(("Displaying Card: " + str(Meta.DISPLAYING_CARD), BLACK))
            Meta.DEBUG_INFO.append(("Cards to Draw: " + str(len(Meta.CARDS_TO_DRAW)), BLACK))
            Meta.DEBUG_INFO.append(("Discard Pile Size: " + str(len(Meta.DISCARD_PILE)), BLACK))
            for card in Meta.DISCARD_PILE:
                Meta.DEBUG_INFO.append((card.displayName, BLACK))
            Meta.DEBUG_INFO.append(("Player Turn Order:", BLACK))
            for player in Meta.PLAYERS:
                text = player.playerName
                if player.setNextRoll is not None:
                    text += " Next Roll: " + str(player.setNextRoll)
                if player == Meta.PLAYERS[Meta.CURRENT_PLAYER]:
                    text += " -"
                Meta.DEBUG_INFO.append((text, player.playerColour))
                for blue_card in player.blueDeck:
                    Meta.DEBUG_INFO.append((blue_card.displayName, BLACK))
                for red_card in player.redDeck:
                    Meta.DEBUG_INFO.append((red_card.displayName, BLACK))
        # Game Events
        Meta.LEFT_MOUSE_RELEASED = False
        Meta.LEFT_ARROW_DOWN = False
        Meta.RIGHT_ARROW_DOWN = False
        Meta.TEXT_CONFIRMED = False
        for event in pygame.event.get():  # Event Handler
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Meta.LEFT_MOUSE_RELEASED = True
            elif event.type == BUTTON_COOLDOWN_EVENT:
                Meta.BUTTONS_ENABLED = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Meta.LEFT_ARROW_DOWN = True
                elif event.key == pygame.K_RIGHT:
                    Meta.RIGHT_ARROW_DOWN = True
                if event.key in ALLOWED_KEYS:
                    if event.key == pygame.K_BACKSPACE:
                        Meta.USER_TEXT = Meta.USER_TEXT[:-1]
                    elif event.key == pygame.K_RETURN:
                        Meta.TEXT_CONFIRMED = True
                    elif Meta.CAN_TEXT_INPUT:
                        Meta.USER_TEXT += event.unicode
        draw_window()
        display_debug_info()
        pygame.display.update()
        if Meta.CARD_TO_REMOVE is not None:
            Meta.CARD_TO_REMOVE[0].remove(Meta.CARD_TO_REMOVE[1])
            if Meta.IS_MULTIPLAYER:
                Meta.NETWORK.send(("Player", Meta.PLAYERS[Meta.CURRENT_PLAYER]))
            Meta.CARD_TO_REMOVE = None


if __name__ == "__main__":
    main()
