from tkinter import filedialog
from tkinter import*
import random
import time
import numpy as np
from numpy.fft import fft
import sys
import numpy
import PIL
from PIL import Image, ImageTk
import io
import base64
import cv2
import math
from io import BytesIO
import codecs

root = Tk()
root.configure(background='lavender')
Tk().withdraw()
root.geometry("600x600+0+0")
root.title("Phase-Only Digital Encryption using a Three-Pass Protocol")
global path_image

image_display_size = 300, 300
#================Variable Declaration==============================
keyAB = IntVar()
keyC = DoubleVar()
folder_path_textfile = StringVar()
status_text = StringVar()
keyC = np.random.rand(1,1)*10**(np.round(np.random.rand(1,1)*6))

#================Window Framing=================================
Tops = Frame(root, width = 1000, relief = SUNKEN)
Tops.pack(side=TOP)
window = Frame(root, width = 1000, relief = SUNKEN)
window.pack(side=TOP)
#=========================Time======================================
localtime=time.asctime(time.localtime(time.time()))
#=========================Info======================================
lblInfo = Label(Tops, font=('arial', 15, 'bold'), text="Phase-Only Digital Encryption \n using a Three-Pass Protocol",fg="Black")
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial', 8, 'bold', 'italic'),
                text=localtime, fg="Black")
lblInfo.grid(row=1,column=0)
lblInfo = Label(window, font=('arial', 8, 'italic', 'bold'),
                text="\n \n \n Attach image file (.jpg)", fg="Steel Blue")
lblInfo.grid(row=3,column=0)
lblInfo = Label(window, font=('arial', 8, 'italic','bold'), text="\n" "\n KEY (string integers no more than 10 digits long) \n", fg="Steel Blue")
lblInfo.grid(row=5,column=0)
#lblInfo = Label(window, font=('arial', 8, 'italic', 'bold'), text="\n c (Spectral Embedding Constant) >> 1 ; \n use only for STEP 1 \n\n", fg="Steel Blue")
#lblInfo.grid(row=7,column=0)
lblInfo = Label(window, font=('arial', 8, 'bold'), text=" \n \n STATUS", fg="Steel Blue")
lblInfo.grid(row=14,column=0)
#=========================Operation=================================
def browse_button_textfile():
    file_path=filedialog.askopenfilename()
    folder_path_textfile.set(file_path)
    print (folder_path_textfile)



def btnClick_STEP1():
    with open(folder_path_textfile.get(), "rb") as image:
        s = base64.b64encode(image.read()).decode('ASCII')

    l1=[c for c in s]
    P=[ord(c) for c in s]
    zero =np.zeros((1))
    P =np.concatenate((zero, P))
    N=np.size(P.transpose(),axis=0)
    np.random.seed(keyAB.get())
    Theta= np.random.rand((N))
    POS=(np.exp(1j*(np.angle(fft(Theta)))))
    E=fft(P)*POS+keyC*(POS)
    E=(np.fft.ifft(E)).real
    np.savetxt("CipherImage1.jpg", E)
    status_text.set("cipherImage 1 text file generated")
def btnClick_STEP2():
    E= np.loadtxt(folder_path_textfile.get())
    N=np.size(E.conj().transpose(),axis=0)
    E=fft(E)
    np.random.seed(keyAB.get())
    Theta= np.random.random((N))
    E=E*(np.exp(1j*(np.angle(fft(Theta)))))
    E=(np.fft.ifft(E)).real
    np.savetxt("CipherImage2.jpg", E)
    status_text.set("cipherImage 2 text file generated")

def btnClick_STEP3():
    E= np.loadtxt(folder_path_textfile.get())
    N=np.size(E.conj().transpose(),axis=0)
    E=fft(E)
    np.random.seed(keyAB.get())
    Theta= np.random.rand((N))
    E=E*(np.exp(-1j*(np.angle(fft(Theta)))))
    E=(np.fft.ifft(E)).real
    np.savetxt("CipherImage3.jpg", E, fmt="%10.5f")
    status_text.set("cipherImage 3 text file generated")


################################################################ADDED CODE##################################################

def btnClick_STEP4():
    E= np.loadtxt(folder_path_textfile.get())
    N=np.size(E.conj().transpose(),axis=0)
    E=fft(E)
    np.random.seed(keyAB.get())
    Theta= np.random.random((N))
    E=E*(np.exp(1j*(np.angle(fft(Theta)))))
    E=(np.fft.ifft(E)).real
    np.savetxt("CipherImage4.jpg", E)
    status_text.set("cipherImage 4 text file generated")
########################################################################################################################


#=========================Display===================================
txtDisplay = Entry(window, font=('arial',8), textvariable=folder_path_textfile, bd=5,width =50, bg="white")
txtDisplay.grid(row=4,column=0)
textvariable=folder_path_textfile.get()
txtDisplay = Entry(window, font=('arial',8), textvariable=keyAB, bd=5, width =20, bg="white")
txtDisplay.grid(row=5,column=1)
#txtDisplay = Entry(window, font=('arial',8), textvariable=keyC, bd=5, width =20, bg="white")
#txtDisplay.grid(row=7,column=1)
#textvariable=keyC
txtDisplay = Entry(window, font=('arial',8),
                   textvariable=status_text, bd=5, width =50, bg="white")
txtDisplay.grid(row=15,column=0)
#=========================Buttons===================================
btnbrowsetxt=Button(window, padx=5,pady=5,bd=5,fg="black",
                    font=('arial', 8,'bold'), text="BROWSE Image File",
                    bg ="brown", command
                    =browse_button_textfile).grid(row=4,column=1)
btnstep1=Button(window, padx=5,pady=5,bd=5,fg="black",
                font=('arial', 12,'bold'), text="STEP 1",
                bg ="powder blue", command
                =btnClick_STEP1).grid(row=9,column=0)
btnstep2=Button(window, padx=5,pady=5,bd=5,fg="black",
                font=('arial', 12,'bold'), text="STEP 2",
                bg ="powder blue", command
                =btnClick_STEP2).grid(row=10,column=0)
btnstep3=Button(window, padx=5,pady=5,bd=5,fg="black",
                font=('arial', 12,'bold'), text="STEP 3",
                bg ="powder blue", command
                =btnClick_STEP3).grid(row=11,column=0)
btnstep4=Button(window, padx=5,pady=5,bd=5,fg="black",
                font=('arial', 12,'bold'), text="STEP 4",
                bg ="powder blue", command
                =btnClick_STEP4).grid(row=12,column=0)





######################################ENCRYPTION STARTS HERE: ADDED CODE############################################################

def on_click():

    global path_image
    # Here, I am trying to open the file in a dialog box, use the tkinter filedialog library.
    # to acquire the path's image
    path_image = filedialog.askopenfilename()
    # Using the path you can be able to load the image.
    load_image = Image.open(path_image)
    # tkinter's thumbnail function can be used to insert the image into the GUI.
    load_image.thumbnail(image_display_size, Image.ANTIALIAS)
    # For faster processing, I then convert the image to a numpy array and set the type to unsigned integer.
    np_load_image = np.asarray(load_image)
    np_load_image = Image.fromarray(np.uint8(np_load_image))
    render = ImageTk.PhotoImage(np_load_image)
    img = Label(root, image=render)
    img.image = render
    img.place(x=500, y=500)


def encrypt_data_into_image():

    global path_image
    data = txt.get(1.0, "end-1c")
    # This is where I load the image
    img = cv2.imread(path_image)
    # Now I then split the image into its component parts. Represent the ASCII characters.
    data = [format(ord(i), '08b') for i in data]
    _, width, _ = img.shape
    # algorithm for image encoding
    PixReq = len(data) * 3

    RowReq = PixReq/width
    RowReq = math.ceil(RowReq)

    count = 0
    charCount = 0

    for i in range(RowReq + 1):

        while(count < width and charCount < len(data)):
            char = data[charCount]
            charCount += 1

            for index_k, k in enumerate(char):
                if((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                    img[i][count][index_k % 3] -= 1
                if(index_k % 3 == 2):
                    count += 1
                if(index_k == 7):
                    if(charCount*3 < PixReq and img[i][count][2] % 2 == 1):
                        E[i][count][2] -= 1
                    if(charCount*3 >= PixReq and img[i][count][2] % 2 == 0):
                        img[i][count][2] -= 1
                    count += 1
        count = 0

    # This is where my encrypted image will be written into a new file
    cv2.imwrite("encrypted_image.tiff", img)
    #This is the statement indicating succceful of the encryption
    status_text.set("Congratulations!!!! Encryption Successful!")



on_click_button = Button(root, text="Browse Image", bg='white', fg='black', command=on_click)
on_click_button.place(x=250, y=10)

txt = Text(root, wrap=WORD, width=30)
txt.place(x=200, y=55, height=165)

encrypt_button = Button(root, text="Encode", bg='white', fg='black', command=encrypt_data_into_image)
encrypt_button.place(x=200, y=230)






######################################ENCRYPTION ENDSS HERE############################################################




######################################DECRYPTION STARTS HERE############################################################

def on_click():

    global path_image
    # Here, I am trying to open the file in a dialog box, use the tkinter filedialog library.
    # to acquire the path's image
    path_image = filedialog.askopenfilename()
    # Using the path you can be able to load the image.
    load_image = Image.open(path_image)
    # tkinter's thumbnail function can be used to insert the image into the GUI.
    load_image.thumbnail(image_display_size, Image.ANTIALIAS)
    # For faster processing, I then convert the image to a numpy array and set the type to unsigned integer.
    np_load_image = np.asarray(load_image)
    np_load_image = Image.fromarray(np.uint8(np_load_image))
    render = ImageTk.PhotoImage(np_load_image)
    img = Label(root, image=render)
    img.image = render
    img.place(x=140, y=340)

def decrypt():

    global path_image
    data2 = txt.get(1.0, "end-1c")
    # This is where I load the image
    img = cv2.imread(path_image)
    # Now I then split the image into its component parts. Represent the ASCII characters.
    data2= [format(ord(i), '08b') for i in data2]
    _, width, _ = img.shape
    # algorithm for image encoding
    PixelRequirement = len(data2) * 3

    RowReq = PixelRequirement/width
    RowReq = math.ceil(RowReq)

    count = 0
    charCount = 0

    for i in range(RowReq + 1):

        while(count < width and charCount < len(data2)):
            char = data2[charCount]
            charCount += 1

            for index_k, k in enumerate(char):
                if((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                    img[i][count][index_k % 3] -= 1
                if(index_k % 3 == 2):
                    count += 1
                if(index_k == 7):
                    if(charCount*3 <  PixelRequirement and img[i][count][2] % 2 == 1):
                        E[i][count][2] -= 1
                    if(charCount*3 >=  PixelRequirement and img[i][count][2] % 2 == 0):
                        img[i][count][2] -= 1
                    count += 1
        count = 0

    # This is where my encrypted image will be written into a new file
    cv2.imwrite("decrypted_image.tiff", img)

    #This is the statement indicating succceful of the decryption
    status_text.set("Congratulations!!!! Decryption Successful!")


on_click_button = Button(root, text="Browse Image", bg='blue', fg='black', command=on_click)
on_click_button.place(x=1080, y=15)

txt = Text(root, wrap=WORD, width=30)
txt.place(x=1050, y=55, height=200)

encrypt_button = Button(root, text="Decode", bg='red', fg='black', command=decrypt)
encrypt_button.place(x=1090, y=265)

root.mainloop()

######################################DECRYPTION ENDSS HERE###########################################################



###################################################################################################################