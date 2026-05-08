from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def describe_color(red, green, blue):
    if blue > red and blue > green:
        return "BLUE", "Blue represents calmness, mystery, sadness, depth, and the unknown."
    elif red > blue and red > green:
        return "RED", "Red represents anger, danger, passion, pain, and urgency."
    elif green > red and green > blue:
        return "GREEN", "Green represents nature, growth, peace, healing, and life."
    else:
        return "MIXED", "This color is mixed and does not strongly match red, green, or blue."

def click_image(event):
    x = event.x
    y = event.y

    # convert clicked resized-image coordinates back to original image coordinates
    original_x = int(x / scale)
    original_y = int(y / scale)

    pixel = original_image.getpixel((original_x, original_y))

    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    hex_color = "#%02x%02x%02x" % (red, green, blue)

    color_name, description = describe_color(red, green, blue)

    result_label.config(
        text="Clicked at: (" + str(original_x) + ", " + str(original_y) + ")\n"
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