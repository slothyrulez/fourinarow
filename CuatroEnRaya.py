#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import pprint

class Ficha(object):
    def __init__(self, color="white"):
        self.color = color if color == "white" else "black"
        print self.color
        self.rep = self.__repr__()
        print self.rep


        
    def __repr__(self):
        if self.color == "white":
            return "X"
        else:
            return "0"

class Jugador(object):
    def __init__(self, ficha, nombre=""):
        self.nombre = nombre
        self.ficha = ficha
        self.movimientos = 0
        self.jugadas = []

    def __repr__(self):
        return "%s - %s - %s" % (self.nombre, self.ficha, self.ficha.rep)

    
class Jugada():
    def __init__(self, columna, jugador):
        self.columna = columna
        self.jugador = jugador
        self.ficha = jugador.ficha
        self.fila = None

    def __repr__(self):
        return "[%s](%s, %s)" % (self.ficha, self.fila, self.columna)

class Partida():
    def __init__(self, jugador1, jugador2):
        self.j1 = jugador1
        self.j2 = jugador2
        self.tablero = Tablero()
        self.last = None
        self.movimientos = 0

        
    def _actualizaDatos(self, jugada):
        self.last = jugada
        jugada.jugador.jugadas.append(jugada)
        self.movimientos += 1
        jugada.jugador.movimientos += 1
        #print "DATOS ACTUALIZADOS"

        
    def juegaTurno(self, jugada):
        if isinstance(jugada, Jugada):
            if ((self.last == None or jugada.jugador != self.last.jugador) and
                ( jugada.jugador == self.j1 or  jugada.jugador == self.j2 )):
                    if self.tablero.validaInserta(jugada):
                        self._actualizaDatos(jugada)
                        return True
        return False
        
    def cuatroRaya(self, jugada):
        return self.tablero.cuatroRaya(jugada)
        
    def tablas(self):
        return self.tablero._tableroLleno()
        
    def finPartida(self, jugada):
        return self.tablas() or self.cuatroRaya(jugada)
        
        
class Tablero(object):
    def __init__(self):
        self.w = 7
        self.h = 6
        self.matrix = []
        self.conecta = 4
        self._nuevoTablero()
        
    def _nuevoTablero(self):
        for x in range(self.h):
            self.matrix.append([None for y in range(self.w)])
        
    def __str__(self):
        return pprint.pformat(self.matrix)

        
    def _tableroLleno(self):
        for c in xrange(self.w):
            if self.matrix[0][c] == None or not isinstance(self.matrix[0][c], Ficha):
                return False
        return True

        
    def _inserta(self, jugada):
        for y in xrange(self.h-1, -1, -1):
            if not self.matrix[y][jugada.columna]:
                self.matrix[y][jugada.columna] = jugada.ficha
                jugada.ficha.fila = y
                #print "INSERTA %s EN F:%s C:%s" % (jugada.ficha, y, jugada.columna)
                break

    def _columnaLlena(self, jugada):
        return True if self.matrix[0][jugada.columna] != None else False

        
    def _valida(self, jugada):
        if type(jugada.columna) != int:
            return False
        if jugada.columna >= self.w:
            return False
        if self._columnaLlena(jugada):
            return False
        return True

        
    def validaInserta(self, jugada):
        if self._tableroLleno():
            return False
        if self._valida(jugada):
            self._inserta(jugada)
            return True
        return False

        
    def cuatroRaya(self, jugada):
        for f in xrange(self.h):
            for c in xrange(self.w):
                #print "F:%s C:%s" % (f,c)
                if (self._cuatroRaya(jugada.ficha, 0, 0, f, c) or
                    self._cuatroRaya(jugada.ficha, 0, 1, f, c) or
                    self._cuatroRaya(jugada.ficha, 0, 2, f, c) or
                    self._cuatroRaya(jugada.ficha, 0, 3, f, c)):
                    return True
        return False

        
    def _fueraTablero(self, fila, columna):
        if (fila < self.h and fila >= 0) and (columna < self.w and columna >= 0):
            return False
        else:
            #print "FUERA %s %s" % (fila, columna)
            return True

            
    def _fichaIncorrecta(self, ficha, fila, columna):
        if self.matrix[fila][columna] is None or ficha.rep != self.matrix[fila][columna].__getattribute__("rep"):
            return True
        else:
            return False

        
    def _cuatroRaya(self, ficha, profundidad, direccion, fila, columna):
        """
        PARTO DE LA POSICION 0,0
        """
        #print "PROFUNDIDAD %s" % profundidad
        if self._fueraTablero(fila, columna) or self._fichaIncorrecta(ficha, fila, columna):
            return False
        if profundidad == self.conecta-1:
            #print "DIREECION ", direccion
            return True
        if direccion == 0: ## ARR -> ABB
            return self._cuatroRaya(ficha, profundidad+1, direccion, fila+1, columna)
        if direccion == 1: ## IZQ -> DER
            return self._cuatroRaya(ficha, profundidad+1, direccion, fila, columna+1)
        if direccion == 2: ## DIAG IZQ -> DER
            return self._cuatroRaya(ficha, profundidad+1, direccion, fila+1, columna+1)
        if direccion == 3: ## DIAG DER -> IZQ
            return self._cuatroRaya(ficha, profundidad+1, direccion, fila+1, columna-1)
