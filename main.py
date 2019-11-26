import cv2
import sys
import pytesseract
from PIL import Image, ImageTk
import tkinter as tk


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python ocr_simple.py image.jpg')
        sys.exit(1)

    imPath = sys.argv[1]

    # Define config parameters.
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    config = ('-l tur --oem 1 --psm 3')

    im = cv2.imread(imPath, cv2.IMREAD_COLOR)

    text = pytesseract.image_to_string(im, config=config)


root = tk.Tk()
############ IMAGE MANIPULATION AND ADDITION ################

basewidth = 10
image = Image.open(imPath)
wpercent = (basewidth/float(image.size[0]))
hsize = int((float(image.size[1])*float(wpercent)))
img = image.resize((basewidth,hsize), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# image = Image.open(imPath)
# resize_image = image.resize((500,200),Image.ANTIALIAS)


image1 = tk.Text(root, height=40, width=80)
image1.insert(tk.END, '\n')
image1.image_create(tk.END, image=photo)

image1.pack(side=tk.LEFT)

text2 = tk.Text(root, height=40, width=80)
scroll = tk.Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)

text2.tag_configure('bold_italics', font=('Arial', 15, 'bold', 'italic'))

text2.tag_configure('big', font=('Verdana', 20, 'bold'))

text2.tag_configure('color', font=('Tempus Sans ITC', 15))



text2.insert(tk.END, text, 'color')
text2.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()





    # print(text)