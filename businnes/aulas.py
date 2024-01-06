import os
import json

def load_aulas_json():
    try:
        with open(os.path.join("data", "aulas.json"), 'r') as aulas_json:
            lista_aulas = json.load(aulas_json)
            print("La lista de aulas ha sido cargada")
            return lista_aulas
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

lista_aulas = load_aulas_json()

def crear_aula():
    nombre_aula = input("Ingrese el nombre del aula: ")
    capacidad_maxima = int(input("Ingrese la capacidad máxima del aula: "))
    asignar_ruta = input("Ingrese la ruta de entrenamiento asignada al aula: ")

    aula = {
        'nombre': nombre_aula,
        'capacidad_maxima': capacidad_maxima,
        'capacidad_actual': 0,
        'ruta_asignada': asignar_ruta
    }

    lista_aulas.append(aula)
    print("Se creó el aula con éxito")
    guardar_json_aulas()

def guardar_json_aulas():
    try:
        with open(os.path.join("data", "aulas.json"), 'w') as aulas_json:
            json.dump(lista_aulas, aulas_json, indent=2)
            print("La lista de aulas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya aulas guardadas.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")

def listar_aulas():
    print("Listado de aulas de entrenamiento: ")
    for aula in lista_aulas:
        print(aula)

