import pygame.draw

from _thread import *

from game import *
from button import Button
from player import Player
from dice import Dice
from server import start_server, check_server, close_server
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
    if Game.CURRENT_STATE == ScreenState.START:  # Start Menu
        WINDOW.fill(GREEN)
        draw_game_image(GAME_TITLE, (960, 90), 1)
        quit_button = Button("Quit", 960, 610, 60)
        if quit_button.check_click():
            pygame.quit()
        new_game_button = Button("Single Device", 960, 470, 60)
        if new_game_button.check_click():
            Game.CURRENT_STATE = ScreenState.NEW_MENU
        local_multiplayer_button = Button("Local Multiplayer", 960, 540, 60)
        if local_multiplayer_button.check_click():
            Game.IS_MULTIPLAYER = True
            Game.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
        rules_button = Button("Game Rules", 1200, 540, 60)
        if rules_button.check_click():
            Game.CURRENT_STATE = ScreenState.GAME_INTRO_ONE
    elif Game.CURRENT_STATE == ScreenState.JOIN_LOCAL_GAME:  # Join/Create a Local Game
        WINDOW.fill(GREEN)
        if Game.HAS_SERVER:
            draw_text("Server Active", SMALL_FONT, ORANGE, (960, 200))
        draw_text("Enter Server IP Address:", SMALL_FONT, ORANGE, (960, 350))
        draw_text_input()
        join_server_button = Button("Join Server", 960, 500, 60)
        if join_server_button.check_click():
            Game.NETWORK = Network(Game.USER_TEXT)
            Game.USER_TEXT = ""
            if Game.NETWORK.success:
                Game.CURRENT_STATE = ScreenState.NAME_LOCAL_PLAYER
        create_server_button = Button("Create Server", 960, 590, 60)
        if create_server_button.check_click():
            Game.CURRENT_STATE = ScreenState.CREATE_SERVER
            Game.CAN_TEXT_INPUT = False
        back_button = Button("Back", 960, 690, 60)
        if back_button.check_click():
            Game.CURRENT_STATE = ScreenState.START
            Game.HAS_SERVER = False
            close_server()
    elif Game.CURRENT_STATE == ScreenState.CREATE_SERVER:  # Sets Player Count for the Server
        WINDOW.fill(GREEN)
        draw_text("How many players?", BIG_FONT, ORANGE, (960, 100))
        back_button = Button("Back", 960, 600, 60)
        if back_button.check_click():
            Game.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
        two_player_button = Button("Two Players", 820, 300, 60, BLUE, ORANGE, SMALL_FONT, 220)
        three_player_button = Button("Three Players", 1100, 300, 60, BLUE, ORANGE, SMALL_FONT, 220)
        four_player_button = Button("Four Players", 820, 400, 60, BLUE, ORANGE, SMALL_FONT, 220)
        five_player_button = Button("Five Players", 1100, 400, 60, BLUE, ORANGE, SMALL_FONT, 220)
        if two_player_button.check_click():
            if check_server(Game.USER_TEXT):
                Game.HAS_SERVER = True
                start_new_thread(start_server, (2, Game.USER_TEXT, Game.BOARD_SQUARES, Game.RED_DRAW_DECK, Game.BLUE_DRAW_DECK))
                Game.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
        elif three_player_button.check_click():
            if check_server(Game.USER_TEXT):
                Game.HAS_SERVER = True
                start_new_thread(start_server, (3, Game.USER_TEXT, Game.BOARD_SQUARES, Game.RED_DRAW_DECK, Game.BLUE_DRAW_DECK))
                Game.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
        elif four_player_button.check_click():
            if check_server(Game.USER_TEXT):
                Game.HAS_SERVER = True
                start_new_thread(start_server, (4, Game.USER_TEXT, Game.BOARD_SQUARES, Game.RED_DRAW_DECK, Game.BLUE_DRAW_DECK))
                Game.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
        elif five_player_button.check_click():
            if check_server(Game.USER_TEXT):
                Game.HAS_SERVER = True
                start_new_thread(start_server, (5, Game.USER_TEXT, Game.BOARD_SQUARES, Game.RED_DRAW_DECK, Game.BLUE_DRAW_DECK))
                Game.CURRENT_STATE = ScreenState.JOIN_LOCAL_GAME
    elif Game.CURRENT_STATE == ScreenState.NAME_LOCAL_PLAYER:  # Names the Player in a Local Game
        WINDOW.fill(GREEN)
        draw_text("Enter your Player Name", MEDIUM_FONT, ORANGE, (960, 69))
        draw_text_input()
        if Game.PLAYER_NUMBER == 69:
            if Game.TEXT_CONFIRMED:
                data = ("Name", Game.USER_TEXT)
                response = Game.NETWORK.send(data)
                Game.PLAYER_NUMBER = response[0]
                Game.PLAYER_COUNT = response[1]
                Game.TEXT_CONFIRMED = False
                Game.CAN_TEXT_INPUT = False
        else:
            network_response = Game.NETWORK.send("?")
            if network_response is not False:
                Game.PLAYERS = network_response[0]
                for x in range(len(Game.PLAYERS)):
                    Game.BOARD_SQUARES[0].players.append(Game.PLAYERS[x])
                Game.RED_DRAW_DECK = network_response[1]
                Game.BLUE_DRAW_DECK = network_response[2]
                Game.CURRENT_STATE = ScreenState.PLAYING_LOCAL_GAME
    elif Game.CURRENT_STATE == ScreenState.NEW_MENU:  # New Game Menu
        WINDOW.fill(GREEN)
        draw_text("How many players?", BIG_FONT, ORANGE, (960, 100))
        back_button = Button("Back", 960, 600, 60)
        if back_button.check_click():
            Game.CURRENT_STATE = ScreenState.START
        two_player_button = Button("Two Players", 820, 300, 60, BLUE, ORANGE, SMALL_FONT, 220)
        three_player_button = Button("Three Players", 1100, 300, 60, BLUE, ORANGE, SMALL_FONT, 220)
        four_player_button = Button("Four Players", 820, 400, 60, BLUE, ORANGE, SMALL_FONT, 220)
        five_player_button = Button("Five Players", 1100, 400, 60, BLUE, ORANGE, SMALL_FONT, 220)
        if two_player_button.check_click():
            Game.PLAYER_COUNT = 2
        elif three_player_button.check_click():
            Game.PLAYER_COUNT = 3
        elif four_player_button.check_click():
            Game.PLAYER_COUNT = 4
        elif five_player_button.check_click():
            Game.PLAYER_COUNT = 5
        if Game.PLAYER_COUNT is not None:
            Game.CAN_TEXT_INPUT = True
            Game.CURRENT_STATE = ScreenState.PLAYER_NAMING
    elif Game.CURRENT_STATE == ScreenState.PLAYER_NAMING:  # Player Naming Menu
        WINDOW.fill(GREEN)
        if Game.CURRENT_PLAYER == Game.PLAYER_COUNT:
            Game.CURRENT_PLAYER = 0
            random.shuffle(Game.PLAYERS)
            Game.CURRENT_STATE = ScreenState.PLAYING_GAME
            for x in range(len(Game.PLAYERS)):
                Game.BOARD_SQUARES[0].players.append(Game.PLAYERS[x])
        else:
            match Game.CURRENT_PLAYER:  # Draw Screen Title
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
            if Game.TEXT_CONFIRMED:
                Game.PLAYERS.append(Player(Game.CURRENT_PLAYER, Game.USER_TEXT))
                Game.USER_TEXT = ""
                Game.CURRENT_PLAYER += 1
                Game.TEXT_CONFIRMED = False
    elif Game.CURRENT_STATE == ScreenState.GAME_INTRO_ONE:
        WINDOW.fill((30, 100, 150))
        draw_text("Welcome to Tyche's Game", BIG_FONT, ORANGE, (960, 69))
        page_background = pygame.Rect((460, 150), (1000, 850))
        pygame.draw.rect(WINDOW, PASTEL_GREEN, page_background, 0, 5)
        back_button = Button("Back", 520, 760, 60, WHITE, BLACK)
        if back_button.check_click():
            Game.CURRENT_STATE = ScreenState.START
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
        if next_button.check_click() or Game.RIGHT_ARROW_DOWN:
            Game.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
    elif Game.CURRENT_STATE == ScreenState.GAME_INTRO_TWO:
        WINDOW.fill((30, 100, 150))
        draw_text("Welcome to Tyche's Game", BIG_FONT, ORANGE, (960, 69))
        page_background = pygame.Rect((460, 150), (1000, 850))
        pygame.draw.rect(WINDOW, PASTEL_GREEN, page_background, 0, 5)
        back_button = Button("Back", 1400, 760, 60, WHITE, BLACK)
        if back_button.check_click():
            Game.CURRENT_STATE = ScreenState.START
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
        if back_button.check_click() or Game.LEFT_ARROW_DOWN:
            Game.CURRENT_STATE = ScreenState.GAME_INTRO_ONE
        elif blue_guide_button.check_click():
            Game.CURRENT_STATE = ScreenState.BLUE_CARD_GUIDE
        elif red_guide_button.check_click():
            Game.CURRENT_STATE = ScreenState.RED_CARD_GUIDE
        elif board_guide_button.check_click():
            Game.CURRENT_STATE = ScreenState.BOARD_SYMBOLS_GUIDE_ONE
    elif Game.CURRENT_STATE == ScreenState.BLUE_CARD_GUIDE:
        WINDOW.fill(PASTEL_GREEN)
        draw_text("Blue Card Guide", MEDIUM_FONT, ORANGE, (960, 69))
        back_button = Button("Back", 960, 950, 60)
        if back_button.check_click():
            Game.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
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
    elif Game.CURRENT_STATE == ScreenState.RED_CARD_GUIDE:
        WINDOW.fill(PASTEL_GREEN)
        draw_text("Red Card Guide", MEDIUM_FONT, ORANGE, (960, 69))
        back_button = Button("Back", 960, 950, 60)
        if back_button.check_click():
            Game.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
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
    elif Game.CURRENT_STATE == ScreenState.BOARD_SYMBOLS_GUIDE_ONE:
        WINDOW.fill(PASTEL_GREEN)
        draw_text("Board Symbols Guide", MEDIUM_FONT, ORANGE, (960, 69))
        back_button = Button("Back", 960, 950, 60)
        if back_button.check_click():
            Game.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
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
        next_button = Button(">", 1750, 540, 60, BLUE, ORANGE, MEDIUM_FONT)
        if next_button.check_click() or Game.RIGHT_ARROW_DOWN:
            Game.CURRENT_STATE = ScreenState.BOARD_SYMBOLS_GUIDE_TWO
        check_hover_boxes()
    elif Game.CURRENT_STATE == ScreenState.BOARD_SYMBOLS_GUIDE_TWO:
        WINDOW.fill(PASTEL_GREEN)
        draw_text("Board Symbols Guide", MEDIUM_FONT, ORANGE, (960, 69))
        back_button = Button("Back", 960, 950, 60)
        if back_button.check_click():
            Game.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
        draw_game_image((NICE_HAND, (89, 89)), (320, 270), 2, True, WHITE, (330, 100),
                        "Nice Hand", "", "Exchange Red and Blue Cards", "with another Player")
        draw_game_image((GRAVITY_WELL, (89, 89)), (640, 270), 2, True, WHITE, (330, 100),
                        "Gravity Well", "", "Attempts to pull", "Players towards you")
        previous_button = Button("<", 300, 540, 60, BLUE, ORANGE, MEDIUM_FONT)
        if previous_button.check_click() or Game.LEFT_ARROW_DOWN:
            Game.CURRENT_STATE = ScreenState.BOARD_SYMBOLS_GUIDE_ONE
        check_hover_boxes()
    elif Game.CURRENT_STATE == ScreenState.PLAYING_LOCAL_GAME:
        WINDOW.fill(WHITE)
        Game.BUTTONS_ENABLED = True
        if Game.SHOW_HAND is None and Game.CHOOSE_DICE is None and Game.CHOOSE_PLAYERS is None and Game.CHOOSE_SQUARE is None and not Game.SQUARE_VOTE:
            quit_button = Button("Quit", 360, 450, 60)
            if quit_button.check_click():
                Game.NETWORK.send("quit")
                pygame.quit()
        check_server_updates()
        current_player = Game.PLAYERS[Game.CURRENT_PLAYER]
        is_your_turn = Game.CURRENT_PLAYER == Game.PLAYER_NUMBER
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
            for event in range(len(Game.EVENT_LIST)):
                draw_text(Game.EVENT_LIST[event][0], TINY_FONT, Game.EVENT_LIST[event][1], (10, 10 + (20 * event)), False)
        else:
            draw_game_image(BLUE_CARD_SYMBOL, (360, 250), 3, True, PASTEL_GREEN, (170, 75),
                            "Blue Draw Pile", "", "Current Size: " + str(len(Game.BLUE_DRAW_DECK)))
            draw_game_image(RED_CARD_SYMBOL, (360, 650), 3, True, PASTEL_GREEN, (170, 75),
                            "Red Draw Pile", "", "Current Size: " + str(len(Game.RED_DRAW_DECK)))
        if is_your_turn:
            if len(current_player.blueDeck) != 0:
                turned_blue_deck_image = pygame.transform.rotate(BLUE_CARD_SYMBOL[0], -90)
                turned_blue_deck_image = pygame.transform.scale(turned_blue_deck_image, (
                BLUE_CARD_SYMBOL[1][1] * 3, BLUE_CARD_SYMBOL[1][0] * 3))
                WINDOW.blit(turned_blue_deck_image, (95, 835))
                if Game.CARD_HANDS_ACTIVE: Game.HOVER_BOXES.append(("board symbol", ["Your Blue Card Hand"],
                                                                    turned_blue_deck_image, (95, 835), (215, 35),
                                                                    PASTEL_GREEN))
                blue_hand_rect = turned_blue_deck_image.get_rect()
                blue_hand_rect.topleft = (95, 835)
                if blue_hand_rect.collidepoint(
                        pygame.mouse.get_pos()) and Game.LEFT_MOUSE_RELEASED and Game.CARD_HANDS_ACTIVE:
                    Game.SHOW_HAND = CardType.BLUE
                    Game.CARD_HANDS_ACTIVE = False
                    if Game.TURN_STAGE == TurnStage.DRAW_CARDS:
                        if Game.DISPLAYING_CARD:
                            Game.CARDS_TO_DRAW.pop(0)
                            Game.DISPLAYING_CARD = False
            if len(current_player.redDeck) != 0:
                turned_red_deck_image = pygame.transform.rotate(RED_CARD_SYMBOL[0], 90)
                turned_red_deck_image = pygame.transform.scale(turned_red_deck_image,
                                                               (RED_CARD_SYMBOL[1][1] * 3, RED_CARD_SYMBOL[1][0] * 3))
                WINDOW.blit(turned_red_deck_image, (1530, 835))
                if Game.CARD_HANDS_ACTIVE: Game.HOVER_BOXES.append(("board symbol", ["Your Red Card Hand"],
                                                                    turned_red_deck_image, (1530, 835), (215, 35),
                                                                    PASTEL_GREEN))
                red_hand_rect = turned_red_deck_image.get_rect()
                red_hand_rect.topleft = (1530, 835)
                if red_hand_rect.collidepoint(
                        pygame.mouse.get_pos()) and Game.LEFT_MOUSE_RELEASED and Game.CARD_HANDS_ACTIVE:
                    Game.SHOW_HAND = CardType.RED
                    Game.CARD_HANDS_ACTIVE = False
                    if Game.TURN_STAGE == TurnStage.DRAW_CARDS:
                        if Game.DISPLAYING_CARD:
                            Game.CARDS_TO_DRAW.pop(0)
                            Game.DISPLAYING_CARD = False
        draw_squares()
        if Game.CHOOSE_SQUARE == "Red Nine":
            is_your_turn = True
        if is_your_turn:
            if Game.SQUARE_VOTE:
                Game.HOVER_BOXES.clear()
                WINDOW.fill(PASTEL_GREEN)
                draw_text("Waiting for the Square Vote to Conclude", MEDIUM_FONT, ORANGE, (960, 69))
                Game.BUTTONS_ENABLED = False
            elif Game.SHOW_HAND == CardType.BLUE:
                Game.HOVER_BOXES.clear()
                WINDOW.fill(PASTEL_GREEN)
                draw_text(current_player.playerName + "'s Blue Card Hand", MEDIUM_FONT, ORANGE, (960, 69))
                back_button = Button("Back", 960, 950, 60)
                if back_button.check_click():
                    Game.SHOW_HAND = None
                    Game.CARD_HANDS_ACTIVE = True
                for x in range(len(current_player.blueDeck)):
                    draw_card(current_player.blueDeck[x], CARD_TO_POSITION[x], 2)
                Game.BUTTONS_ENABLED = False
                check_hover_boxes()
            elif Game.SHOW_HAND == CardType.RED:
                Game.HOVER_BOXES.clear()
                WINDOW.fill(PASTEL_GREEN)
                draw_text(current_player.playerName + "'s Red Card Hand", MEDIUM_FONT, ORANGE, (960, 69))
                back_button = Button("Back", 960, 950, 60)
                if back_button.check_click():
                    Game.SHOW_HAND = None
                    Game.CARD_HANDS_ACTIVE = True
                for x in range(len(current_player.redDeck)):
                    draw_card(current_player.redDeck[x], CARD_TO_POSITION[x], 2)
                Game.BUTTONS_ENABLED = False
                check_hover_boxes()
            elif Game.CHOOSE_PLAYERS is not None:
                Game.HOVER_BOXES.clear()
                WINDOW.fill(PASTEL_GREEN)
                draw_text("Choose a Player:", MEDIUM_FONT, ORANGE, (960, 69))
                player = None
                for x in range(len(Game.PLAYERS)):
                    if Game.PLAYERS[x] != current_player:
                        if Game.CHOOSE_PLAYERS == "Red Five":
                            if Game.PLAYERS[x].setPlayerRoll is None:
                                button = Button(Game.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                                if button.check_click():
                                    player = Game.PLAYERS[x]
                        elif Game.CHOOSE_PLAYERS == "Blue Five":
                            if Game.PLAYERS[x].setNextRoll is None:
                                button = Button(Game.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                                if button.check_click():
                                    player = Game.PLAYERS[x]
                        else:
                            button = Button(Game.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                            if button.check_click():
                                player = Game.PLAYERS[x]
                if player is not None:
                    if Game.CHOOSE_PLAYERS == "Blue Three":
                        event_data = []
                        for x in range(len(Game.PLAYERS)):
                            if Game.PLAYERS[x] != player and Game.PLAYERS[x] != current_player:
                                red_card = Game.RED_DRAW_DECK.pop()
                                Game.PLAYERS[x].redDeck.append(red_card)
                                event_data.append((Game.PLAYERS[x].playerName + " drew the " + red_card.displayName, Game.PLAYERS[x].playerColour))
                        Game.NETWORK.send(("PlayersRedEvents", Game.PLAYERS, Game.RED_DRAW_DECK, event_data))
                        Game.CHOOSE_PLAYERS = None
                    elif Game.CHOOSE_PLAYERS == "Red Three":
                        event_data = []
                        for x in range(len(Game.PLAYERS)):
                            if Game.PLAYERS[x] != player and Game.PLAYERS[x] != current_player:
                                blue_card = Game.BLUE_DRAW_DECK.pop()
                                Game.PLAYERS[x].blueDeck.append(blue_card)
                                event_data.append((Game.PLAYERS[x].playerName + " drew the " + blue_card.displayName, Game.PLAYERS[x].playerColour))
                        Game.NETWORK.send(("PlayersBlueEvents", Game.PLAYERS, Game.BLUE_DRAW_DECK, event_data))
                        Game.CHOOSE_PLAYERS = None
                    elif Game.CHOOSE_PLAYERS == "Blue Five":
                        Game.CHOOSE_PLAYERS = None
                        Game.CHOOSE_DICE = player
                    elif Game.CHOOSE_PLAYERS == "Red Five":
                        Game.CHOOSE_PLAYERS = None
                        player.setPlayerRoll = current_player
                        Game.NETWORK.send(("PlayerEvents", player, [(player.playerName + " will set a dice roll for " + current_player.playerName, player.playerColour)]))
                    elif Game.CHOOSE_PLAYERS == "NiceHand":
                        event_data = []
                        for card in current_player.redDeck:  # Give the Other Player the Red Cards
                            event_data.append((
                                              current_player.playerName + " gave " + player.playerName + " the " + card.displayName,
                                              current_player.playerColour))
                            player.redDeck.append(card)
                        for card in player.blueDeck:  # Give the Current Player the Blue Cards
                            event_data.append((
                                              player.playerName + " gave " + current_player.playerName + " the " + card.displayName,
                                              player.playerColour))
                            current_player.blueDeck.append(card)
                        current_player.redDeck.clear()
                        player.blueDeck.clear()
                        Game.NETWORK.send(("PlayersEvents", Game.PLAYERS, event_data))
                        Game.TURN_STAGE = TurnStage.END_TURN
                        Game.CHOOSE_PLAYERS = None
                Game.BUTTONS_ENABLED = False
            elif Game.CHOOSE_DICE is not None:
                Game.HOVER_BOXES.clear()
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
                    Game.CHOOSE_DICE.setNextRoll = 1
                    Game.NETWORK.send(("PlayerEvents", Game.CHOOSE_DICE, [(current_player.playerName + " set " + Game.CHOOSE_DICE.playerName + " to Roll a One", current_player.playerColour)]))
                    Game.CHOOSE_DICE = None
                if two_d6.check_click(False):
                    Game.CHOOSE_DICE.setNextRoll = 2
                    Game.NETWORK.send(("PlayerEvents", Game.CHOOSE_DICE, [(current_player.playerName + " set " + Game.CHOOSE_DICE.playerName + " to Roll a Two", current_player.playerColour)]))
                    Game.CHOOSE_DICE = None
                if three_d6.check_click(False):
                    Game.CHOOSE_DICE.setNextRoll = 3
                    Game.NETWORK.send(("PlayerEvents", Game.CHOOSE_DICE, [(current_player.playerName + " set " + Game.CHOOSE_DICE.playerName + " to Roll a Three", current_player.playerColour)]))
                    Game.CHOOSE_DICE = None
                if four_d6.check_click(False):
                    Game.CHOOSE_DICE.setNextRoll = 4
                    Game.NETWORK.send(("PlayerEvents", Game.CHOOSE_DICE, [(current_player.playerName + " set " + Game.CHOOSE_DICE.playerName + " to Roll a Four", current_player.playerColour)]))
                    Game.CHOOSE_DICE = None
                if five_d6.check_click(False):
                    Game.CHOOSE_DICE.setNextRoll = 5
                    Game.NETWORK.send(("PlayerEvents", Game.CHOOSE_DICE, [(current_player.playerName + " set " + Game.CHOOSE_DICE.playerName + " to Roll a Five", current_player.playerColour)]))
                    Game.CHOOSE_DICE = None
                if six_d6.check_click(False):
                    Game.CHOOSE_DICE.setNextRoll = 6
                    Game.NETWORK.send(("PlayerEvents", Game.CHOOSE_DICE, [(current_player.playerName + " set " + Game.CHOOSE_DICE.playerName + " to Roll a Six", current_player.playerColour)]))
                    Game.CHOOSE_DICE = None
                Game.BUTTONS_ENABLED = False
            elif Game.CHOOSE_SQUARE is not None:
                Game.HOVER_BOXES.clear()
                WINDOW.fill(PASTEL_GREEN)
                draw_text("Choose a Square:", MEDIUM_FONT, ORANGE, (960, 30))
                draw_squares()
                square_clicked = check_squares_clicked()
                if square_clicked is not None and Game.BOARD_SQUARES.index(square_clicked) != 99 and Game.BOARD_SQUARES.index(square_clicked) != 0:
                    if Game.CHOOSE_SQUARE == "Blue Nine":
                        if not square_clicked.hasBarrier:
                            square_clicked.hasBarrier = True
                            Game.NETWORK.send(("SquareEvents", (Game.BOARD_SQUARES.index(square_clicked), square_clicked), [(current_player.playerName +
                                               " placed a Magic Barrier", current_player.playerColour)]))
                            Game.CHOOSE_SQUARE = None
                    else:
                        if not square_clicked.hasBarrier:
                            Game.NETWORK.send(("SquareVote", Game.BOARD_SQUARES.index(square_clicked), [(Game.PLAYERS[Game.PLAYER_NUMBER].playerName +
                                               " voted for Square " + str(Game.BOARD_SQUARES.index(square_clicked)), Game.PLAYERS[Game.PLAYER_NUMBER].playerColour)]))
                            Game.CHOOSE_SQUARE = None
                Game.BUTTONS_ENABLED = False
            elif Game.TURN_STAGE == TurnStage.START_TURN:
                if current_player.missNextTurn:
                    draw_text("You don't get to take this turn", SMALL_FONT, BLACK, (1680, 240))
                    continue_button = Button("Continue", 1680, 600, 60)
                    if continue_button.check_click():
                        current_player.missNextTurn = False
                        Game.NETWORK.send(("PlayerEvents", current_player, [(current_player.playerName + " Missed their Last Turn", current_player.playerColour)]))
                        end_turn()
                else:
                    if current_player.setPlayerRoll is not None:
                        draw_text("Set " + current_player.setPlayerRoll.playerName + "'s", SMALL_FONT, BLACK,
                                  (1680, 230))
                        draw_text("Next Dice Roll", SMALL_FONT, BLACK, (1680, 260))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            Game.CHOOSE_DICE = current_player.setPlayerRoll
                            current_player.setPlayerRoll = None
                            Game.NETWORK.send(("Player", current_player))
                    else:
                        if Game.FORCED_CARD is None:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.THREE:
                                    Game.FORCED_CARD = CardValue.THREE
                                    break
                                if card.cardValue == CardValue.FIVE:
                                    can_force = False
                                    for player in Game.PLAYERS:
                                        if player.playerNumber != Game.PLAYER_NUMBER and player.setPlayerRoll is None:
                                            can_force = True
                                            break
                                    if can_force:
                                        Game.FORCED_CARD = CardValue.FIVE
                                    break
                                if card.cardValue == CardValue.NINE:
                                    Game.FORCED_CARD = CardValue.NINE
                                    break
                        if Game.FORCED_CARD == CardValue.THREE:
                            draw_text("Use your Red Three Card!", SMALL_FONT, BLACK, (1680, 240))
                        elif Game.FORCED_CARD == CardValue.FIVE:
                            draw_text("Use your Red Five Card!", SMALL_FONT, BLACK, (1680, 240))
                        elif Game.FORCED_CARD == CardValue.NINE:
                            draw_text("Use your Red Nine Card!", SMALL_FONT, BLACK, (1680, 240))
                        elif Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth > 0:
                            D20.enabled = True
                            D20_2.enabled = True
                            D20_3.enabled = True
                            Game.SUCCEEDED_DEFENCE = None
                            Game.TURN_STAGE = TurnStage.MONSTER_ATTACK
                        else:  # Roll Dice
                            Game.TOP_DICE = [D6]
                            Game.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            draw_dice_sets()
                            D6.enabled = True
                            D6_2.enabled = True
                            Game.TURN_STAGE = TurnStage.ROLL_DICE
            elif Game.TURN_STAGE == TurnStage.MONSTER_ATTACK:  # Monster Attacks
                if Game.SUCCEEDED_DEFENCE is None: draw_text("Defend against the Monster!", SMALL_FONT, BLACK, (1680, 240))
                if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                    for card in current_player.redDeck:
                        if card.cardValue == CardValue.TWO:
                            Game.FORCED_CARD = CardValue.TWO
                if Game.FORCED_CARD is None and Game.SUCCEEDED_DEFENCE:
                    for card in current_player.redDeck:
                        if card.cardValue == CardValue.EIGHT:
                            Game.FORCED_CARD = CardValue.EIGHT
                if Game.FORCED_CARD == CardValue.TWO:
                    draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                elif Game.FORCED_CARD == CardValue.EIGHT:
                    draw_text("Use your Red Eight Card!", SMALL_FONT, BLACK, (1680, 240))
                else:
                    if D20_3.enabled:
                        D20_3.sideFacing = random.randrange(1, 21)
                        D20_3.enabled = False
                    draw_dice(D20_3, (1680, 330), 2)
                    if Game.ROLLING_WITH_ADVANTAGE:
                        Game.TOP_DICE = [D20, D20_2]
                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                        Game.BOTTOM_DICE = [D10, D10_2, D12, D12_2, D4]
                        D20.check_click()
                        D20_2.check_click()
                        if not D20.enabled and not D20_2.enabled and Game.SUCCEEDED_DEFENCE is None:
                            Game.SUCCEEDED_DEFENCE = max(D20.sideFacing, D20_2.sideFacing) >= D20_3.sideFacing
                            if not Game.SUCCEEDED_DEFENCE:
                                for card in current_player.blueDeck:
                                    if card.cardValue == CardValue.EIGHT:
                                        Game.CARD_TO_REMOVE = (current_player.blueDeck, card, True)
                                        Game.DISCARD_PILE.append(card)
                                        Game.NETWORK.send(("DiscardEvents", Game.DISCARD_PILE, [(current_player.playerName + " used the " + card.displayName, current_player.playerColour)]))
                                        Game.SHIELD_ACTIVE = True
                                        break
                    elif Game.ROLLING_WITH_DISADVANTAGE:
                        Game.TOP_DICE = [D20, D20_2]
                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                        Game.BOTTOM_DICE = [D10, D10_2, D12, D12_2, D4]
                        D20.check_click()
                        D20_2.check_click()
                        if not D20.enabled and not D20_2.enabled and Game.SUCCEEDED_DEFENCE is None:
                            Game.SUCCEEDED_DEFENCE = min(D20.sideFacing, D20_2.sideFacing) >= D20_3.sideFacing
                            if not Game.SUCCEEDED_DEFENCE:
                                for card in current_player.blueDeck:
                                    if card.cardValue == CardValue.EIGHT:
                                        Game.CARD_TO_REMOVE = (current_player.blueDeck, card, True)
                                        Game.DISCARD_PILE.append(card)
                                        Game.NETWORK.send(("DiscardEvents", Game.DISCARD_PILE, [(current_player.playerName + " used the " + card.displayName, current_player.playerColour)]))
                                        Game.SHIELD_ACTIVE = True
                                        break
                    else:
                        Game.TOP_DICE = [D20]
                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                        Game.BOTTOM_DICE = [D10_2, D12, D12_2, D20_2, D4]
                        if D20.check_click():
                            Game.SUCCEEDED_DEFENCE = D20.sideFacing >= D20_3.sideFacing
                            if not Game.SUCCEEDED_DEFENCE:
                                for card in current_player.blueDeck:
                                    if card.cardValue == CardValue.EIGHT:
                                        Game.CARD_TO_REMOVE = (current_player.blueDeck, card, True)
                                        Game.DISCARD_PILE.append(card)
                                        Game.NETWORK.send(("DiscardEvents", Game.DISCARD_PILE, [(current_player.playerName + " used the " + card.displayName, current_player.playerColour)]))
                                        Game.SHIELD_ACTIVE = True
                                        break
                    draw_dice_sets(500)
                    if Game.SUCCEEDED_DEFENCE is not None:
                        if not Game.SUCCEEDED_DEFENCE:  # Player Loses
                            if Game.SHIELD_ACTIVE:
                                draw_text("Your Shield saved you", SMALL_FONT, BLACK, (1680, 230))
                                draw_text("You survived the encounter", SMALL_FONT, BLACK, (1680, 260))
                                continue_button = Button("Continue", 1680, 600, 60)
                                if continue_button.check_click():
                                    Game.ROLLING_WITH_ADVANTAGE = False
                                    Game.ROLLING_WITH_DISADVANTAGE = False
                                    Game.TOP_DICE = [D12]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                    Game.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                    Game.TURN_STAGE = TurnStage.ATTACK_MONSTER
                                    D12.enabled = True
                                    D12_2.enabled = True
                                    Game.SHIELD_ACTIVE = False
                            else:
                                draw_text("You Failed your Defence Roll", SMALL_FONT, BLACK, (1680, 200))
                                draw_text("The Monster will knock you", SMALL_FONT, BLACK, (1680, 230))
                                draw_text("back 4 spaces", SMALL_FONT, BLACK, (1680, 260))
                                continue_button = Button("Continue", 1680, 600, 60)
                                if continue_button.check_click():
                                    Game.ROLLING_WITH_ADVANTAGE = False
                                    Game.ROLLING_WITH_DISADVANTAGE = False
                                    updated_squares = []
                                    player_to_remove = None
                                    print("Debug: Current Player: " + current_player.playerName)
                                    for player in Game.BOARD_SQUARES[current_player.currentSquare].players:
                                        print("Debug: Player in Square " + str(current_player.currentSquare) + ": " + player.playerName)
                                        if player.playerNumber == current_player.playerNumber:
                                            player_to_remove = player
                                    if player_to_remove is None:
                                        print("No Player to Remove")
                                    else:
                                        print("Player to Remove: " + player_to_remove.playerName)
                                    Game.BOARD_SQUARES[current_player.currentSquare].players.remove(player_to_remove)
                                    updated_squares.append((current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]))
                                    current_player.currentSquare -= 4
                                    Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    updated_squares.append((current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]))
                                    Game.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [(current_player.playerName + " Failed their Defence", current_player.playerColour)]))
                                    Game.TURN_STAGE = TurnStage.START_TURN
                        else:
                            draw_text("You defended yourself", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Game.ROLLING_WITH_ADVANTAGE = False
                                Game.ROLLING_WITH_DISADVANTAGE = False
                                Game.TOP_DICE = [D12]
                                Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                Game.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                Game.TURN_STAGE = TurnStage.ATTACK_MONSTER
                                D12.enabled = True
                                D12_2.enabled = True
            elif Game.TURN_STAGE == TurnStage.ATTACK_MONSTER:  # Attacking a Monster
                if Game.FORCED_CARD is None and not Game.TAKING_FOUR and not Game.TAKEN_FOUR:
                    for card in current_player.redDeck:
                        if card.cardValue == CardValue.FOUR:
                            Game.FORCED_CARD = CardValue.FOUR
                if Game.FORCED_CARD == CardValue.FOUR:
                    draw_text("Use your Red Four!", SMALL_FONT, BLACK, (1680, 240))
                else:
                    if Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth <= 0:
                        draw_text("Congratulations!", SMALL_FONT, BLACK, (1680, 200))
                        draw_text("You have killed the Monster!", SMALL_FONT, BLACK, (1680, 230))
                        draw_text("You can roll movement now", SMALL_FONT, BLACK, (1680, 260))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            Game.TURN_STAGE = TurnStage.START_TURN
                            Game.ADDING_FOUR = False
                            Game.TAKING_FOUR = False
                            Game.TAKEN_FOUR = False
                            Game.ROLLING_WITH_ADVANTAGE = False
                            Game.BOARD_SQUARES[current_player.currentSquare].monsterAwake = False
                            Game.NETWORK.send(("SquareEvents", (current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]), [(current_player.playerName + " killed the Monster", current_player.playerColour)]))
                    elif not D12.enabled and not D12_2.enabled:
                        if Game.ADDING_FOUR:
                            draw_text("Add a d4 to the Attack:", SMALL_FONT, BLACK, (1680, 240))
                            Game.TOP_DICE = [D4]
                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                            Game.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                            draw_dice_sets()
                            if D4.check_click():
                                Game.ADDING_FOUR = False
                                Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= D4.sideFacing
                                Game.NETWORK.send(("SquareEvents", (current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]),
                                                   [(current_player.playerName + " hit the Monster for " + str(D4.sideFacing), current_player.playerColour)]))
                        elif Game.TAKING_FOUR and not Game.TAKEN_FOUR:
                            draw_text("Take a d4 from the Attack:", SMALL_FONT, BLACK, (1680, 240))
                            Game.TOP_DICE = [D4]
                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                            Game.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                            draw_dice_sets()
                            if D4.check_click():
                                Game.TAKEN_FOUR = True
                                Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth += D4.sideFacing
                                Game.NETWORK.send(("SquareEvents", (current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]),
                                                   [(current_player.playerName + " healed the Monster for " + str(D4.sideFacing), current_player.playerColour)]))
                        else:
                            draw_text("You did not kill the Monster", SMALL_FONT, BLACK, (1680, 240))
                            end_turn_button = Button("End Turn", 1680, 600, 60)
                            if end_turn_button.check_click():
                                end_turn()
                                Game.TAKEN_FOUR = False
                                Game.TAKING_FOUR = False
                                Game.ROLLING_WITH_ADVANTAGE = False
                    else:
                        draw_text("Attack the Monster:", SMALL_FONT, BLACK, (1680, 240))
                        if Game.ROLLING_WITH_ADVANTAGE:
                            Game.TOP_DICE = [D12, D12_2]
                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                            Game.BOTTOM_DICE = [D10, D10_2, D20, D20_2, D4]
                        if not Game.ROLLING_WITH_ADVANTAGE:
                            if D12.check_click():
                                D12_2.enabled = False
                                Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= D12.sideFacing
                                Game.NETWORK.send(("SquareEvents", (current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]),
                                                   [(current_player.playerName + " hit the Monster for " + str(D12.sideFacing), current_player.playerColour)]))
                        else:
                            D12.check_click()
                            D12_2.check_click()
                            if not D12.enabled and not D12_2.enabled:
                                Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= max(D12.sideFacing, D12_2.sideFacing)
                                Game.NETWORK.send(("SquareEvents", (current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]),
                                                   [(current_player.playerName + " hit the Monster for " + str(max(D12.sideFacing, D12_2.sideFacing)), current_player.playerColour)]))
                    draw_dice_sets()
            elif Game.TURN_STAGE == TurnStage.ROLL_DICE:  # Rolling the Movement Dice
                if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                    for card in current_player.redDeck:
                        if card.cardValue == CardValue.TWO:
                            Game.FORCED_CARD = CardValue.TWO
                if Game.FORCED_CARD is None and not Game.ROLLING_WITH_FOUR:
                    for card in current_player.redDeck:
                        if card.cardValue == CardValue.JACK:
                            Game.FORCED_CARD = CardValue.JACK
                if Game.FORCED_CARD == CardValue.TWO:
                    draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                elif Game.FORCED_CARD == CardValue.JACK:
                    draw_text("Use your Red Jack Card!", SMALL_FONT, BLACK, (1680, 240))
                else:
                    if Game.ROLLING_WITH_FOUR:
                        Game.TOP_DICE = [D4]
                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                        Game.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                        draw_text("Roll d4 to move:", SMALL_FONT, BLACK, (1680, 240))
                        draw_dice_sets()
                        if D4.check_click():
                            Game.ROLLING_WITH_FOUR = False
                            Game.SQUARES_TO_MOVE = D4.sideFacing
                            Game.TURN_STAGE = TurnStage.MOVEMENT
                    elif Game.ROLLING_WITH_ADVANTAGE and Game.DICE_ROLLED == 2:
                        draw_text("Pick a dice to use:", SMALL_FONT, BLACK, (1680, 240))
                        draw_dice_sets()
                        if D6.check_click(False):
                            Game.ROLLING_WITH_ADVANTAGE = False
                            Game.DICE_ROLLED = 0
                            Game.SQUARES_TO_MOVE = D6.sideFacing
                            Game.TURN_STAGE = TurnStage.MOVEMENT
                            Game.TOP_DICE = [D6]
                            Game.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                        if D6_2.check_click(False):
                            Game.ROLLING_WITH_ADVANTAGE = False
                            Game.DICE_ROLLED = 0
                            Game.SQUARES_TO_MOVE = D6_2.sideFacing
                            Game.TURN_STAGE = TurnStage.MOVEMENT
                            Game.TOP_DICE = [D6_2]
                            Game.MIDDLE_DICE = [D6, D8, D8_2, D10, D10_2]
                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                    else:
                        draw_text("Roll d6 to move:", SMALL_FONT, BLACK, (1680, 240))
                        if not Game.ROLLING_WITH_ADVANTAGE and not Game.ROLLING_DOUBLE and not Game.ROLLING_WITH_DISADVANTAGE:
                            draw_dice_sets()
                            if D6.check_click():
                                Game.TURN_STAGE = TurnStage.MOVEMENT
                                Game.SQUARES_TO_MOVE = D6.sideFacing
                        elif Game.ROLLING_WITH_ADVANTAGE:
                            Game.TOP_DICE = [D6, D6_2]
                            Game.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            draw_dice_sets()
                            if D6.check_click():
                                Game.DICE_ROLLED += 1
                            if D6_2.check_click():
                                Game.DICE_ROLLED += 1
                            if Game.DICE_ROLLED == 2:
                                D6.enabled = True
                                D6_2.enabled = True
                        elif Game.ROLLING_WITH_DISADVANTAGE:
                            Game.TOP_DICE = [D6, D6_2]
                            Game.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            draw_dice_sets()
                            D6.check_click()
                            D6_2.check_click()
                            if not D6.enabled and not D6_2.enabled:
                                Game.SQUARES_TO_MOVE = min(D6.sideFacing, D6_2.sideFacing)
                                if D6.sideFacing > D6_2.sideFacing:
                                    Game.TOP_DICE = [D6_2]
                                    Game.MIDDLE_DICE = [D6, D8, D8_2, D10, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                else:
                                    Game.TOP_DICE = [D6]
                                    Game.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                Game.TURN_STAGE = TurnStage.MOVEMENT
                                Game.ROLLING_WITH_DISADVANTAGE = False
                        elif Game.ROLLING_DOUBLE:
                            Game.TOP_DICE = [D6, D6_2]
                            Game.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            draw_dice_sets()
                            D6.check_click()
                            D6_2.check_click()
                            if not D6.enabled and not D6_2.enabled:
                                Game.SQUARES_TO_MOVE = D6.sideFacing + D6_2.sideFacing
                                Game.TURN_STAGE = TurnStage.MOVEMENT
                                Game.ROLLING_DOUBLE = False
            elif Game.TURN_STAGE == TurnStage.MOVEMENT:  # Moving the Current Player
                draw_dice_sets()
                for x in range(Game.SQUARES_TO_MOVE):
                    if Game.BOARD_SQUARES[current_player.currentSquare + x].hasBarrier and x != 0:
                        has_ten = False
                        for card in current_player.blueDeck:
                            if card.cardValue == CardValue.TEN:
                                Game.CARD_TO_REMOVE = (current_player.blueDeck, card, True)
                                Game.DISCARD_PILE.append(card)
                                Game.NETWORK.send(("DiscardEvents", Game.DISCARD_PILE, [(current_player.playerName + " used the " + card.displayName, current_player.playerColour)]))
                                has_ten = True
                                break
                        if not has_ten:
                            Game.SQUARES_TO_MOVE = x
                            Game.BOARD_SQUARES[current_player.currentSquare + x].hasBarrier = False
                            break
                    elif Game.BOARD_SQUARES[current_player.currentSquare + x].monsterAwake:
                        Game.SQUARES_TO_MOVE = x
                        break
                player_to_remove = None
                print("Debug: Current Player: " + current_player.playerName)
                for player in Game.BOARD_SQUARES[current_player.currentSquare].players:
                    print("Debug: Player in Square " + str(current_player.currentSquare) + ": " + player.playerName)
                    if player.playerNumber == current_player.playerNumber:
                        player_to_remove = player
                if player_to_remove is None:
                    print("No Player to Remove")
                else:
                    print("Player to Remove: " + player_to_remove.playerName)
                Game.BOARD_SQUARES[current_player.currentSquare].players.remove(player_to_remove)
                updated_squares = [(current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare])]
                current_player.currentSquare = min(99, current_player.currentSquare + Game.SQUARES_TO_MOVE)
                Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                updated_squares.append((current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]))
                Game.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [(current_player.playerName + " moved " + str(Game.SQUARES_TO_MOVE), current_player.playerColour)]))
                Game.TURN_STAGE = TurnStage.SQUARE_ACTION
                Game.CAN_PROGRESS = False
                if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                    Game.FORCED_MOVEMENT = True
                    D10.enabled = True
                    D10_2.enabled = True
                    D8.enabled = True
                    D8_2.enabled = True
                elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                    Game.BONUS_MOVEMENT = True
                    D10.enabled = True
                    D10_2.enabled = True
                    D8.enabled = True
                    D8_2.enabled = True
            elif Game.TURN_STAGE == TurnStage.SQUARE_ACTION:  # Doing what the Square wants
                draw_dice_sets()
                current_square = Game.BOARD_SQUARES[current_player.currentSquare]
                if current_player.currentSquare == 99:
                    Game.TURN_STAGE = TurnStage.GAME_WON
                else:
                    if current_square.symbol == "OneBlue":
                        Game.TURN_STAGE = TurnStage.DRAW_CARDS
                        Game.CARDS_TO_DRAW.append(CardType.BLUE)
                    elif current_square.symbol == "OneRed":
                        Game.TURN_STAGE = TurnStage.DRAW_CARDS
                        Game.CARDS_TO_DRAW.append(CardType.RED)
                    elif current_square.symbol == "TwoRed":
                        Game.TURN_STAGE = TurnStage.DRAW_CARDS
                        Game.CARDS_TO_DRAW.append(CardType.RED)
                        Game.CARDS_TO_DRAW.append(CardType.RED)
                    elif current_square.symbol == "TwoBlue":
                        Game.TURN_STAGE = TurnStage.DRAW_CARDS
                        Game.CARDS_TO_DRAW.append(CardType.BLUE)
                        Game.CARDS_TO_DRAW.append(CardType.BLUE)
                    elif current_square.symbol == "BlueRed":
                        Game.TURN_STAGE = TurnStage.DRAW_CARDS
                        Game.CARDS_TO_DRAW.append(CardType.BLUE)
                        Game.CARDS_TO_DRAW.append(CardType.RED)
                    elif current_square.symbol == "Roll10":
                        if Game.FORCED_CARD is None and Game.BONUS_MOVEMENT:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.SIX:
                                    Game.FORCED_CARD = CardValue.SIX
                        if Game.FORCED_CARD == CardValue.SIX:
                            draw_text("Use your Red Six Card!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Game.BONUS_MOVEMENT:
                                draw_text("You don't get this benefit", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                                    for card in current_player.redDeck:
                                        if card.cardValue == CardValue.TWO:
                                            Game.FORCED_CARD = CardValue.TWO
                                if Game.FORCED_CARD == CardValue.TWO:
                                    draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                                else:
                                    draw_text("Roll d10 to Move:", SMALL_FONT, BLACK, (1680, 240))
                                    if Game.ROLLING_WITH_ADVANTAGE:
                                        Game.TOP_DICE = [D10, D10_2]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        D10.check_click()
                                        D10_2.check_click()
                                        if not D10.enabled and not D10_2.enabled:
                                            Game.BONUS_MOVEMENT = False
                                            if D10.sideFacing >= D10_2.sideFacing:
                                                Game.TOP_DICE = [D10]
                                                Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Game.SQUARES_TO_MOVE = D10.sideFacing
                                            else:
                                                Game.TOP_DICE = [D10_2]
                                                Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Game.SQUARES_TO_MOVE = D10_2.sideFacing
                                            Game.TURN_STAGE = TurnStage.MOVEMENT
                                    elif Game.ROLLING_WITH_DISADVANTAGE:
                                        Game.TOP_DICE = [D10, D10_2]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        D10.check_click()
                                        D10_2.check_click()
                                        if not D10.enabled and not D10_2.enabled:
                                            Game.BONUS_MOVEMENT = False
                                            if D10.sideFacing <= D10_2.sideFacing:
                                                Game.TOP_DICE = [D10]
                                                Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Game.SQUARES_TO_MOVE = D10.sideFacing
                                            else:
                                                Game.TOP_DICE = [D10_2]
                                                Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Game.SQUARES_TO_MOVE = D10_2.sideFacing
                                            Game.TURN_STAGE = TurnStage.MOVEMENT
                                    else:
                                        Game.TOP_DICE = [D10]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        if D10.check_click():
                                            Game.BONUS_MOVEMENT = False
                                            Game.TOP_DICE = [D10]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Game.SQUARES_TO_MOVE = D10.sideFacing
                                            Game.TURN_STAGE = TurnStage.MOVEMENT
                    elif current_square.symbol == "Roll8":
                        if Game.FORCED_CARD is None and Game.BONUS_MOVEMENT:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.SIX:
                                    Game.FORCED_CARD = CardValue.SIX
                        if Game.FORCED_CARD == CardValue.SIX:
                            draw_text("Use your Red Six Card!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Game.BONUS_MOVEMENT:
                                draw_text("You don't get this benefit", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                                    for card in current_player.redDeck:
                                        if card.cardValue == CardValue.TWO:
                                            Game.FORCED_CARD = CardValue.TWO
                                if Game.FORCED_CARD == CardValue.TWO:
                                    draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                                else:
                                    draw_text("Roll d8 to Move:", SMALL_FONT, BLACK, (1680, 240))
                                    if Game.ROLLING_WITH_ADVANTAGE:
                                        Game.TOP_DICE = [D8, D8_2]
                                        Game.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        D8.check_click()
                                        D8_2.check_click()
                                        if not D8.enabled and not D8_2.enabled:
                                            Game.BONUS_MOVEMENT = False
                                            if D8.sideFacing >= D8_2.sideFacing:
                                                Game.TOP_DICE = [D8]
                                                Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Game.SQUARES_TO_MOVE = D8.sideFacing
                                            else:
                                                Game.TOP_DICE = [D8_2]
                                                Game.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Game.SQUARES_TO_MOVE = D8_2.sideFacing
                                            Game.TURN_STAGE = TurnStage.MOVEMENT
                                    elif Game.ROLLING_WITH_DISADVANTAGE:
                                        Game.TOP_DICE = [D8, D8_2]
                                        Game.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        D8.check_click()
                                        D8_2.check_click()
                                        if not D8.enabled and not D8_2.enabled:
                                            Game.BONUS_MOVEMENT = False
                                            if D8.sideFacing <= D8_2.sideFacing:
                                                Game.TOP_DICE = [D8]
                                                Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Game.SQUARES_TO_MOVE = D8.sideFacing
                                            else:
                                                Game.TOP_DICE = [D8_2]
                                                Game.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                                Game.SQUARES_TO_MOVE = D8_2.sideFacing
                                            Game.TURN_STAGE = TurnStage.MOVEMENT
                                    else:
                                        Game.TOP_DICE = [D8]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        draw_dice_sets()
                                        if D8.check_click():
                                            Game.BONUS_MOVEMENT = False
                                            Game.TOP_DICE = [D8]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Game.SQUARES_TO_MOVE = D8.sideFacing
                                            Game.TURN_STAGE = TurnStage.MOVEMENT
                    elif current_square.symbol == "Back10":
                        if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.TWO:
                                    Game.FORCED_CARD = CardValue.TWO
                        if Game.FORCED_CARD == CardValue.TWO:
                            draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Game.FORCED_MOVEMENT:
                                draw_text("You are safe for now", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                draw_text("Roll d10 to go Back:", SMALL_FONT, BLACK, (1680, 240))
                                if Game.ROLLING_WITH_ADVANTAGE:
                                    Game.TOP_DICE = [D10, D10_2]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D10.check_click()
                                    D10_2.check_click()
                                    if not D10.enabled and not D10_2.enabled:
                                        Game.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        if D10.sideFacing <= D10_2.sideFacing:
                                            Game.TOP_DICE = [D10]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D10.sideFacing
                                        else:
                                            Game.TOP_DICE = [D10_2]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D10_2.sideFacing
                                        Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.current_square, Game.BOARD_SQUARES[current_player.currentSquare]))
                                        Game.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [(current_player.playerName + " moved backward", current_player.playerColour)]))
                                        if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Game.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Game.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                elif Game.ROLLING_WITH_DISADVANTAGE:
                                    Game.TOP_DICE = [D10, D10_2]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D10.check_click()
                                    D10_2.check_click()
                                    if not D10.enabled and not D10_2.enabled:
                                        Game.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        if D10.sideFacing >= D10_2.sideFacing:
                                            Game.TOP_DICE = [D10]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D10.sideFacing
                                        else:
                                            Game.TOP_DICE = [D10_2]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D10_2.sideFacing
                                        Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]))
                                        Game.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [(current_player.playerName + " moved backward", current_player.playerColour)]))
                                        if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Game.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Game.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                else:
                                    Game.TOP_DICE = [D10]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    if D10.check_click():
                                        Game.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        Game.TOP_DICE = [D10]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D10.sideFacing
                                        Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]))
                                        Game.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [(current_player.playerName + " moved backward", current_player.playerColour)]))
                                        if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Game.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Game.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                    elif current_square.symbol == "Back8":
                        if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.TWO:
                                    Game.FORCED_CARD = CardValue.TWO
                        if Game.FORCED_CARD == CardValue.TWO:
                            draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Game.FORCED_MOVEMENT:
                                draw_text("You are safe for now", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                draw_text("Roll d8 to go Back:", SMALL_FONT, BLACK, (1680, 240))
                                if Game.ROLLING_WITH_ADVANTAGE:
                                    Game.TOP_DICE = [D8, D8_2]
                                    Game.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D8.check_click()
                                    D8_2.check_click()
                                    if not D8.enabled and not D8_2.enabled:
                                        Game.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        if D8.sideFacing <= D8_2.sideFacing:
                                            Game.TOP_DICE = [D8]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D8.sideFacing
                                        else:
                                            Game.TOP_DICE = [D8_2]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D8_2.sideFacing
                                        Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]))
                                        Game.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [(current_player.playerName + " moved backward", current_player.playerColour)]))
                                        if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Game.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Game.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                elif Game.ROLLING_WITH_DISADVANTAGE:
                                    Game.TOP_DICE = [D8, D8_2]
                                    Game.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D8.check_click()
                                    D8_2.check_click()
                                    if not D8.enabled and not D8_2.enabled:
                                        Game.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        if D8.sideFacing >= D8_2.sideFacing:
                                            Game.TOP_DICE = [D8]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D8.sideFacing
                                        else:
                                            Game.TOP_DICE = [D8_2]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            current_player.currentSquare -= D8_2.sideFacing
                                        Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]))
                                        Game.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [(current_player.playerName + " moved backward", current_player.playerColour)]))
                                        if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Game.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Game.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                else:
                                    Game.TOP_DICE = [D8]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    if D8.check_click():
                                        Game.FORCED_MOVEMENT = False
                                        current_square.players.remove(current_player)
                                        updated_squares = [(current_player.currentSquare, current_square)]
                                        Game.TOP_DICE = [D8]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D8.sideFacing
                                        Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                        updated_squares.append((current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]))
                                        Game.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [(current_player.playerName + " moved backward", current_player.playerColour)]))
                                        if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                            Game.FORCED_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                                        elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                            Game.BONUS_MOVEMENT = True
                                            D10.enabled = True
                                            D10_2.enabled = True
                                            D8.enabled = True
                                            D8_2.enabled = True
                    elif current_square.symbol == "DownKey":
                        if not Game.FORCED_MOVEMENT:
                            draw_text("You gain common sense", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("The key unlocks a door", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("Use the door to go South", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Game.FORCED_MOVEMENT = False
                                current_square.players.remove(current_player)
                                updated_squares = [(current_player.currentSquare, current_square)]
                                current_player.currentSquare = current_square.keyLocation
                                Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                updated_squares.append((current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]))
                                Game.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [(current_player.playerName + " moved down", current_player.playerColour)]))
                    elif current_square.symbol == "GoBack":
                        if not Game.FORCED_MOVEMENT:
                            draw_text("You beat fate this time", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("You are going back", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("from whence you came", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Game.FORCED_MOVEMENT = False
                                current_square.players.remove(current_player)
                                updated_squares = [(current_player.currentSquare, current_square)]
                                current_player.currentSquare -= Game.SQUARES_TO_MOVE
                                Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                updated_squares.append((current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]))
                                Game.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [(current_player.playerName + " moved back from whence they came", current_player.playerColour)]))
                                if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                    Game.FORCED_MOVEMENT = True
                                    D10.enabled = True
                                    D10_2.enabled = True
                                    D8.enabled = True
                                    D8_2.enabled = True
                                elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                    Game.BONUS_MOVEMENT = True
                                    D10.enabled = True
                                    D10_2.enabled = True
                                    D8.enabled = True
                                    D8_2.enabled = True
                    elif current_square.symbol == "UpKey":
                        if Game.FORCED_CARD is None and Game.BONUS_MOVEMENT:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.SIX:
                                    Game.FORCED_CARD = CardValue.SIX
                        if Game.FORCED_CARD == CardValue.SIX:
                            draw_text("Use your Red Six!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Game.BONUS_MOVEMENT:
                                draw_text("You don't get to move", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                draw_text("You find a key", SMALL_FONT, BLACK, (1680, 230))
                                draw_text("Use the key to go North", SMALL_FONT, BLACK, (1680, 260))
                                continue_button = Button("Continue", 1680, 600, 60)
                                if continue_button.check_click():
                                    Game.BONUS_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    updated_squares = [(current_player.currentSquare, current_square)]
                                    current_player.currentSquare = current_square.keyLocation
                                    Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    updated_squares.append((current_player.currentSquare, Game.BOARD_SQUARES[current_player.currentSquare]))
                                    Game.NETWORK.send(("PlayerSquaresEvents", current_player, updated_squares, [(current_player.playerName + " moved up", current_player.playerColour)]))
                    elif current_square.symbol == "Redo":
                        if Game.FORCED_CARD is None and Game.BONUS_MOVEMENT:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.SIX:
                                    Game.FORCED_CARD = CardValue.SIX
                        if Game.FORCED_CARD == CardValue.SIX:
                            draw_text("Use your Red Six!", SMALL_FONT, BLACK, (1680, 240))
                        else:
                            if not Game.BONUS_MOVEMENT:
                                draw_text("You don't get to move", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("End Turn", 1680, 600, 60)
                                if continue_button.check_click(): end_turn()
                            else:
                                draw_text("You get Double Movement", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("Continue", 1680, 600, 60)
                                if continue_button.check_click():
                                    Game.BONUS_MOVEMENT = False
                                    Game.TURN_STAGE = TurnStage.MOVEMENT
                    elif current_square.symbol == "MissTurn":
                        draw_text("You Miss your Next Turn", SMALL_FONT, BLACK, (1680, 240))
                        current_player.missNextTurn = True
                        Game.NETWORK.send(("Player", current_player))
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
                                    Game.NETWORK.send(("SquareEvents", (current_player.currentSquare, current_square), [(current_player.playerName + " woke a Monster", current_player.playerColour)]))
                                    D12.enabled = True
                                    D12_2.enabled = True
                                    Game.TOP_DICE = [D12]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                    Game.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                    Game.TURN_STAGE = TurnStage.ATTACK_MONSTER
                            else:
                                draw_text("You join a Monster fight!", SMALL_FONT, BLACK, (1680, 240))
                                continue_button = Button("Fight!", 1680, 600, 60)
                                if continue_button.check_click():
                                    Game.NETWORK.send(("Events", [(current_player.playerName + " joined a Monster Fight", current_player.playerColour)]))
                                    D12.enabled = True
                                    D12_2.enabled = True
                                    Game.TOP_DICE = [D12]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                    Game.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                    Game.TURN_STAGE = TurnStage.ATTACK_MONSTER
                        else:
                            Game.CAN_PROGRESS = True
                    elif current_square.symbol == "NiceHand":
                        if Game.PLAYER_COUNT == 2:
                            draw_text("You will now get the", SMALL_FONT, BLACK, (1680, 200))
                            draw_text("other Player's Blue Cards", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("and give them your Red Ones", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                event_data = []
                                other_player = Game.PLAYERS[1 if Game.PLAYER_NUMBER == 0 else 0]
                                for card in current_player.redDeck:  # Give the Other Player the Red Cards
                                    event_data.append((current_player.playerName + " gave " + other_player.playerName + " the " + card.displayName, current_player.playerColour))
                                    other_player.redDeck.append(card)
                                for card in other_player.blueDeck:  # Give the Current Player the Blue Cards
                                    event_data.append((other_player.playerName + " gave " + current_player.playerName + " the " + card.displayName, other_player.playerColour))
                                    current_player.blueDeck.append(card)
                                current_player.redDeck.clear()
                                other_player.blueDeck.clear()
                                Game.NETWORK.send(("PlayersEvents", Game.PLAYERS, event_data))
                                Game.TURN_STAGE = TurnStage.END_TURN
                        else:
                            draw_text("You will now get another", SMALL_FONT, BLACK, (1680, 200))
                            draw_text("Player's Blue Cards", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("and give them your Red Ones", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Choose Player", 1680, 600, 60)
                            if continue_button.check_click():
                                Game.CHOOSE_PLAYERS = "NiceHand"
                    elif current_square.symbol == "GravityWell":
                        draw_text("The other Players will now", SMALL_FONT, BLACK, (1680, 200))
                        draw_text("be pulled toward you", SMALL_FONT, BLACK, (1680, 230))
                        draw_text("unless they can't be moved", SMALL_FONT, BLACK, (1680, 260))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            event_data = []
                            updated_squares = []
                            discard_pile_changed = False
                            for player in Game.PLAYERS:
                                if player.currentSquare != current_player.currentSquare and check_can_move(player):
                                    if player.currentSquare > current_player.currentSquare:  # Pull Player Back
                                        # Remove Player from Previous Square:
                                        player_to_remove = None
                                        print("Debug: Player: " + player.playerName)
                                        for square_player in Game.BOARD_SQUARES[player.currentSquare].players:
                                            print("Debug: Player in Square " + str(player.currentSquare) + ": " + square_player.playerName)
                                            if square_player.playerNumber == player.playerNumber:
                                                player_to_remove = square_player
                                        if player_to_remove is None:
                                            print("No Player to Remove")
                                        else:
                                            print("Player to Remove: " + player_to_remove.playerName)
                                        Game.BOARD_SQUARES[player.currentSquare].players.remove(player_to_remove)
                                        # Add Previous Square to Updated Squares:
                                        square_index = 69
                                        for i in range(len(updated_squares)):
                                            if updated_squares[i][1].center == Game.BOARD_SQUARES[player.currentSquare].center:
                                                square_index = i
                                                break
                                        if square_index != 69:
                                            updated_squares[square_index] = (player.currentSquare, Game.BOARD_SQUARES[player.currentSquare])
                                        else:
                                            updated_squares.append((player.currentSquare, Game.BOARD_SQUARES[player.currentSquare]))
                                        player.currentSquare = max(player.currentSquare - 5, current_player.currentSquare)  # Move the Player Back
                                        event_data.append((player.playerName + " was pulled towards " + current_player.playerName, player.playerColour))
                                        Game.BOARD_SQUARES[player.currentSquare].players.append(player)  # Adds the Player to the New Square
                                        # Add New Square to Updated Squares:
                                        square_index = 69
                                        for i in range(len(updated_squares)):
                                            if updated_squares[i][1].center == Game.BOARD_SQUARES[player.currentSquare].center:
                                                square_index = i
                                                break
                                        if square_index != 69:
                                            updated_squares[square_index] = (player.currentSquare, Game.BOARD_SQUARES[player.currentSquare])
                                        else:
                                            updated_squares.append((player.currentSquare, Game.BOARD_SQUARES[player.currentSquare]))
                                    else:  # Pull Player Forward
                                        # Remove the Player from Previous Square:
                                        player_to_remove = None
                                        print("Debug: Player: " + player.playerName)
                                        for square_player in Game.BOARD_SQUARES[player.currentSquare].players:
                                            print("Debug: Player in Square " + str(player.currentSquare) + ": " + square_player.playerName)
                                            if square_player.playerNumber == player.playerNumber:
                                                player_to_remove = square_player
                                        if player_to_remove is None:
                                            print("No Player to Remove")
                                        else:
                                            print("Player to Remove: " + player_to_remove.playerName)
                                        Game.BOARD_SQUARES[player.currentSquare].players.remove(player_to_remove)
                                        # Add Previous Square to Updated Squares:
                                        square_index = 69
                                        for i in range(len(updated_squares)):
                                            if updated_squares[i][1].center == Game.BOARD_SQUARES[player.currentSquare].center:
                                                square_index = i
                                                break
                                        if square_index != 69:
                                            updated_squares[square_index] = (player.currentSquare, Game.BOARD_SQUARES[player.currentSquare])
                                        else:
                                            updated_squares.append((player.currentSquare, Game.BOARD_SQUARES[player.currentSquare]))
                                        # Move the Player Forward:
                                        squares_to_move = 5
                                        for x in range(1, 5):
                                            if Game.BOARD_SQUARES[player.currentSquare + x].hasBarrier:
                                                has_ten = False
                                                for card in player.blueDeck:
                                                    if card.cardValue == CardValue.TEN:
                                                        Game.CARD_TO_REMOVE = (player.blueDeck, card, False)
                                                        Game.DISCARD_PILE.append(card)
                                                        event_data.append((player.playerName + " used their " + card.displayName, player.playerColour))
                                                        discard_pile_changed = True
                                                        has_ten = True
                                                        break
                                                if not has_ten:
                                                    squares_to_move = x
                                                    Game.BOARD_SQUARES[player.currentSquare + x].hasBarrier = False
                                                    break
                                            elif Game.BOARD_SQUARES[player.currentSquare + x].monsterAwake:
                                                squares_to_move = x
                                                break
                                            elif player.currentSquare + x == current_player.currentSquare:
                                                squares_to_move = x
                                                break
                                        player.currentSquare += squares_to_move
                                        event_data.append((player.playerName + " was pulled towards " + current_player.playerName, player.playerColour))
                                        # Deals with the New Square:
                                        Game.BOARD_SQUARES[player.currentSquare].players.append(player)
                                        square_index = 69
                                        for i in range(len(updated_squares)):
                                            if updated_squares[i][1].center == Game.BOARD_SQUARES[player.currentSquare].center:
                                                square_index = i
                                                break
                                        if square_index != 69:
                                            updated_squares[square_index] = (player.currentSquare, Game.BOARD_SQUARES[player.currentSquare])
                                        else:
                                            updated_squares.append((player.currentSquare, Game.BOARD_SQUARES[player.currentSquare]))
                            if discard_pile_changed:
                                Game.NETWORK.send(("PlayersSquaresDiscardEvents", Game.PLAYERS, updated_squares, Game.DISCARD_PILE, event_data))
                            else:
                                Game.NETWORK.send(("PlayersSquaresEvents", Game.PLAYERS, updated_squares, event_data))
                            Game.TURN_STAGE = TurnStage.END_TURN
                    elif current_square.symbol is None:
                        Game.CAN_PROGRESS = True
                    if Game.CAN_PROGRESS:
                        Game.TURN_STAGE = TurnStage.END_TURN
            elif Game.TURN_STAGE == TurnStage.DRAW_CARDS:
                if Game.FORCED_CARD is None and len(Game.CARDS_TO_DRAW) > 0:
                    for card_type in Game.CARDS_TO_DRAW:
                        if card_type == CardType.BLUE:
                            for card in current_player.redDeck:
                                if card.cardValue == CardValue.QUEEN:
                                    Game.FORCED_CARD = CardValue.QUEEN
                            break
                if Game.FORCED_CARD == CardValue.QUEEN:
                    draw_text("Use your Red Queen Card!", SMALL_FONT, BLACK, (1680, 240))
                else:
                    if len(Game.CARDS_TO_DRAW) == 0:
                        Game.TURN_STAGE = TurnStage.END_TURN
                    else:
                        draw_dice_sets()
                        if Game.CARDS_TO_DRAW[0] == CardType.BLUE:
                            if not Game.DISPLAYING_CARD:
                                draw_text("Draw a Blue Card:", SMALL_FONT, BLACK, (1680, 240))
                                check_get_card(CardType.BLUE)
                            else:
                                draw_card(current_player.blueDeck[len(current_player.blueDeck) - 1], (1680, 380), 3)
                                if len(Game.CARDS_TO_DRAW) == 1:
                                    text = "End Turn"
                                else:
                                    text = "Continue"
                                continue_button = Button(text, 1680, 600, 60)
                                if continue_button.check_click():
                                    Game.DISPLAYING_CARD = False
                                    Game.CARDS_TO_DRAW.pop(0)
                                    if len(Game.CARDS_TO_DRAW) == 0:
                                        end_turn()
                        else:
                            if not Game.DISPLAYING_CARD:
                                draw_text("Draw a Red Card:", SMALL_FONT, BLACK, (1680, 240))
                                check_get_card(CardType.RED)
                            else:
                                draw_card(current_player.redDeck[len(current_player.redDeck) - 1], (1680, 380), 3)
                                if len(Game.CARDS_TO_DRAW) == 1:
                                    text = "End Turn"
                                else:
                                    text = "Continue"
                                continue_button = Button(text, 1680, 600, 60)
                                if continue_button.check_click():
                                    Game.DISPLAYING_CARD = False
                                    Game.CARDS_TO_DRAW.pop(0)
                                    if len(Game.CARDS_TO_DRAW) == 0:
                                        end_turn()
            elif Game.TURN_STAGE == TurnStage.END_TURN:
                draw_dice_sets()
                continue_button = Button("End Turn", 1680, 600, 60)
                if continue_button.check_click():
                    end_turn()
            elif Game.TURN_STAGE == TurnStage.GAME_WON:
                draw_text(current_player.playerName + " has Won!!", SMALL_FONT, BLACK, (1680, 240))
            check_hover_boxes()
    elif Game.CURRENT_STATE == ScreenState.PLAYING_GAME:
        WINDOW.fill(WHITE)
        Game.BUTTONS_ENABLED = True
        current_player = Game.PLAYERS[Game.CURRENT_PLAYER]
        draw_text(current_player.playerName + "'s Turn", SMALL_FONT, PLAYER_TO_COLOUR[current_player.playerNumber], (960, 30))
        game_board = pygame.Rect((480, 60), (960, 960))
        pygame.draw.rect(WINDOW, BLUE, game_board)
        roll_background = pygame.Rect((1460, 100), (440, 700))
        pygame.draw.rect(WINDOW, PASTEL_GREEN, roll_background, 0, 20)
        draw_game_image(BLUE_CARD_SYMBOL, (360, 250), 3, True, PASTEL_GREEN, (170, 75),
                        "Blue Draw Pile", "", "Current Size: " + str(len(Game.BLUE_DRAW_DECK)))
        draw_game_image(RED_CARD_SYMBOL, (360, 650), 3, True, PASTEL_GREEN, (170, 75),
                        "Red Draw Pile", "", "Current Size: " + str(len(Game.RED_DRAW_DECK)))
        if len(current_player.blueDeck) != 0:
            turned_blue_deck_image = pygame.transform.rotate(BLUE_CARD_SYMBOL[0], -90)
            turned_blue_deck_image = pygame.transform.scale(turned_blue_deck_image, (BLUE_CARD_SYMBOL[1][1] * 3, BLUE_CARD_SYMBOL[1][0] * 3))
            WINDOW.blit(turned_blue_deck_image, (95, 835))
            if Game.CARD_HANDS_ACTIVE: Game.HOVER_BOXES.append(("board symbol", ["Your Blue Card Hand"], turned_blue_deck_image, (95, 835), (215, 35), PASTEL_GREEN))
            blue_hand_rect = turned_blue_deck_image.get_rect()
            blue_hand_rect.topleft = (95, 835)
            if blue_hand_rect.collidepoint(pygame.mouse.get_pos()) and Game.LEFT_MOUSE_RELEASED and Game.CARD_HANDS_ACTIVE:
                Game.SHOW_HAND = CardType.BLUE
                Game.CARD_HANDS_ACTIVE = False
                if Game.TURN_STAGE == TurnStage.DRAW_CARDS:
                    if Game.DISPLAYING_CARD:
                        Game.CARDS_TO_DRAW.pop(0)
                        Game.DISPLAYING_CARD = False
        if len(current_player.redDeck) != 0:
            turned_red_deck_image = pygame.transform.rotate(RED_CARD_SYMBOL[0], 90)
            turned_red_deck_image = pygame.transform.scale(turned_red_deck_image, (RED_CARD_SYMBOL[1][1] * 3, RED_CARD_SYMBOL[1][0] * 3))
            WINDOW.blit(turned_red_deck_image, (1530, 835))
            if Game.CARD_HANDS_ACTIVE: Game.HOVER_BOXES.append(("board symbol", ["Your Red Card Hand"], turned_red_deck_image, (1530, 835), (215, 35), PASTEL_GREEN))
            red_hand_rect = turned_red_deck_image.get_rect()
            red_hand_rect.topleft = (1530, 835)
            if red_hand_rect.collidepoint(pygame.mouse.get_pos()) and Game.LEFT_MOUSE_RELEASED and Game.CARD_HANDS_ACTIVE:
                Game.SHOW_HAND = CardType.RED
                Game.CARD_HANDS_ACTIVE = False
                if Game.TURN_STAGE == TurnStage.DRAW_CARDS:
                    if Game.DISPLAYING_CARD:
                        Game.CARDS_TO_DRAW.pop(0)
                        Game.DISPLAYING_CARD = False
        draw_squares()
        if Game.SHOW_HAND == CardType.BLUE:
            Game.HOVER_BOXES.clear()
            WINDOW.fill(PASTEL_GREEN)
            draw_text(current_player.playerName + "'s Blue Card Hand", MEDIUM_FONT, ORANGE, (960, 69))
            back_button = Button("Back", 960, 950, 60)
            if back_button.check_click():
                Game.SHOW_HAND = None
                Game.CARD_HANDS_ACTIVE = True
            for x in range(len(current_player.blueDeck)):
                draw_card(current_player.blueDeck[x], CARD_TO_POSITION[x], 2)
            Game.BUTTONS_ENABLED = False
            check_hover_boxes()
        elif Game.SHOW_HAND == CardType.RED:
            Game.HOVER_BOXES.clear()
            WINDOW.fill(PASTEL_GREEN)
            draw_text(current_player.playerName + "'s Red Card Hand", MEDIUM_FONT, ORANGE, (960, 69))
            back_button = Button("Back", 960, 950, 60)
            if back_button.check_click():
                Game.SHOW_HAND = None
                Game.CARD_HANDS_ACTIVE = True
            for x in range(len(current_player.redDeck)):
                draw_card(current_player.redDeck[x], CARD_TO_POSITION[x], 2)
            Game.BUTTONS_ENABLED = False
            check_hover_boxes()
        elif Game.CHOOSE_PLAYERS is not None:
            Game.HOVER_BOXES.clear()
            WINDOW.fill(PASTEL_GREEN)
            draw_text("Choose a Player:", MEDIUM_FONT, ORANGE, (960, 69))
            player = None
            for x in range(len(Game.PLAYERS)):
                if Game.PLAYERS[x] != current_player:
                    if Game.CHOOSE_PLAYERS == "Red Five":
                        if Game.PLAYERS[x].setPlayerRoll is None:
                            button = Button(Game.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                            if button.check_click():
                                player = Game.PLAYERS[x]
                    elif Game.CHOOSE_PLAYERS == "Blue Five":
                        if Game.PLAYERS[x].setNextRoll is None:
                            button = Button(Game.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                            if button.check_click():
                                player = Game.PLAYERS[x]
                    else:
                        button = Button(Game.PLAYERS[x].playerName, CARD_TO_POSITION[x][0], CARD_TO_POSITION[x][1], 60)
                        if button.check_click():
                            player = Game.PLAYERS[x]
            if player is not None:
                if Game.CHOOSE_PLAYERS == "Blue Three":
                    for x in range(len(Game.PLAYERS)):
                        if Game.PLAYERS[x] != player and Game.PLAYERS[x] != current_player:
                            Game.PLAYERS[x].redDeck.append(Game.RED_DRAW_DECK.pop())
                    Game.CHOOSE_PLAYERS = None
                elif Game.CHOOSE_PLAYERS == "Red Three":
                    for x in range(len(Game.PLAYERS)):
                        if Game.PLAYERS[x] != player and Game.PLAYERS[x] != current_player:
                            Game.PLAYERS[x].blueDeck.append(Game.BLUE_DRAW_DECK.pop())
                    Game.CHOOSE_PLAYERS = None
                elif Game.CHOOSE_PLAYERS == "Blue Five":
                    Game.CHOOSE_PLAYERS = None
                    Game.CHOOSE_DICE = player
                elif Game.CHOOSE_PLAYERS == "Red Five":
                    Game.CHOOSE_PLAYERS = None
                    player.setPlayerRoll = current_player
                elif Game.CHOOSE_PLAYERS == "NiceHand":
                    for card in current_player.redDeck:  # Give the Other Player the Red Cards
                        player.redDeck.append(card)
                    for card in player.blueDeck:  # Give the Current Player the Blue Cards
                        current_player.blueDeck.append(card)
                    current_player.redDeck.clear()
                    player.blueDeck.clear()
                    Game.TURN_STAGE = TurnStage.END_TURN
                    Game.CHOOSE_PLAYERS = None
            Game.BUTTONS_ENABLED = False
        elif Game.CHOOSE_DICE is not None:
            Game.HOVER_BOXES.clear()
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
                Game.CHOOSE_DICE.setNextRoll = 1
                Game.CHOOSE_DICE = None
            if two_d6.check_click(False):
                Game.CHOOSE_DICE.setNextRoll = 2
                Game.CHOOSE_DICE = None
            if three_d6.check_click(False):
                Game.CHOOSE_DICE.setNextRoll = 3
                Game.CHOOSE_DICE = None
            if four_d6.check_click(False):
                Game.CHOOSE_DICE.setNextRoll = 4
                Game.CHOOSE_DICE = None
            if five_d6.check_click(False):
                Game.CHOOSE_DICE.setNextRoll = 5
                Game.CHOOSE_DICE = None
            if six_d6.check_click(False):
                Game.CHOOSE_DICE.setNextRoll = 6
                Game.CHOOSE_DICE = None
            Game.BUTTONS_ENABLED = False
        elif Game.CHOOSE_SQUARE is not None:
            Game.HOVER_BOXES.clear()
            WINDOW.fill(PASTEL_GREEN)
            draw_text("Choose a Square:", MEDIUM_FONT, ORANGE, (960, 30))
            draw_squares()
            square_clicked = check_squares_clicked()
            if square_clicked is not None and Game.BOARD_SQUARES.index(square_clicked) != 99 and Game.BOARD_SQUARES.index(square_clicked) != 0:
                if Game.CHOOSE_SQUARE == "Blue Nine" or Game.CHOOSE_SQUARE == "Red Nine":
                    if not square_clicked.hasBarrier:
                        square_clicked.hasBarrier = True
                        Game.CHOOSE_SQUARE = None
            Game.BUTTONS_ENABLED = False
        elif Game.TURN_STAGE == TurnStage.START_TURN:  # Calculations at the start of all turns
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
                        Game.CHOOSE_DICE = current_player.setPlayerRoll
                        current_player.setPlayerRoll = None
                else:
                    if Game.FORCED_CARD is None:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.THREE:
                                Game.FORCED_CARD = CardValue.THREE
                                break
                            if card.cardValue == CardValue.FIVE:
                                can_force = False
                                for player in Game.PLAYERS:
                                    if Game.IS_MULTIPLAYER:
                                        if player.playerNumber != Game.PLAYER_NUMBER and player.setNextRoll is None:
                                            can_force =  True
                                    else:
                                        if player.playerNumber != Game.CURRENT_PLAYER and player.setNextRoll is None:
                                            can_force = True
                                if can_force:
                                    Game.FORCED_CARD = CardValue.FIVE
                                break
                            if card.cardValue == CardValue.NINE:
                                Game.FORCED_CARD = CardValue.NINE
                                break
                    if Game.FORCED_CARD == CardValue.THREE:
                        draw_text("Use your Red Three Card!", SMALL_FONT, BLACK, (1680, 240))
                    elif Game.FORCED_CARD == CardValue.FIVE:
                        draw_text("Use your Red Five Card!", SMALL_FONT, BLACK, (1680, 240))
                    elif Game.FORCED_CARD == CardValue.NINE:
                        draw_text("Use your Red Nine Card!", SMALL_FONT, BLACK, (1680, 240))
                    elif Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth > 0:
                        D20.enabled = True
                        D20_2.enabled = True
                        D20_3.enabled = True
                        Game.SUCCEEDED_DEFENCE = None
                        Game.TURN_STAGE = TurnStage.MONSTER_ATTACK
                    else:  # Roll Dice
                        Game.TOP_DICE = [D6]
                        Game.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                        draw_dice_sets()
                        D6.enabled = True
                        D6_2.enabled = True
                        Game.TURN_STAGE = TurnStage.ROLL_DICE
        elif Game.TURN_STAGE == TurnStage.MONSTER_ATTACK:  # Monster Attacks
            if Game.SUCCEEDED_DEFENCE is None: draw_text("Defend against the Monster!", SMALL_FONT, BLACK, (1680, 240))
            if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                for card in current_player.redDeck:
                    if card.cardValue == CardValue.TWO:
                        Game.FORCED_CARD = CardValue.TWO
            if Game.FORCED_CARD is None and Game.SUCCEEDED_DEFENCE:
                for card in current_player.redDeck:
                    if card.cardValue == CardValue.EIGHT:
                        Game.FORCED_CARD = CardValue.EIGHT
            if Game.FORCED_CARD == CardValue.TWO:
                draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
            elif Game.FORCED_CARD == CardValue.EIGHT:
                draw_text("Use your Red Eight Card!", SMALL_FONT, BLACK, (1680, 240))
            else:
                if D20_3.enabled:
                    D20_3.sideFacing = random.randrange(1, 21)
                    D20_3.enabled = False
                draw_dice(D20_3, (1680, 330), 2)
                if Game.ROLLING_WITH_ADVANTAGE:
                    Game.TOP_DICE = [D20, D20_2]
                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                    Game.BOTTOM_DICE = [D10, D10_2, D12, D12_2, D4]
                    D20.check_click()
                    D20_2.check_click()
                    if not D20.enabled and not D20_2.enabled and Game.SUCCEEDED_DEFENCE is None:
                        Game.SUCCEEDED_DEFENCE = max(D20.sideFacing, D20_2.sideFacing) >= D20_3.sideFacing
                        if not Game.SUCCEEDED_DEFENCE:
                            for card in current_player.blueDeck:
                                if card.cardValue == CardValue.EIGHT:
                                    Game.CARD_TO_REMOVE = (current_player.blueDeck, card)
                                    Game.DISCARD_PILE.append(card)
                                    Game.SHIELD_ACTIVE = True
                                    break
                elif Game.ROLLING_WITH_DISADVANTAGE:
                    Game.TOP_DICE = [D20, D20_2]
                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                    Game.BOTTOM_DICE = [D10, D10_2, D12, D12_2, D4]
                    D20.check_click()
                    D20_2.check_click()
                    if not D20.enabled and not D20_2.enabled and Game.SUCCEEDED_DEFENCE is None:
                        Game.SUCCEEDED_DEFENCE = min(D20.sideFacing, D20_2.sideFacing) >= D20_3.sideFacing
                        if not Game.SUCCEEDED_DEFENCE:
                            for card in current_player.blueDeck:
                                if card.cardValue == CardValue.EIGHT:
                                    Game.CARD_TO_REMOVE = (current_player.blueDeck, card)
                                    Game.DISCARD_PILE.append(card)
                                    Game.SHIELD_ACTIVE = True
                                    break
                else:
                    Game.TOP_DICE = [D20]
                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                    Game.BOTTOM_DICE = [D10_2, D12, D12_2, D20_2, D4]
                    if D20.check_click():
                        Game.SUCCEEDED_DEFENCE = D20.sideFacing >= D20_3.sideFacing
                        if not Game.SUCCEEDED_DEFENCE:
                            for card in current_player.blueDeck:
                                if card.cardValue == CardValue.EIGHT:
                                    Game.CARD_TO_REMOVE = (current_player.blueDeck, card)
                                    Game.DISCARD_PILE.append(card)
                                    Game.SHIELD_ACTIVE = True
                                    break
                draw_dice_sets(500)
                if Game.SUCCEEDED_DEFENCE is not None:
                    if not Game.SUCCEEDED_DEFENCE:  # Player Loses
                        if Game.SHIELD_ACTIVE:
                            draw_text("Your Shield saved you", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("You survived the encounter", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Game.ROLLING_WITH_ADVANTAGE = False
                                Game.ROLLING_WITH_DISADVANTAGE = False
                                Game.TOP_DICE = [D12]
                                Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                Game.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                Game.TURN_STAGE = TurnStage.ATTACK_MONSTER
                                D12.enabled = True
                                D12_2.enabled = True
                                Game.SHIELD_ACTIVE = False
                        else:
                            draw_text("You failed your Defence Roll", SMALL_FONT, BLACK, (1680, 200))
                            draw_text("The Monster will knock you", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("back 4 spaces", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Game.ROLLING_WITH_ADVANTAGE = False
                                Game.ROLLING_WITH_DISADVANTAGE = False
                                Game.BOARD_SQUARES[current_player.currentSquare].players.remove(current_player)
                                current_player.currentSquare -= 4
                                Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                Game.TURN_STAGE = TurnStage.START_TURN
                    else:
                        draw_text("You defended yourself", SMALL_FONT, BLACK, (1680, 240))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            Game.ROLLING_WITH_ADVANTAGE = False
                            Game.ROLLING_WITH_DISADVANTAGE = False
                            Game.TOP_DICE = [D12]
                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                            Game.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                            Game.TURN_STAGE = TurnStage.ATTACK_MONSTER
                            D12.enabled = True
                            D12_2.enabled = True
        elif Game.TURN_STAGE == TurnStage.ATTACK_MONSTER:  # Attacking a Monster
            if Game.FORCED_CARD is None and not Game.TAKING_FOUR and not Game.TAKEN_FOUR:
                for card in current_player.redDeck:
                    if card.cardValue == CardValue.FOUR:
                        Game.FORCED_CARD = CardValue.FOUR
            if Game.FORCED_CARD == CardValue.FOUR:
                draw_text("Use your Red Four!", SMALL_FONT, BLACK, (1680, 240))
            else:
                if Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth <= 0:
                    draw_text("Congratulations!", SMALL_FONT, BLACK, (1680, 200))
                    draw_text("You have killed the Monster!", SMALL_FONT, BLACK, (1680, 230))
                    draw_text("You can roll movement now", SMALL_FONT, BLACK, (1680, 260))
                    continue_button = Button("Continue", 1680, 600, 60)
                    if continue_button.check_click():
                        Game.TURN_STAGE = TurnStage.START_TURN
                        Game.ADDING_FOUR = False
                        Game.TAKING_FOUR = False
                        Game.TAKEN_FOUR = False
                        Game.ROLLING_WITH_ADVANTAGE = False
                        Game.BOARD_SQUARES[current_player.currentSquare].monsterAwake = False
                elif not D12.enabled and not D12_2.enabled:
                    if Game.ADDING_FOUR:
                        draw_text("Add a d4 to the Attack:", SMALL_FONT, BLACK, (1680, 240))
                        Game.TOP_DICE = [D4]
                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                        Game.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                        draw_dice_sets()
                        if D4.check_click():
                            Game.ADDING_FOUR = False
                            Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= D4.sideFacing
                    elif Game.TAKING_FOUR and not Game.TAKEN_FOUR:
                        draw_text("Take a d4 from the Attack:", SMALL_FONT, BLACK, (1680, 240))
                        Game.TOP_DICE = [D4]
                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                        Game.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                        draw_dice_sets()
                        if D4.check_click():
                            Game.TAKEN_FOUR = True
                            Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth += D4.sideFacing
                    else:
                        draw_text("You did not kill the Monster", SMALL_FONT, BLACK, (1680, 240))
                        end_turn_button = Button("End Turn", 1680, 600, 60)
                        if end_turn_button.check_click():
                            end_turn()
                            Game.TAKEN_FOUR = False
                            Game.TAKING_FOUR = False
                            Game.ROLLING_WITH_ADVANTAGE = False
                else:
                    draw_text("Attack the Monster:", SMALL_FONT, BLACK, (1680, 240))
                    if Game.ROLLING_WITH_ADVANTAGE:
                        Game.TOP_DICE = [D12, D12_2]
                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                        Game.BOTTOM_DICE = [D10, D10_2, D20, D20_2, D4]
                    if not Game.ROLLING_WITH_ADVANTAGE:
                        if D12.check_click():
                            D12_2.enabled = False
                            Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= D12.sideFacing
                    else:
                        D12.check_click()
                        D12_2.check_click()
                        if not D12.enabled and not D12_2.enabled:
                            Game.BOARD_SQUARES[current_player.currentSquare].monsterHealth -= max(D12.sideFacing, D12_2.sideFacing)
                draw_dice_sets()
        elif Game.TURN_STAGE == TurnStage.ROLL_DICE:  # Rolling the Movement Dice
            if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                for card in current_player.redDeck:
                    if card.cardValue == CardValue.TWO:
                        Game.FORCED_CARD = CardValue.TWO
            if Game.FORCED_CARD is None and not Game.ROLLING_WITH_FOUR:
                for card in current_player.redDeck:
                    if card.cardValue == CardValue.JACK:
                        Game.FORCED_CARD = CardValue.JACK
            if Game.FORCED_CARD == CardValue.TWO:
                draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
            elif Game.FORCED_CARD == CardValue.JACK:
                draw_text("Use your Red Jack Card!", SMALL_FONT, BLACK, (1680, 240))
            else:
                if Game.ROLLING_WITH_FOUR:
                    Game.TOP_DICE = [D4]
                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                    Game.BOTTOM_DICE = [D10_2, D12, D12_2, D20, D20_2]
                    draw_text("Roll d4 to move:", SMALL_FONT, BLACK, (1680, 240))
                    draw_dice_sets()
                    if D4.check_click():
                        Game.ROLLING_WITH_FOUR = False
                        Game.SQUARES_TO_MOVE = D4.sideFacing
                        Game.TURN_STAGE = TurnStage.MOVEMENT
                elif Game.ROLLING_WITH_ADVANTAGE and Game.DICE_ROLLED == 2:
                    draw_text("Pick a dice to use:", SMALL_FONT, BLACK, (1680, 240))
                    draw_dice_sets()
                    if D6.check_click(False):
                        Game.ROLLING_WITH_ADVANTAGE = False
                        Game.DICE_ROLLED = 0
                        Game.SQUARES_TO_MOVE = D6.sideFacing
                        Game.TURN_STAGE = TurnStage.MOVEMENT
                        Game.TOP_DICE = [D6]
                        Game.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                    if D6_2.check_click(False):
                        Game.ROLLING_WITH_ADVANTAGE = False
                        Game.DICE_ROLLED = 0
                        Game.SQUARES_TO_MOVE = D6_2.sideFacing
                        Game.TURN_STAGE = TurnStage.MOVEMENT
                        Game.TOP_DICE = [D6_2]
                        Game.MIDDLE_DICE = [D6, D8, D8_2, D10, D10_2]
                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                else:
                    draw_text("Roll d6 to move:", SMALL_FONT, BLACK, (1680, 240))
                    if not Game.ROLLING_WITH_ADVANTAGE and not Game.ROLLING_DOUBLE and not Game.ROLLING_WITH_DISADVANTAGE:
                        draw_dice_sets()
                        if D6.check_click():
                            Game.TURN_STAGE = TurnStage.MOVEMENT
                            Game.SQUARES_TO_MOVE = D6.sideFacing
                    elif Game.ROLLING_WITH_ADVANTAGE:
                        Game.TOP_DICE = [D6, D6_2]
                        Game.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                        draw_dice_sets()
                        if D6.check_click():
                            Game.DICE_ROLLED += 1
                        if D6_2.check_click():
                            Game.DICE_ROLLED += 1
                        if Game.DICE_ROLLED == 2:
                            D6.enabled = True
                            D6_2.enabled = True
                    elif Game.ROLLING_WITH_DISADVANTAGE:
                        Game.TOP_DICE = [D6, D6_2]
                        Game.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                        draw_dice_sets()
                        D6.check_click()
                        D6_2.check_click()
                        if not D6.enabled and not D6_2.enabled:
                            Game.SQUARES_TO_MOVE = min(D6.sideFacing, D6_2.sideFacing)
                            if D6.sideFacing > D6_2.sideFacing:
                                Game.TOP_DICE = [D6_2]
                                Game.MIDDLE_DICE = [D6, D8, D8_2, D10, D10_2]
                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            else:
                                Game.TOP_DICE = [D6]
                                Game.MIDDLE_DICE = [D6_2, D8, D8_2, D10, D10_2]
                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                            Game.TURN_STAGE = TurnStage.MOVEMENT
                            Game.ROLLING_WITH_DISADVANTAGE = False
                    elif Game.ROLLING_DOUBLE:
                        Game.TOP_DICE = [D6, D6_2]
                        Game.MIDDLE_DICE = [D8, D8_2, D10, D10_2]
                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                        draw_dice_sets()
                        D6.check_click()
                        D6_2.check_click()
                        if not D6.enabled and not D6_2.enabled:
                            Game.SQUARES_TO_MOVE = D6.sideFacing + D6_2.sideFacing
                            Game.TURN_STAGE = TurnStage.MOVEMENT
                            Game.ROLLING_DOUBLE = False
        elif Game.TURN_STAGE == TurnStage.MOVEMENT:  # Moving the Current Player
            draw_dice_sets()
            for x in range(Game.SQUARES_TO_MOVE):
                if Game.BOARD_SQUARES[current_player.currentSquare + x].hasBarrier and x != 0:
                    has_ten = False
                    for card in current_player.blueDeck:
                        if card.cardValue == CardValue.TEN:
                            Game.CARD_TO_REMOVE = (current_player.blueDeck, card)
                            Game.DISCARD_PILE.append(card)
                            has_ten = True
                            break
                    if not has_ten:
                        Game.SQUARES_TO_MOVE = x
                        Game.BOARD_SQUARES[current_player.currentSquare + x].hasBarrier = False
                        break
                elif Game.BOARD_SQUARES[current_player.currentSquare + x].monsterAwake:
                    Game.SQUARES_TO_MOVE = x
                    break
            Game.BOARD_SQUARES[current_player.currentSquare].players.remove(current_player)
            current_player.currentSquare = min(99, current_player.currentSquare + Game.SQUARES_TO_MOVE)
            Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
            Game.TURN_STAGE = TurnStage.SQUARE_ACTION
            Game.CAN_PROGRESS = False
            if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                Game.FORCED_MOVEMENT = True
                D10.enabled = True
                D10_2.enabled = True
                D8.enabled = True
                D8_2.enabled = True
            elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                Game.BONUS_MOVEMENT = True
                D10.enabled = True
                D10_2.enabled = True
                D8.enabled = True
                D8_2.enabled = True
        elif Game.TURN_STAGE == TurnStage.SQUARE_ACTION:  # Doing what the Square wants
            draw_dice_sets()
            current_square = Game.BOARD_SQUARES[current_player.currentSquare]
            if current_player.currentSquare == 99:
                Game.TURN_STAGE = TurnStage.GAME_WON
            else:
                if current_square.symbol == "OneBlue":
                    Game.TURN_STAGE = TurnStage.DRAW_CARDS
                    Game.CARDS_TO_DRAW.append(CardType.BLUE)
                elif current_square.symbol == "OneRed":
                    Game.TURN_STAGE = TurnStage.DRAW_CARDS
                    Game.CARDS_TO_DRAW.append(CardType.RED)
                elif current_square.symbol == "TwoRed":
                    Game.TURN_STAGE = TurnStage.DRAW_CARDS
                    Game.CARDS_TO_DRAW.append(CardType.RED)
                    Game.CARDS_TO_DRAW.append(CardType.RED)
                elif current_square.symbol == "TwoBlue":
                    Game.TURN_STAGE = TurnStage.DRAW_CARDS
                    Game.CARDS_TO_DRAW.append(CardType.BLUE)
                    Game.CARDS_TO_DRAW.append(CardType.BLUE)
                elif current_square.symbol == "BlueRed":
                    Game.TURN_STAGE = TurnStage.DRAW_CARDS
                    Game.CARDS_TO_DRAW.append(CardType.BLUE)
                    Game.CARDS_TO_DRAW.append(CardType.RED)
                elif current_square.symbol == "Roll10":
                    if Game.FORCED_CARD is None and Game.BONUS_MOVEMENT:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.SIX:
                                Game.FORCED_CARD = CardValue.SIX
                    if Game.FORCED_CARD == CardValue.SIX:
                        draw_text("Use your Red Six Card!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Game.BONUS_MOVEMENT:
                            draw_text("You don't get this benefit", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                                for card in current_player.redDeck:
                                    if card.cardValue == CardValue.TWO:
                                        Game.FORCED_CARD = CardValue.TWO
                            if Game.FORCED_CARD == CardValue.TWO:
                                draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                            else:
                                draw_text("Roll d10 to Move:", SMALL_FONT, BLACK, (1680, 240))
                                if Game.ROLLING_WITH_ADVANTAGE:
                                    Game.TOP_DICE = [D10, D10_2]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D10.check_click()
                                    D10_2.check_click()
                                    if not D10.enabled and not D10_2.enabled:
                                        Game.BONUS_MOVEMENT = False
                                        if D10.sideFacing >= D10_2.sideFacing:
                                            Game.TOP_DICE = [D10]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Game.SQUARES_TO_MOVE = D10.sideFacing
                                        else:
                                            Game.TOP_DICE = [D10_2]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Game.SQUARES_TO_MOVE = D10_2.sideFacing
                                        Game.TURN_STAGE = TurnStage.MOVEMENT
                                elif Game.ROLLING_WITH_DISADVANTAGE:
                                    Game.TOP_DICE = [D10, D10_2]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D10.check_click()
                                    D10_2.check_click()
                                    if not D10.enabled and not D10_2.enabled:
                                        Game.BONUS_MOVEMENT = False
                                        if D10.sideFacing <= D10_2.sideFacing:
                                            Game.TOP_DICE = [D10]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Game.SQUARES_TO_MOVE = D10.sideFacing
                                        else:
                                            Game.TOP_DICE = [D10_2]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Game.SQUARES_TO_MOVE = D10_2.sideFacing
                                        Game.TURN_STAGE = TurnStage.MOVEMENT
                                else:
                                    Game.TOP_DICE = [D10]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    if D10.check_click():
                                        Game.BONUS_MOVEMENT = False
                                        Game.TOP_DICE = [D10]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        Game.SQUARES_TO_MOVE = D10.sideFacing
                                        Game.TURN_STAGE = TurnStage.MOVEMENT
                elif current_square.symbol == "Roll8":
                    if Game.FORCED_CARD is None and Game.BONUS_MOVEMENT:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.SIX:
                                Game.FORCED_CARD = CardValue.SIX
                    if Game.FORCED_CARD == CardValue.SIX:
                        draw_text("Use your Red Six Card!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Game.BONUS_MOVEMENT:
                            draw_text("You don't get this benefit", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                                for card in current_player.redDeck:
                                    if card.cardValue == CardValue.TWO:
                                        Game.FORCED_CARD = CardValue.TWO
                            if Game.FORCED_CARD == CardValue.TWO:
                                draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                            else:
                                draw_text("Roll d8 to Move:", SMALL_FONT, BLACK, (1680, 240))
                                if Game.ROLLING_WITH_ADVANTAGE:
                                    Game.TOP_DICE = [D8, D8_2]
                                    Game.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D8.check_click()
                                    D8_2.check_click()
                                    if not D8.enabled and not D8_2.enabled:
                                        Game.BONUS_MOVEMENT = False
                                        if D8.sideFacing >= D8_2.sideFacing:
                                            Game.TOP_DICE = [D8]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Game.SQUARES_TO_MOVE = D8.sideFacing
                                        else:
                                            Game.TOP_DICE = [D8_2]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Game.SQUARES_TO_MOVE = D8_2.sideFacing
                                        Game.TURN_STAGE = TurnStage.MOVEMENT
                                elif Game.ROLLING_WITH_DISADVANTAGE:
                                    Game.TOP_DICE = [D8, D8_2]
                                    Game.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    D8.check_click()
                                    D8_2.check_click()
                                    if not D8.enabled and not D8_2.enabled:
                                        Game.BONUS_MOVEMENT = False
                                        if D8.sideFacing <= D8_2.sideFacing:
                                            Game.TOP_DICE = [D8]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Game.SQUARES_TO_MOVE = D8.sideFacing
                                        else:
                                            Game.TOP_DICE = [D8_2]
                                            Game.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                            Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                            Game.SQUARES_TO_MOVE = D8_2.sideFacing
                                        Game.TURN_STAGE = TurnStage.MOVEMENT
                                else:
                                    Game.TOP_DICE = [D8]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    draw_dice_sets()
                                    if D8.check_click():
                                        Game.BONUS_MOVEMENT = False
                                        Game.TOP_DICE = [D8]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        Game.SQUARES_TO_MOVE = D8.sideFacing
                                        Game.TURN_STAGE = TurnStage.MOVEMENT
                elif current_square.symbol == "Back10":
                    if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.TWO:
                                Game.FORCED_CARD = CardValue.TWO
                    if Game.FORCED_CARD == CardValue.TWO:
                        draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Game.FORCED_MOVEMENT:
                            draw_text("You are safe for now", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("Roll d10 to go Back:", SMALL_FONT, BLACK, (1680, 240))
                            if Game.ROLLING_WITH_ADVANTAGE:
                                Game.TOP_DICE = [D10, D10_2]
                                Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                D10.check_click()
                                D10_2.check_click()
                                if not D10.enabled and not D10_2.enabled:
                                    Game.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    if D10.sideFacing <= D10_2.sideFacing:
                                        Game.TOP_DICE = [D10]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D10.sideFacing
                                    else:
                                        Game.TOP_DICE = [D10_2]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D10_2.sideFacing
                                    Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Game.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Game.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                            elif Game.ROLLING_WITH_DISADVANTAGE:
                                Game.TOP_DICE = [D10, D10_2]
                                Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2]
                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                D10.check_click()
                                D10_2.check_click()
                                if not D10.enabled and not D10_2.enabled:
                                    Game.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    if D10.sideFacing >= D10_2.sideFacing:
                                        Game.TOP_DICE = [D10]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D10.sideFacing
                                    else:
                                        Game.TOP_DICE = [D10_2]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D10_2.sideFacing
                                    Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Game.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Game.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                            else:
                                Game.TOP_DICE = [D10]
                                Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                if D10.check_click():
                                    Game.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    Game.TOP_DICE = [D10]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    current_player.currentSquare -= D10.sideFacing
                                    Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Game.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Game.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                elif current_square.symbol == "Back8":
                    if Game.FORCED_CARD is None and not Game.ROLLING_WITH_DISADVANTAGE:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.TWO:
                                Game.FORCED_CARD = CardValue.TWO
                    if Game.FORCED_CARD == CardValue.TWO:
                        draw_text("Use your Red Two Card!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Game.FORCED_MOVEMENT:
                            draw_text("You are safe for now", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("Roll d8 to go Back:", SMALL_FONT, BLACK, (1680, 240))
                            if Game.ROLLING_WITH_ADVANTAGE:
                                Game.TOP_DICE = [D8, D8_2]
                                Game.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                D8.check_click()
                                D8_2.check_click()
                                if not D8.enabled and not D8_2.enabled:
                                    Game.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    if D8.sideFacing <= D8_2.sideFacing:
                                        Game.TOP_DICE = [D8]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D8.sideFacing
                                    else:
                                        Game.TOP_DICE = [D8_2]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D8_2.sideFacing
                                    Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Game.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Game.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                            elif Game.ROLLING_WITH_DISADVANTAGE:
                                Game.TOP_DICE = [D8, D8_2]
                                Game.MIDDLE_DICE = [D6, D6_2, D10, D10_2]
                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                D8.check_click()
                                D8_2.check_click()
                                if not D8.enabled and not D8_2.enabled:
                                    Game.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    if D8.sideFacing >= D8_2.sideFacing:
                                        Game.TOP_DICE = [D8]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D8.sideFacing
                                    else:
                                        Game.TOP_DICE = [D8_2]
                                        Game.MIDDLE_DICE = [D6, D6_2, D8, D10, D10_2]
                                        Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                        current_player.currentSquare -= D8_2.sideFacing
                                    Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Game.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Game.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                            else:
                                Game.TOP_DICE = [D8]
                                Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                draw_dice_sets()
                                if D8.check_click():
                                    Game.FORCED_MOVEMENT = False
                                    current_square.players.remove(current_player)
                                    Game.TOP_DICE = [D8]
                                    Game.MIDDLE_DICE = [D6, D6_2, D8_2, D10, D10_2]
                                    Game.BOTTOM_DICE = [D12, D12_2, D20, D20_2, D4]
                                    current_player.currentSquare -= D8.sideFacing
                                    Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                                    if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                        Game.FORCED_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                                    elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                        Game.BONUS_MOVEMENT = True
                                        D10.enabled = True
                                        D10_2.enabled = True
                                        D8.enabled = True
                                        D8_2.enabled = True
                elif current_square.symbol == "DownKey":
                    if not Game.FORCED_MOVEMENT:
                        draw_text("You gain common sense", SMALL_FONT, BLACK, (1680, 240))
                        continue_button = Button("End Turn", 1680, 600, 60)
                        if continue_button.check_click(): end_turn()
                    else:
                        draw_text("The key unlocks a door", SMALL_FONT, BLACK, (1680, 230))
                        draw_text("Use the door to go South", SMALL_FONT, BLACK, (1680, 260))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            Game.FORCED_MOVEMENT = False
                            current_square.players.remove(current_player)
                            current_player.currentSquare = current_square.keyLocation
                            Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                elif current_square.symbol == "GoBack":
                    if not Game.FORCED_MOVEMENT:
                        draw_text("You beat fate this time", SMALL_FONT, BLACK, (1680, 240))
                        continue_button = Button("End Turn", 1680, 600, 60)
                        if continue_button.check_click(): end_turn()
                    else:
                        draw_text("You are going back", SMALL_FONT, BLACK, (1680, 230))
                        draw_text("from whence you came", SMALL_FONT, BLACK, (1680, 260))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            Game.FORCED_MOVEMENT = False
                            current_square.players.remove(current_player)
                            current_player.currentSquare -= Game.SQUARES_TO_MOVE
                            Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                            if Game.BOARD_SQUARES[current_player.currentSquare].symbol == "GoBack" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "DownKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Back10":
                                Game.FORCED_MOVEMENT = True
                                D10.enabled = True
                                D10_2.enabled = True
                                D8.enabled = True
                                D8_2.enabled = True
                            elif Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Redo" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "UpKey" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll8" or Game.BOARD_SQUARES[current_player.currentSquare].symbol == "Roll10":
                                Game.BONUS_MOVEMENT = True
                                D10.enabled = True
                                D10_2.enabled = True
                                D8.enabled = True
                                D8_2.enabled = True
                elif current_square.symbol == "UpKey":
                    if Game.FORCED_CARD is None and Game.BONUS_MOVEMENT:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.SIX:
                                Game.FORCED_CARD = CardValue.SIX
                    if Game.FORCED_CARD == CardValue.SIX:
                        draw_text("Use your Red Six!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Game.BONUS_MOVEMENT:
                            draw_text("You don't get to move", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("You find a key", SMALL_FONT, BLACK, (1680, 230))
                            draw_text("Use the key to go North", SMALL_FONT, BLACK, (1680, 260))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Game.BONUS_MOVEMENT = False
                                current_square.players.remove(current_player)
                                current_player.currentSquare = current_square.keyLocation
                                Game.BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
                elif current_square.symbol == "Redo":
                    if Game.FORCED_CARD is None and Game.BONUS_MOVEMENT:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.SIX:
                                Game.FORCED_CARD = CardValue.SIX
                    if Game.FORCED_CARD == CardValue.SIX:
                        draw_text("Use your Red Six!", SMALL_FONT, BLACK, (1680, 240))
                    else:
                        if not Game.BONUS_MOVEMENT:
                            draw_text("You don't get to move", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("End Turn", 1680, 600, 60)
                            if continue_button.check_click(): end_turn()
                        else:
                            draw_text("You get Double Movement", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("Continue", 1680, 600, 60)
                            if continue_button.check_click():
                                Game.BONUS_MOVEMENT = False
                                Game.TURN_STAGE = TurnStage.MOVEMENT
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
                                Game.TOP_DICE = [D12]
                                Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                Game.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                Game.TURN_STAGE = TurnStage.ATTACK_MONSTER
                        else:
                            draw_text("You join a Monster fight!", SMALL_FONT, BLACK, (1680, 240))
                            continue_button = Button("Fight!", 1680, 600, 60)
                            if continue_button.check_click():
                                D12.enabled = True
                                D12_2.enabled = True
                                Game.TOP_DICE = [D12]
                                Game.MIDDLE_DICE = [D6, D6_2, D8, D8_2, D10]
                                Game.BOTTOM_DICE = [D10_2, D12_2, D20, D20_2, D4]
                                Game.TURN_STAGE = TurnStage.ATTACK_MONSTER
                    else:
                        Game.CAN_PROGRESS = True
                elif current_square.symbol == "NiceHand":
                    if Game.PLAYER_COUNT == 2:
                        draw_text("You will now get the", SMALL_FONT, BLACK, (1680, 200))
                        draw_text("other Player's Blue Cards", SMALL_FONT, BLACK, (1680, 230))
                        draw_text("and give them your Red Ones", SMALL_FONT, BLACK, (1680, 260))
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            other_player = Game.PLAYERS[1 if Game.PLAYER_NUMBER == 0 else 0]
                            for card in current_player.redDeck:  # Give the Other Player the Red Cards
                                other_player.redDeck.append(card)
                            for card in other_player.blueDeck:  # Give the Current Player the Blue Cards
                                current_player.blueDeck.append(card)
                            current_player.redDeck.clear()
                            other_player.blueDeck.clear()
                            Game.TURN_STAGE = TurnStage.END_TURN
                    else:
                        draw_text("You will now get another", SMALL_FONT, BLACK, (1680, 200))
                        draw_text("Player's Blue Cards", SMALL_FONT, BLACK, (1680, 230))
                        draw_text("and give them your Red Ones", SMALL_FONT, BLACK, (1680, 260))
                        continue_button = Button("Choose Player", 1680, 600, 60)
                        if continue_button.check_click():
                            Game.CHOOSE_PLAYERS = "NiceHand"
                elif current_square.symbol == "GravityWell":
                    draw_text("The other Players will now", SMALL_FONT, BLACK, (1680, 200))
                    draw_text("be pulled toward you", SMALL_FONT, BLACK, (1680, 230))
                    draw_text("unless they can't be moved", SMALL_FONT, BLACK, (1680, 260))
                    continue_button = Button("Continue", 1680, 600, 60)
                    if continue_button.check_click():
                        for player in Game.PLAYERS:
                            if player.currentSquare != current_player.currentSquare and check_can_move(player):
                                if player.currentSquare > current_player.currentSquare:  # Pull Player Back
                                    Game.BOARD_SQUARES[player.currentSquare].players.remove(player)  # Remove Player from Previous Square
                                    player.currentSquare = max(player.currentSquare - 5, current_player.currentSquare)  # Move the Player Back
                                    Game.BOARD_SQUARES[player.currentSquare].players.append(player)  # Adds the Player to the New Square
                                else:  # Pull Player Forward
                                    Game.BOARD_SQUARES[player.currentSquare].players.remove(player)
                                    # Move the Player Forward:
                                    squares_to_move = 5
                                    for x in range(1, 5):
                                        if Game.BOARD_SQUARES[player.currentSquare + x].hasBarrier:
                                            has_ten = False
                                            for card in player.blueDeck:
                                                if card.cardValue == CardValue.TEN:
                                                    Game.CARD_TO_REMOVE = (player.blueDeck, card, False)
                                                    Game.DISCARD_PILE.append(card)
                                                    has_ten = True
                                                    break
                                            if not has_ten:
                                                squares_to_move = x
                                                Game.BOARD_SQUARES[player.currentSquare + x].hasBarrier = False
                                                break
                                        elif Game.BOARD_SQUARES[player.currentSquare + x].monsterAwake:
                                            squares_to_move = x
                                            break
                                        elif player.currentSquare + x == current_player.currentSquare:
                                            squares_to_move = x
                                            break
                                    player.currentSquare += squares_to_move
                                    Game.BOARD_SQUARES[player.currentSquare].players.append(player)
                        Game.TURN_STAGE = TurnStage.END_TURN
                elif current_square.symbol is None:
                    Game.CAN_PROGRESS = True
                if Game.CAN_PROGRESS:
                    Game.TURN_STAGE = TurnStage.END_TURN
        elif Game.TURN_STAGE == TurnStage.DRAW_CARDS:
            if Game.FORCED_CARD is None and len(Game.CARDS_TO_DRAW) > 0:
                for card_type in Game.CARDS_TO_DRAW:
                    if card_type == CardType.BLUE:
                        for card in current_player.redDeck:
                            if card.cardValue == CardValue.QUEEN:
                                Game.FORCED_CARD = CardValue.QUEEN
                        break
            if Game.FORCED_CARD == CardValue.QUEEN:
                draw_text("Use your Red Queen Card!", SMALL_FONT, BLACK, (1680, 240))
            else:
                if len(Game.CARDS_TO_DRAW) == 0:
                    Game.TURN_STAGE = TurnStage.END_TURN
                else:
                    draw_dice_sets()
                    if Game.CARDS_TO_DRAW[0] == CardType.BLUE:
                        if not Game.DISPLAYING_CARD:
                            draw_text("Draw a Blue Card:", SMALL_FONT, BLACK, (1680, 240))
                            check_get_card(CardType.BLUE)
                        else:
                            draw_card(current_player.blueDeck[len(current_player.blueDeck) - 1], (1680, 380), 3)
                            if len(Game.CARDS_TO_DRAW) == 1:
                                text = "End Turn"
                            else:
                                text = "Continue"
                            continue_button = Button(text, 1680, 600, 60)
                            if continue_button.check_click():
                                Game.DISPLAYING_CARD = False
                                Game.CARDS_TO_DRAW.pop(0)
                                if len(Game.CARDS_TO_DRAW) == 0:
                                    end_turn()
                    else:
                        if not Game.DISPLAYING_CARD:
                            draw_text("Draw a Red Card:", SMALL_FONT, BLACK, (1680, 240))
                            check_get_card(CardType.RED)
                        else:
                            draw_card(current_player.redDeck[len(current_player.redDeck) - 1], (1680, 380), 3)
                            if len(Game.CARDS_TO_DRAW) == 1:
                                text = "End Turn"
                            else:
                                text = "Continue"
                            continue_button = Button(text, 1680, 600, 60)
                            if continue_button.check_click():
                                Game.DISPLAYING_CARD = False
                                Game.CARDS_TO_DRAW.pop(0)
                                if len(Game.CARDS_TO_DRAW) == 0:
                                    end_turn()
        elif Game.TURN_STAGE == TurnStage.END_TURN:
            draw_dice_sets()
            continue_button = Button("End Turn", 1680, 600, 60)
            if continue_button.check_click():
                end_turn()
        elif Game.TURN_STAGE == TurnStage.GAME_WON:
            draw_text(current_player.playerName + " has Won!!", SMALL_FONT, BLACK, (1680, 240))
        if Game.SHOW_HAND is None and Game.CHOOSE_DICE is None and Game.CHOOSE_PLAYERS is None and Game.CHOOSE_SQUARE is None:
            quit_button = Button("Quit", 360, 450, 60)
            if quit_button.check_click():
                pygame.quit()
        check_hover_boxes()


def check_server_updates():
    network_response = Game.NETWORK.send("!")
    if network_response:
        if "curr_player" in network_response:
            Game.CURRENT_PLAYER = network_response["curr_player"]
            if Game.CURRENT_PLAYER == Game.PLAYER_NUMBER:
                Game.EVENT_LIST.clear()
        if "players" in network_response:
            Game.PLAYERS = network_response["players"]
        if "board" in network_response:
            Game.BOARD_SQUARES = network_response["board"]
            if Game.SQUARE_VOTE:
                Game.SQUARE_VOTE = False
        if "discard" in network_response:
            Game.DISCARD_PILE = network_response["discard"]
        if "red" in network_response:
            Game.RED_DRAW_DECK = network_response["red"]
        if "blue" in network_response:
            Game.BLUE_DRAW_DECK = network_response["blue"]
        if "events" in network_response:
            for event in network_response["events"]:
                Game.EVENT_LIST.append(event)
        if "square_vote" in network_response:
            Game.CHOOSE_SQUARE = "Red Nine"
        if "quit" in network_response:
            pygame.quit()


def draw_dice_sets(top_height = 330):
    if len(Game.TOP_DICE) == 1:
        draw_dice(Game.TOP_DICE[0], (1680, top_height), 2)
    else:
        draw_dice(Game.TOP_DICE[0], (1628, top_height), 2)
        draw_dice(Game.TOP_DICE[1], (1732, top_height), 2)
    for x in range(len(Game.MIDDLE_DICE)):
        draw_dice(Game.MIDDLE_DICE[x], (1550 + (60 * x), 690), 1)
    for x in range(len(Game.BOTTOM_DICE)):
        draw_dice(Game.BOTTOM_DICE[x], (1550 + (60 * x), 760), 1)


def end_turn():
    if Game.IS_MULTIPLAYER:
        Game.CURRENT_PLAYER = Game.NETWORK.send("End Turn")
    else:
        if Game.CURRENT_PLAYER == Game.PLAYER_COUNT - 1:
            Game.CURRENT_PLAYER = 0
        else:
            Game.CURRENT_PLAYER += 1
    Game.TURN_STAGE = TurnStage.START_TURN
    if Game.ROLLING_DOUBLE: Game.ROLLING_DOUBLE = False


def draw_squares():
    for x in range(len(Game.BOARD_SQUARES)):
        square = Game.BOARD_SQUARES[x]
        square_rect = pygame.Rect((square.center[0] - 44, square.center[1] - 44), (89, 89))
        pygame.draw.rect(WINDOW, WHITE, square_rect)
        if square.symbol is not None:
            if square.symbol == "Monster":
                if square.monsterHealth > 0:
                    draw_game_image((ID_TO_SYMBOLS[square.symbol], (89, 89)), (square.center[0] + 1, square.center[1] + 1), 1)
                    draw_text(str(square.monsterHealth) + "hp", TINY_FONT, BLUE,
                              (square.center[0] - 10, square.center[1] + 20), False)
            else:
                draw_game_image((ID_TO_SYMBOLS[square.symbol], (89, 89)), (square.center[0] + 1, square.center[1] + 1), 1)
        if square.hasBarrier:
            if Game.BOARD_SQUARES[x + 1].center[0] > square.center[0]:
                barrier_rect = pygame.Rect((square.center[0] + 34, square.center[1] - 39), (5, 79))
            elif Game.BOARD_SQUARES[x + 1].center[0] < square.center[0]:
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


def check_can_move(player):
    if Game.BOARD_SQUARES[player.currentSquare].symbol == "GravityWell":
        return False
    if Game.BOARD_SQUARES[player.currentSquare].symbol == "Monster" and Game.BOARD_SQUARES[player.currentSquare].monsterHealth > 0:
        return False
    if player.missNextTurn:
        return False
    player.wasPulledOrPushed = True
    return True


def draw_text(text, font, colour, location, center = True):  # Draws text centered on a location
    text_surface = font.render(text, True, colour)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    if center:
        WINDOW.blit(text_surface, (location[0] - (text_width/2), location[1] - (text_height/2)))
    else:
        WINDOW.blit(text_surface, location)


def draw_text_input(location = (960, 400), max_length = 300):  # Creates Text Input Visuals
    text_surface = SMALL_FONT.render(Game.USER_TEXT, True, ORANGE)
    if text_surface.get_width() >= max_length:
        Game.CAN_TEXT_INPUT = False
    else:
        Game.CAN_TEXT_INPUT = True
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
        if Game.SHOW_HAND is not None and check_card_usable(card):
            card_usable = True
            card_rect = card_image.get_rect()
            card_rect.topleft = new_location
            if card_rect.collidepoint(pygame.mouse.get_pos()) and Game.LEFT_MOUSE_RELEASED:
                perform_card_action(card)
        Game.HOVER_BOXES.append(("card", card, card_image, new_location, card_usable))
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
        Game.HOVER_BOXES.append(("board symbol", desc_lines, image, new_location, desc_size, colour))
    WINDOW.blit(image, new_location)


def check_get_card(card_colour):
    mouse_pos = pygame.mouse.get_pos()
    if card_colour == CardType.BLUE:
        if BLUE_DRAW_DECK_RECT.collidepoint(mouse_pos) and Game.LEFT_MOUSE_RELEASED:
            card = Game.BLUE_DRAW_DECK.pop()
            Game.PLAYERS[Game.CURRENT_PLAYER].blueDeck.append(card)
            if Game.IS_MULTIPLAYER:
                Game.NETWORK.send(("PlayerBlueEvents", Game.PLAYERS[Game.CURRENT_PLAYER], Game.BLUE_DRAW_DECK, [(Game.PLAYERS[Game.CURRENT_PLAYER].playerName +
                                   " drew the " + card.displayName, Game.PLAYERS[Game.CURRENT_PLAYER].playerColour)]))
            Game.DISPLAYING_CARD = True
            return True
    else:
        if RED_DRAW_DECK_RECT.collidepoint(mouse_pos) and Game.LEFT_MOUSE_RELEASED:
            card = Game.RED_DRAW_DECK.pop()
            Game.PLAYERS[Game.CURRENT_PLAYER].redDeck.append(card)
            if Game.IS_MULTIPLAYER:
                Game.NETWORK.send(("PlayerRedEvents", Game.PLAYERS[Game.CURRENT_PLAYER], Game.RED_DRAW_DECK, [(Game.PLAYERS[Game.CURRENT_PLAYER].playerName +
                                   " drew the " + card.displayName, Game.PLAYERS[Game.CURRENT_PLAYER].playerColour)]))
            Game.DISPLAYING_CARD = True
            return True
    return False


def check_card_usable(card):
    if Game.PLAYERS[Game.CURRENT_PLAYER].missNextTurn: return False
    if card.cardType == CardType.BLUE:
        if Game.FORCED_CARD is not None: return False
        match card.cardValue:
            case CardValue.ACE:  # True if there is a non-Joker and non-Ace Card in the Discard Pile
                for card in Game.DISCARD_PILE:
                    if card.cardValue != CardValue.JOKER and card.cardValue != CardValue.ACE:
                        return True
            case CardValue.TWO:  # True anytime you need to roll a dice but not when in disadvantage or being controlled
                if (((Game.TURN_STAGE == TurnStage.ROLL_DICE and Game.PLAYERS[Game.CURRENT_PLAYER].setNextRoll is None) or
                     (Game.TURN_STAGE == TurnStage.MONSTER_ATTACK and Game.SUCCEEDED_DEFENCE is None) or
                     (Game.TURN_STAGE == TurnStage.SQUARE_ACTION and Game.BOARD_SQUARES[Game.PLAYERS[Game.CURRENT_PLAYER].currentSquare].symbol == "Back8" and
                      Game.FORCED_MOVEMENT) or
                     (Game.TURN_STAGE == TurnStage.ATTACK_MONSTER and D12.enabled)) and
                        (not Game.ROLLING_WITH_DISADVANTAGE and not Game.ROLLING_WITH_ADVANTAGE and not Game.ROLLING_DOUBLE)):
                    return True
            case CardValue.THREE:  # Always True
                return True
            case CardValue.FOUR:  # True anytime you are about to roll for damage
                if Game.TURN_STAGE == TurnStage.ATTACK_MONSTER and D12.enabled and D12_2.enabled and not Game.TAKING_FOUR:
                    return True
            case CardValue.FIVE:  # True if there is another player that hasn't got their next dice set
                for player in Game.PLAYERS:
                    if Game.IS_MULTIPLAYER:
                        if player.playerNumber != Game.PLAYER_NUMBER and player.setNextRoll is None:
                            return True
                    else:
                        if player != Game.PLAYERS[Game.CURRENT_PLAYER] and player.setNextRoll is None:
                            return True
                return False
            case CardValue.SIX:  # True when about to force movement
                return Game.FORCED_MOVEMENT
            case CardValue.SEVEN:
                return True
            case CardValue.EIGHT:  # Never True, Uses Automatically
                return False
            case CardValue.NINE:  # True before movement
                if Game.TURN_STAGE == TurnStage.ROLL_DICE:
                    return True
            case CardValue.TEN:  # Never True (Card Uses Automatically)
                return False
            case CardValue.JACK:  # True anytime you are about to roll for movement but not when in advantage or disadvantage
                if Game.TURN_STAGE == TurnStage.ROLL_DICE and not Game.ROLLING_WITH_ADVANTAGE and not Game.ROLLING_WITH_DISADVANTAGE:
                    return True
            case CardValue.KING:
                return True
            case CardValue.QUEEN:  # True anytime you need to draw Red Cards
                for card_type in Game.CARDS_TO_DRAW:
                    if card_type == CardType.RED:
                        return True
            case CardValue.JOKER:
                return True
    else:
        match card.cardValue:
            case CardValue.ACE:
                return True
            case CardValue.TWO:
                return Game.FORCED_CARD == CardValue.TWO
            case CardValue.THREE:
                return Game.FORCED_CARD == CardValue.THREE
            case CardValue.FOUR:
                return Game.FORCED_CARD == CardValue.FOUR
            case CardValue.FIVE:
                return Game.FORCED_CARD == CardValue.FIVE
            case CardValue.SIX:
                return Game.FORCED_CARD == CardValue.SIX
            case CardValue.SEVEN:
                return True
            case CardValue.EIGHT:
                return Game.FORCED_CARD == CardValue.EIGHT
            case CardValue.NINE:
                return Game.FORCED_CARD == CardValue.NINE
            case CardValue.TEN:
                return True
            case CardValue.JACK:
                return Game.FORCED_CARD == CardValue.JACK
            case CardValue.KING:
                return True
            case CardValue.QUEEN:
                return Game.FORCED_CARD == CardValue.QUEEN
            case CardValue.JOKER:
                return True
    return False


def perform_card_action(card):
    current_player = Game.PLAYERS[Game.CURRENT_PLAYER]
    event_data = [(current_player.playerName + " Used the " + card.displayName, current_player.playerColour)]
    if card.cardType == CardType.BLUE:
        match card.cardValue:
            case CardValue.ACE:  # Swaps with the last non-Joker and non-Ace card in the Discard Pile
                for x in range(len(Game.DISCARD_PILE)):
                    if Game.DISCARD_PILE[len(Game.DISCARD_PILE) - (x + 1)].cardValue != CardValue.JOKER and Game.DISCARD_PILE[len(Game.DISCARD_PILE) - (x + 1)].cardValue != CardValue.ACE:
                        new_card = Game.DISCARD_PILE.pop()
                        if new_card.cardType == CardType.BLUE:
                            current_player.blueDeck.append(new_card)
                        else:
                            current_player.redDeck.append(new_card)
                        if Game.IS_MULTIPLAYER:
                            event_data.append((current_player.playerName + " got the " + new_card.displayName, current_player.playerColour))
                        break
            case CardValue.TWO:  # Rolls dice with advantage
                Game.ROLLING_WITH_ADVANTAGE = True
            case CardValue.THREE:  # Open menu for choosing another player and give all others a Red Card
                if Game.PLAYER_COUNT > 3: Game.CHOOSE_PLAYERS = "Blue Three"
                else:
                    player_cards = []
                    for player in Game.PLAYERS:
                        if player != Game.PLAYERS[Game.CURRENT_PLAYER]:
                            new_card = Game.RED_DRAW_DECK.pop()
                            player.redDeck.append(new_card)
                            player_cards.append((player, new_card))
                    if Game.IS_MULTIPLAYER:
                        for player_card in player_cards:
                            event_data.append((player_card[0].playerName + " got the " + player_card[1].displayName, player_card[0].playerColour))
                        Game.NETWORK.send(("PlayersRed", Game.PLAYERS, Game.RED_DRAW_DECK))
            case CardValue.FOUR:
                Game.ADDING_FOUR = True
                D4.enabled = True
            case CardValue.FIVE:
                Game.CHOOSE_PLAYERS = "Blue Five"
            case CardValue.SIX:
                Game.FORCED_MOVEMENT = False
            case CardValue.SEVEN:
                print("Card Used: " + card.displayName)
            case CardValue.EIGHT:
                print("Card Used: " + card.displayName)
            case CardValue.NINE:  # Tells the player to click on a square and place a magic barrier there
                Game.CHOOSE_SQUARE = "Blue Nine"
            case CardValue.TEN:
                print("Card Used: " + card.displayName)
            case CardValue.JACK:
                Game.ROLLING_DOUBLE = True
            case CardValue.KING:
                print("Card Used: " + card.displayName)
            case CardValue.QUEEN:  # Removes the need to draw any Red Cards
                while CardType.RED in Game.CARDS_TO_DRAW:
                    Game.CARDS_TO_DRAW.remove(CardType.RED)
                print("Card Used: " + card.displayName)
            case CardValue.JOKER:
                print("Card Used: " + card.displayName)
        Game.CARD_TO_REMOVE = (current_player.blueDeck, card, True)
    else:
        match card.cardValue:
            case CardValue.ACE:
                print("Card Used: " + card.displayName)
            case CardValue.TWO:
                Game.FORCED_CARD = None
                Game.ROLLING_WITH_DISADVANTAGE = True
                print("Card Used: " + card.displayName)
            case CardValue.THREE:
                Game.FORCED_CARD = None
                if Game.PLAYER_COUNT > 3: Game.CHOOSE_PLAYERS = "Red Three"
                else:
                    player_cards = []
                    for player in Game.PLAYERS:
                        if player != Game.PLAYERS[Game.CURRENT_PLAYER]:
                            new_card = Game.BLUE_DRAW_DECK.pop()
                            player.blueDeck.append(new_card)
                            player_cards.append((player, new_card))
                    if Game.IS_MULTIPLAYER:
                        for player_card in player_cards:
                            event_data.append((player_card[0].playerName + " got the " + player_card[1].displayName, player_card[0].playerColour))
                        Game.NETWORK.send(("PlayersBlue", Game.PLAYERS, Game.BLUE_DRAW_DECK))
            case CardValue.FOUR:
                Game.FORCED_CARD = None
                Game.TAKING_FOUR = True
                D4.enabled = True
            case CardValue.FIVE:
                Game.FORCED_CARD = None
                Game.CHOOSE_PLAYERS = "Red Five"
            case CardValue.SIX:
                Game.FORCED_CARD = None
                Game.BONUS_MOVEMENT = False
            case CardValue.SEVEN:
                print("Card Used: " + card.displayName)
            case CardValue.EIGHT:
                Game.FORCED_CARD = None
                Game.SUCCEEDED_DEFENCE = False
            case CardValue.NINE:
                Game.FORCED_CARD = None
                if Game.IS_MULTIPLAYER:
                    Game.SQUARE_VOTE = Game.NETWORK.send("StartSquareVote")
                else:
                    Game.CHOOSE_SQUARE = "Red Nine"
            case CardValue.TEN:
                print("Card Used: " + card.displayName)
            case CardValue.JACK:
                Game.FORCED_CARD = None
                Game.ROLLING_WITH_FOUR = True
                D4.enabled = True
            case CardValue.KING:
                print("Card Used: " + card.displayName)
            case CardValue.QUEEN:
                Game.FORCED_CARD = None
                while CardType.BLUE in Game.CARDS_TO_DRAW:
                    Game.CARDS_TO_DRAW.remove(CardType.BLUE)
            case CardValue.JOKER:
                print("Card Used: " + card.displayName)
        Game.CARD_TO_REMOVE = (current_player.redDeck, card, True)
    Game.DISCARD_PILE.append(card)
    if Game.IS_MULTIPLAYER:
        Game.NETWORK.send(("DiscardEvents", Game.DISCARD_PILE, event_data))
    Game.SHOW_HAND = None
    Game.CARD_HANDS_ACTIVE = True


def check_hover_boxes():
    for hover_box in Game.HOVER_BOXES:
        if hover_box[0] == "card":
            card_rect = hover_box[2].get_rect()
            card_rect.topleft = hover_box[3]
            mouse_pos = pygame.mouse.get_pos()
            if card_rect.collidepoint(mouse_pos):
                rect_size = hover_box[1].descRectSize
                desc_lines = hover_box[1].descLines
                if Game.SHOW_HAND is not None:
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
    for square in Game.BOARD_SQUARES:
        if square.currentRect.collidepoint(pygame.mouse.get_pos()) and Game.LEFT_MOUSE_RELEASED:
            return square
    return None


def display_debug_info():
    if DEBUG_MODE:
        for x in range(len(Game.DEBUG_INFO)):
            draw_text(Game.DEBUG_INFO[x][0], TINY_FONT, Game.DEBUG_INFO[x][1], (10, 10 + (20 * x)), False)


def main():  # Game Loop
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        Game.HOVER_BOXES.clear()
        Game.DEBUG_INFO.clear()
        if Game.CURRENT_STATE == ScreenState.PLAYING_GAME:
            Game.DEBUG_INFO.append((str(Game.TURN_STAGE), BLACK))
            Game.DEBUG_INFO.append(("Rolling with Advantage: " + str(Game.ROLLING_WITH_ADVANTAGE), BLACK))
            Game.DEBUG_INFO.append(("Rolling with Disadvantage: " + str(Game.ROLLING_WITH_DISADVANTAGE), BLACK))
            Game.DEBUG_INFO.append(("Rolling Double: " + str(Game.ROLLING_DOUBLE), BLACK))
            Game.DEBUG_INFO.append(("Adding Four: " + str(Game.ADDING_FOUR), BLACK))
            Game.DEBUG_INFO.append(("Taking Four: " + str(Game.TAKING_FOUR), BLACK))
            Game.DEBUG_INFO.append(("Shield Active: " + str(Game.SHIELD_ACTIVE), BLACK))
            Game.DEBUG_INFO.append(("Forced Movement: " + str(Game.FORCED_MOVEMENT), BLACK))
            Game.DEBUG_INFO.append(("D4: " + str(D4.enabled), BLACK))
            Game.DEBUG_INFO.append(("D6 One: " + str(D6.enabled), BLACK))
            Game.DEBUG_INFO.append(("D6 Two: " + str(D6_2.enabled), BLACK))
            Game.DEBUG_INFO.append(("D12 One: " + str(D12.enabled), BLACK))
            Game.DEBUG_INFO.append(("D12 Two: " + str(D12_2.enabled), BLACK))
            Game.DEBUG_INFO.append(("D20 One: " + str(D20.enabled), BLACK))
            Game.DEBUG_INFO.append(("D20 Two: " + str(D20_2.enabled), BLACK))
            Game.DEBUG_INFO.append(("Dice Rolled: " + str(Game.DICE_ROLLED), BLACK))
            Game.DEBUG_INFO.append(("Displaying Card: " + str(Game.DISPLAYING_CARD), BLACK))
            Game.DEBUG_INFO.append(("Cards to Draw: " + str(len(Game.CARDS_TO_DRAW)), BLACK))
            Game.DEBUG_INFO.append(("Discard Pile Size: " + str(len(Game.DISCARD_PILE)), BLACK))
            for card in Game.DISCARD_PILE:
                Game.DEBUG_INFO.append((card.displayName, BLACK))
            Game.DEBUG_INFO.append(("Player Turn Order:", BLACK))
            for player in Game.PLAYERS:
                text = player.playerName
                if player.setNextRoll is not None:
                    text += " Next Roll: " + str(player.setNextRoll)
                if player == Game.PLAYERS[Game.CURRENT_PLAYER]:
                    text += " -"
                Game.DEBUG_INFO.append((text, player.playerColour))
                for blue_card in player.blueDeck:
                    Game.DEBUG_INFO.append((blue_card.displayName, BLACK))
                for red_card in player.redDeck:
                    Game.DEBUG_INFO.append((red_card.displayName, BLACK))
        # Game Events
        Game.LEFT_MOUSE_RELEASED = False
        Game.LEFT_ARROW_DOWN = False
        Game.RIGHT_ARROW_DOWN = False
        Game.TEXT_CONFIRMED = False
        for event in pygame.event.get():  # Event Handler
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Game.LEFT_MOUSE_RELEASED = True
            elif event.type == BUTTON_COOLDOWN_EVENT:
                Game.BUTTONS_ENABLED = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Game.LEFT_ARROW_DOWN = True
                elif event.key == pygame.K_RIGHT:
                    Game.RIGHT_ARROW_DOWN = True
                if event.key in ALLOWED_KEYS:
                    if event.key == pygame.K_BACKSPACE:
                        Game.USER_TEXT = Game.USER_TEXT[:-1]
                    elif event.key == pygame.K_RETURN:
                        Game.TEXT_CONFIRMED = True
                    elif Game.CAN_TEXT_INPUT:
                        Game.USER_TEXT += event.unicode
        draw_window()
        display_debug_info()
        pygame.display.update()
        if Game.CARD_TO_REMOVE is not None:
            Game.CARD_TO_REMOVE[0].remove(Game.CARD_TO_REMOVE[1])
            if Game.IS_MULTIPLAYER:
                if Game.CARD_TO_REMOVE[2]:
                    Game.NETWORK.send(("Player", Game.PLAYERS[Game.CURRENT_PLAYER]))
            Game.CARD_TO_REMOVE = None


if __name__ == "__main__":
    main()
