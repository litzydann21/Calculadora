# AVANCE PARA LA CALCULADORA 
#LITZY DANARI HERNÁNDEZ ARGUELLES 25/10/2026
v1=float(input("Ingresa el primer número:"))
v2=float(input("Ingresa el segundo número:"))
operacion=input("Ingresa la operación:").upper()
def operaciones(v1,v2, operacion):
    if operacion=="SUMA":
        print("suma =",v1+v2)
    elif operacion=="RESTA":
        print("resta =",v1-v2)
    elif operacion=="MULTIPLICACION":
        print("multiplicacion =",v1*v2)
    elif operacion=="DIVISION":
        print("division =",v1/v2)
    elif operacion=="DIVISION DE ENTEROS":
        print("division de enteros =",v1//v2)
    elif operacion=="POTENCIA":
        print("potencia =",v1**v2)
    else:
        print("operacion no valida")
operaciones(v1,v2,operacion)


