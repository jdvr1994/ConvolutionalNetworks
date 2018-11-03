from PIL import Image

print ("Load, Create and Show Images Script")

# ---------------------------------------
# Load Image from file
image = Image.open('photo.jpg')

# Image transform to RGB format
rgb_im = image.convert('RGB')
pixelsLoad = image.load()

# Get values (r,g,b) of the pixel 1,1
r, g, b = rgb_im.getpixel((200, 300))
print(r, g, b)

# Get and Print values (r,g,b) of the pixel 200,300
print(pixelsLoad[200, 300][0])
print(pixelsLoad[200, 300][1])
print(pixelsLoad[200, 300][2])

# Show the image
image.show()
# ---------------------------------------

# Create a new Image
myImg = Image.new('RGB', (image.size[0], image.size[1]), "black")
# Create the pixel map
pixels = myImg.load()

for i in range(myImg.size[0]):    # for every col:
    for j in range(myImg.size[1]):    # For every row
        grayScaleValue = (pixelsLoad[i, j][0] +
                          pixelsLoad[i, j][1] +
                          pixelsLoad[i, j][2]) / 3

        pixels[i, j] = (grayScaleValue, grayScaleValue, grayScaleValue)

myImg.show()

input()
