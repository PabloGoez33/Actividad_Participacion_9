from typing import Tuple

class DatosMeteorologicos:

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        
        temperatura = 0
        humedad = 0
        presion = 0
        velocidad_viento = 0
        direcciones_viento = []

        try:

            with open(self.nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    if linea.startswith("Temperatura:"):
                        temperatura += float(linea.split(":")[1].strip())
                    elif linea.startswith("Humedad:"):
                        humedad += float(linea.split(":")[1].strip())
                    elif linea.startswith("Presion:"):
                        presion += float(linea.split(":")[1].strip())
                    elif linea.startswith("Viento:"):
                        informacion_viento = linea.split(":")[1].strip().split(",")
                        velocidad_viento += float(informacion_viento[0])
                        direcciones_viento.append(informacion_viento[1])
            
            numero_registro = len(direcciones_viento)
            temperatura_promedio = temperatura / numero_registro
            humedad_promedio = humedad / numero_registro
            presion_promedio = presion / numero_registro
            velocidad_viento_promedio = velocidad_viento / numero_registro

            direccion_predominante_viento = calcular_direccion_predominante(direcciones_viento)

            return (temperatura_promedio, round(humedad_promedio, 2), presion_promedio, velocidad_viento_promedio, direccion_predominante_viento)
        
        except FileNotFoundError:
            print(f"El archivo {self.nombre_archivo} no fue encontrado.")
            return (0, 0, 0, 0, "")
        
def calcular_direccion_predominante(direcciones):
    
    direccion_grados = {
        "N": 0,
        "NNE": 22.5,
        "NE": 45,
        "ENE": 67.5,
        "E": 90,
        "ESE": 112.5,
        "SE": 135,
        "SSE": 157.5,
        "S": 180,
        "SSW": 202.5,
        "SW": 225,
        "WSW": 247.5,
        "W": 270,
        "WNW": 292.5,
        "NW": 315,
        "NNW": 337.5,
    }

    direcciones_en_grados = [direccion_grados[d] for d in direcciones]
    direcciones_promedio_en_grados = sum(direcciones_en_grados) / len(direcciones_en_grados)

    direcciones_posibles = list(direccion_grados.values())
    direccion_predominante_grados = min(direcciones_posibles, key=lambda x: abs(x - direcciones_promedio_en_grados))

    for direccion, grados in direccion_grados.items():
        if grados == direccion_predominante_grados:
            return direccion