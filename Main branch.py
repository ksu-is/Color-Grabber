#Main branch



"""from PIL import Image
print("Pillow works!")"""
#from PIL import Image

from PIL import Image

image = Image.open("sunset.jpg")

image.show()

print("Image size:",image.size)

x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))

# Get RGB color from pixel
pixel = image.getpixel((x, y))
print("\nRGB Value:", pixel)

red = pixel[0]
green = pixel[1]
blue = pixel[2]

# Detect dominant color
if blue > red and blue > green:

    print("\nDetected Color: BLUE")
    print("Blue is commonly used in art and movies to represent calmness, mystery, sadness, peace, hope, or loneliness. Dark blues often create feelings of fear, depth, and uncertainty.")
    print("unlike the other colors, a lighter blue is often used to represent dystopian atmopheres like in bladerunner 2047")
    print("Dark ocean blues can create feelings of fear, uncertainty, depth, and hidden danger beneath. Movies like The Abyss (1989) or Moonlight (2016) are great examples of how blue capture the wonder and horror of the ocean ")

elif red > blue and red > green:

    print("\nDetected Color: RED")
    print("Red is commonly used to represent anger, danger, passion, love, pain, power, and rage. It’s a primal color that demands attention" \
    "In movies, red lighting is often used, during intense or violent scenes." \
    "Red is used in frightening scenes from movies like The Shining (1980), " \
    "or associated with evil and introductions like In Pulp Fiction (1994)")

elif green > red and green > blue:

    print("\nDetected Color: GREEN")
    print("Green is commonly used to represent nature, life, growth, healing, peace, and balance. In movies and games, darker greens can sometimes create feelings of poison, danger, or uneasiness, while lighter greens often feel refreshing and alive.")
    print("unlike the other colors, a green can be used to represent whismey, like with peter pan")


else:
    print("\nNo strong color was detected.") 
    #working on this