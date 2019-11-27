import cv2
import sys
import pytesseract
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from googletrans import Translator


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ///////////// GUI \\\\\\\\\\\\\\\\
root = tk.Tk()
config = ('-l tur --oem 1 --psm 3 ')

def selector():
    global root, imPath, scaled_image, img, img_width_percent,img_width, text, image
    imPath = askopenfilename()
    print(imPath)
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)
    text = pytesseract.image_to_string(im, config=config) # ASIL İŞLENEN GÖRÜNTÜ BURADA

    translator = Translator()
    translations = translator.translate(text)

    img_width = 500 # GÖRSELİN MAX GENİŞLİĞİ
    image = Image.open(imPath) # GORSEL BURADA ALINIYOR
    img_width_percent = (img_width / float(image.size[0]))
    img_height_size = int((float(image.size[1]) * float(img_width_percent)))
    img = image.resize((img_width, img_height_size), Image.ANTIALIAS)
    scaled_image = ImageTk.PhotoImage(img)

    label_photo = tk.Label(root,text="OCR Photo")
    label_OCR_out = tk.Label(root, text="OCR Text")
    label_Translation = tk.Label(root, text="OCR Translation")

    label_photo.grid(row=0,column=0)
    label_OCR_out.grid(row=0, column=1)
    label_Translation.grid(row=0, column=2)

    panel = tk.Label(root, image=scaled_image) # Previw IMAGE BURADAN GELIYOR
    panel.grid(row=1,column=0)

    text2 = tk.Text(root, height=30, width=70)
    text2.insert(tk.END, text) # TEXT BURADA TK'YA INSERT EDILIYOR
    text2.config(state="disabled",font=("Times New Roman",14))
    text2.grid(row=1,column=1)

    text3 = tk.Text(root, height=30, width=70)
    text3.insert(tk.END, translations.text) # ÇEVRİLMİŞ TEXT BURADA GELİYOR
    text3.config(state="disabled",font=("Times New Roman",14))
    text3.grid(row=1,column=2)

    return imPath, scaled_image


SelectButton = tk.Button(root, text="Dosya Seç", command=selector)
SelectButton.grid(row=2,column=1)

root.mainloop()