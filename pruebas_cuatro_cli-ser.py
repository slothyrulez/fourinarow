#! -*- coding:utf-8 -*-

from CuatroEnRaya import (Ficha, Jugada, Tablero,
                            Jugador, Partida)


import socket
import threading
import sys

def cuatro_server():
    print "SERVER"
def cuatro_client():
    print "CLIENT"
if __name__ == "__main__":
    if sys.argv[1] == "server":
        cuatro_server()
    else:
        cuatro_client()
        