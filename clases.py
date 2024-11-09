class Detector:
    esPositivo = True
    esNegativo = False

    def __init__(self,esPositvo,esNegativo):
        self.esPositivo = esPositvo
        self.esNegativo = esPositvo

    def detectar_mutantes()


# 1.
# class Detector:
#     def __init__(self, adn):
#         self.adn = adn  # La matriz de ADN
#         self.mutante = False  # Estado de si es mutante o no

#     def detectar_mutantes(self):
#         # Método principal que detectará mutaciones
#         return self.detectar_horizontal() or self.detectar_vertical() or self.detectar_diagonal()

#     def detectar_horizontal(self):
#         # Implementar detección horizontal de mutantes
#         pass

#     def detectar_vertical(self):
#         # Implementar detección vertical de mutantes
#         pass

#     def detectar_diagonal(self):
#         # Implementar detección diagonal de mutantes
#         pass

# Nacho esto:
# class Detector:
#     def __init__(self, matriz):
#         self.matriz = matriz

#     def detectar_mutantes(self):
#         """Verificar si hay mutaciones en la matriz (horizontal, vertical, diagonal)."""
#         return self._verificar_horizontal() or self._verificar_vertical() or self._verificar_diagonal()

#     def _verificar_horizontal(self):
#         """Verificar mutaciones horizontales."""
#         for fila in self.matriz:
#             if fila.count(fila[0]) >= 4:
#                 return True
#         return False

#     def _verificar_vertical(self):
#         """Verificar mutaciones verticales."""
#         for col in range(6):
#             columna = "".join([fila[col] for fila in self.matriz])
#             if columna.count(columna[0]) >= 4:
#                 return True
#         return False

#     def _verificar_diagonal(self):
#         """Verificar mutaciones diagonales."""
#         for i in range(3):  # Limitarse a las primeras 3 filas
#             for j in range(3):  # Limitarse a las primeras 3 columnas
#                 diagonal = "".join([self.matriz[i+k][j+k] for k in range(4)])
#                 if diagonal.count(diagonal[0]) >= 4:
#                     return True
#         return False

# class Mutador:
#     def __init__(self, base_nitrogenada, matriz):
#         self.base_nitrogenada = base_nitrogenada
#         self.matriz = matriz

#     def crear_mutante(self, tipo, posicion, orientacion=None):
#         """Crear una mutación en la matriz."""
#         if tipo == "horizontal":
#             return self._mutar_horizontal(posicion)
#         elif tipo == "vertical":
#             return self._mutar_vertical(posicion)
#         elif tipo == "diagonal":
#             return self._mutar_diagonal(posicion)
#         return self.matriz

#     def _mutar_horizontal(self, posicion):
#         """Crear mutación horizontal."""
#         for i in range(4):
#             self.matriz[posicion[0]] = self.matriz[posicion[0][:posicion[1]] + self.base_nitrogenada + self.matriz[posicion[0][posicion[1] + 1:]]


#     def _mutar_vertical

