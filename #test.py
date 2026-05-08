from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def describe_color(red, green, blue):

    # BLACK
    if red < 90 and green < 90 and blue < 90:
        return "BLACK", (
            "Black represents fear, death, mystery, power, emptiness, "
            "and darkness. It is heavily used in horror and dramatic scenes."
        )

    # WHITE
    elif red > 170 and green > 170 and blue > 170:
        return "WHITE", (
            "White represents purity, peace, innocence, hope, and cleanliness. "
            "It can also feel cold or isolated in certain scenes."
        )

    # YELLOW
    elif red > 170 and green > 170 and blue < 140:
        return "YELLOW", (
            "Yellow represents happiness, energy, warmth, optimism, "
            "and attention. In some films it can also create feelings "
            "of discomfort or madness."
        )

    # BROWN
    elif red > 80 and green > 40 and green < 120 and blue < 80:
        return "BROWN", (
            "Brown represents stability, earth, reliability, age, "
            "comfort, and ruggedness. Dark browns may also feel lonely or worn."
        )

    # BLUE
    elif blue > red and blue > green:
        return "BLUE", (
            "Blue represents calmness, mystery, sadness, depth, hope, "
            "and the unknown. Dark blues often create feelings of fear "
            "or isolation in movies and games."
        )

    # RED
    elif red > blue and red > green:
        return "RED", (
            "Red represents anger, danger, passion, pain, power, "
            "and urgency. Red lighting is often used during intense scenes."
        )

    # GREEN
    elif green > red and green > blue:
        return "GREEN", (
            "Green represents nature, growth, healing, life, and peace. "
            "Dark greens can also feel toxic or unsettling."
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