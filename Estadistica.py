
class Estadistica:
    def numeroElementos(self, cadena):
        if (cadena == ""):
            return 0
        else:
            numeros = cadena.split(",")
            return len(numeros)

    def minimoElementos (self, cadena):
        if cadena == "":
            return 0
        else:
            numeros = cadena.split(",")
            numeros.sort()
            return int(numeros[0])

    def maximoElementos(self, cadena):
        if cadena == "":
            return 0
        else:
            numeros = cadena.split(",")
            numeros.sort()
            numeros.reverse()
            return int(numeros[0])

    def promedioElemntos(self,cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            return (int(cadena[0])+int(cadena[2]))/2
        else:
            return int(cadena)