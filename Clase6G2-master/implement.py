from datetime import date, time, datetime

from sistemaVet import *

clasegato = []
claseperro = []

def main():
    servicio_hospitalario = sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))

        if menu == 1:
            servicio_hospitalario.verNumeroMascotas()
            historia = int(input(" ingrese la historia clinica de la mascota: "))
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                if tipo == "felino":
                    clasegato = +1
                    if clasegato >= 7:
                        print("espacio insuficiente")
                        continue
                else:
                    claseperro = +1
                    if claseperro >= 7:
                        print("espacio insuficiente")
                        continue
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                medicamento=Medicamento()
                if medicamento.verific(medicamento) == False:
                    medicamento.asignarNombre(input("Ingrese nombre del medicamento: "))
                    medicamento.asignarDosis(int(input("Ingrese dosis del medicamento: ")))
                    
                mas = Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarMedicamento(medicamento)
                servicio_hospitalario.ingresarMascota(mas)
                medicamento.ingreMedi(mas)

            else:
                print("Ya existe una mascota con el numero de historia clínica ingresado.") 

            
        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota"))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha != None:  
                datetime.strptime('fecha', '%d/%m/%Y')
                print("La fecha de ingreso de la mascota es: " + {fecha} )
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
          
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4:
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento=servicio_hospitalario.verMedicamento(q)
            if medicamento != None: 
                print(f"El medicamento suministrado es: {medicamento.verNombre()} con dosis {medicamento.verDosis()}")
                while True:
                    print("Desea eliminar un medicamento?")
                    m = input("si o no")
                    if m == "si":
                        J= int(input("Ingrese la historia clínica de la mascota: (precione unes para salir)"))
                        medicamento=servicio_hospitalario.verMedicamento(q)
                        H =input("nombre del medicamento")
                        elimin = servicio_hospitalario.eliminarMedicamento(H)
                        if elimin == True:
                            print("se elimino")
                            break
                        if J == "unes":
                            break
                        else:
                            print("no se puido")
                            continue
                    else:
                        break
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")



