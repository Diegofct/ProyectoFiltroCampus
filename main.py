from commons.utils import limpiar_pantalla
from commons.menus import menu_principal,menu_trainers,menu_campers,menu_matriculas,menu_aulas,menu_reportes,menu_rutas_entrenamiento
from businnes.campers import crear_camper,listar_campers, registrar_notas_prueba
from businnes.rutasEntrenamiento import rutas_entrenamiento
from businnes.aulas import crear_aula, listar_aulas
from businnes.trainers import crear_trainer, ver_lista_trainers
from businnes.matricula import realizar_matricula
from businnes.filtros import registrar_notas_filtro

def campers():      
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
       crear_camper()
       input("Presiona cualquier tecla para continuar: ")
    if op==2:
       listar_campers()
       input("Presiona cualquier tecla para continuar: ")
    if op==3:
       registrar_notas_prueba()
       input("Presiona cualquier tecla para continuar: ")

def rutas_entrenamiento():
   limpiar_pantalla()
   op=menu_rutas_entrenamiento()
   if op==1:
       rutas_entrenamiento()
       input("Presiona cualquier tecla para continuar: ")

def trainers():
    limpiar_pantalla()    
    op=menu_trainers()
    if op==1:
        crear_trainer()
        input("Presiona cualquier tecla para continuar: ")
    if op==2:
        ver_lista_trainers()
        input("Presiona cualquier tecla para continuar: ")

def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()
    if op==1:
        realizar_matricula()
        input("Presiona cualquier tecla para continuar: ")
    if op==2:
        registrar_notas_filtro()
        input("Presiona cualquier tecla para continuar: ")

def aulas():
    limpiar_pantalla()    
    op=menu_aulas()
    if op==1:
        crear_aula()
        input("Presiona cualquier tecla para continuar: ")
    if op==2:
        listar_aulas()
        input("Presiona cualquier tecla para continuar: ")
    
def reportes():
    limpiar_pantalla()    
    op=menu_reportes()


while True: 
   limpiar_pantalla()
   op=menu_principal()
   if  op==1:
       campers()
   elif op==2:
       rutas_entrenamiento()
   elif op==3:
       trainers()
   elif op==4:
       matriculas()
   elif op==5:
       aulas()
   elif op==6:
       reportes()
   elif op==7:
       print("Saliendo del programa, ¡Hasta luego!")
       break
       