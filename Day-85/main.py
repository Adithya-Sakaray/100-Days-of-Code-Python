from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageFont, ImageDraw

YELLOW = "#f7f5dd"
FONT_NAME = "Arial"


def add_watermark(path):
    image = Image.open(path).convert("RGBA")
    txt = Image.new('RGBA', image.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(txt)

    height, width = image.size
    h = int(height / 2)
    w = int(width / 2)

    if h > w:
        font_size = w
    elif w > h:
        font_size = h
    else:
        font_size = h

    font = ImageFont.truetype("arial.ttf", int(font_size / 12))

    draw.text((h / 4, w / 6), "watermark", fill=(255, 255, 255, 100), font=font, anchor="ms")
    combined = Image.alpha_composite(image, txt)
    converted = combined.convert("RGB")

    converted.save("watermarked.jpg")

    label.configure(text="Watermark Saved successfully!!!")


def openFile():
    # selecting the file using the askopenfilename() method of filedialog
    the_file = fd.askopenfilename(
        title="Select a file of any type",
        filetypes=[("Images", "*.jpg*")]
    )

    image = Image.open(the_file)
    # Calculate the aspect ratio of the image
    width, height = image.size
    aspect_ratio = width / height
    # Determine the new dimensions to fit within 300x300 canvas
    new_width, new_height = 300, int(300 / aspect_ratio)
    # Resize the image while maintaining the aspect ratio
    image = image.resize((new_width, new_height), Image.ANTIALIAS)
    # Create a PhotoImage from the resized image
    photo = ImageTk.PhotoImage(image)
    # Display the image on the canvas
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.photo = photo

    create_watermark_button = Button(text="Put Watermark", command=lambda: add_watermark(the_file))
    create_watermark_button.grid(row=3, column=2)


window = Tk()
window.title("Add watermark to your Image")
window.config(padx=100, pady=100, bg=YELLOW)

label = Label(text="Select your image", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg="black")
label.grid(row=0, column=1, columnspan=2)

canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=2)

spacer = Label(text="", pady=10)
spacer.grid(row=2, column=1)

button = Button(text="Select File", command=openFile)
button.grid(row=3, column=1)

window.mainloop()
