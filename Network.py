import socket
import pickle


class Network:
    """Class contains all methods required to communication

    Attributes:
        client (socket): socket
        server (string): server address
        port (int): port number used for connection
        p: data packed by pickle

    """

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        f = open("server.txt", "r")
        address_s = f.read().split('#')
        self.server = str(address_s[0])
        print(self.server)
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self._connect()

    def get_p(self):
        """Returns data packed by pickle."""
        return self.p

    def _connect(self):
        # Tries to connect to player address

        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        """Tries to send data to player."""

        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
