#Tarea #5 Curso de Microelectronica
#Ana Eugenia Sanchez Villalobos 
#B87382
import numpy as np
import matplotlib.pyplot as plt

#Definicion de parametros 

p = 1  #peso de los cables

#Posicion A
x_a = 0.5
y_a = 1
#Posicion B
x_b = 0
y_b = 0.25
#Posicion C
x_c = 1
y_c = 0


#arreglos para dibujar
x_ports = [x_a, x_b, x_c]
y_ports = [y_a, y_b, y_c]

# Funciones en matrices ya derivadas
matrix_a = np.array([[4,0,-2], [0,6,-2],[-2,-2,6]])

#Matriz b, para soluciones con derivadas parciales de x
matrix_b = np.array([2*p*x_a, (2*p*x_a + 2*p*x_b), 2*p*x_c])

x = np.linalg.solve(matrix_a, matrix_b)

# Funciones en matrices ya derivadas
matrix_a = np.array([[4,0,-2], [0,6,-2],[-2,-2,6]])

#Matriz b, para soluciones con derivadas parciales de y
matrix_c = np.array([2*p*y_a, (2*p*y_a + 2*p*y_b), 2*p*y_c])

y = np.linalg.solve(matrix_a, matrix_c)

#arreglos para dibujar
x_cells = [x[0], x[1], x[2]]
y_cells = [y[0], y[1], y[2]]

#Impresiones
print("Las posiciones de x_1 y y_1 son:", np.array([x[0], y[0]]), "\n")
print("Las posiciones de x_2 y y_2 son:", np.array([x[1], y[1]]), "\n")
print("Las posiciones de x_3 y y_3 son:", np.array([x[2], y[2]]), "\n")

#Codigo tomado del profesor
"""
Esta funcion recibe 4 parámetros:
x_ports: Un arreglo de 3 entradas con [x_a, x_b, x_c]
y_ports: Un arreglo de 3 entradas con [y_a, y_b, y_c]
x_cells: Un arreglo de 3 entradas con [x_1, x_2, x_3]
y_cells: Un arreglo de 3 entradas con [y_1, y_2, y_3]
"""
def plot_solution(x_ports, y_ports, x_cells, y_cells):

    plt.plot([0,0], [0,1], color="black", linewidth=2)
    plt.plot([0,1], [0,0], color="black", linewidth=2)
    plt.plot([1,1], [0,1], color="black", linewidth=2)
    plt.plot([0,1], [1,1], color="black", linewidth=2)

    plt.plot([x_ports[0],x_cells[0]], [y_ports[0],y_cells[0]], color="black", linewidth=0.75)
    plt.plot([x_ports[0],x_cells[1]], [y_ports[0],y_cells[1]], color="black", linewidth=0.75)
    plt.plot([x_ports[1],x_cells[1]], [y_ports[1],y_cells[1]], color="black", linewidth=0.75)
    plt.plot([x_ports[2],x_cells[2]], [y_ports[2],y_cells[2]], color="black", linewidth=0.75)
    plt.plot([x_cells[0],x_cells[2]], [y_cells[0],y_cells[2]], color="black", linewidth=0.75)
    plt.plot([x_cells[1],x_cells[2]], [y_cells[1],y_cells[2]], color="black", linewidth=0.75)

    plt.scatter(x_ports, y_ports, color="blue", marker="s", s=100)
    plt.scatter([x_cells[0],x_cells[1],x_cells[2]],[y_cells[0],y_cells[1],y_cells[2]], color="red", marker="o", s=100)
    plt.title("Netlist with Placement Algorithm, with p = 1")
    plt.suptitle("Tarea #5 - Ana Eugenia Sanchez Villalobos", color="green")
    plt.show()

plot_solution(x_ports, y_ports, x_cells, y_cells)