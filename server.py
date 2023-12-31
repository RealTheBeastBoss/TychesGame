import socket
from _thread import *
import pickle
from player import Player
import statistics

port = 5555


class Server:
    sock = None
    client_addresses = []
    added_players = 0
    player_count = 0
    players = []
    current_player = 0
    current_player_to_update = []
    players_to_update = []
    board_to_update = []
    red_cards_to_update = []
    blue_cards_to_update = []
    discards_to_update = []
    board_squares = []
    discard_pile = []
    red_cards = []
    blue_cards = []
    event_to_send = []
    square_vote_to_send = []
    square_votes = []
    games_to_quit = []


def threaded_client(conn, ip):
    while True:  # Send and Receive Data
        try:
            data = pickle.loads(conn.recv(2048*10))
            if not data:
                print(ip[0] + " Disconnected")
                break
            else:  # Update Players, Update Card Piles, Update Board Squares, Card Actions
                if data == "?":  # Check if Game is Starting
                    if Server.added_players == Server.player_count:
                        data = [Server.players, Server.red_cards, Server.blue_cards]  # Sends the Players and Card Piles
                    else:
                        data = False
                elif data == "!":  # Check for Updates
                    data = {}
                    if ip in Server.current_player_to_update:
                        data["curr_player"] = Server.current_player
                        Server.current_player_to_update.remove(ip)
                    if ip in Server.players_to_update:
                        data["players"] = Server.players
                        Server.players_to_update.remove(ip)
                    if ip in Server.board_to_update:
                        data["board"] = Server.board_squares
                        Server.board_to_update.remove(ip)
                    if ip in Server.discards_to_update:
                        data["discard"] = Server.discard_pile
                        Server.discards_to_update.remove(ip)
                    if ip in Server.red_cards_to_update:
                        data["red"] = Server.red_cards
                        Server.red_cards_to_update.remove(ip)
                    if ip in Server.blue_cards_to_update:
                        data["blue"] = Server.blue_cards
                        Server.blue_cards_to_update.remove(ip)
                    if Server.event_to_send:
                        if ip in Server.event_to_send[1]:
                            data["events"] = Server.event_to_send[0]
                            Server.event_to_send[1].remove(ip)
                    if ip in Server.square_vote_to_send:
                        data["square_vote"] = 1
                        Server.square_vote_to_send.remove(ip)
                    if ip in Server.games_to_quit:
                        data["quit"] = 1
                        Server.games_to_quit.remove(ip)
                elif data == "End Turn":  # Ends the Player's Turn
                    print("From " + ip[0] + ", Received End Turn")
                    if Server.current_player == Server.player_count - 1:
                        Server.current_player = 0
                    else:
                        Server.current_player += 1
                    Server.current_player_to_update = Server.client_addresses.copy()
                    Server.current_player_to_update.remove(ip)
                    data = Server.current_player
                elif data == "StartSquareVote":
                    print("From " + ip[0] + ", Received Start of a Square Vote")
                    Server.square_vote_to_send = Server.client_addresses.copy()
                    Server.square_vote_to_send.remove(ip)
                    data = True
                elif data == "quit":
                    print("From " + ip[0] + ", Received Quit Game")
                    Server.games_to_quit = Server.client_addresses.copy()
                    Server.games_to_quit.remove(ip)
                    data = False
                elif data[0] == "PlayersRedEvents":
                    print("From " + ip[0] + ", Received: " + str(data))
                    Server.players = data[1]
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    Server.red_cards = data[2]
                    Server.red_cards_to_update = Server.client_addresses.copy()
                    Server.red_cards_to_update.remove(ip)
                    Server.event_to_send = [data[3], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "PlayersBlueEvents":
                    print("From " + ip[0] + ", Received: " + str(data))
                    Server.players = data[1]
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    Server.blue_cards = data[2]
                    Server.blue_cards_to_update = Server.client_addresses.copy()
                    Server.blue_cards_to_update.remove(ip)
                    Server.event_to_send = [data[3], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "PlayerBlueEvents":
                    print("From " + ip[0] + ", Received: " + str(data))
                    player = data[1]
                    player_num = player.playerNumber
                    Server.players[player_num] = player
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    Server.blue_cards = data[2]
                    Server.blue_cards_to_update = Server.client_addresses.copy()
                    Server.blue_cards_to_update.remove(ip)
                    Server.event_to_send = [data[3], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "PlayerRedEvents":
                    print("From " + ip[0] + ", Received: " + str(data))
                    player = data[1]
                    player_num = player.playerNumber
                    Server.players[player_num] = player
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    Server.red_cards = data[2]
                    Server.red_cards_to_update = Server.client_addresses.copy()
                    Server.red_cards_to_update.remove(ip)
                    Server.event_to_send = [data[3], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "PlayersBlue":
                    print("From " + ip[0] + ", Received: " + str(data))
                    Server.players = data[1]
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    Server.blue_cards = data[2]
                    Server.blue_cards_to_update = Server.client_addresses.copy()
                    Server.blue_cards_to_update.remove(ip)
                    data = False
                elif data[0] == "PlayersRed":
                    print("From " + ip[0] + ", Received: " + str(data))
                    Server.players = data[1]
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    Server.red_cards = data[2]
                    Server.red_cards_to_update = Server.client_addresses.copy()
                    Server.red_cards_to_update.remove(ip)
                    data = False
                elif data[0] == "PlayerEvents":
                    print("From " + ip[0] + ", Received: " + str(data))
                    player = data[1]
                    player_num = player.playerNumber
                    Server.players[player_num] = player
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    Server.event_to_send = [data[2], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "PlayersEvents":
                    print("From " + ip[0] + ", Received: " + str(data))
                    Server.players = data[1]
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    Server.event_to_send = [data[2], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "SquareEvents":
                    print("From " + ip[0] + ", Received: " + str(data))
                    square = data[1][1]
                    square_num = data[1][0]
                    Server.board_squares[square_num] = square
                    Server.board_to_update = Server.client_addresses.copy()
                    Server.board_to_update.remove(ip)
                    Server.event_to_send = [data[2], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "Player":
                    print("From " + ip[0] + ", Received: " + str(data))
                    player = data[1]
                    player_num = player.playerNumber
                    Server.players[player_num] = player
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    data = False
                elif data[0] == "PlayerSquaresEvents":
                    print("From " + ip[0] + ", Received: " + str(data))
                    player = data[1]
                    player_num = player.playerNumber
                    Server.players[player_num] = player
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    for square in data[2]:
                        Server.board_squares[square[0]] = square[1]
                    Server.board_to_update = Server.client_addresses.copy()
                    Server.board_to_update.remove(ip)
                    Server.event_to_send = [data[3], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "PlayersSquaresEvents":
                    print("From " + ip[0] + ", Received: " + str(data))
                    Server.players = data[1]
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    for square in data[2]:
                        Server.board_squares[square[0]] = square[1]
                    Server.board_to_update = Server.client_addresses.copy()
                    Server.board_to_update.remove(ip)
                    Server.event_to_send = [data[3], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "PlayersSquaresDiscardEvents":
                    print("From " + ip[0] + ", Received: " + str(data))
                    Server.players = data[1]
                    Server.players_to_update = Server.client_addresses.copy()
                    Server.players_to_update.remove(ip)
                    for square in data[2]:
                        Server.board_squares[square[0]] = square[1]
                    Server.board_to_update = Server.client_addresses.copy()
                    Server.board_to_update.remove(ip)
                    Server.discard_pile = data[3]
                    Server.discards_to_update = Server.client_addresses.copy()
                    Server.discards_to_update.remove(ip)
                    Server.event_to_send = [data[4], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "DiscardEvents":
                    print("From " + ip[0] + ", Received: " + str(data))
                    Server.discard_pile = data[1]
                    Server.discards_to_update = Server.client_addresses.copy()
                    Server.discards_to_update.remove(ip)
                    Server.event_to_send = [data[2], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "Events":
                    print("From " + ip[0] + ", Received: " + str(data))
                    Server.event_to_send = [data[1], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "SquareVote":
                    print("From " + ip[0] + ", Received: " + str(data))
                    Server.square_votes.append(data[1])
                    if len(Server.square_votes) == Server.player_count - 1:
                        mode = statistics.mode(Server.square_votes)
                        Server.board_squares[mode].hasBarrier = True
                        Server.board_to_update = Server.client_addresses.copy()
                        Server.square_votes.clear()
                    Server.event_to_send = [data[2], Server.client_addresses.copy()]
                    Server.event_to_send[1].remove(ip)
                    data = False
                elif data[0] == "Name":  # Creates a Player
                    print("From " + str(ip[0]) + ", Received Player Name: " + str(data[1]))
                    Server.players.append(Player(Server.added_players, data[1]))
                    data = (Server.added_players, Server.player_count)  # Sends Player Number and Player Count
                    Server.added_players += 1
                if data:
                    print("Sending " + str(data) + " to " + ip[0])
                conn.sendall(pickle.dumps(data))
        except error:
            break
    print(ip[0] + " Lost Connection")
    conn.close()


def check_server(server):
    Server.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        Server.sock.bind((server, port))
        return True
    except socket.error:
        return False


def start_server(count, server, game_board, red_cards, blue_cards):
    Server.player_count = count
    Server.board_squares = game_board
    Server.red_cards = red_cards
    Server.blue_cards = blue_cards
    Server.sock.listen(Server.player_count)
    print("Waiting for Connection, Server Started at " + server)
    while True:
        connect, addr = Server.sock.accept()
        print(addr[0] + " has Connected")
        Server.client_addresses.append(addr)
        start_new_thread(threaded_client, (connect, addr))


def close_server():
    Server.sock.close()
