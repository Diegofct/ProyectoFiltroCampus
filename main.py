from commons.utils import limpiar_pantalla
from commons.menus import menu_principal,menu_trainers,menu_campers,menu_matriculas,menu_aulas,menu_reportes,menu_rutas_entrenamiento
from businnes.campers import crear_camper,listar_campers
from businnes.rutasEntrenamiento import rutas_entrenamiento, listar_rutas


# funtions
def campers():      
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
       crear_camper()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       listar_campers()
       input("Clic cualquier teclas [continuar]: ")

def rutas_entrenamiento():
   limpiar_pantalla()
   op=menu_rutas_entrenamiento()
   if op==1:
       listar_rutas()
       input("Clic cualquier teclas [continuar]: ")

def trainers():
    limpiar_pantalla()    
    op=menu_trainers()

def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()

def aulas():
    limpiar_pantalla()    
    op=menu_aulas()

def reportes():
    limpiar_pantalla()    
    op=menu_reportes()


#start
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
       print("Saliendo")
       break
       