from tkinter import Tk, Label, Button, Entry, END, messagebox, filedialog as fd
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Color and font constants
BG_COLOR = '#2F801B'
WHITE = '#FFFFFF'
FONT = ('Arial', 16)
YELLOW = (255, 255, 0)


def center_window(win: Tk):
    """ Centeres the main window using geometry """

    width = win.winfo_screenwidth()

    height = win.winfo_screenheight()

    x = int((width/2) - (win['width']/2))
    y = int((height/2) - (win['height']/2))

    win.geometry(f"{win['width']}x{win['height']}+{x}+{y}")


def resize_image(img):
    """ Resize the pillow image object """

    width, height = img.size
    ratio = height / width
    img = img.resize((300, int(300 * ratio)))
    return img


def choose_image():
    """ opens a open file dialog to choose an image, resize the image and show it in a label object  """

    global filename
    file_types = (
        ('JPEG File', '*jpg'),
        ('PNG File', '*png')
    )
    filename = fd.askopenfilename(
        title='Open Image File',
        initialdir='/',
        filetypes=file_types
    )

    if not filename:
        return

    with Image.open(filename) as image_to_edit:
        image_to_edit = resize_image(image_to_edit)
        image_to_edit = ImageTk.PhotoImage(image_to_edit)
        image_label = Label(root, image=image_to_edit, padx=10, pady=10)
        image_label.image = image_to_edit
        image_label.grid(row=1, column=0, columnspan=2)


def make_watermark():
    """ write a text on the image  """
    global filename
    text = text_to_add.get()
    if text == '':
        return messagebox.showinfo(title='add watermark',
                                   message='Enter a text to draw on the image')
    if not filename:
        return messagebox.showerror(title='Choose Image',
                                    message='Choose Image to add a watermark on')
    with Image.open(filename) as img:
        img = img.convert('RGB')
        fnt = ImageFont.truetype('Gidole-Regular.ttf', size=120)
        image_draw = ImageDraw.Draw(img)
        image_draw.text((10, 10), text, YELLOW, font=fnt)
        image_to_save = img
        img = resize_image(img)
        new_img = ImageTk.PhotoImage(image=img)
        image_label = Label(root, image=new_img, padx=10, pady=10)
        image_label.image = new_img
        image_label.grid(row=1, column=0, columnspan=2)
        new_filename = fd.asksaveasfile(
            initialfile='Untitiled.jpg',
            defaultextension='.jpg',
            filetypes=[
                ('All Files', '*.*'),
                ('JPG File', '*.jpg'),
                ('PNG File', '*.png')
            ]
        )

        if not new_filename:
            return
        image_to_save.save(new_filename)


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
