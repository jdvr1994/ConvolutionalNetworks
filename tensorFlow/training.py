import sys
import os
import PIL

from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K

print("Running Code")

K.clear_session()

data_entrenamiento = './data/entrenamiento'
data_validacion = './data/validacion'

## Parametros
epocas = 20
altura, longitud = 100, 100 #Escalar imagenes 100px * 100 px
batch_size = 32 #En cada paso entrena con 32 imagenes
pasos = 1000 #Numero de pasos por cada epoca
pasos_validacion = 200 #Pasos dados despues de cada epoca para evaluar el progreso de la red
filtrosConv1 = 32 # Numero de filtros primera capa de convolucion
filtrosConv2 = 64 # Numero de filtros segunda capa de convolucion
tamano_filtro1 = (3,3) # Tamaño de los filtros de la primera capa de convolucion
tamano_filtro2 = (2,2) # Tamaño de los filtros de la segunda capa de convolucion
tamano_pool = (2,2) # Tamaño de matriz para Max Pooling 
clases = 3 #Clases (Perros, Gatos, Gorilaz)
lr = 0.0005 #Learning rate (Que tanto se mueve la perilla para corregir la red)

##pre_procesamiento_de_imagenes

entranamiento_datagen = ImageDataGenerator(
	rescale = 1./255, #Valores normalizados
	shear_range = 0.3, #Girar las imagenes
	zoom_range = 0.3, #Acercar las imagenes
	horizontal_flip = True #Reflejar las imagenes
)

validacion_datagen = ImageDataGenerator(
	rescale = 1./255 #Normlizar valores pixeles
)

imagen_entrenamiento = entranamiento_datagen.flow_from_directory(
	data_entrenamiento,
	target_size = (altura, longitud),
	batch_size = batch_size,
	class_mode = 'categorical'
)

imagen_validacion = validacion_datagen.flow_from_directory(
	data_validacion,
	target_size = (altura, longitud),
	batch_size = batch_size,
	class_mode = 'categorical'
)

# Crear nuestra red convolucional

cnn = Sequential()

cnn.add(
	Convolution2D(
		filtrosConv1, #numero de filtros de convolucion
		tamano_filtro1, #tamaño de los filtros de convolucion
		padding='same', # padding
		input_shape = (altura, longitud, 3), #tamaño de imagenes que entran a la red
		activation = 'relu' #Funcion de activacion Relu f(x) = max(0,x)
	)
)

cnn.add(MaxPooling2D(
	pool_size = tamano_pool
	))

cnn.add(
	Convolution2D(
		filtrosConv2,
		tamano_filtro2,
		padding = 'same',
		activation = 'relu'
	)
)

cnn.add(MaxPooling2D(
	pool_size = tamano_pool
	))

cnn.add(Flatten()) #Convertimos toda la informacion obtenida de las capas en 1 sola dimension
cnn.add(Dense(256, activation = 'relu')) #256 Neuronas con activacion Relu
cnn.add(Dropout(0.5)) #Apagamos el 50% de las neuronas de la capa (aleatorias) para conseguir que todas se entrenen
cnn.add(Dense(clases,activation = 'softmax'))

cnn.compile(
	loss = 'categorical_crossentropy',
	optimizer = optimizers.Adam(lr = lr),
	metrics = ['accuracy'] #Va a optimizar el porcentaje de imagenes que clasifica correctamente
)

cnn.fit_generator(
				 imagen_entrenamiento,
                 steps_per_epoch=pasos,
                 epochs=epocas,
                 validation_data=imagen_validacion,
                 validation_steps=pasos_validacion
)

cnn.fit()

dir = './modelo/'

if not os.path.exists(dir):
	os.mkdir(dir)

cnn.save('./modelo/modelo.h5')
cnn.save_weights('./modelo/pesos.h5')


