import numpy as np
import cv2 as cv
from tkinter import ttk
from tkinter import *
from PIL import ImageTk
import PIL
import mahotas
import mahotas.demos

class MainSolution():
    def __init__(self):
      self.picfiltr = cv.imread('filtr.jpg',cv.IMREAD_GRAYSCALE)
      self.segm = cv.imread('segm.jpg',cv.IMREAD_GRAYSCALE)

    def filtr(self):
      median_image = cv.medianBlur(self.picfiltr,7)
      median_image = PIL.Image.fromarray(median_image)
      median_image = median_image.resize((300, 300))
      size = (3,3)
      shape = cv.MORPH_RECT
      kernel = cv.getStructuringElement(shape, size)
      min_image = cv.erode(self.picfiltr, kernel)
      max_image = cv.dilate(self.picfiltr, kernel)
      min_image = PIL.Image.fromarray(min_image)
      min_image = min_image.resize((300, 300))
      max_image = PIL.Image.fromarray(max_image)
      max_image = max_image.resize((300, 300))
      return ImageTk.PhotoImage(median_image),ImageTk.PhotoImage(min_image),ImageTk.PhotoImage(max_image)
      
    def getorig(self):
      img = PIL.Image.fromarray(self.picfiltr)
      img = img.resize((300, 300))
      img2 = PIL.Image.fromarray(self.segm)
      img2 = img2.resize((300, 300))
      return ImageTk.PhotoImage(img),ImageTk.PhotoImage(img2)

    def adaptivethresholding(self):
      th3 = cv.adaptiveThreshold(self.segm,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
      img = PIL.Image.fromarray(th3)
      img = img.resize((300, 300))
      return ImageTk.PhotoImage(img)

    def bernsenthresholding(self):
      img = self.segm
      img = mahotas.thresholding.bernsen(img, 5, 15)
      img = PIL.Image.fromarray(img)
      img = img.resize((300, 300))
      return ImageTk.PhotoImage(img)

    def niblackthreshholding(self):
      img = cv.imread('segm.jpg',cv.IMREAD_GRAYSCALE)
      img = cv.ximgproc.niBlackThreshold(img,maxValue = 255,type =  cv.THRESH_BINARY,  blockSize = 15, k = -0.2)
      img = PIL.Image.fromarray(img)
      img = img.resize((300, 300))
      return ImageTk.PhotoImage(img)


if __name__ == "__main__":
    root = Tk()
    ms = MainSolution()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"1250x700")
    lbl_text1 = ttk.Label(text="Реализация нелинейных фильтров")
    lbl_text1.place(x=590, y=10)
    lbl_text2 = ttk.Label(text="Оригинал")
    lbl_text2.place(x=110, y=350)
    lbl_text3 = ttk.Label(text="Медианный фильтр")
    lbl_text3.place(x=410, y=350)
    lbl_text4 = ttk.Label(text="Фильтр минимума")
    lbl_text4.place(x=740, y=350)
    lbl_text5 = ttk.Label(text="Фильтр максимума")
    lbl_text5.place(x=1050, y=350)
    lbl_text6 = ttk.Label(text="Оригинал")
    lbl_text6.place(x=110, y=370)
    lbl_text7 = ttk.Label(text="Метод Бернсена")
    lbl_text7.place(x=410, y=370)
    lbl_text8 = ttk.Label(text="Метод Ниблацка")
    lbl_text8.place(x=740, y=370)
    lbl_text9 = ttk.Label(text="Адаптивная пороговая обработка")
    lbl_text9.place(x=1000, y=370)
    img1,img3,img4 = ms.filtr()
    lbl1 = ttk.Label(image=img1)
    lbl1.image = img1
    lbl1.place(x=310, y=40, width=300, height=300)
    img2,img6 = ms.getorig()
    lbl2 = ttk.Label(image=img2)
    lbl2.image = img2
    lbl2.place(x=10, y=40, width=300, height=300)
    lbl3 = ttk.Label(image=img3)
    lbl3.image = img3
    lbl3.place(x=630, y=40, width=300, height=300)
    lbl4 = ttk.Label(image=img4)
    lbl4.image = img4
    lbl4.place(x=940, y=40, width=300, height=300)
    img5 = ms.bernsenthresholding()
    lbl5 = ttk.Label(image=img5)
    lbl5.image = img5
    lbl5.place(x=310, y=390, width=300, height=300)
    lbl6 = ttk.Label(image=img6)
    lbl6.image = img6
    lbl6.place(x=10, y=390, width=300, height=300)
    img7 = ms.niblackthreshholding()
    lbl7 = ttk.Label(image=img7)
    lbl7.image = img7
    lbl7.place(x=630, y=390, width=300, height=300)
    img8 = ms.adaptivethresholding()
    lbl8 = ttk.Label(image=img8)
    lbl8.image = img8
    lbl8.place(x=940, y=390, width=300, height=300)
    root.mainloop()