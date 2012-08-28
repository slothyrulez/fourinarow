#! -*- coding:utf-8 -*-

import unittest
from CuatroEnRaya import (Ficha, Jugada, Tablero,
                            Jugador, Partida)

class TestJugador(unittest.TestCase):
    def setUp(self):
        fw = Ficha()
        self.ju = Jugador(fw, "Alex")

    def test_init_jugador(self):
        self.assertEquals(self.ju.nombre, "Alex")
        self.assertIsInstance(self.ju.ficha, Ficha)
        self.assertEquals(self.ju.movimientos, 0)
        self.assertEquals(self.ju.jugadas, [])

class TestFicha(unittest.TestCase):
    def test_init_color(self):
        fw = Ficha()
        fb = Ficha("red")
        self.assertEquals("X", fw.rep)
        self.assertNotEquals("X", fb.rep)

class TestJugada(unittest.TestCase):
    def setUp(self):
        self.f = Ficha()
        self.ju = Jugador(self.f, "Alex")
        self.j = Jugada(0,self.ju)
        
    def test_init_jugada(self):
        self.assertIsInstance(self.j.ficha,Ficha)

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.f = Ficha()
        self.ju = Jugador(self.f, "Alex")
        self.t = Tablero()
        
    def test_init_tablero(self):
        self.assertIsInstance(self.t, Tablero)
        
    def llenaTablero(self):
        for i in xrange(self.t.w):
            for j in xrange(self.t.h):
                self.t._inserta(Jugada(i,self.ju))
                
    def vaciaTablero(self):
        for i in xrange(self.t.w):
            for j in xrange(self.t.h):
               self.t.matrix[j][i] = None
               
    def test_lleno_tablero(self):
        self.llenaTablero()
        for i in xrange(self.t.w):
            for j in xrange(self.t.h):
                self.assertEquals(self.t.matrix[j][i], self.f)

    def test_no_caben(self):
        self.llenaTablero()
        for i in xrange(self.t.w):
            self.assertEquals(self.t._columnaLlena(Jugada(i,self.ju)),True)
            self.assertNotEquals(self.t._valida(Jugada(i, self.ju)),True)

    def test_tableroLleno(self):
        self.llenaTablero()
        self.assertEquals(self.t._tableroLleno(),True)
        self.vaciaTablero()
        self.assertEquals(self.t._tableroLleno(), False)

class TestPartida(unittest.TestCase):
    def setUp(self):
        self.f1 = Ficha()
        self.f2 = Ficha("black")
        self.j1 = Jugador(self.f1, "Player1")
        self.j2 = Jugador(self.f2, "Player2")
        self.t = Tablero()
        self.p = Partida(self.j1, self.j2)

    def test_init_partida(self):
        self.assertNotEquals(self.p.tablero._tableroLleno(), True)
        self.assertNotEquals(self.j1, self.j2)
        self.assertNotEquals(self.j1.ficha.rep, self.j2.ficha.rep)

    def test_partida_tablas(self):
        fin = False
        #while not fin:
        for f in xrange(self.t.h):
            for c in xrange(self.t.w):
                if (c + f) % 2: ##IMPAR
                    self.j = Jugada(c, self.j1)
                else: ## PAR
                    self.j = Jugada(c, self.j2)
                self.assertEquals(self.p.juegaTurno(self.j),True)
                fin = self.p.finPartida(self.j)
        self.assertEquals(self.p.tablas(), True)


    def test_partida_4raya(self):
        for f in xrange(self.t.h):
            for c in xrange(self.t.w):
                if (c + f) % 2: ##IMPAR
                    self.j = Jugada(f, self.j1)
                else: ## PAR
                    self.j = Jugada(c, self.j2)
                self.assertEquals(self.p.juegaTurno(self.j),True)
                fin = self.p.finPartida(self.j)
                print self.p.tablero, self.p.last, self.p.movimientos
                if self.p.movimientos == 13:
                    print "FIN: %s" % fin
                    self.assertEquals(fin, True)
                    break

        """
        PARTICA COMPLETA HATA TABLAS
        """
            
            
        
if __name__ == "__main__":
    unittest.main()

