import sys

import Sorular
import time

import tanimlar
import pygame

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import tanimlar


def show_frame(frame):
    if frame == oyunFrame1:
        time.sleep(0.1)
        messagebox.showinfo("!!!!", "Göreviniz Astroitlere Çarpmadan Mars Uzay Üssüne Gitmeniz")
        import uzayOyun
        frame.tkraise()
    time.sleep(0.1)
    frame.tkraise()

Puan = [0]
def soru1Degerlendirme():
    if soru1StringVar.get() == "1":
        pass
    elif soru1StringVar.get() == "2":
        Puan[0] += 10
    elif soru1StringVar.get() == "3":
        pass
    elif soru1StringVar.get() == "4":
        pass
    show_frame(soruFrame2)
def soru2Degerlendirme():
    if soru2StringVar.get() == "1":
        pass
    elif soru2StringVar.get() == "2":
        pass
    elif soru2StringVar.get() == "3":
        pass
    elif soru2StringVar.get() == "4":
        Puan[0] += 10
    show_frame(soruFrame3)
def soru3Degerlendirme():
    if soru3StringVar.get() == "1":
        pass
    elif soru3StringVar.get() == "2":
        pass
    elif soru3StringVar.get() == "3":
        Puan[0] += 10
    elif soru3StringVar.get() == "4":
        pass
    show_frame(soruFrame4)
def soru4Degerlendirme():
    if soru4StringVar.get() == "1":
        pass
    elif soru4StringVar.get() == "2":
        pass
    elif soru4StringVar.get() == "3":
        Puan[0] += 10
    elif soru4StringVar.get() == "4":
        pass
    show_frame(soruFrame5)
def soru5Degerlendirme():
    if soru5StringVar.get() == "1":
        pass
    elif soru5StringVar.get() == "2":
        Puan[0] += 10
    elif soru5StringVar.get() == "3":
        pass
    elif soru5StringVar.get() == "4":
        pass
    show_frame(soruFrame6)
def soru6Degerlendirme():
    if soru6StringVar.get() == "1":
        pass
    elif soru6StringVar.get() == "2":
        Puan[0] += 10
    elif soru6StringVar.get() == "3":
        pass
    elif soru6StringVar.get() == "4":
        pass
    show_frame(soruFrame7)
def soru7Degerlendirme():
    if soru7StringVar.get() == "1":
        pass
    elif soru7StringVar.get() == "2":
        pass
    elif soru7StringVar.get() == "3":
        Puan[0] += 10
    elif soru7StringVar.get() == "4":
        pass
    show_frame(soruFrame8)
def soru8Degerlendirme():
    if soru8StringVar.get() == "1":
        pass
    elif soru8StringVar.get() == "2":
        pass
    elif soru8StringVar.get() == "3":
        Puan[0] += 10
    elif soru8StringVar.get() == "4":
        pass
    show_frame(soruFrame9)
def soru9Degerlendirme():
    if soru9StringVar.get() == "1":
        Puan[0] += 10
    elif soru9StringVar.get() == "2":
        pass
    elif soru9StringVar.get() == "3":
        pass
    elif soru9StringVar.get() == "4":
        pass
    show_frame(soruFrame10)
def soru10Degerlendirme():
    if soru10StringVar.get() == "1":
        pass
    elif soru10StringVar.get() == "2":
        pass
    elif soru10StringVar.get() == "3":
        Puan[0] += 10
    elif soru10StringVar.get() == "4":
        pass
    puan = Puan[0]
    time.sleep(0.2)
    messagebox.showinfo("Puanınız", puan)
    Puan[0] = 0
    soru1StringVar.set(0)
    soru2StringVar.set(0)
    soru3StringVar.set(0)
    soru4StringVar.set(0)
    soru5StringVar.set(0)
    soru6StringVar.set(0)
    soru7StringVar.set(0)
    soru8StringVar.set(0)
    soru9StringVar.set(0)
    soru10StringVar.set(0)
    show_frame(oyunFrame)
def cikis():
    cevap = messagebox.askquestion("!!!", "Uygulamadan çıkılsın mı? ")
    if cevap == 'yes':
        sys.exit(0)
    elif cevap == 'no':
        pass
    else:
        pass
root = Tk()
root.geometry('800x600+400+150')
root.title("Evren")
root.resizable(False, False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
# Frame's **************************************************************************************************************
menuFrame = Frame(root)
samanyoluFrame = Frame(root)
andromedaFrame = Frame(root)
siyahgozFrame = Frame(root)
ngc221Frame = Frame(root)
ngc628Frame = Frame(root)
ngc4321Frame = Frame(root)
ngc205Frame = Frame(root)
yildizFrame1 = Frame(root)
yildizFrame2 = Frame(root)
yildizFrame3 = Frame(root)
yildizFrame4 = Frame(root)
yildizFrame5 = Frame(root)
yildizFrame6 = Frame(root)
yildizFrame7 = Frame(root)
yildizFrame8 = Frame(root)
yildizFrame9 = Frame(root)
gezegenFrame1 = Frame(root)
gezegenFrame2 = Frame(root)
gezegenFrame3 = Frame(root)
gezegenFrame4 = Frame(root)
gezegenFrame5 = Frame(root)
gezegenFrame6 = Frame(root)
gezegenFrame7 = Frame(root)
oyunFrame = Frame(root)
oyunFrame1 = Frame(root)
oyunFrame2 = Frame(root)
soruFrame1 = Frame(root)
soruFrame2 = Frame(root)
soruFrame3 = Frame(root)
soruFrame4 = Frame(root)
soruFrame5 = Frame(root)
soruFrame6 = Frame(root)
soruFrame7 = Frame(root)
soruFrame8 = Frame(root)
soruFrame9 = Frame(root)
soruFrame10 = Frame(root)

# **********************************************************************************************************************

for frame in (menuFrame, samanyoluFrame, andromedaFrame, siyahgozFrame, ngc221Frame, ngc628Frame, ngc205Frame, ngc4321Frame,  yildizFrame1, yildizFrame2, yildizFrame3, yildizFrame4, yildizFrame5, yildizFrame6, yildizFrame7, yildizFrame8, yildizFrame9, gezegenFrame1, gezegenFrame2, gezegenFrame3, gezegenFrame4, gezegenFrame5, gezegenFrame6, gezegenFrame7, oyunFrame, oyunFrame1, oyunFrame2, soruFrame1, soruFrame2, soruFrame3, soruFrame4, soruFrame5, soruFrame6, soruFrame7, soruFrame8, soruFrame9, soruFrame10):
    frame.grid(row=0, column=0, sticky="nsew")

#  menuFrame code ******************************************************************************************************

img1 = ImageTk.PhotoImage(Image.open("resimler/uzay.PNG"))
label = Label(menuFrame, image=img1)
label.place(x=0, y=0)

buton_evren = Button(menuFrame, text="Evren", bg="black", fg="white", font="Times", activebackground="white", activeforeground="black", command=lambda: show_frame(samanyoluFrame))
buton_evren.place(x=330, y=300, height=30, width=50)

buton_oyun = Button(menuFrame, text="Oyun", bg="black", fg="white", font="Times", activebackground="white", activeforeground="black", command=lambda: show_frame(oyunFrame))
buton_oyun.place(x=430, y=300, height=30, width=50)

buton_cikis = Button(menuFrame, text="Çıkıs", bg="black", fg="white", font="Times", activebackground="white", activeforeground="black", command=cikis)
buton_cikis.place(x=385, y=550, height=30, width=50)

# oyunFrame ************************************************************************************************************

img = ImageTk.PhotoImage(Image.open("resimler/uzay.PNG"))
label2 = Label(oyunFrame, image=img)
label2.place(x=0, y=0)

oyun1 = Button(oyunFrame, text="Uzay üssü", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(oyunFrame1))
oyun1.place(x=230, y=300, height=30, width=100)

oyun2 = Button(oyunFrame, text="Evreni ne kadar tanıyorsun", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(oyunFrame2))
oyun2.place(x=380, y=300, height=30, width=230)

anaMenuButon = Button(oyunFrame, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# oyunFrame1 ***********************************************************************************************************

oyunFrame1.config(bg="black")

# oyunFrame2 ***********************************************************************************************************

oyunFrame2.config(bg="black")

infoLabel = Label(oyunFrame2, text="10 TANE SORU SORULACAKTİR! HER SORU 10 PUAN", bg="black", fg="white", font="Times")
infoLabel.place(x=180, y=180)

baslaButon = Button(oyunFrame2, text="Hazırsan Tıkla", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(soruFrame1))
baslaButon.place(x=340, y=250)

# soruFrame1  **********************************************************************************************************

soruFrame1.config(bg="black")

soru1Label = Label(soruFrame1, text=Sorular.soru1, bg="black", fg="white", font="Times")
soru1Label.place(x=170, y=160)

soru1Cevap1Label = Label(soruFrame1, text=Sorular.soru1Cevap1, bg="black", fg="white", font="Times")
soru1Cevap1Label.place(x=170, y=220)

soru1Cevap2Label = Label(soruFrame1, text=Sorular.soru1Cevap2, bg="black", fg="white", font="Times")
soru1Cevap2Label.place(x=170, y=250)

soru1Cevap3Label = Label(soruFrame1, text=Sorular.soru1Cevap3, bg="black", fg="white", font="Times")
soru1Cevap3Label.place(x=170, y=280)

soru1Cevap4Label = Label(soruFrame1, text=Sorular.soru1Cevap4, bg="black", fg="white", font="Times")
soru1Cevap4Label.place(x=170, y=310)

soru1StringVar = StringVar()

radioButon1Cevap1 = Radiobutton(soruFrame1, text="", value=1, bg="black", variable=soru1StringVar)
radioButon1Cevap1.place(x=140, y=220)

radioButon1Cevap2 = Radiobutton(soruFrame1, text="", value=2, bg="black", variable=soru1StringVar)
radioButon1Cevap2.place(x=140, y=250)

radioButon1Cevap3 = Radiobutton(soruFrame1, text="", value=3, bg="black", variable=soru1StringVar)
radioButon1Cevap3.place(x=140, y=280)

radioButon1Cevap4 = Radiobutton(soruFrame1, text="", value=4, bg="black", variable=soru1StringVar)
radioButon1Cevap4.place(x=140, y=310)

soru1GecButton = Button(soruFrame1, text="->", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=soru1Degerlendirme)
soru1GecButton.place(x=600, y=400)

# soruFrame2  **********************************************************************************************************

soruFrame2.config(bg="black")

soru2Label = Label(soruFrame2, text=Sorular.soru2, bg="black", fg="white", font="Times")
soru2Label.place(x=170, y=160)

soru2Cevap1Label = Label(soruFrame2, text=Sorular.soru2Cevap1, bg="black", fg="white", font="Times")
soru2Cevap1Label.place(x=170, y=220)

soru2Cevap2Label = Label(soruFrame2, text=Sorular.soru2Cevap2, bg="black", fg="white", font="Times")
soru2Cevap2Label.place(x=170, y=250)

soru2Cevap3Label = Label(soruFrame2, text=Sorular.soru2Cevap3, bg="black", fg="white", font="Times")
soru2Cevap3Label.place(x=170, y=280)

soru2Cevap4Label = Label(soruFrame2, text=Sorular.soru2Cevap4, bg="black", fg="white", font="Times")
soru2Cevap4Label.place(x=170, y=310)

soru2StringVar = StringVar()

radioButon2Cevap1 = Radiobutton(soruFrame2, text="", value=1, bg="black", variable=soru2StringVar)
radioButon2Cevap1.place(x=140, y=220)

radioButon2Cevap2 = Radiobutton(soruFrame2, text="", value=2, bg="black", variable=soru2StringVar)
radioButon2Cevap2.place(x=140, y=250)

radioButon2Cevap3 = Radiobutton(soruFrame2, text="", value=3, bg="black", variable=soru2StringVar)
radioButon2Cevap3.place(x=140, y=280)

radioButon2Cevap4 = Radiobutton(soruFrame2, text="", value=4, bg="black", variable=soru2StringVar)
radioButon2Cevap4.place(x=140, y=310)

soru2GecButton = Button(soruFrame2, text="->", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=soru2Degerlendirme)
soru2GecButton.place(x=600, y=400)

# soruFrame3  **********************************************************************************************************

soruFrame3.config(bg="black")

soru3Label = Label(soruFrame3, text=Sorular.soru3, bg="black", fg="white", font="Times")
soru3Label.place(x=170, y=160)

soru3Secenek1Label = Label(soruFrame3, text=Sorular.soru3Secenek1, bg="black", fg="white", font="Times")
soru3Secenek1Label.place(x=170, y=220)

soru3Secenek2Label = Label(soruFrame3, text=Sorular.soru3Secenek2, bg="black", fg="white", font="Times")
soru3Secenek2Label.place(x=170, y=250)

soru3Secenek3Label = Label(soruFrame3, text=Sorular.soru3Secenek3, bg="black", fg="white", font="Times")
soru3Secenek3Label.place(x=170, y=280)

soru3Secenek4Label = Label(soruFrame3, text=Sorular.soru3Secenek4, bg="black", fg="white", font="Times")
soru3Secenek4Label.place(x=170, y=310)


soru3Cevap1Label = Label(soruFrame3, text=Sorular.soru3Cevap1, bg="black", fg="white", font="Times")
soru3Cevap1Label.place(x=200, y=355)

soru3Cevap2Label = Label(soruFrame3, text=Sorular.soru3Cevap2, bg="black", fg="white", font="Times")
soru3Cevap2Label.place(x=200, y=385)

soru3Cevap3Label = Label(soruFrame3, text=Sorular.soru3Cevap3, bg="black", fg="white", font="Times")
soru3Cevap3Label.place(x=200, y=415)

soru3Cevap4Label = Label(soruFrame3, text=Sorular.soru3Cevap4, bg="black", fg="white", font="Times")
soru3Cevap4Label.place(x=200, y=445)

soru3StringVar = StringVar()

radioButon3Cevap1 = Radiobutton(soruFrame3, text="", value=1, bg="black", variable=soru3StringVar)
radioButon3Cevap1.place(x=170, y=355)

radioButon3Cevap2 = Radiobutton(soruFrame3, text="", value=2, bg="black", variable=soru3StringVar)
radioButon3Cevap2.place(x=170, y=385)

radioButon3Cevap3 = Radiobutton(soruFrame3, text="", value=3, bg="black", variable=soru3StringVar)
radioButon3Cevap3.place(x=170, y=415)

radioButon3Cevap4 = Radiobutton(soruFrame3, text="", value=4, bg="black", variable=soru3StringVar)
radioButon3Cevap4.place(x=170, y=445)

soru3GecButton = Button(soruFrame3, text="->", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=soru3Degerlendirme)
soru3GecButton.place(x=600, y=400)


# soruFrame4  **********************************************************************************************************

soruFrame4.config(bg="black")

soru4Label = Label(soruFrame4, text=Sorular.soru4, bg="black", fg="white", font="Times")
soru4Label.place(x=170, y=160)

soru4Cevap1Label = Label(soruFrame4, text=Sorular.soru4Cevap1, bg="black", fg="white", font="Times")
soru4Cevap1Label.place(x=170, y=220)

soru4Cevap2Label = Label(soruFrame4, text=Sorular.soru4Cevap2, bg="black", fg="white", font="Times")
soru4Cevap2Label.place(x=170, y=250)

soru4Cevap3Label = Label(soruFrame4, text=Sorular.soru4Cevap3, bg="black", fg="white", font="Times")
soru4Cevap3Label.place(x=170, y=280)

soru4Cevap4Label = Label(soruFrame4, text=Sorular.soru4Cevap4, bg="black", fg="white", font="Times")
soru4Cevap4Label.place(x=170, y=310)

soru4StringVar = StringVar()

radioButon4Cevap1 = Radiobutton(soruFrame4, text="", value=1, bg="black", variable=soru4StringVar)
radioButon4Cevap1.place(x=140, y=220)

radioButon4Cevap2 = Radiobutton(soruFrame4, text="", value=2, bg="black", variable=soru4StringVar)
radioButon4Cevap2.place(x=140, y=250)

radioButon4Cevap3 = Radiobutton(soruFrame4, text="", value=3, bg="black", variable=soru4StringVar)
radioButon4Cevap3.place(x=140, y=280)

radioButon4Cevap4 = Radiobutton(soruFrame4, text="", value=4, bg="black", variable=soru4StringVar)
radioButon4Cevap4.place(x=140, y=310)

soru4GecButton = Button(soruFrame4, text="->", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=soru4Degerlendirme)
soru4GecButton.place(x=600, y=400)

# soruFrame5  **********************************************************************************************************

soruFrame5.config(bg="black")

soru5Label = Label(soruFrame5, text=Sorular.soru5, bg="black", fg="white", font="Times")
soru5Label.place(x=170, y=160)

soru5Cevap1Label = Label(soruFrame5, text=Sorular.soru5Cevap1, bg="black", fg="white", font="Times")
soru5Cevap1Label.place(x=170, y=220)

soru5Cevap2Label = Label(soruFrame5, text=Sorular.soru5Cevap2, bg="black", fg="white", font="Times")
soru5Cevap2Label.place(x=170, y=250)

soru5Cevap3Label = Label(soruFrame5, text=Sorular.soru5Cevap3, bg="black", fg="white", font="Times")
soru5Cevap3Label.place(x=170, y=280)

soru5Cevap4Label = Label(soruFrame5, text=Sorular.soru5Cevap4, bg="black", fg="white", font="Times")
soru5Cevap4Label.place(x=170, y=310)

soru5StringVar = StringVar()

radioButon5Cevap1 = Radiobutton(soruFrame5, text="", value=1, bg="black", variable=soru5StringVar)
radioButon5Cevap1.place(x=140, y=220)

radioButon5Cevap2 = Radiobutton(soruFrame5, text="", value=2, bg="black", variable=soru5StringVar)
radioButon5Cevap2.place(x=140, y=250)

radioButon5Cevap3 = Radiobutton(soruFrame5, text="", value=3, bg="black", variable=soru5StringVar)
radioButon5Cevap3.place(x=140, y=280)

radioButon5Cevap4 = Radiobutton(soruFrame5, text="", value=4, bg="black", variable=soru5StringVar)
radioButon5Cevap4.place(x=140, y=310)

soru5GecButton = Button(soruFrame5, text="->", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=soru5Degerlendirme)
soru5GecButton.place(x=600, y=400)

# soruFrame6  **********************************************************************************************************

soruFrame6.config(bg="black")

soru6Label = Label(soruFrame6, text=Sorular.soru6, bg="black", fg="white", font="Times")
soru6Label.place(x=170, y=160)

soru6Cevap1Label = Label(soruFrame6, text=Sorular.soru6Cevap1, bg="black", fg="white", font="Times")
soru6Cevap1Label.place(x=170, y=220)

soru6Cevap2Label = Label(soruFrame6, text=Sorular.soru6Cevap2, bg="black", fg="white", font="Times")
soru6Cevap2Label.place(x=170, y=250)

soru6Cevap3Label = Label(soruFrame6, text=Sorular.soru6Cevap3, bg="black", fg="white", font="Times")
soru6Cevap3Label.place(x=170, y=280)

soru6Cevap4Label = Label(soruFrame6, text=Sorular.soru6Cevap4, bg="black", fg="white", font="Times")
soru6Cevap4Label.place(x=170, y=310)

soru6StringVar = StringVar()

radioButon6Cevap1 = Radiobutton(soruFrame6, text="", value=1, bg="black", variable=soru6StringVar)
radioButon6Cevap1.place(x=140, y=220)

radioButon6Cevap2 = Radiobutton(soruFrame6, text="", value=2, bg="black", variable=soru6StringVar)
radioButon6Cevap2.place(x=140, y=250)

radioButon6Cevap3 = Radiobutton(soruFrame6, text="", value=3, bg="black", variable=soru6StringVar)
radioButon6Cevap3.place(x=140, y=280)

radioButon6Cevap4 = Radiobutton(soruFrame6, text="", value=4, bg="black", variable=soru6StringVar)
radioButon6Cevap4.place(x=140, y=310)

soru6GecButton = Button(soruFrame6, text="->", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=soru6Degerlendirme)
soru6GecButton.place(x=600, y=400)


# soruFrame7  **********************************************************************************************************

soruFrame7.config(bg="black")

soru7Label = Label(soruFrame7, text=Sorular.soru7, bg="black", fg="white", font="Times")
soru7Label.place(x=170, y=160)

soru7Cevap1Label = Label(soruFrame7, text=Sorular.soru7Cevap1, bg="black", fg="white", font="Times")
soru7Cevap1Label.place(x=170, y=220)

soru7Cevap2Label = Label(soruFrame7, text=Sorular.soru7Cevap2, bg="black", fg="white", font="Times")
soru7Cevap2Label.place(x=170, y=250)

soru7Cevap3Label = Label(soruFrame7, text=Sorular.soru7Cevap3, bg="black", fg="white", font="Times")
soru7Cevap3Label.place(x=170, y=280)

soru7Cevap4Label = Label(soruFrame7, text=Sorular.soru7Cevap4, bg="black", fg="white", font="Times")
soru7Cevap4Label.place(x=170, y=310)

soru7StringVar = StringVar()

radioButon7Cevap1 = Radiobutton(soruFrame7, text="", value=1, bg="black", variable=soru7StringVar)
radioButon7Cevap1.place(x=140, y=220)

radioButon7Cevap2 = Radiobutton(soruFrame7, text="", value=2, bg="black", variable=soru7StringVar)
radioButon7Cevap2.place(x=140, y=250)

radioButon7Cevap3 = Radiobutton(soruFrame7, text="", value=3, bg="black", variable=soru7StringVar)
radioButon7Cevap3.place(x=140, y=280)

radioButon7Cevap4 = Radiobutton(soruFrame7, text="", value=4, bg="black", variable=soru7StringVar)
radioButon7Cevap4.place(x=140, y=310)

soru7GecButton = Button(soruFrame7, text="->", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=soru7Degerlendirme)
soru7GecButton.place(x=600, y=400)


# soruFrame8  **********************************************************************************************************

soruFrame8.config(bg="black")

soru8Label = Label(soruFrame8, text=Sorular.soru8, bg="black", fg="white", font="Times")
soru8Label.place(x=170, y=160)

soru8Cevap1Label = Label(soruFrame8, text=Sorular.soru8Cevap1, bg="black", fg="white", font="Times")
soru8Cevap1Label.place(x=170, y=220)

soru8Cevap2Label = Label(soruFrame8, text=Sorular.soru8Cevap2, bg="black", fg="white", font="Times")
soru8Cevap2Label.place(x=170, y=250)

soru8Cevap3Label = Label(soruFrame8, text=Sorular.soru8Cevap3, bg="black", fg="white", font="Times")
soru8Cevap3Label.place(x=170, y=280)

soru8Cevap4Label = Label(soruFrame8, text=Sorular.soru8Cevap4, bg="black", fg="white", font="Times")
soru8Cevap4Label.place(x=170, y=310)

soru8StringVar = StringVar()

radioButon8Cevap1 = Radiobutton(soruFrame8, text="", value=1, bg="black", variable=soru8StringVar)
radioButon8Cevap1.place(x=140, y=220)

radioButon8Cevap2 = Radiobutton(soruFrame8, text="", value=2, bg="black", variable=soru8StringVar)
radioButon8Cevap2.place(x=140, y=250)

radioButon8Cevap3 = Radiobutton(soruFrame8, text="", value=3, bg="black", variable=soru8StringVar)
radioButon8Cevap3.place(x=140, y=280)

radioButon8Cevap4 = Radiobutton(soruFrame8, text="", value=4, bg="black", variable=soru8StringVar)
radioButon8Cevap4.place(x=140, y=310)

soru8GecButton = Button(soruFrame8, text="->", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=soru8Degerlendirme)
soru8GecButton.place(x=600, y=400)

# soruFrame9  **********************************************************************************************************

soruFrame9.config(bg="black")

soru9Label = Label(soruFrame9, text=Sorular.soru9, bg="black", fg="white", font="Times")
soru9Label.place(x=170, y=160)

soru9Cevap1Label = Label(soruFrame9, text=Sorular.soru9Cevap1, bg="black", fg="white", font="Times")
soru9Cevap1Label.place(x=170, y=220)

soru9Cevap2Label = Label(soruFrame9, text=Sorular.soru9Cevap2, bg="black", fg="white", font="Times")
soru9Cevap2Label.place(x=170, y=250)

soru9Cevap3Label = Label(soruFrame9, text=Sorular.soru9Cevap3, bg="black", fg="white", font="Times")
soru9Cevap3Label.place(x=170, y=280)

soru9Cevap4Label = Label(soruFrame9, text=Sorular.soru9Cevap4, bg="black", fg="white", font="Times")
soru9Cevap4Label.place(x=170, y=310)

soru9StringVar = StringVar()

radioButon9Cevap1 = Radiobutton(soruFrame9, text="", value=1, bg="black", variable=soru9StringVar)
radioButon9Cevap1.place(x=140, y=220)

radioButon9Cevap2 = Radiobutton(soruFrame9, text="", value=2, bg="black", variable=soru9StringVar)
radioButon9Cevap2.place(x=140, y=250)

radioButon9Cevap3 = Radiobutton(soruFrame9, text="", value=3, bg="black", variable=soru9StringVar)
radioButon9Cevap3.place(x=140, y=280)

radioButon9Cevap4 = Radiobutton(soruFrame9, text="", value=4, bg="black", variable=soru9StringVar)
radioButon9Cevap4.place(x=140, y=310)

soru9GecButton = Button(soruFrame9, text="->", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=soru9Degerlendirme)
soru9GecButton.place(x=600, y=400)

# soruFrame10  **********************************************************************************************************

soruFrame10.config(bg="black")

soru10Label = Label(soruFrame10, text=Sorular.soru10, bg="black", fg="white", font="Times")
soru10Label.place(x=170, y=160)

soru10Cevap1Label = Label(soruFrame10, text=Sorular.soru10Cevap1, bg="black", fg="white", font="Times")
soru10Cevap1Label.place(x=170, y=220)

soru10Cevap2Label = Label(soruFrame10, text=Sorular.soru10Cevap2, bg="black", fg="white", font="Times")
soru10Cevap2Label.place(x=170, y=250)

soru10Cevap3Label = Label(soruFrame10, text=Sorular.soru10Cevap3, bg="black", fg="white", font="Times")
soru10Cevap3Label.place(x=170, y=280)

soru10Cevap4Label = Label(soruFrame10, text=Sorular.soru10Cevap4, bg="black", fg="white", font="Times")
soru10Cevap4Label.place(x=170, y=310)

soru10StringVar = StringVar()

radioButon10Cevap1 = Radiobutton(soruFrame10, text="", value=1, bg="black", variable=soru10StringVar)
radioButon10Cevap1.place(x=140, y=220)

radioButon10Cevap2 = Radiobutton(soruFrame10, text="", value=2, bg="black", variable=soru10StringVar)
radioButon10Cevap2.place(x=140, y=250)

radioButon10Cevap3 = Radiobutton(soruFrame10, text="", value=3, bg="black", variable=soru10StringVar)
radioButon10Cevap3.place(x=140, y=280)

radioButon10Cevap4 = Radiobutton(soruFrame10, text="", value=4, bg="black", variable=soru10StringVar)
radioButon10Cevap4.place(x=140, y=310)

soru10GecButton = Button(soruFrame10, text="Bitir", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=soru10Degerlendirme)
soru10GecButton.place(x=600, y=400)

#  samanyoluFrame  *****************************************************************************************************

samanyoluFrame.config(bg="black")
img2 = ImageTk.PhotoImage(Image.open("resimler/samanyolugalaksi.jpg"))
label2 = Label(samanyoluFrame, image=img2)
label2.pack()
label3 = Label(samanyoluFrame, text="Samanyolu", bg="black", fg="white", font="Times")
label3.place(x=350, y=360)
text = Text(samanyoluFrame, height=12, width=40, bg="black", fg="white")
text.insert(END, tanimlar.samanyolu)
text.config(state="disabled")
text.place(x=10, y=400)

yildizButon = Button(samanyoluFrame, text="Yıldızlar", bg="black", fg="white", font="Times", height=1,  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame1))
yildizButon.place(x=460, y=400)

gezegenButon = Button(samanyoluFrame, text="Gezegenler", bg="black", fg="white", font="Times", height=1,  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame1))
gezegenButon.place(x=590, y=400)

andromedaButon = Button(samanyoluFrame, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(andromedaFrame))
andromedaButon.place(x=560, y=480)

anaMenuButon = Button(samanyoluFrame, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=700, y=560)

#  andromedaFrame  *****************************************************************************************************

andromedaFrame.config(bg="black")

img3 = ImageTk.PhotoImage(Image.open("resimler/andromedagalaksisi.jpg"))
label4 = Label(andromedaFrame, image=img3)
label4.pack()
label5 = Label(andromedaFrame, text="Andromeda", bg="black", fg="white", font="Times")
label5.place(x=350, y=360)
text = Text(andromedaFrame, height=12, width=40, bg="black", fg="white")
text.insert(END, tanimlar.andromeda)
text.config(state="disabled")
text.place(x=10, y=400)

samanyoluGeriButon = Button(andromedaFrame, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(samanyoluFrame))
samanyoluGeriButon.place(x=500, y=480)

siyahgozButon = Button(andromedaFrame, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(siyahgozFrame))
siyahgozButon.place(x=560, y=480)

anaMenuButon = Button(andromedaFrame, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=700, y=560)

#  siyahgozFrame  *****************************************************************************************************

siyahgozFrame.config(bg="black")

img4 = ImageTk.PhotoImage(Image.open("resimler/siyahgoz.jpg"))
label6 = Label(siyahgozFrame, image=img4)
label6.pack()
label7 = Label(siyahgozFrame, text="Siyah Göz", bg="black", fg="white", font="Times")
label7.place(x=350, y=360)
text = Text(siyahgozFrame, height=12, width=40, bg="black", fg="white")
text.insert(END, tanimlar.siyahgozgalaksi)
text.config(state="disabled")
text.place(x=10, y=400)

andromedaGeriButon = Button(siyahgozFrame, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(andromedaFrame))
andromedaGeriButon.place(x=500, y=480)

ngc221Buton = Button(siyahgozFrame, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(ngc221Frame))
ngc221Buton.place(x=560, y=480)

anaMenuButon = Button(siyahgozFrame, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=700, y=560)

#  ngc221Frame  *****************************************************************************************************

ngc221Frame.config(bg="black")

img5 = ImageTk.PhotoImage(Image.open("resimler/ngc221.jpg"))
label8 = Label(ngc221Frame, image=img5)
label8.pack()
label9 = Label(ngc221Frame, text="NGC 221", bg="black", fg="white", font="Times")
label9.place(x=350, y=360)
text = Text(ngc221Frame, height=12, width=40, bg="black", fg="white")
text.insert(END, tanimlar.ngc221)
text.config(state="disabled")
text.place(x=10, y=400)

siyahgozGeriButon = Button(ngc221Frame, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(siyahgozFrame))
siyahgozGeriButon.place(x=500, y=480)

ngc628Buton = Button(ngc221Frame, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(ngc628Frame))
ngc628Buton.place(x=560, y=480)

anaMenuButon = Button(ngc221Frame, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=700, y=560)

#  ngc628Frame  *****************************************************************************************************

ngc628Frame.config(bg="black")

img6 = ImageTk.PhotoImage(Image.open("resimler/ngc628.jpg"))
label10 = Label(ngc628Frame, image=img6)
label10.pack()
label11 = Label(ngc628Frame, text="NGC 628", bg="black", fg="white", font="Times")
label11.place(x=350, y=360)
text = Text(ngc628Frame, height=12, width=40, bg="black", fg="white")
text.insert(END, tanimlar.ngc628)
text.config(state="disabled")
text.place(x=10, y=400)

ngc221GeriButon = Button(ngc628Frame, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(ngc221Frame))
ngc221GeriButon.place(x=500, y=480)

ngc205Buton = Button(ngc628Frame, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(ngc205Frame))
ngc205Buton.place(x=560, y=480)

anaMenuButon = Button(ngc628Frame, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=700, y=560)

#  ngc205Frame  *****************************************************************************************************

ngc205Frame.config(bg="black")

img7 = ImageTk.PhotoImage(Image.open("resimler/ngc205.jpg"))
label12 = Label(ngc205Frame, image=img7)
label12.pack()
label13 = Label(ngc205Frame, text="NGC 205", bg="black", fg="white", font="Times")
label13.place(x=350, y=360)
text = Text(ngc205Frame, height=12, width=40, bg="black", fg="white")
text.insert(END, tanimlar.ngc205)
text.config(state="disabled")
text.place(x=10, y=400)

ngc628GeriButon = Button(ngc205Frame, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(ngc628Frame))
ngc628GeriButon.place(x=500, y=480)

ngc4321Buton = Button(ngc205Frame, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(ngc4321Frame))
ngc4321Buton.place(x=560, y=480)

anaMenuButon = Button(ngc205Frame, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=700, y=560)

#  ngc4321Frame  *****************************************************************************************************

ngc4321Frame.config(bg="black")

img8 = ImageTk.PhotoImage(Image.open("resimler/ngc4321.jpg"))
label12 = Label(ngc4321Frame, image=img8)
label12.pack()
label13 = Label(ngc4321Frame, text="NGC 4321", bg="black", fg="white", font="Times")
label13.place(x=350, y=360)
text = Text(ngc4321Frame, height=12, width=40, bg="black", fg="white")
text.insert(END, tanimlar.ngc4321)
text.config(state="disabled")
text.place(x=10, y=400)

ngc205GeriButon = Button(ngc4321Frame, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(ngc205Frame))
ngc205GeriButon.place(x=500, y=480)

anaMenuButon = Button(ngc4321Frame, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=700, y=560)

# ********************************************YILDIZLAR*****************************************************************
#  yildizFrame1 code ***************************************************************************************************

yildizFrame1.config(bg="black")

labelYildiz1 = Label(yildizFrame1, text="Proxima Centauri", bg="black", fg="white", font="Times")
labelYildiz1.place(x=20, y=40)
textYildiz1 = Text(yildizFrame1, height=13, width=74, bg="black", fg="white")
textYildiz1.insert(END, tanimlar.yildiz1)
textYildiz1.place(x=200, y=40)
yildizImg1 = ImageTk.PhotoImage(Image.open("resimler/yildiz/Proxima.jpg"))
labelImage1 = Label(yildizFrame1, image=yildizImg1)
labelImage1.place(x=20, y=100)

labelYildiz2 = Label(yildizFrame1, text="Güneş", bg="black", fg="white", font="Times")
labelYildiz2.place(x=20, y=300)
textYildiz2 = Text(yildizFrame1, height=12, width=74, bg="black", fg="white")
textYildiz2.insert(END, tanimlar.yildiz2)
textYildiz2.place(x=200, y=300)
yildizImg2 = ImageTk.PhotoImage(Image.open("resimler/yildiz/gunes.jpg"))
labelImage2 = Label(yildizFrame1, image=yildizImg2)
labelImage2.place(x=20, y=350)

samanyoluFrameGeriButon = Button(yildizFrame1, text="<<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(samanyoluFrame))
samanyoluFrameGeriButon.place(x=40, y=550)

yildizFrame2Buton = Button(yildizFrame1, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame2))
yildizFrame2Buton.place(x=740, y=550)

anaMenuButon = Button(yildizFrame1, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# yildizFrame2 code ****************************************************************************************************

yildizFrame2.config(bg="black")

labelYildiz3 = Label(yildizFrame2, text="Barnard Yıldızı", bg="black", fg="white", font="Times")
labelYildiz3.place(x=20, y=40)
textYildiz3 = Text(yildizFrame2, height=14, width=74, bg="black", fg="white")
textYildiz3.insert(END, tanimlar.yildiz3)
textYildiz3.place(x=200, y=40)
yildizImg3 = ImageTk.PhotoImage(Image.open("resimler/yildiz/Barnard.jpg"))
labelImage3 = Label(yildizFrame2, image=yildizImg3)
labelImage3.place(x=20, y=100)

labelYildiz4 = Label(yildizFrame2, text="Sirius", bg="black", fg="white", font="Times")
labelYildiz4.place(x=20, y=300)
textYildiz4 = Text(yildizFrame2, height=12, width=74, bg="black", fg="white")
textYildiz4.insert(END, tanimlar.yildiz4)
textYildiz4.place(x=200, y=300)
yildizImg4 = ImageTk.PhotoImage(Image.open("resimler/yildiz/sirius.jpg"))
labelImage4 = Label(yildizFrame2, image=yildizImg4)
labelImage4.place(x=20, y=350)

yildizFrame1GeriButon = Button(yildizFrame2, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame1))
yildizFrame1GeriButon.place(x=40, y=550)

yildizFrame3Buton = Button(yildizFrame2, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame3))
yildizFrame3Buton.place(x=740, y=550)

anaMenuButon = Button(yildizFrame2, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# yildizFrame3 code ****************************************************************************************************

yildizFrame3.config(bg="black")

labelYildiz5 = Label(yildizFrame3, text="UY Scuti", bg="black", fg="white", font="Times")
labelYildiz5.place(x=20, y=40)
textYildiz5 = Text(yildizFrame3, height=14, width=74, bg="black", fg="white")
textYildiz5.insert(END, tanimlar.yildiz5)
textYildiz5.place(x=200, y=40)
yildizImg5 = ImageTk.PhotoImage(Image.open("resimler/yildiz/UY_Scuti.png"))
labelImage5 = Label(yildizFrame3, image=yildizImg5)
labelImage5.place(x=20, y=100)


labelYildiz6 = Label(yildizFrame3, text="VY Canis Majoris", bg="black", fg="white", font="Times")
labelYildiz6.place(x=20, y=300)
textYildiz6 = Text(yildizFrame3, height=12, width=74, bg="black", fg="white")
textYildiz6.insert(END, tanimlar.yildiz6)
textYildiz6.place(x=200, y=300)
yildizImg6 = ImageTk.PhotoImage(Image.open("resimler/yildiz/CanisMajoris.jpg"))
labelImage6 = Label(yildizFrame3, image=yildizImg6)
labelImage6.place(x=20, y=350)

yildizFrame2GeriButon = Button(yildizFrame3, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame2))
yildizFrame2GeriButon.place(x=40, y=550)

yildizFrame4Buton = Button(yildizFrame3, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame4))
yildizFrame4Buton.place(x=740, y=550)

anaMenuButon = Button(yildizFrame3, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# yildizFrame4 code ****************************************************************************************************
yildizFrame4.config(bg="black")

labelYildiz7 = Label(yildizFrame4, text="NML Cygni", bg="black", fg="white", font="Times")
labelYildiz7.place(x=20, y=40)
textYildiz7 = Text(yildizFrame4, height=14, width=74, bg="black", fg="white")
textYildiz7.insert(END, tanimlar.yildiz7)
textYildiz7.place(x=200, y=40)
yildizImg7 = ImageTk.PhotoImage(Image.open("resimler/yildiz/NML_Cygni.jpg"))
labelImage7 = Label(yildizFrame4, image=yildizImg7)
labelImage7.place(x=20, y=100)


labelYildiz8 = Label(yildizFrame4, text="V766 Centauri", bg="black", fg="white", font="Times")
labelYildiz8.place(x=20, y=300)
textYildiz8 = Text(yildizFrame4, height=12, width=74, bg="black", fg="white")
textYildiz8.insert(END, tanimlar.yildiz8)
textYildiz8.place(x=200, y=300)
yildizImg8 = ImageTk.PhotoImage(Image.open("resimler/yildiz/V766_Centauri.jpg"))
labelImage8 = Label(yildizFrame4, image=yildizImg8)
labelImage8.place(x=20, y=350)

yildizFrame3GeriButon = Button(yildizFrame4, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame3))
yildizFrame3GeriButon.place(x=40, y=550)

yildizFrame5Buton = Button(yildizFrame4, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame5))
yildizFrame5Buton.place(x=740, y=550)

anaMenuButon = Button(yildizFrame4, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# yildizFrame5 code ****************************************************************************************************

yildizFrame5.config(bg="black")

labelYildiz9 = Label(yildizFrame5, text="V354 Cephei", bg="black", fg="white", font="Times")
labelYildiz9.place(x=20, y=40)
textYildiz9 = Text(yildizFrame5, height=14, width=74, bg="black", fg="white")
textYildiz9.insert(END, tanimlar.yildiz9)
textYildiz9.place(x=200, y=40)
yildizImg9 = ImageTk.PhotoImage(Image.open("resimler/yildiz/V354_Cephei.jpg"))
labelImage9 = Label(yildizFrame5, image=yildizImg9)
labelImage9.place(x=20, y=100)


labelYildiz10 = Label(yildizFrame5, text="Tabanca Yıldızı", bg="black", fg="white", font="Times")
labelYildiz10.place(x=20, y=300)
textYildiz10 = Text(yildizFrame5, height=12, width=74, bg="black", fg="white")
textYildiz10.insert(END, tanimlar.yildiz10)
textYildiz10.place(x=200, y=300)
yildizImg10 = ImageTk.PhotoImage(Image.open("resimler/yildiz/Tabanca_Yıldızı.jpg"))
labelImage10 = Label(yildizFrame5, image=yildizImg10)
labelImage10.place(x=20, y=350)

yildizFrame4GeriButon = Button(yildizFrame5, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame4))
yildizFrame4GeriButon.place(x=40, y=550)

yildizFrame6Buton = Button(yildizFrame5, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame6))
yildizFrame6Buton.place(x=740, y=550)

anaMenuButon = Button(yildizFrame5, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# yildizFrame6 code ****************************************************************************************************

yildizFrame6.config(bg="black")

labelYildiz11 = Label(yildizFrame6, text="Stephenson 2-18", bg="black", fg="white", font="Times")
labelYildiz11.place(x=20, y=40)
textYildiz11 = Text(yildizFrame6, height=14, width=74, bg="black", fg="white")
textYildiz11.insert(END, tanimlar.yildiz11)
textYildiz11.place(x=200, y=40)
yildizImg11 = ImageTk.PhotoImage(Image.open("resimler/yildiz/Stephenson.jpg"))
labelImage11 = Label(yildizFrame6, image=yildizImg11)
labelImage11.place(x=20, y=100)


labelYildiz10 = Label(yildizFrame6, text="LBV 1806-20", bg="black", fg="white", font="Times")
labelYildiz10.place(x=20, y=300)
textYildiz10 = Text(yildizFrame6, height=12, width=74, bg="black", fg="white")
textYildiz10.insert(END, tanimlar.yildiz12)
textYildiz10.place(x=200, y=300)
yildizImg12 = ImageTk.PhotoImage(Image.open("resimler/yildiz/LBV_1806-20.jpg"))
labelImage12 = Label(yildizFrame6, image=yildizImg12)
labelImage12.place(x=20, y=350)


yildizFrame5GeriButon = Button(yildizFrame6, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame5))
yildizFrame5GeriButon.place(x=40, y=550)

yildizFrame7Buton = Button(yildizFrame6, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame7))
yildizFrame7Buton.place(x=740, y=550)

anaMenuButon = Button(yildizFrame6, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# yildizFrame7 code ****************************************************************************************************

yildizFrame7.config(bg="black")

labelYildiz12 = Label(yildizFrame7, text="2M1207", bg="black", fg="white", font="Times")
labelYildiz12.place(x=20, y=40)
textYildiz12 = Text(yildizFrame7, height=14, width=74, bg="black", fg="white")
textYildiz12.insert(END, tanimlar.yildiz13)
textYildiz12.place(x=200, y=40)
yildizImg13 = ImageTk.PhotoImage(Image.open("resimler/yildiz/2M1207.jpg"))
labelImage13 = Label(yildizFrame7, image=yildizImg13)
labelImage13.place(x=20, y=100)


labelYildiz11 = Label(yildizFrame7, text="Gliese 876", bg="black", fg="white", font="Times")
labelYildiz11.place(x=20, y=300)
textYildiz11 = Text(yildizFrame7, height=12, width=74, bg="black", fg="white")
textYildiz11.insert(END, tanimlar.yildiz14)
textYildiz11.place(x=200, y=300)
yildizImg14 = ImageTk.PhotoImage(Image.open("resimler/yildiz/Gliese_876.jpg"))
labelImage14 = Label(yildizFrame7, image=yildizImg14)
labelImage14.place(x=20, y=350)


yildizFrame6GeriButon = Button(yildizFrame7, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame6))
yildizFrame6GeriButon.place(x=40, y=550)

yildizFrame8Buton = Button(yildizFrame7, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame8))
yildizFrame8Buton.place(x=740, y=550)

anaMenuButon = Button(yildizFrame7, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# yildizFrame8 code ****************************************************************************************************

yildizFrame8.config(bg="black")

labelYildiz12 = Label(yildizFrame8, text="Fomalhaut", bg="black", fg="white", font="Times")
labelYildiz12.place(x=20, y=40)
textYildiz12 = Text(yildizFrame8, height=14, width=74, bg="black", fg="white")
textYildiz12.insert(END, tanimlar.yildiz15)
textYildiz12.place(x=200, y=40)
yildizImg15 = ImageTk.PhotoImage(Image.open("resimler/yildiz/Fomalhaut.jpg"))
labelImage15 = Label(yildizFrame8, image=yildizImg15)
labelImage15.place(x=20, y=100)


labelYildiz11 = Label(yildizFrame8, text="HD 10647", bg="black", fg="white", font="Times")
labelYildiz11.place(x=20, y=300)
textYildiz11 = Text(yildizFrame8, height=12, width=74, bg="black", fg="white")
textYildiz11.insert(END, tanimlar.yildiz16)
textYildiz11.place(x=200, y=300)
yildizImg16 = ImageTk.PhotoImage(Image.open("resimler/yildiz/HD_10647.jpg"))
labelImage16 = Label(yildizFrame8, image=yildizImg16)
labelImage16.place(x=20, y=350)


yildizFrame7GeriButon = Button(yildizFrame8, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame7))
yildizFrame7GeriButon.place(x=40, y=550)

yildizFrame9Buton = Button(yildizFrame8, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame9))
yildizFrame9Buton.place(x=740, y=550)

anaMenuButon = Button(yildizFrame8, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# yildizFrame9 code ****************************************************************************************************

yildizFrame9.config(bg="black")

labelYildiz13 = Label(yildizFrame9, text="HD 40307", bg="black", fg="white", font="Times")
labelYildiz13.place(x=20, y=40)
textYildiz13 = Text(yildizFrame9, height=14, width=74, bg="black", fg="white")
textYildiz13.insert(END, tanimlar.yildiz17)
textYildiz13.place(x=200, y=40)
yildizImg17 = ImageTk.PhotoImage(Image.open("resimler/yildiz/HD_40307.jpg"))
labelImage17 = Label(yildizFrame9, image=yildizImg17)
labelImage17.place(x=20, y=100)

labelYildiz12 = Label(yildizFrame9, text="Mu Arae", bg="black", fg="white", font="Times")
labelYildiz12.place(x=20, y=300)
textYildiz12 = Text(yildizFrame9, height=12, width=74, bg="black", fg="white")
textYildiz12.insert(END, tanimlar.yildiz18)
textYildiz12.place(x=200, y=300)
yildizImg18 = ImageTk.PhotoImage(Image.open("resimler/yildiz/MuArae.jpg"))
labelImage18 = Label(yildizFrame9, image=yildizImg18)
labelImage18.place(x=20, y=350)


yildizFrame8GeriButon = Button(yildizFrame9, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(yildizFrame8))
yildizFrame8GeriButon.place(x=40, y=550)

anaMenuButon = Button(yildizFrame9, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# **********************************************************************************************************************

# ********************************************GEZEGENLER****************************************************************

# gezegenFrame1 code   *************************************************************************************************

gezegenFrame1.config(bg="black")

labelGezegen1 = Label(gezegenFrame1, text="Merkür", bg="black", fg="white", font="Times")
labelGezegen1.place(x=20, y=40)
textGezegen1 = Text(gezegenFrame1, height=14, width=74, bg="black", fg="white")
textGezegen1.insert(END, tanimlar.gezegen1)
textGezegen1.place(x=200, y=40)
gezegenImg1 = ImageTk.PhotoImage(Image.open("resimler/gezegen/merkur.jpg"))
label2Image1 = Label(gezegenFrame1, image=gezegenImg1)
label2Image1.place(x=20, y=100)


labelGezegen2 = Label(gezegenFrame1, text="Venüs", bg="black", fg="white", font="Times")
labelGezegen2.place(x=20, y=300)
textGezegen2 = Text(gezegenFrame1, height=14, width=74, bg="black", fg="white")
textGezegen2.insert(END, tanimlar.gezegen2)
textGezegen2.place(x=200, y=300)
gezegenImg2 = ImageTk.PhotoImage(Image.open("resimler/gezegen/venus.PNG"))
label2Image2 = Label(gezegenFrame1, image=gezegenImg2)
label2Image2.place(x=20, y=350)


samanyoluFrameGeri2Buton = Button(gezegenFrame1, text="<<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(samanyoluFrame))
samanyoluFrameGeri2Buton.place(x=40, y=550)

GezegenFrame2Buton = Button(gezegenFrame1, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame2))
GezegenFrame2Buton.place(x=740, y=550)

anaMenuButon = Button(gezegenFrame1, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# gezegenFrame2 code   *************************************************************************************************

gezegenFrame2.config(bg="black")

labelGezegen3 = Label(gezegenFrame2, text="Dünya", bg="black", fg="white", font="Times")
labelGezegen3.place(x=20, y=40)
textGezegen3 = Text(gezegenFrame2, height=14, width=74, bg="black", fg="white")
textGezegen3.insert(END, tanimlar.gezegen3)
textGezegen3.place(x=200, y=40)
gezegenImg3 = ImageTk.PhotoImage(Image.open("resimler/gezegen/dunya.PNG"))
label2Image3 = Label(gezegenFrame2, image=gezegenImg3)
label2Image3.place(x=20, y=100)


labelGezegen4 = Label(gezegenFrame2, text="Mars", bg="black", fg="white", font="Times")
labelGezegen4.place(x=20, y=300)
textGezegen4 = Text(gezegenFrame2, height=14, width=74, bg="black", fg="white")
textGezegen4.insert(END, tanimlar.gezegen4)
textGezegen4.place(x=200, y=300)
gezegenImg4 = ImageTk.PhotoImage(Image.open("resimler/gezegen/mars.PNG"))
label2Image4 = Label(gezegenFrame2, image=gezegenImg4)
label2Image4.place(x=20, y=350)


GezegenFrame1GeriButon = Button(gezegenFrame2, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame1))
GezegenFrame1GeriButon.place(x=40, y=550)

GezegenFrame3Buton = Button(gezegenFrame2, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame3))
GezegenFrame3Buton.place(x=740, y=550)

anaMenuButon = Button(gezegenFrame2, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# gezegenFrame3 code   *************************************************************************************************

gezegenFrame3.config(bg="black")

labelGezegen5 = Label(gezegenFrame3, text="Jüpiter", bg="black", fg="white", font="Times")
labelGezegen5.place(x=20, y=40)
textGezegen5 = Text(gezegenFrame3, height=14, width=74, bg="black", fg="white")
textGezegen5.insert(END, tanimlar.gezegen5)
textGezegen5.place(x=200, y=40)
gezegenImg5 = ImageTk.PhotoImage(Image.open("resimler/gezegen/jupiter.PNG"))
label2Image5 = Label(gezegenFrame3, image=gezegenImg5)
label2Image5.place(x=20, y=100)


labelGezegen6 = Label(gezegenFrame3, text="Satürn", bg="black", fg="white", font="Times")
labelGezegen6.place(x=20, y=300)
textGezegen6 = Text(gezegenFrame3, height=14, width=74, bg="black", fg="white")
textGezegen6.insert(END, tanimlar.gezegen6)
textGezegen6.place(x=200, y=300)
gezegenImg6 = ImageTk.PhotoImage(Image.open("resimler/gezegen/saturn.PNG"))
label2Image6 = Label(gezegenFrame3, image=gezegenImg6)
label2Image6.place(x=20, y=350)


GezegenFrame2GeriButon = Button(gezegenFrame3, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame2))
GezegenFrame2GeriButon.place(x=40, y=550)

GezegenFrame4Buton = Button(gezegenFrame3, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame4))
GezegenFrame4Buton.place(x=740, y=550)

anaMenuButon = Button(gezegenFrame3, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# gezegenFrame4 code   *************************************************************************************************
gezegenFrame4.config(bg="black")

labelGezegen7 = Label(gezegenFrame4, text="Uranüs", bg="black", fg="white", font="Times")
labelGezegen7.place(x=20, y=40)
textGezegen7 = Text(gezegenFrame4, height=14, width=74, bg="black", fg="white")
textGezegen7.insert(END, tanimlar.gezegen7)
textGezegen7.place(x=200, y=40)
gezegenImg7 = ImageTk.PhotoImage(Image.open("resimler/gezegen/uranus.PNG"))
label2Image7 = Label(gezegenFrame4, image=gezegenImg7)
label2Image7.place(x=20, y=100)


labelGezegen8 = Label(gezegenFrame4, text="Neptün", bg="black", fg="white", font="Times")
labelGezegen8.place(x=20, y=300)
textGezegen8 = Text(gezegenFrame4, height=14, width=74, bg="black", fg="white")
textGezegen8.insert(END, tanimlar.gezegen8)
textGezegen8.place(x=200, y=300)
gezegenImg8 = ImageTk.PhotoImage(Image.open("resimler/gezegen/neptun.PNG"))
label2Image8 = Label(gezegenFrame4, image=gezegenImg8)
label2Image8.place(x=20, y=350)

GezegenFrame3GeriButon = Button(gezegenFrame4, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame3))
GezegenFrame3GeriButon.place(x=40, y=550)

GezegenFrame5Buton = Button(gezegenFrame4, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame5))
GezegenFrame5Buton.place(x=740, y=550)

anaMenuButon = Button(gezegenFrame4, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# gezegenFrame5 code   *************************************************************************************************

gezegenFrame5.config(bg="black")

labelGezegen8 = Label(gezegenFrame5, text="Gliese 581 c", bg="black", fg="white", font="Times")
labelGezegen8.place(x=20, y=40)
textGezegen8 = Text(gezegenFrame5, height=14, width=74, bg="black", fg="white")
textGezegen8.insert(END, tanimlar.gezegen9)
textGezegen8.place(x=200, y=40)
gezegenImg9 = ImageTk.PhotoImage(Image.open("resimler/gezegen/Gliese581c.jpg"))
label2Image9 = Label(gezegenFrame5, image=gezegenImg9)
label2Image9.place(x=20, y=100)


labelGezegen9 = Label(gezegenFrame5, text="PSR B1620-26 b", bg="black", fg="white", font="Times")
labelGezegen9.place(x=20, y=300)
textGezegen9 = Text(gezegenFrame5, height=14, width=74, bg="black", fg="white")
textGezegen9.insert(END, tanimlar.gezegen10)
textGezegen9.place(x=200, y=300)
gezegenImg10 = ImageTk.PhotoImage(Image.open("resimler/gezegen/PSRB1620-26b.jpg"))
label2Image10 = Label(gezegenFrame5, image=gezegenImg10)
label2Image10.place(x=20, y=350)

GezegenFrame4GeriButon = Button(gezegenFrame5, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame4))
GezegenFrame4GeriButon.place(x=40, y=550)

GezegenFrame6Buton = Button(gezegenFrame5, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame6))
GezegenFrame6Buton.place(x=740, y=550)

anaMenuButon = Button(gezegenFrame5, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# gezegenFrame6 code   *************************************************************************************************

gezegenFrame6.config(bg="black")

labelGezegen10 = Label(gezegenFrame6, text="Gliese 876 b", bg="black", fg="white", font="Times")
labelGezegen10.place(x=20, y=40)
textGezegen10 = Text(gezegenFrame6, height=14, width=74, bg="black", fg="white")
textGezegen10.insert(END, tanimlar.gezegen11)
textGezegen10.place(x=200, y=40)
gezegenImg11 = ImageTk.PhotoImage(Image.open("resimler/gezegen/Gliese876b.jpg"))
label2Image11 = Label(gezegenFrame6, image=gezegenImg11)
label2Image11.place(x=20, y=100)


labelGezegen11 = Label(gezegenFrame6, text="Gliese 876 d", bg="black", fg="white", font="Times")
labelGezegen11.place(x=20, y=300)
textGezegen11 = Text(gezegenFrame6, height=14, width=74, bg="black", fg="white")
textGezegen11.insert(END, tanimlar.gezegen12)
textGezegen11.place(x=200, y=300)
gezegenImg12 = ImageTk.PhotoImage(Image.open("resimler/gezegen/Gliese876d.jpg"))
label2Image12 = Label(gezegenFrame6, image=gezegenImg12)
label2Image12.place(x=20, y=350)


GezegenFrame5GeriButon = Button(gezegenFrame6, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame5))
GezegenFrame5GeriButon.place(x=40, y=550)

GezegenFrame7Buton = Button(gezegenFrame6, text=">", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame7))
GezegenFrame7Buton.place(x=740, y=550)

anaMenuButon = Button(gezegenFrame6, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

# gezegenFrame7 code   *************************************************************************************************

gezegenFrame7.config(bg="black")

labelGezegen11 = Label(gezegenFrame7, text="Gliese 876 c", bg="black", fg="white", font="Times")
labelGezegen11.place(x=20, y=40)
textGezegen11 = Text(gezegenFrame7, height=14, width=74, bg="black", fg="white")
textGezegen11.insert(END, tanimlar.gezegen13)
textGezegen11.place(x=200, y=40)
gezegenImg13 = ImageTk.PhotoImage(Image.open("resimler/gezegen/Gliese581c.jpg"))
label2Image13 = Label(gezegenFrame7, image=gezegenImg13)
label2Image13.place(x=20, y=100)


labelGezegen12 = Label(gezegenFrame7, text="Gliese 876 e", bg="black", fg="white", font="Times")
labelGezegen12.place(x=20, y=300)
textGezegen12 = Text(gezegenFrame7, height=14, width=74, bg="black", fg="white")
textGezegen12.insert(END, tanimlar.gezegen14)
textGezegen12.place(x=200, y=300)
gezegenImg14 = ImageTk.PhotoImage(Image.open("resimler/gezegen/Gliese876e.png"))
label2Image14 = Label(gezegenFrame7, image=gezegenImg14)
label2Image14.place(x=20, y=350)


GezegenFrame6GeriButon = Button(gezegenFrame7, text="<", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(gezegenFrame6))
GezegenFrame6GeriButon.place(x=40, y=550)

anaMenuButon = Button(gezegenFrame7, text="Ana Menu", bg="black", fg="white", font="Times",  activebackground="white", activeforeground="black", command=lambda: show_frame(menuFrame))
anaMenuButon.place(x=350, y=560)

show_frame(menuFrame)
root.mainloop()