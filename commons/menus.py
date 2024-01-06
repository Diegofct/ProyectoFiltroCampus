from commons.utils import validar_opcion

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Campers")
    print("2. Rutas de entrenamiento")
    print("3. Trainers")
    print("4. Matriculas")
    print("5. Aulas")
    print("6. Reportes")
    print("7. Salir")       
    op=validar_opcion("Opcion: ",1,7)
    return op

def menu_campers():
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. listar campers")
    print("3. Modificar campers")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_rutas_entrenamiento():
    print("----------- Menú rutas de entrenamiento-----------")
    print("1. Ver lista de rutas de entrenamiento")
    print("2. Salir")
    op=validar_opcion("Opcion: ",1,2)
    return op
    
def menu_trainers():
    print("----------- Menú Trainers-----------")
    print("1. Crear trainer")
    print("2. Buscar trainer")
    print("3. Modificar trainer")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_matriculas():
    print("----------- Menú Matriculas-----------")
    print("1. Crear Matriculas")
    print("2. Buscar Matriculas")
    print("3. Modificar Matriuclas")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_aulas():
    print("----------- Menú Aulas-----------")
    print("1. Crear Aulas")
    print("2. Buscar Aulas")
    print("3. Modificar Aulas")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_reportes():
    print("----------- Menú Reportes-----------")
    print("1. Listar campers estado inscripto")
    print("2. Listar campers aprobaron examen")
    print("3. Listar trainers trabajando en campus")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op