import socket
from commonthread import commonThread
ADDRESS = "localhost"
PORT = 6667


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ADDRESS, PORT))
    print("Server is listening at : ", PORT)
    clientthread = commonThread(ADDRESS, PORT, s)
    clientthread.start()


if __name__ == "__main__":
    main()
