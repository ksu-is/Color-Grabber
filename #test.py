#test

# Color Grabber - Clickable Version
# Will Kennedy

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def describe_color(red, green, blue):
    if blue > red and blue > green:
        return "BLUE", "Blue represents calmness, mystery, sadness, and depth."
    elif red > blue and red > green:
        return "RED", "Red represents anger, danger, passion, and intensity."
    elif green > red and green > blue:
        return "GREEN", "Green represents nature, growth, peace, and life."
    else:
        return "MIXED", "This color is a mix and does not strongly match one category."

def click_image(event):
    x = event.x
    y = event.y

    pixel = image.getpixel((x, y))
    red, green, blue = pixel

    hex_color = "#%02x%02x%02x" % (red, green, blue)
    color_name, description = describe_color(red, green, blue)

    result_label.config(
        text=f"Clicked at: ({x}, {y})\nRGB: {pixel}\nHEX: {hex_color}\n\n{color_name}\n{description}"
    )

# Create window
root = Tk()
root.title("Color Grabber")

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
)

image = Image.open(file_path)
tk_image = ImageTk.PhotoImage(image)

image_label = Label(root, image=tk_image)
image_label.pack()

image_label.bind("<Button-1>", click_image)

result_label = Label(root, text="Click anywhere on the image", font=("Arial", 14))
result_label.pack()

root.mainloop()