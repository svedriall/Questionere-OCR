import cv2
import sys
import pytesseract
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfilename

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ///////////// GUI \\\\\\\\\\\\\\\\
root = tk.Tk()
config = ('-l tur --oem 1 --psm 3')

def selector():
    global root, imPath, scaled_image, img, img_width_percent,img_width, text, image
    imPath = askopenfilename()
    print(imPath)
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)
    text = pytesseract.image_to_string(im, config=config)

    img_width = 500
    image = Image.open(imPath) # GORSEL BURADA ALINIYOR
    img_width_percent = (img_width / float(image.size[0]))
    img_height_size = int((float(image.size[1]) * float(img_width_percent)))
    img = image.resize((img_width, img_height_size), Image.ANTIALIAS)
    scaled_image = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=scaled_image) # IMAGE BURADAN GELIYOR
    panel.grid(row=0,column=0)
    # image1 = tk.Label(root, image=scaled_image)
    # image1.pack(side=tk.LEFT)
    text2 = tk.Text(root, height=30, width=50)
    text2.insert(tk.END, text)
    text2.config(state="disabled",font=("Times New Roman",14))
    text2.grid(row=0,column=1)
    return imPath, scaled_image


SelectButton = tk.Button(root, text="Dosya Seç", command=selector)
SelectButton.grid(row=1,column=1)

root.mainloop()