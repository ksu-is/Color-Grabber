#Main branch



"""from PIL import Image
print("Pillow works!")"""
#from PIL import Image

from PIL import Image

image = Image.open("sunset.jpg")

image.show()

print(image.size)
