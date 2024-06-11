import os, time 
from funcionescentromedico import menu_principal, validar_rut, validar_nombre, validar_direccion

pacientes = []
banderaMenu = True

while banderaMenu:
    os.system("cls")
    menu_principal()
    try:
        opcion = int(input("ingrese una opcion\n"))
        if opcion == 1:
            banderaPaciente = True
            while banderaPaciente:
                
                banderaEdad = True
                print("Registrar Paciente")
                os.system("cls")
                
                
                while True:
                    rutS = input("ingrese rut \n")
                    
                    validar_rut(rutS)
                    break
                    
                string = input("ingrese nombre\n")
                validar_nombre(string)
                    
                direccion = input("ingrese direccion\n")
                validar_direccion(direccion)
               
                    
                correo = input("ingrese correo\n")
                while "@" not in correo:
                    correo = input("campo correo debe contener al menos un @\n")
                    
                while banderaEdad:
                    try:
                        edad = int(input("ingrese edad\n"))
                        while edad < 0 or edad > 110:
                            edad = int(input("ingrese edad, entre 0 110\n"))
                        banderaEdad = False
                    except:
                        print("en campo edad no se aceptan caracteres")
                        
                sexo = input("ingrese sexo\n").lower()
                while sexo != 'f' and sexo != 'm':
                    sexo = input("ingrese sexo 'f' o 'm'\n").lower()
                    
                #registro lo creare si el paciente asiste a la consulta
                
                prevision = input("ingrese su prevision\n").lower()
                while prevision != "fonasa" and prevision != "isapre":
                    prevision = input("ingrese su prevision\n").lower()
                    
                paciente = [rut, nombre, direccion, correo, edad, sexo, prevision]
                pacientes.append(paciente)
                
                otroPaciente = int(input("deseas agregar otro paciente?  1.Si  2.No\n"))
                if otroPaciente == 1:
                    continue
                else:
                    banderaPaciente = False
                print(pacientes)
                x = input("enter para continuar")
        elif opcion == 2:
            os.system("cls")
            print("Atencion Paciente")
            rutBuscar = int(input("ingrese rut a atender\n"))
            for paciente in pacientes:
                if paciente[0] == rutBuscar:
                    print("adelante ", paciente[1])
                    registro = input("ingresar sintomas\n")
                    while registro == "":
                        registro = input("ingresar sintomas\n")
                    paciente.append(registro)
                    print(paciente)
                    input("enter para continuar")
        elif opcion == 3:
            print("Gestionar Paciente")
            subMenu = True
            while subMenu:
                print("1) Consultar datos Paciente")
                print("2) Modificar Paciente")
                print("3) Eliminar Paciente")
                print("4) Regresar al menu principal")
                try:
                    opcion2 = int(input("ingrese opcion\n"))
                    if opcion2 == 1:
                        pacienteEncontrado = None
                        print("Consultar datos Paciente")
                        rut_buscar = int(input("ingrese rut a buscar\n"))
                        for paciente in pacientes:
                            if paciente[0] == rut_buscar:
                                pacienteEncontrado = paciente
                                break
                        if pacienteEncontrado:
                            print("Paciente ", pacienteEncontrado[1])
                            print("Rut: ", pacienteEncontrado[0])
                            print("Direccion: ", pacienteEncontrado[2])
                            print("Correo: ", pacienteEncontrado[3])
                            print("Edad: ", pacienteEncontrado[4])
                            print("Sexo: ", pacienteEncontrado[5])
                            print("Prevision: ", pacienteEncontrado[6])
                            print("Registro: ", pacienteEncontrado[7])
                        else:
                            print("segun nuestros registros, este rut no tiene ficha")
                        input("enter para continuar...")
                    elif opcion2 == 2:
                        print("Modificar Paciente")
                        rut_editar = int(input("ingrese rut de paciente\n"))
                        pacienteEditado = None
                        for paciente in pacientes:
                            if paciente[0] == rut_editar:
                                pacienteEditado = paciente
                                break
                        if pacienteEditado:
                            dato = input("ingrese dato que desea editar (nombre, direccion, correo, edad, sexo, prevision)")
                            if dato in ['nombre', 'direccion', 'correo', 'edad', 'sexo', 'prevision']:
                                valor_editar = input(f"ingrese el nuevo valor para el dato {dato}")
                                if dato == 'edad':
                                    valor_editar = int(valor_editar)
                                    pacienteEditado[4] = valor_editar
                                if dato == 'nombre':
                                    pacienteEditado[1] = valor_editar
                                
                    elif opcion2 == 3:
                        print("Eliminar Paciente")
                        rut_eliminar = int(input("ingrese rut a buscar\n"))
                        for paciente in pacientes:
                            if paciente[0] == rut_eliminar:
                                try:
                                    pacientes.remove(paciente)
                                except:
                                    print("no existe ese rut para eliminar")
                        print("paciente eliminado con exito")
                        input("enter para continuar")
                    elif opcion2 == 4:
                        print("saliendo de sub menu...")
                        time.sleep(1)
                        subMenu = False
                except:
                    print("opcion ingresa no es valida")
                
                
        elif opcion == 4:
            print("Ha salido del sistema…")
            x = input("enter para salir...")
            banderaMenu = False
    except:
        print("opcion no es valida")
