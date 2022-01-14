from tkinter import *
import json

from PIL import Image, ImageFilter
import urllib.request as url
import numpy as np
import cv2



"""Function Part"""
def search():
    # data=json.load(open('data.json'))
    # print(data['words'])
    data=json.load(open('data2.json'))
    # print(type(data))
    word=enterwordentry.get()
    parsedWord=word.__len__()
    print(parsedWord)
    # print(word)
    # if word in data:
    #     image=data[word]
    #     # print(type(image))
    #     imageURL=image[0]
    #     print(type(imageURL))
    #     # textarea.insert(END,imageURL)
    #     req = url.urlopen(imageURL)
    #     arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    #     img = cv2.imdecode(arr, -1)
    #     # print(img.shape)
    #     imgResize=cv2.resize(img,(400,400))
    #     cv2.imshow('image A', imgResize)
    #
    #     cv2.waitKey()


    if(parsedWord==1):
        if word in data:
            image=data[word]
            # print(type(image))
            imageURL=image[0]
            print(type(imageURL))
            # textarea.insert(END,imageURL)
            req = url.urlopen(imageURL)
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1)
            # print(img.shape)
            imgResize=cv2.resize(img,(400,400))
            cv2.imshow('image A', imgResize)

            cv2.waitKey()
    else:
        lineData = json.load(open('Lines.json'))
        print(lineData)
        







"""GUI Part"""
root = Tk()

root.geometry('1000x600+150+80')
"""
set height and width of screen and fix the position of screen
"""

root.title("Sign Dictionary for impaired people")
root.resizable(False,False)
bgImage=PhotoImage(file='background.png')
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)



enterwordLabel = Label(root, text='Enter Word', font=('castellar', 20, 'bold'), fg='red3', bg='whitesmoke')
enterwordLabel.place(x=530, y=15)

enterwordentry = Entry(root, font=('arial', 20, 'bold'), bd=3, relief=GROOVE, justify=CENTER)
enterwordentry.place(x=500, y=80)


enterwordentry.focus_set()

searchimage = PhotoImage(file='search.png')
searchButton = Button(root, image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=search)
searchButton.place(x=550, y=150)


micimage = PhotoImage(file='microphone.png')
micButton = Button(root, image=micimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                   cursor='hand2')
micButton.place(x=710, y=153)


# meaninglabel = Label(root, text='Meaning', font=('castellar', 20, 'bold'), fg='red3', bg='whitesmoke')
# meaninglabel.place(x=580, y=240)
#
# textarea = Text(root, font=('arial', 18, 'bold'), height=4, width=35, bd=2, relief=GROOVE, wrap='word')
# textarea.place(x=460, y=300)


# audioimage = PhotoImage(file='voice-search.png')
# audioButton = Button(root, image=audioimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
#                      cursor='hand2')
# audioButton.place(x=530, y=420)
#
# clearimage = PhotoImage(file='clear.png')
# clearButton = Button(root, image=clearimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2')
# clearButton.place(x=660, y=420)
#
# exitimage = PhotoImage(file='exit.png')
# exitButton = Button(root, image=exitimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2')
# exitButton.place(x=790, y=420)





root.mainloop();
# print("hello")
