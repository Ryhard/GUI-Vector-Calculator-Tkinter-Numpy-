# Librerias que usaremos para este proyecto
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Listas para los vectores 2D o 3D y resultados
listaV1 = []
listaV2 = []
resultado = []

# Funciones para operar con vectores

# Funciones que solicitara las coordenadas de los vectores 
def solicitarValoresVECTORES2D(numeroA1, numeroA2, numeroB1, numeroB2):
    listaV1.clear()
    listaV2.clear()
    listaV1.extend([numeroA1, numeroA2])
    listaV2.extend([numeroB1, numeroB2])

def solicitarValoresVECTORES3D(numeroA1, numeroA2, numeroA3, numeroB1, numeroB2, numeroB3):
    listaV1.clear()
    listaV2.clear()
    listaV1.extend([numeroA1, numeroA2, numeroA3])
    listaV2.extend([numeroB1, numeroB2, numeroB3])

# Funciones de las operaciones que se realizaran

# Funcion SUMA
def sumaVECTORES():
    resultado.clear()
    resultado.extend([listaV1[i] + listaV2[i] for i in range(len(listaV1))])
    mostrarResultado("Suma")

# Funcion Resta
def restaVECTORES():
    resultado.clear()
    resultado.extend([listaV1[i] - listaV2[i] for i in range(len(listaV1))])
    mostrarResultado("Resta")

# Funcion Producto Escalar
def escalarVECTORES(escalar):
    resultado.clear()
    resultado.extend([listaV1[i] * escalar for i in range(len(listaV1))])
    mostrarResultado("Multiplicación Escalar")

# Funcion Magnitud del VectorA
def magnitudVECTORES():
    resultado.clear()
    magnitud = sum(x * x for x in listaV1) ** 0.5
    mostrarResultado("Magnitud", [magnitud])

# Funcion Vector unitario del VectorA
def vectorUnitarioVECTORES():
    magnitud = sum(x * x for x in listaV1) ** 0.5
    if magnitud == 0:
        messagebox.showerror("Error", "No se puede calcular el vector unitario de un vector nulo.")
        return
    resultado.clear()
    resultado.extend([x / magnitud for x in listaV1])
    mostrarResultado("Vector Unitario")

# Funcion Producto Punto
def productoPuntoVECTORES():
    resultado.clear()
    escalar = sum(listaV1[i] * listaV2[i] for i in range(len(listaV1)))
    mostrarResultado("Producto Punto", escalar)

# Funcion Proyeccion del VectorA sobre el VectorB
def proyeccionVECTORES():
    productoPunto = sum(listaV1[i] * listaV2[i] for i in range(len(listaV1)))
    magnitud = sum(x * x for x in listaV2)
    
    if magnitud == 0:
        messagebox.showerror("Error", "No se puede proyectar sobre un vector nulo.")
        return
    
    division = productoPunto / magnitud
    resultado.clear()
    resultado.extend([listaV2[i] * division for i in range(len(listaV2))])
    mostrarResultado("Proyección")

# Funcion Producto Cruz (Solo para vectores 3D)
def productoCruzVECTORES():
    if len(listaV1) == 3 and len(listaV2) == 3:
        resultado.clear()
        resultado.append((listaV1[1] * listaV2[2]) - (listaV1[2] * listaV2[1]))
        resultado.append((listaV1[2] * listaV2[0]) - (listaV1[0] * listaV2[2]))
        resultado.append((listaV1[0] * listaV2[1]) - (listaV1[1] * listaV2[0]))
        mostrarResultado("Producto Cruz")
    else:
        messagebox.showerror("Error", "El producto cruz solo es válido para vectores 3D.")

# Funcion que mostrara los resultados
def mostrarResultado(operacion, res=None):
    res = resultado if res is None else res
    messagebox.showinfo(f"Resultado de {operacion}", f"El resultado es: {res}")

# Función para mostrar los vectores en una grafica 2D con numpy
def mostrarGraficaVectores():
    # Intentar obtener valores de los entry de vectores A y B
    try:
        vecA_x = float(entryA1.get())
        vecA_y = float(entryA2.get())
        vecB_x = float(entryB1.get())
        vecB_y = float(entryB2.get())

        # Si está en 3D, intenta obtener el tercer valor
        vecA_z = float(entryA3.get()) if entryA3.get() else 0
        vecB_z = float(entryB3.get()) if entryB3.get() else 0
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos para los vectores en 2D.")
        return

    # Obtener los ángulos de los vectores (0 si solo se usara las coordenadas como referencia)
    try:
        angA = float(entryAngA.get())
        angB = float(entryAngB.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa ángulos válidos en grados.")
        return

    # Ventana que iniciara la grafica de los vectores
    ventana_grafica = tk.Toplevel()
    ventana_grafica.title("Gráfica de Vectores")
    
    fig = plt.figure(figsize=(6, 5))      # Tamaño de la ventana
    fig.patch.set_facecolor('lightblue')  # Color de fondo de la ventana

    # Crear los ejes
    ax = fig.add_subplot(111)
    # Establecer el color de fondo del área de los ejes
    ax.set_facecolor('white')

    # Convertir ángulos a radianes
    radA = np.deg2rad(angA)
    radB = np.deg2rad(angB)

    # Aplicar ángulo a los vectores A y B
    vecA_rotado = [np.cos(radA) * vecA_x - np.sin(radA) * vecA_y, 
                   np.sin(radA) * vecA_x + np.cos(radA) * vecA_y]
    vecB_rotado = [np.cos(radB) * vecB_x - np.sin(radB) * vecB_y, 
                   np.sin(radB) * vecB_x + np.cos(radB) * vecB_y]

    # Graficar vectores rotados
    ax.quiver(0, 0, vecA_rotado[0], vecA_rotado[1], angles='xy', scale_units='xy', scale=1, color='r', label="Vector A")
    ax.quiver(0, 0, vecB_rotado[0], vecB_rotado[1], angles='xy', scale_units='xy', scale=1, color='b', label="Vector B")

    # Graficar Vector Resultado si la lista dee Resultado contiene valores
    if resultado:
        vecResultado_x = resultado[0]
        vecResultado_y = resultado[1]
        angResultado = float(entryAngA.get())

        radResultado = np.deg2rad(angResultado)
        vecResultado_rotado = [
            np.cos(radResultado) * vecResultado_x - np.sin(radResultado) * vecResultado_y, 
            np.sin(radResultado) * vecResultado_x + np.cos(radResultado) * vecResultado_y
        ]

        ax.quiver(0, 0, vecResultado_rotado[0], vecResultado_rotado[1], angles='xy', scale_units='xy', scale=1, color='g', label="Vector Resultado")

    max_val = max(max(abs(np.array(vecA_rotado))), max(abs(np.array(vecB_rotado))), (max(abs(np.array(vecResultado_rotado))) if resultado else 0)) + 1
    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)
    ax.grid(True)
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=ventana_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Función para mostrar los vectores en una grafica 3D con numpy
def mostrarGraficaVectores3D():
    try:
        vecA_x = float(entryA1.get())
        vecA_y = float(entryA2.get())
        vecA_z = float(entryA3.get())
        vecB_x = float(entryB1.get())
        vecB_y = float(entryB2.get())
        vecB_z = float(entryB3.get())
    except ValueError:
        messagebox.showerror("ERROR", "Por favor ingresa valores válidos para los vectores en 3D.")
        return

    try:
        angA = float(entryAngA.get())
        angB = float(entryAngB.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa ángulos válidos en grados.")
        return

    # Ventana que iniciara la grafica de los vectores
    ventana_grafica = tk.Toplevel()
    ventana_grafica.title("Gráfica de Vectores 3D")

    fig = plt.figure(figsize=(6, 5))  # Tamaño de la ventana
    fig.patch.set_facecolor('lightblue')  # Color de fondo de la figura
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('lightblue')  # Color de fondo del área de dibujo del gráfico
    
    # Convertir ángulos a radianes
    radA = np.deg2rad(angA)
    radB = np.deg2rad(angB)

    # Rotar los vectores A y B en el plano XY usando los ángulos dados
    vecA_rotado = [
        np.cos(radA) * vecA_x - np.sin(radA) * vecA_y,
        np.sin(radA) * vecA_x + np.cos(radA) * vecA_y,
        vecA_z
    ]

    vecB_rotado = [
        np.cos(radB) * vecB_x - np.sin(radB) * vecB_y,
        np.sin(radB) * vecB_x + np.cos(radB) * vecB_y,
        vecB_z
    ]

    # Graficar vectores rotados en 3D
    ax.quiver(0, 0, 0, vecA_rotado[0], vecA_rotado[1], vecA_rotado[2], color='r', label="Vector A")
    ax.quiver(0, 0, 0, vecB_rotado[0], vecB_rotado[1], vecB_rotado[2], color='b', label="Vector B")

    # Comprueba si las coordenadas son adecuadas para los vectores 3D
    if resultado and len(resultado) == 3:
        vecResultado_x = resultado[0]
        vecResultado_y = resultado[1]
        vecResultado_z = resultado[2]

        vecResultado_rotado = [
            np.cos(radA) * vecResultado_x - np.sin(radA) * vecResultado_y,
            np.sin(radA) * vecResultado_x + np.cos(radA) * vecResultado_y,
            vecResultado_z
        ]

        ax.quiver(0, 0, 0, vecResultado_rotado[0], vecResultado_rotado[1], vecResultado_rotado[2], color='g', label="Vector Resultado")

# Perzonalizacion de coordenadas
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    ax.set_xlabel('X axis', color='blue')
    ax.set_ylabel('Y axis', color='red')
    ax.set_zlabel('Z axis', color='yellow')

# Valor maximo para las coordenadas 3D == al valor mas alto (Permite que ningun vector se salga de la grafica)
    max_val = max(
        abs(vecA_rotado[0]), abs(vecA_rotado[1]), abs(vecA_rotado[2]), 
        abs(vecB_rotado[0]), abs(vecB_rotado[1]), abs(vecB_rotado[2]), 
        *(abs(v) for v in vecResultado_rotado) if resultado else [0]
    ) + 1

    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)
    ax.set_zlim(-max_val, max_val)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=ventana_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack()


# GUI Principal
ventana = tk.Tk()
ventana.title("Operaciones con Vectores")
ventana.geometry("300x550+800+300")
ventana.resizable(False,False)
ventana.configure(bg="lightblue3")

# Función para capturar datos y realizar operaciones
def realizarOperacion(operacion):
    try:
        nA1 = float(entryA1.get())
        nA2 = float(entryA2.get())
        nB1 = float(entryB1.get())
        nB2 = float(entryB2.get())
        nA3 = float(entryA3.get()) if entryA3.get() else None
        nB3 = float(entryB3.get()) if entryB3.get() else None
        
        if nA3 is not None and nB3 is not None:
            solicitarValoresVECTORES3D(nA1, nA2, nA3, nB1, nB2, nB3)
        else:
            solicitarValoresVECTORES2D(nA1, nA2, nB1, nB2)
        
        if operacion == "suma":
            sumaVECTORES()
        elif operacion == "resta":
            restaVECTORES()
        elif operacion == "multiplicacion":
            escalar = float(entryEscalar.get())
            escalarVECTORES(escalar)
        elif operacion == "magnitud":
            magnitudVECTORES()
        elif operacion == "producto_punto":
            productoPuntoVECTORES()
        elif operacion == "proyeccion":
            proyeccionVECTORES()
        elif operacion == "producto_cruz":
            productoCruzVECTORES()
        elif operacion == "vector_unitario":
            vectorUnitarioVECTORES()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Crear un marco (frame) con borde
frame = tk.Frame(ventana, bg="lightblue", bd=5, relief="groove")
frame.pack(padx=10, pady=10)  # Espacio alrededor del marco

# Widgets de la GUI

# Titullos y entry de los vectores A
TituloA1 = tk.Label(frame, text="VECTOR A", bg="CadetBlue2", font=("Arial Black", 12), fg="White")
labelA1 = tk.Label(frame, text="Coordenada X:", bg="lightblue", font=("Arial Narrow", 10))
entryA1 = tk.Entry(frame,width="12")
labelA2 = tk.Label(frame, text="Coordenada Y:", bg="lightblue", font=("Arial Narrow", 10))
entryA2 = tk.Entry(frame,width="12")
labelA3 = tk.Label(frame, text="(Opcional) Coordenada Z:", bg="lightblue", font=("Arial Narrow", 10))
entryA3 = tk.Entry(frame,width="12")

# Titullos y entry de los vectores B
TituloB1 = tk.Label(frame, text="VECTOR B", bg="CadetBlue2", font=("Arial Black", 12), fg="White")
labelB1 = tk.Label(frame, text="Coordenada X:", bg="lightblue", font=("Arial Narrow", 10))
entryB1 = tk.Entry(frame,width="12")
labelB2 = tk.Label(frame, text="Coordenada Y:", bg="lightblue", font=("Arial Narrow", 10))
entryB2 = tk.Entry(frame,width="12")
labelB3 = tk.Label(frame, text="(Opcional) Coordenada Z:", bg="lightblue", font=("Arial Narrow", 10))
entryB3 = tk.Entry(frame,width="12")

# Entry para el valor Escalar
labelEscalar = tk.Label(frame, text="Escalar :", bg="LightSkyBlue1", font=("Arial Narrow", 10),padx=15)
entryEscalar = tk.Entry(frame,width="12")

# Botones de las operaciones
TituloOp = tk.Label(frame, text="OPERACIONES", bg="gold", font=("Arial Black", 12), fg="White")
botonSuma = tk.Button(frame, text="Suma", command=lambda: realizarOperacion("suma"), bg="LightCyan2",width="18")
botonResta = tk.Button(frame, text="Resta", command=lambda: realizarOperacion("resta"),width="18")
botonMultiplicacion = tk.Button(frame, text="Producto Escalar", command=lambda: realizarOperacion("multiplicacion"),width="18")
botonMagnitud = tk.Button(frame, text="Magnitud", command=lambda: realizarOperacion("magnitud"), bg="LightCyan2",width="18")
botonProductoPunto = tk.Button(frame, text="Producto Punto", command=lambda: realizarOperacion("producto_punto"), bg="LightCyan2",width="18")
botonProyeccion = tk.Button(frame, text="Proyección", command=lambda: realizarOperacion("proyeccion"),width="18")
botonProductoCruz = tk.Button(frame, text="Producto Cruz", command=lambda: realizarOperacion("producto_cruz"),width="18")
botonVectorUnitario = tk.Button(frame, text="Vector Unitario", command=lambda: realizarOperacion("vector_unitario"), bg="LightCyan2",width="18")

# Agregar etiquetas y entradas para ángulos
labelAngA = tk.Label(frame, text="Ángulo Vector A:", bg="lightblue", font=("Arial Narrow", 10), width="18")
entryAngA = tk.Entry(frame, width="18")
labelAngB = tk.Label(frame, text="Ángulo Vector B:", bg="lightblue", font=("Arial Narrow", 10), width="18")
entryAngB = tk.Entry(frame, width="18")

# Boton para Graficar los vectores
botonMostrarVectores = tk.Button(frame, text="Mostrar Gráfica 2D", command=mostrarGraficaVectores, bg="LightGreen", width="18")
btnGrafica3D = tk.Button(frame, text="Mostrar Gráfica 3D", command=mostrarGraficaVectores3D, bg="khaki1", width="18")

# Posicionamiento en filas y columnas con grid

# Titulos y entry de los vectores A
TituloA1.grid(row=0, column=0, columnspan=2, pady=(3, 5))
labelA1.grid(row=1, column=0, sticky='e')
entryA1.grid(row=1, column=1, sticky='w')
labelA2.grid(row=2, column=0, sticky='e')
entryA2.grid(row=2, column=1, sticky='w')
labelA3.grid(row=3, column=0, sticky='e')
entryA3.grid(row=3, column=1, sticky='w')

# Titullos y entry de los vectores B
TituloB1.grid(row=4, column=0, columnspan=2, pady=(10, 5))
labelB1.grid(row=5, column=0, sticky='e')
entryB1.grid(row=5, column=1, sticky='w')
labelB2.grid(row=6, column=0, sticky='e')
entryB2.grid(row=6, column=1, sticky='w')
labelB3.grid(row=7, column=0, sticky='e')
entryB3.grid(row=7, column=1, sticky='w')

# Titullos y entry deL Escalar
labelEscalar.grid(row=8, column=0, sticky='e')
entryEscalar.grid(row=8, column=1, sticky='w')

# Botones de las operaciones
TituloOp.grid(row=9, column=0, columnspan=2, pady=(10, 0))
botonSuma.grid(row=10, column=0, pady=(10,0))
botonResta.grid(row=10, column=1, pady=(10,0))
botonMultiplicacion.grid(row=11, column=0)
botonMagnitud.grid(row=11, column=1)
botonProductoPunto.grid(row=12, column=0)
botonProyeccion.grid(row=12, column=1)
botonProductoCruz.grid(row=13, column=0, pady=(0, 5))
botonVectorUnitario.grid(row=13, column=1, columnspan=2, pady=(0, 5))

# Mostrar vectores en los graficos
labelAngA.grid(row=14, column=0, sticky='e')
labelAngB.grid(row=14, column=1, sticky='w')
entryAngA.grid(row=15, column=0, sticky='e', padx=(0,3), pady=(0,10))
entryAngB.grid(row=15, column=1, sticky='w', padx=(3,0), pady=(0,10))
botonMostrarVectores.grid(row=16, column=0, columnspan=2, pady=(0,5))
btnGrafica3D.grid(row=17, column=0, columnspan=2, pady=(0, 10))

#Inicializacion de la ventana
ventana.mainloop()
