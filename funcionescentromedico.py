#funciones 

def menu_principal ():
    print("1) Registrar Paciente")
    print("2) Atencion Paciente")
    print("3) Gestionar Paciente")
    print("4) Salir")
    
def validar_rut(rutS):
    
    while rutS == "":
        rutS = input("ingrese rut, no debe venir vacio \n")
    try:
        rut = int(rutS)
        while rut < 5000000 or rut > 30000000:
            rut = int(input("ingrese rut, debe estar en rango 5M Y 30M\n"))
                        
    except:
        print("en campo rut, no se aceptan caracteres")
        input("presione una tecla para continuar")
        
    return rutS
    

def validar_nombre(string):
    while string == "" and string== " ":
        string = input("nombre no puede guardarse vacio\n")
    return string

def validar_direccion(direccion):
    while direccion == "" and direccion == " ":
        direccion = input("direccion no puede guardarse vacio\n")
    return direccion