from unittest import TestCase

from Estadistica import Estadistica

class TestEstadistica(TestCase):

    def test_numeroElementos(self):
        self.assertEqual(Estadistica().numeroElementos( "" ),0,"Cadena vacia")
    def test_numeroElementosUnNumero(self):
        self.assertEqual(Estadistica().numeroElementos("1"), 1, "Un numero")
    def test_numeroElementosDosNumeros(self):
        self.assertEqual(Estadistica().numeroElementos("1,2"), 2, "Dos numeros")
    def test_numeroElementosNnumeros(self):
        self.assertEqual(Estadistica().numeroElementos("1,2,4,7,6,3"), 6, "N numeros")

    def test_minimoElemtos(self):
        self.assertEqual(Estadistica().minimoElementos(""), 0, "Cadena vacia")