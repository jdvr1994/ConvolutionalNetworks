
import numpy as np
from scipy.ndimage import convolve

print("Jugando con matrices")

"""
imagen = np.array([[3, 0, 1, 2, 7, 4], 
    	 [1, 5, 8, 9, 3, 1],
    	 [2, 7, 2, 5, 1, 3],
    	 [0, 1, 3, 1, 7, 8],
    	 [4, 2, 1, 6, 2, 8],
    	 [2, 4, 5, 2, 3, 9]])
"""

imagen = np.array([[10, 10, 10, 10, 0, 0, 0, 0],
		 [10, 10, 10, 10, 0, 0, 0, 0], 
    	 [10, 10, 10, 10, 0, 0, 0, 0],
    	 [10, 10, 10, 10, 0, 0, 0, 0],
    	 [10, 10, 10, 10, 0, 0, 0, 0],
    	 [10, 10, 10, 10, 0, 0, 0, 0],
    	 [10, 10, 10, 10, 0, 0, 0, 0],
    	 [10, 10, 10, 10, 0, 0, 0, 0]])

imagen2 = np.array([[10, 10, 10, 0, 0, 0], 
    	 [10, 10, 10, 0, 0, 0],
    	 [10, 10, 10, 0, 0, 0],
    	 [10, 10, 10, 0, 0, 0],
    	 [10, 10, 10, 0, 0, 0],
    	 [10, 10, 10, 0, 0, 0]])

filtro = np.array([[1,0,-1],
		 [1,0,-1],
		 [1,0,-1]])


sizeResultado = imagen.shape[0] - filtro.shape[0] + 1
resultado = np.zeros( (sizeResultado, sizeResultado) )

for cr in range(sizeResultado):
	for fr in range(sizeResultado):
		suma = 0
		for c in range(filtro.shape[1]):
			for f in range (filtro.shape[0]):

				fIma = f+fr
				cIma = c + cr
				suma = suma + (imagen[fIma][cIma] * filtro[f][c])

		resultado[fr][cr] = suma


print(resultado)

resultado2 = convolve(imagen2, filtro, mode = 'constant', cval=0.0)
resultado2 = convolve(imagen2, filtro)

print(resultado2)