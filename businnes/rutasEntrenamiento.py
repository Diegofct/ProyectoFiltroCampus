import os
import json

def load_rutas_json():
    try:
        with open(os.path.join("data", "rutasEntrenamiento.json"), 'r') as rutas_json:        
            lista_rutasEntrenamiento = json.load(rutas_json)
            print("La lista de rutas de entrenamiento ha sido cargada")
            return lista_rutasEntrenamiento
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

lista_rutasEntrenamiento = load_rutas_json()


def rutas_entrenamiento():
    cantidadRutas = 3
    for i in range(cantidadRutas):
        nombreRuta = input(f"Digite el nombre de la ruta {i}")

    ruta_nodejs = {
        "nombre": nombreRuta,
        "fundamentos": ["Introducción a la algoritmia", "PSeInt", "Python"],
        "programacion_web": ["HTML", "CSS", "Bootstrap"],
        "programacion_formal": ["JavaScript"],
        "bases_datos": ["MongoDb", "Postgresql"],
        "backend": ["NodeJS", "Express"]
    }

    ruta_java = {
        "nombre": nombreRuta,
        "fundamentos": ["Introducción a la algoritmia", "PSeInt", "Python"],
        "programacion_web": ["HTML", "CSS", "Bootstrap", "JavaScript"],
        "programacion_formal": ["Java"],
        "bases_datos": ["Mysql", "MongoDb"],
        "backend": ["Spring Boot"]
    }

    ruta_netcore = {
        "nombre": nombreRuta,
        "fundamentos": ["Introducción a la algoritmia", "PSeInt", "Python"],
        "programacion_web": ["HTML", "CSS", "JavaScript"],
        "programacion_formal": ["C#"],
        "bases_datos": ["Mysql", "MongoDb", "Postgresql"],
        "backend": ["NetCore"]
    }

    lista_rutasEntrenamiento.append(ruta_nodejs, ruta_java, ruta_netcore)
    guardar_json()


def guardar_json():
    try:
      with open(os.path.join("data", "campers.json"), 'w') as rutas_json:
        json.dump(lista_rutasEntrenamiento, rutas_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")


def listar_rutas():
    print("Listado de las rutas de entrenamiento: ")
    for ruta in lista_rutasEntrenamiento:
        print(ruta)
