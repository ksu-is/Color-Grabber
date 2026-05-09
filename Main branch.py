#Main branch

#from PIL import Image

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def describe_color(red, green, blue):


    if red < 90 and green < 90 and blue < 90:
        return "BLACK", (
            "Black represents fear, death, mystery, power, emptiness, "
            "and darkness. It is heavily used in horror and dramatic scenes."
        )


    elif red > 170 and green > 170 and blue > 170:
        return "WHITE", (
            "White represents purity, peace, innocence, hope, and cleanliness. "
            "It can also feel cold or isolated in certain scenes."
        )


    elif red > 170 and green > 170 and blue < 140:
        return "YELLOW", (
            "Yellow represents happiness, energy, warmth, optimism, "
            "and attention. In some films it can also create feelings "
            "of discomfort or madness."
        )


    elif red > 80 and green > 40 and green < 120 and blue < 80:
        return "BROWN", (
            "Brown represents stability, earth, reliability, age, "
            "comfort, and ruggedness. Dark browns may also feel lonely or worn."
        )


    elif blue > red and blue > green:
        return "BLUE", (
            "Blue is commonly used in art and movies to represent calmness, mystery, sadness, peace, hope, or loneliness. Dark blues often create feelings of fear, depth, and uncertainty. " \
            "Unlike the other colors, a lighter blue is often used to represent dystopian atmopheres like in Bladerunner 2047 (2017) " \
            "Dark ocean blues can create feelings of fear, uncertainty, depth, and hidden danger beneath. Movies like The Abyss (1989) or Moonlight (2016) " 
            "are great examples of how blue capture the wonder and horror of the ocean "
        )


    elif red > blue and red > green:
        return "RED", (
            "Red is commonly used to represent anger, danger, passion, love, pain, power, and rage. " 
            "It’s a primal color that demands attention " \
            "In movies, red lighting is often used, during intense or violent scenes. " \
            "Red is used in frightening scenes from movies like The Shining (1980), " \
            "or associated with evil and introductions like in Pulp Fiction (1994) "
        )

   

    elif green > red and green > blue:
        return "GREEN", (
            "Green is commonly used to represent nature, life, growth, healing, peace, and balance. In movies and games, darker greens can sometimes create feelings of poison, danger, or uneasiness, while lighter greens often feel refreshing and alive."
            "unlike the other colors, a green can be used to represent whismey, like with peter pan"
        )

    else:
        return "MIXED", (
            "This color is mixed and does not strongly match one category."
        )
    














def click_image(event):
    x = event.x
    y = event.y

    original_x = int(x / scale)
    original_y = int(y / scale)

    pixel = original_image.getpixel((original_x, original_y))

    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    hex_color = "#%02x%02x%02x" % (red, green, blue)

    color_name, description = describe_color(red, green, blue)

    result_label.config(
        text=
        "Clicked at: (" + str(original_x) + ", " + str(original_y) + ")\n"
        + "RGB: " + str(pixel) + "\n"
        + "HEX: " + hex_color + "\n"
        + "Detected Color: " + color_name + "\n\n"
        + description
    )

root = Tk()
root.title("The Color Grabber")

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

if file_path == "":
    print("No image selected.")
    root.destroy()

else:
    original_image = Image.open(file_path)

    max_width = 700
    max_height = 450

    width = original_image.width
    height = original_image.height

    scale_width = max_width / width
    scale_height = max_height / height

    scale = min(scale_width, scale_height)

    new_width = int(width * scale)
    new_height = int(height * scale)

    display_image = original_image.resize((new_width, new_height))

    tk_image = ImageTk.PhotoImage(display_image)

    image_label = Label(root, image=tk_image)
    image_label.pack()

    image_label.bind("<Button-1>", click_image)

    result_label = Label(
        root,
        text="Click on the image to grab a color.",
        font=("Arial", 14),
        justify=LEFT,
        wraplength=700
    )

    result_label.pack()

    root.mainloop()
    