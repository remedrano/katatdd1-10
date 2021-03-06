
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

    def promedioElemntos(self, cadena):
        if cadena == "":
            return 0
        else:
            numeros = cadena.split(",")
            suma = 0.0
            for num in numeros:
                suma += int(num)
            return suma / len(numeros)