from tkinter import Tk
from image_watermark import ImageWatermark


root = Tk()
root.title("Image Watermark Maker")
root.config(width=500, height=400, bg=BG_COLOR)
root.resizable(False, False)
center_window(root)


choose_image_label = Label(
    root,
    text="Choose an image to work on:",
    padx=10,
    pady=10,
    bg=BG_COLOR,
    foreground=WHITE,
    font=FONT
)
choose_image_label.grid(row=0, column=0, pady=10, sticky='W')

filename = ""

btn_choose_image = Button(
    root,
    text="Choose Image",
    command=choose_image,
    bg=BG_COLOR,
    foreground=WHITE,
    font=FONT
)
btn_choose_image.grid(row=0, column=1, pady=10, sticky='W')

image_label = Label(
    root,
    padx=10,
    pady=10,
    width=30,
    height=10,
    bg=BG_COLOR)
image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

text_to_add_label = Label(
    root,
    text="Watermark text to add:",
    bg=BG_COLOR,
    foreground=WHITE,
    font=FONT
)
text_to_add_label.grid(row=2, column=0, pady=10, padx=10, sticky='W')

text_to_add = Entry(root, width=15, font=FONT)
text_to_add.grid(row=2, column=1, pady=10, sticky='W')

btn_add_watermark = Button(
    root,
    text='Add Watermark',
    command=make_watermark,
    bg=BG_COLOR,
    foreground=WHITE,
    font=FONT
)
btn_add_watermark.grid(row=3, column=0, columnspan=2)


root.mainloop()
