import os
import json

def load_json_trainers():
    try:
        with open(os.path.join("data", "trainers.json"), 'r') as trainers_json:
            lista_trainers = json.load(trainers_json)
            print("La lista de trainers ha sido cargada")
            return lista_trainers
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

lista_trainers = load_json_trainers()

def crear_trainer():
    identificacion = int(input("Ingrese el número de identificación del trainer: "))
    nombre = input("Ingrese el nombre del profesor: ")
    apellidos = input("Ingrese los apellidos del profesor: ")
    edad = int(input("Ingrese la edad del profesor: "))
    profesion = input("¿Cuál es la profesión del profesor?: ")
    
    jornada_manana = {'Primera clase': '6:00 am - 10:00 am', 'Segunda clase': '10:00 am - 2:00 pm'}
    jornada_tarde = {'Primera clase': '2:00 pm - 6:00 pm', 'Segunda clase': '6:00 pm - 10:00 pm'}

    horario = {
        'Jornada Mañana': jornada_manana,
        'Jornada Tarde': jornada_tarde
    }

    trainer = {
        'id': identificacion,
        'Nombre': nombre,
        'Apellidos': apellidos,
        'Edad': edad,
        'Profesion': profesion,
        'Horario': horario
    }

    lista_trainers.append(trainer)

    print("Se ha registrado el trainer correctamente:")
    guardar_json_trainers()

    return trainer

def guardar_json_trainers():
    try:
        with open(os.path.join("data", "trainers.json"), 'w') as trainers_json:
            json.dump(lista_trainers, trainers_json, indent=2)
            print("La lista de trainers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya trainers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")


def ver_lista_trainers():
    print("Lista de trainers:")
    for trainer in lista_trainers:
        print(trainer)