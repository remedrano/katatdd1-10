
class Estadistica:
    def numeroElementos(self, cadena):
        if (cadena == ""):
            return 0
        elif len(cadena) > 3:
            numeros = cadena.split(",")
            cantidad = 0
            for num in numeros:
                cantidad += 1
            return cantidad
        elif ("," in cadena):
            return 2
        else:
            return 1