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
    def test_minimoElemtosUnNumero(self):
        self.assertEqual(Estadistica().minimoElementos("1"), 1, "Un numero")
    def test_minimoElemtosDosNumeros(self):
        self.assertEqual(Estadistica().minimoElementos("1,2"), 1, "Dos numeros")
    def test_minimoElemtosNNumeros(self):
        self.assertEqual(Estadistica().minimoElementos("4,3,1,2"), 1, "N numeros")

    def test_maximoElemtos(self):
        self.assertEqual(Estadistica().maximoElementos(""), 0, "Cadena vacia")
