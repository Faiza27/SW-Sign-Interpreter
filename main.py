from tkinter import *
import json
from PIL import Image, ImageFilter
import urllib.request as url
import numpy as np
import cv2




"""Function Part"""
def search():
    data=json.load(open('data2.json'))
    # print(type(data))
    word=enter_word_entry.get()
    parsed_word=word.__len__()
    print(parsed_word)
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


    if(parsed_word==1):
        if word in data:
            image=data[word]
            # print(type(image))
            image_url=image[0]
            print(type(image_url))
            # textarea.insert(END,imageURL)
            req = url.urlopen(image_url)
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1)
            # print(img.shape)
            img_resize=cv2.resize(img,(400,400))
            cv2.imshow('image A', img_resize)

            cv2.waitKey()
        else:
            print("Word Doesn't exist in Dictionary")



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

enter_word_label = Label(root, text='Enter Word', font=('castellar', 20, 'bold'), fg='red3', bg='whitesmoke')
enter_word_label.place(x=530, y=15)

enter_word_entry = Entry(root, font=('arial', 20, 'bold'), bd=3, relief=GROOVE, justify=CENTER)
enter_word_entry.place(x=500, y=80)
enter_word_entry.focus_set()

searchimage = PhotoImage(file='search.png')
searchButton = Button(root, image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=search)
searchButton.place(x=550, y=150)


root.mainloop();
# print("hello")
