#! -*- coding:utf-8 -*-

from CuatroEnRaya import (Ficha, Jugada, Tablero,
                            Jugador, Partida)

f1 = Ficha("white")
j1 = Jugador(f1)

f2 = Ficha("black")
j2 = Jugador(f2)

p = Partida(j1,j2)

for c in xrange(p.tablero.h):
    print c, p.tablero.h
    for f in xrange(p.tablero.w):
        print f, p.tablero.w
        if (c % 2) > 0:
            j = Jugada(c, j1)
        else:
            j = Jugada(c, j2)
        res = p.juegaTurno(j)
        if not res:
            if p.finPartida(j):
               raise Exception

        print p.tablero
        
            