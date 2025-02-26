import math
from decimal import Decimal
jugadores = ["Sancet", "Lewandowski", "Niko"]
equipo = ("FC Barcelona", "Borussia Dortmund")
balones_perdidos = [8.1]
goles_liga = [20]
minutos_partido = Decimal(78.71)
goleador_liga ={
		"nombre" : "Robert Lewandowski",
		"edad" : 36,
		"nacionalidad" : "polaco",
		"equipo" : "FC Barcelona"
		}

print("Redondear el flotador hacia arriba:",math.ceil(balones_perdidos[0]), "\n")

print("Obtener la raíz cuadrada del flotador:", math.sqrt(balones_perdidos[0]), "\n")

print("Primer elemento del diccionario:", goleador_liga["nombre"], "\n")

print("Segundo elemento de la tupla:", equipo[1], "\n")

jugadores.append('Lamine')

print("Agregar elemento al final de la lista:", jugadores, "\n")		
								 
jugadores[0] = "Wiliams"

print("Reemplazar el primer elemento de la lista:", jugadores, "\n")

jugadores.sort()

print("Ordenar la lista alfabéticamente:", jugadores, "\n")

equipo += ("Bayern Múnich",)

print("Agregar elemento a la tupla:", equipo)
















