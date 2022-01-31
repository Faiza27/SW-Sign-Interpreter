
"""
Important modules
numpy
cv2
PIL  for image and image filtering
tkinter for GUI
urllib.request for getting data through image url
json for manipulating json data
"""
from tkinter import *
import json
from PIL import Image, ImageFilter
import urllib.request as url
import numpy as np
import cv2
import tkinter as tk


def dictionary():

    """Function Part"""


    def search():
        """
           This function search letter from JSON data
           :return: corresponding image of the letter
           """
        data = json.load(open('D:\\SW\\Model\\data2.json'))
        """
           Loads JSON data and opens it & stores it in data variable
        """
        # print(type(data))
        word = enter_word_entry.get()
        """
           Get the input letter from the input box and stores it in word variable

        """
        parsed_word = word.__len__()
        """
           This function counts the word length of input data
         """
        print(parsed_word)


        if (parsed_word == 1):
            if word in data:
                image = data[word]
                # print(type(image))
                image_url = image[0]
                print(type(image_url))
                # textarea.insert(END,imageURL)
                req = url.urlopen(image_url)
                """
                          This function open image url
                """
                arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
                """
                          This funtion converts image as numpy array 
                          :return: array
                """
                img = cv2.imdecode(arr, -1)
                """
                          This function decode the array and convert it to a picture
                """
                # print(img.shape)
                img_resize = cv2.resize(img, (400, 400))
                """
                       This function takes an array and a 2d array as image size and resize it
                       :return: resized image
                """
                cv2.imshow('image A', img_resize)
                """
                           This function takes a string parameter & a variable
                           :return: show the image through separate window
                 """

                cv2.waitKey()
            else:
                print("Word Doesn't exist in Dictionary")


    """GUI Part"""
    root = tk.Toplevel()

    root.geometry('1000x600+150+80')
    """
    set height and width of screen and fix the position of screen
    """

    root.title("Sign Dictionary for impaired people")
    root.resizable(False, False)
    bgImage = PhotoImage(file='D:\\SW\\Model\\img_1.png')
    """
    This funtion takes a image file as an input
    return: store the image on bgImage variable
    """
    bgLabel = Label(root, image=bgImage)
    """
    Set input image as background of tkinter GUI and store it in bgLabel variable
    """
    bgLabel.place(x=0, y=0)
    """
    This function set position of the bgLabel
    """

    enter_word_label = Label(root, text='Enter a letter', font=('castellar', 20, 'bold'), fg='red3', bg='whitesmoke')
    """
    This create header text label on GUI
    """

    enter_word_label.place(x=530, y=15)
    """
    This function set position of header text field on GUI
    """

    enter_word_entry = Entry(root, font=('arial', 20, 'bold'), bd=3, relief=GROOVE, justify=CENTER)
    """
    This function creates entry field on GUI
    """
    enter_word_entry.place(x=500, y=80)
    """
    This function set the position of entry field on GUI
    """
    enter_word_entry.focus_set()

    searchimage = PhotoImage(file='D:\\SW\\Model\\img.png')
    """
    This funtion takes a image file as an input
    return: store the image on searchImage variable
    """
    searchButton = Button(root, image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=search)
    """
    This function creates search button on GUI
    """
    searchButton.place(x=550, y=150)
    """
    This function set the position of set button on GUI
    """

    root.mainloop();
    # print("hello")

#dictionary()