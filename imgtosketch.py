import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mgbx
import cv2

def convert():
        src = src_location.get()
        dest = dest_location.get()
        image = cv2.imread(src)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        inverted = 255 - gray
        blur = cv2.GaussianBlur(inverted, (21, 21), 0)
        inverted_blur = 255 - blur
        sketch = cv2.divide(gray, inverted_blur, scale = 256.0)
        try:
                cv2.imwrite(dest+r"/sketch.png", sketch)
                mgbx.showinfo("Done", "Successful!")
        except:
                mgbx.showerror("Error", "The image was not converted!")

def browse_img():
        app.files_list = list(filedialog.askopenfilenames(initialdir =r"C:\Users\harsh\OneDrive\Pictures"))
        sourceText.insert('1', app.files_list)
def browse_dest():
        destinationdirectory = filedialog.askdirectory(initialdir =r"C:\Users\harsh\OneDrive\Pictures")
        destinationText.insert('1', destinationdirectory)

app = tk.Tk()
app.geometry("500x500")
app.title("Img to Sketch")

src_location = StringVar()
dest_location = StringVar()

heading = Label(app, text="Python Image to Sketch App",
                bg="purple", fg = "white", font=("Algerian",24),
                width="500", height="3")
heading.pack()

l1 = Label(text="Select the image to convert : ",
           font=("Algerian",18))
l1.place(x=20, y=150)
sourceText = Entry(width=40, textvariable=src_location,
                   font=18)
sourceText.place(x=20, y=190)
src_browse = Button(text="Browse", font=("ALgerian",18),
                    command=browse_img)
src_browse.place(x=300, y=230)

l2 = Label(text="Select the destination : ",
           font=("Algerian",18))
l2.place(x=20, y=280)
destinationText = Entry(width=40, textvariable=dest_location,
                   font=18)
destinationText.place(x=20, y=320)
dest_browse = Button(text="Browse", font=("ALgerian",18),
                    command=browse_dest)
dest_browse.place(x=300, y=360)

con = Button(text="Convert", font=("Algerian",18),
             command=convert)
con.place(x=100, y=430)

mainloop()
