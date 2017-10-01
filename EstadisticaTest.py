from unittest import TestCase

from Estadistica import Estadistica

class TestEstadistica(TestCase):

    def test_numeroElementos(self):
        self.assertEqual(Estadistica().numeroElementos( "" ),0,"Cadena vacia")
    def test_numeroElementosUnNumero(self):
        self.assertEqual(Estadistica().numeroElementos("1"), 1, "Un numero")