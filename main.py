# Codigo para realizar las operaciones basicas con los vectores
# Debe realizar 1) SUMA 2) RESTA 3) DIVISIONPORUNESCALAR 4) MULTIPLICACION 5) PRODUCTO PUNTO 6) PROYECCION 7) Producto Cruz

#Lista de los vectores
listaV1 = []
listaV2 = []
resultado = []
numeroA1, numeroA2, numeroB1, numeroB2, escalar,numeroA3, numeroB3 = None, None, None, None, None, None, None


#Solicitar valores para un solo vectorY UN ESCALAR
def solicitarValoresVECTORyESCALAR2D():
    print("Ingresa los valores de tu vector A")
    global numeroA1, numeroA2, escalar
    numeroA1 = int(input("1A: "))
    numeroA2 = int(input("2A: "))
    listaV1.clear() # Cada vez que llamemos esta funcion limpiara la lista antes de asignar
    listaV1.append(numeroA1)
    listaV1.append(numeroA2)
    escalar = int(input("Escalar: "))


# Solicitar valores para ambos vectores
def solicitarValoresVECTORES2D(numeroA1, numeroA2, numeroB1, numeroB2):
    print("Ingresa los valores de tu vector A")
    #numeroA1 = int(input("1X: "))
    #numeroA2 = int(input("2Y: "))
    listaV1.clear() # Cada vez que llamemos esta funcion limpiara la lista antes de asignar
    listaV2.clear() # Cada vez que llamemos esta funcion limpiara la lista antes de asignar
    listaV1.append(numeroA1)
    listaV1.append(numeroA2)
    print("Ingresa los valores de tu vector B")
    #numeroB1 = int(input("1X: "))
    #numeroB2 = int(input("2Y: "))
    listaV2.append(numeroB1)
    listaV2.append(numeroB2)

# Solicitar valores para tres vectores
def solicitarValoresVECTORES3D():
    print("Ingresa los valores de tu vector A")
    global numeroA1, numeroA2, numeroA3, numeroB1, numeroB2, numeroB3
    numeroA1 = int(input("1X: "))
    numeroA2 = int(input("2Y: "))
    numeroA3 = int(input("3Z: "))
    listaV1.clear() # Cada vez que llamemos esta funcion limpiara la lista antes de asignar
    listaV2.clear() # Cada vez que llamemos esta funcion limpiara la lista antes de asignar
    listaV1.append(numeroA1)
    listaV1.append(numeroA2)
    listaV1.append(numeroA3)
    print("Ingresa los valores de tu vector B")
    numeroB1 = int(input("1X: "))
    numeroB2 = int(input("2Y: "))
    numeroB3 = int(input("3Z: "))
    listaV2.append(numeroB1)
    listaV2.append(numeroB2)
    listaV2.append(numeroB3)

#Realizamos la suma
def sumaVECTORES():
    resultado.clear() # Cada vez que llamemos esta funcion limpiara la lista antes de asignar
    for i in range(len(listaV1)):
        resultado.append(listaV1[i] + listaV2[i])

#Realizamos la resta
def restaVECTORES():
    resultado.clear() # Cada vez que llamemos esta funcion limpiara la lista antes de asignar
    for i in range(len(listaV1)):
        resultado.append(listaV1[i] - listaV2[i])

# Realizamos la multiplicacion escalar
def escalarVECTORES():
    resultado.clear() # Cada vez que llamemos esta funcion limpiara la lista antes de asignar
    for i in range(len(listaV1)):
        resultado.append(listaV1[i] * escalar)

#Division por un escalar
def escalarDivisionVECTORES():
    resultado.clear() # Cada vez que llamemos esta funcion limpiara la lista antes de asignar
    for i in range(len(listaV1)):
        resultado.append(listaV1[i] / escalar)
    
# Realizamos por producto punto
def productoPuntoVECTORES():
    resultado.clear() # Cada vez que llamemos esta funcion limpiara la lista antes de asignar
    for i in range(len(listaV1)):
        resultado.append(listaV1[i] * listaV2[i])
    escalar = sum(resultado)
    resultado.clear()
    resultado.append(escalar)
    
# Realizamos la proyeccion
def proyeccionVECTORES():
    # Vector V = v1 U = = v2
    productoPuntoVECTORES()
    productoPunto  = resultado[0]
    magnitud = []
    for i in range(len(listaV2)):
        magnitud.append(listaV2[i] * listaV2[i])
    resultadoMagnitud = sum(magnitud)
    division = productoPunto / resultadoMagnitud
    print("Magnitud (v2): ", resultadoMagnitud)
    print("Producto Punto (v1) (V2): ", productoPunto)
    print("Division: ", division)
    resultado.clear() # Cada vez que llamemos esta funcion limpiara la lista antes de asignar
    for i in range(len(listaV1)):
        resultado.append(listaV2[i] * division)
    print("Este es el resultado Final: ", resultado)


# Realizamos Producto Cruz (Solo para V3)
def productoCruzVECTORES():
    resultado.clear() 
    resultado.append((listaV1[1] * listaV2[2])-(listaV1[2] * listaV2[1]))
    resultado.append(-((listaV1[0] * listaV2[2])-(listaV1[2] * listaV2[0])))
    resultado.append((listaV1[0] * listaV2[1])-(listaV1[1] * listaV2[0]))
    print(resultado)





