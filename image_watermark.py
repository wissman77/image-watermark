from tkinter import Frame, Label, Button, Entry, messagebox, StringVar
from tkinter.filedialog import askopenfilename, asksaveasfile
from PIL import Image, ImageTk, ImageDraw, ImageFont


# Color and font constants
BG_COLOR = '#42855B'
WHITE = '#FFFFFF'
FONT = ('Arial', 16)
YELLOW = (255, 255, 0)


class ImageWatermark:

    def __init__(self, root):

        root.title("Image Watermark Maker")
        root.config(width=500, height=400, bg=BG_COLOR)
        root.resizable(False, False)
        self.center_window(root)

        self.filename = ""

        self.frame = Frame(root, bg=BG_COLOR).grid(
            row=0, column=0, sticky=('N', 'W', 'E', 'S'))

        Label(
            self.frame,
            text="Choose an image to work on:",
            padx=10,
            pady=10,
            foreground=WHITE,
            bg=BG_COLOR,
            font=FONT
        ).grid(row=0, column=0, pady=10, sticky='W')

        Button(
            self.frame,
            text="Choose Image",
            command=self.choose_image,
            bg=BG_COLOR,
            foreground=WHITE,
            font=FONT
        ).grid(row=0, column=1, pady=10, sticky='W')

        self.image_label = Label(
            self.frame,
            padx=10,
            pady=10,
            width=30,
            height=10,
            bg=BG_COLOR
        ).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        Label(
            self.frame,
            text="Watermark text to add:",
            bg=BG_COLOR,
            foreground=WHITE,
            font=FONT
        ).grid(row=2, column=0, pady=10, padx=10, sticky='W')

        self.text_to_add = StringVar()

        Entry(self.frame, width=15, font=FONT, textvariable=self.text_to_add).grid(
            row=2, column=1, pady=10, sticky='W')

        Button(
            self.frame,
            text='Add Watermark',
            command=self.make_watermark,
            bg=BG_COLOR,
            foreground=WHITE,
            font=FONT
        ).grid(row=3, column=0, columnspan=2)

    def center_window(self, win):
        """ Centeres the main window using geometry """

        width = win.winfo_screenwidth()

        height = win.winfo_screenheight()

        x = int((width/2) - (win['width']/2))
        y = int((height/2) - (win['height']/2))

        win.geometry(f"{win['width']}x{win['height']}+{x}+{y}")

    def resize_image(self, img):
        """ Resize the pillow image object """

        width, height = img.size
        ratio = height / width
        img = img.resize((300, int(300 * ratio)))
        return img

    def choose_image(self):
        """ opens a open file dialog to choose an image, resize the image and show it in a label object  """

        file_types = (
            ('JPEG File', '*jpg'),
            ('PNG File', '*png')
        )
        self.filename = askopenfilename(
            title='Open Image File',
            initialdir='/',
            filetypes=file_types
        )

        if not self.filename:
            return

        with Image.open(self.filename) as image_to_edit:
            image_to_edit = self.resize_image(image_to_edit)
            image_to_edit = ImageTk.PhotoImage(image_to_edit)
            self.image_label = Label(
                self.frame, image=image_to_edit, padx=10, pady=10)
            self.image_label.image = image_to_edit
            self.image_label.grid(row=1, column=0, columnspan=2)

    def make_watermark(self):
        """ write a text on the image  """

        text = self.text_to_add.get()
        if not text:
            return messagebox.showinfo(title='add watermark',
                                       message='Enter a text to draw on the image')
        if not self.filename:
            return messagebox.showinfo(title='Choose Image',
                                       message='Choose Image to add a watermark on')
        with Image.open(self.filename) as img:
            img = img.convert('RGB')
            fnt = ImageFont.truetype('Gidole-Regular.ttf', size=120)
            image_draw = ImageDraw.Draw(img)
            image_draw.text((10, 10), text, YELLOW, font=fnt)
            image_to_save = img
            img = self.resize_image(img)
            new_img = ImageTk.PhotoImage(image=img)
            self.image_label = Label(
                self.frame, image=new_img, padx=10, pady=10)
            self.image_label.image = new_img
            self.image_label.grid(row=1, column=0, columnspan=2)
            new_filename = asksaveasfile(
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
