from modelo.AP9 import DatosMeteorologicos

datos = DatosMeteorologicos("src/datos.txt")
estadisticas = datos.procesar_datos()
print(f"Temperatura promedio: {estadisticas[0]}")
print(f"Humedad promedio: {estadisticas[1]}")
print(f"Presion promedio: {estadisticas[2]}")
print(f"Velocidad promedio del viento: {estadisticas[3]}")
print(f"Direccion predominante del viento: {estadisticas[4]}")