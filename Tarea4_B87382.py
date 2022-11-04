#Tarea 4 de Microelectronica
#Ana Eugenia Sanchez Vilalobos B87382

from pprint import pprint
from numpy import asarray
from numpy import exp
import random
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed

# objective function
def objective(x1,x2):
	return x1*(x1-5) + pow(x2,3) - x1*(x2+11)


# simulated annealing algorithm
from traceback import print_tb

from pandas import array

t = 100
for i in range(100):
    t = t*0.99
    #print(t)


def simulated_annealing(t):
    lista = []
  #valor inicial de x1 y x2
    x1 = 7
    x2 = 17
    array = [x1,x2]
    #ecuacion evaluada en el punto incial
    best_eval = objective(x1,x2)
    curr, curr_eval = array, best_eval
    
    #algoritmo
    for i in range(100000):
        #step
        candidate_x1 =  curr[0] + random.uniform(-0.1, 0.1) 
        candidate_x2 = curr[1] + random.uniform(-0.1, 0.1) 
        array_it = [candidate_x1, candidate_x2]

        candidate_eval = objective(candidate_x1,candidate_x2)

        if candidate_eval < best_eval:
            #nuevo punto de comienzo
            curr, curr_eval = array_it, candidate_eval
            lista.append(candidate_eval)
                #array, best_eval = array_it, candidate_eval
            #report progress
            print('>%d f(%s) = %.5f' % (i, curr, curr_eval))
        #difference between candidate and current point evaluation
        diff = candidate_eval - curr_eval
        #calculate temperature for current epoch
        t = t*0.99
        #calculate metropolis acceptance criterion
        metropolis = exp(-diff / t)
        #check if we should keep the new point
        if diff > 0 and rand() < metropolis:
            #store the new current point
            curr, curr_eval = array_it, candidate_eval
            print('>%d f(%s) = %.5f' % (i, curr, curr_eval))
            lista.append(candidate_eval)
            #print("La temperatura actual es: ", t, "\n")
            
        if i > 99 and candidate_eval >= 0.0001:
            print("-------------------------------------------------------------------------")
            print("No ha logrado una mejora mayor a 0.000001, luego de 100 iteraciones \n ")
            print("El mejor resultado obtenido fue, de todas las 100 iteraciones: ", min(lista))
            break 
    return [array_it, candidate_eval]

best, score = simulated_annealing(t)

print("\n",'----------------------------RESULTADO FINAL ------------------------------')
print("La ultima iteracion fue: \n",'f(%s) = %f' % (best, score))
