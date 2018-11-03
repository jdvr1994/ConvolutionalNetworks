from PIL import Image
import numpy as np
from scipy.ndimage import convolve
import math

print ("hola bienvenido")
a = [1, 2, 3]
a.append(4)
print (a)

# ---------------------------------------
# Load Image from file
image = Image.open('photo.jpg')

# Image transform to RGB format
rgb_im = image.convert('RGB')
pixelsLoad = image.load()

# Get values (r,g,b) of the pixel 1,1
r, g, b = rgb_im.getpixel((200, 300))
print(r, g, b)

print(pixelsLoad[200, 300][0])
print(pixelsLoad[200, 300][1])
print(pixelsLoad[200, 300][2])

# Show the image
image.show()
# ---------------------------------------

# -------- Make Convolutions -----------
imgArray = np.zeros( (image.size[0], image.size[1]) )

# Edges detected
filterEdge = np.array([[1,0,-1],
		 [1,0,-1],
		 [1,0,-1]])

# Blur Effect
sizeFB = 9
filterBlur = np.ones((sizeFB,sizeFB))
divFactor = 1.0 / (sizeFB*sizeFB)
filterBlur = filterBlur*divFactor

# GrayScale image converter to np.array  (imagen2)
for f in range(image.size[0]):
	for c in range(image.size[1]):
		color = (pixelsLoad[f, c][0] +
             pixelsLoad[f, c][1] +
             pixelsLoad[f, c][2]) / 3
		imgArray[f][c] = color

# Convolution with convolve Function
sizeResultadoX = imgArray.shape[0] - filterBlur.shape[0] + 1
sizeResultadoY = imgArray.shape[1] - filterBlur.shape[1] + 1
convResult = np.zeros( (sizeResultadoX, sizeResultadoY) )

print(sizeResultadoX)
print(imgArray.shape[0])
print(convResult.shape[0])


for cr in range(convResult.shape[1]):
	for fr in range(convResult.shape[0]):
		suma = 0
		for c in range(filterBlur.shape[1]):
			for f in range (filterBlur.shape[0]):

				fIma = f+fr
				cIma = c + cr
				suma = suma + (imgArray[fIma][cIma] * filterBlur[f][c])

		convResult[fr][cr] = suma

# Create a new Image 1920x1080
myImg = Image.new('RGB', (image.size[0], image.size[1]), "black")
# Create the pixel map
pixels = myImg.load()

for i in range(convResult.shape[0]):    # for every row:
    for j in range(convResult.shape[1]):    # For every col
        pixels[i, j] = (int(convResult[i][j]), int(convResult[i][j]), int(convResult[i][j])) # Put the convoltion result into myImg

myImg.show()

input()
