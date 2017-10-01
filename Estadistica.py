
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

    def minimoElementos(self, cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            if int(cadena[0]) < int(cadena[2]):
                return int(cadena[0])
            else:
                return int(cadena[2])
        else:
            return int(cadena)