import socket
from _thread import *
from Player import Player
import pickle
from Properties import *
import sys


class Server:
    """Class used as server which sends and receives data from one player to another.

    Attributes:
        disconnected (int): number of disconnected players
        number_of_players (int): number of players online
        port (int): game system port
        players (list): two element list of players

    """

    def __init__(self):
        self.disconnected = 0
        self.number_of_players = 0
        self.port = 5555
        self.players = [Player(100, 80, player_width, player_height),
                        Player(700, 100, player_width, player_height)]

    def run(self):
        """Starts the server."""

        f = open("server.txt", "r")
        address_s = f.read().split('#')
        server = str(address_s[0])
        print(server)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # (IPV4, TCP)
        try:
            s.bind((server, self.port))
        except socket.error as e:
            str(e)

        s.listen(2)
        print("Waiting for a connection, Server started")

        while True:
            conn, addr = s.accept()
            print("Connected to:", addr)
            start_new_thread(self.threaded_client, (conn, self.number_of_players))
            self.number_of_players += 1
            if self.number_of_players == 2:
                while True:
                    if self.disconnected == 2:
                        exit()
                    pass

    def threaded_client(self, conn, player, ):
        """A thread that deals with the exchange of data between a single player and a server.

        Arguments:
            conn (conn): argument returned by s.accept() function. Represents connection.
            player (class): player instance

        """

        self.players[player].num_of_players = self.number_of_players
        conn.send(pickle.dumps(self.players[player]))
        while True:
            try:
                data = pickle.loads(conn.recv(2048))
                self.players[player] = data

                if not data:
                    break
                else:
                    if player == 1:
                        reply = self.players[0]
                    else:
                        reply = self.players[1]

                conn.sendall(pickle.dumps(reply))
            except:
                break

        print("Connection lost!")
        self.disconnected += 1
        sys.exit()


if __name__ == "__main__":
    Server().run()
