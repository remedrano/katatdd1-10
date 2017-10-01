
class Estadistica:
    def numeroElementos(self, cadena):
        if (cadena == ""):
            return 0
        else:
            numeros = cadena.split(",")
            cantidad = 0
            for num in numeros:
                cantidad += 1
            return cantidad

    def minimoElementos (self, cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            numeros = cadena.split(",")
            numeros.sort()
            return int(numeros[0])
        else:
            return int(cadena)