# video 5 del curso
# existen funciones predefinidas en el lenguaje y las propias del usuario

print("estamos aprendiendo Python")


# si queremos que una función se repita x número de veces

def mensaje():
    print("estamos aprendiendo Python mejor")

# para que funcione, hay que llamarla

mensaje()


#video 6 - parametros

def suma():
    num1=5
    num2=7
    print(num1+num2)

suma()

# Çpara sumar valores distintos cada vez

def suma2(num3,num4):
    print(num4+num3)

suma2(30,40)
suma2(2,3)

#vamos a utilizar el valor return

def suma3(num5,num6):
    resultado=num5+num6
    return resultado

print(suma3(10,20))


# Video 7
