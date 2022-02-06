import numpy as np
"""this is numpy module"""
import matplotlib.pyplot as plt
"""this is matplotlib as """
import cv2
"""for image processing cv2"""
from easygui import *
"""
for GUI Programming
"""
import os
import string
"""os provide function for interacting with the operating system"""
from PIL import Image, ImageTk
""" 
PTL for python python image library
"""
from itertools import count
"""
iterators to produce complex iterators
"""
import tkinter as tk
"""
Tkinter is for GUI framework
"""

import audio_data



def text_to_sign(text):
    """
    This function will will match the text which was a input from user with data from audio_data.py
    and images(letters folder) and gifs(Gifs folder).Then show the matched output in a tkinkter window.
    First it will match output with gifs that are in Gifs folder . In Gifs folder there are images only for
    which are defined in audio_data.py (my_inputs). This function will not work for any other inputs. It will
    also show what the user has inputted in text format.

    :param: text: text
    :return: Corresponding sign output for text input

    It will take text as a parameter which can be a string
    or a single character that is going to passed into this function as text and return or show image or gif
    in tkinkter window
    """
    alphabet = text
    print('You said: ' + alphabet.lower())
    """
    Taking input for letters
    """

    for itr in string.punctuation:
        alphabet = alphabet.replace(itr, "")
        """
        For replacing string punctuation iterating through the alphabet sets
        """
    
        if (alphabet.lower() == 'goodbye' or alphabet.lower() == 'good bye' or alphabet.lower() == 'bye'):
            print("oops!Time To say good bye")
            break
    
        elif (alphabet.lower() in audio_data.my_inputs):
    
            #print("entered into elif for gif")
    
            class ImageLabel(tk.Label):
                """
                a label that displays images, and plays them, if they are gifs
    
                """
    
                def load(self, image):
                    if isinstance(image, str):
                        image =Image.open(image)
                        """
                        load all the frames inside the images
                         """
                    self.loc = 0
                    self.frames = []
                    """
                    start the animation
                    """
                    try:
                        for i in count(1):
                            self.frames.append(ImageTk.PhotoImage(image.copy()))
                            image.seek(i)
                            """Seeks image to the given file"""
    
                    except EOFError:
    
                        pass
    
                    try:
                        self.delay = image.info['duration']
                    except:
                        self.delay = 100
    
                    if len(self.frames) == 1:
                        self.config(image=self.frames[0])
                    else:
                        self.next_frame()
    
                def unload(self):
                    self.config(image=None)
                    self.frames = None
                    """
                    unload() function config if no image is found for corresponding input
                    """
    
                def next_frame(self):
                    if self.frames:
                        self.loc += 1
                        self.loc %= len(self.frames)
                        self.config(image=self.frames[self.loc])
                        self.after(self.delay, self.next_frame)
                    """
                    next_frame() function matches image with corresponding input
                    """
    
    
            root = tk.Tk()
            """
            root is To initialize tkinter
            """
            lbl = ImageLabel(root)
            """
            label  is for displaying tkinter image or text
            """
            lbl.pack()
            """
            pack() method tells tk to fit the window of the given text
            """
    
            lbl.load(r'Gifs/{0}.gif'.format(alphabet))
            """load gif"""
            root.mainloop()
            """ root.mainloop() is an eventloop for appearing Tkinter window """
    
    
            choices = ["Continue watching", "Quit"]
            """
            Option 1 for continue
            Option 2 for Terminate the program
            """
            reply = buttonbox(choices=choices)
    
            """
            buttonbox method has 3 parameter(text,title,button_list)
            """
            if reply == choices[0]:
                continue
            elif reply == choices[1]:
                quit()
        elif(alphabet.lower() in audio_data.arr_letter):
    
                    ImageAddress = 'letters/' + alphabet + '.jpg'
                    ImageItself = Image.open(ImageAddress)
                    ImageNumpyFormat = np.asarray(ImageItself)
                    plt.imshow(ImageNumpyFormat)
                    plt.draw()
                    plt.pause(0.8)
    
    
                    choices = ["Continue watching", "Quit"]
                    """
                    Option 1 for continue
                    Option 2 for Terminate the program
                    """
                    reply = buttonbox(choices=choices)
    
                    """
                     buttonbox method has 3 parameter(text,title,button_list)
                    """
                    if reply == choices[0]:
                        continue
                    elif reply == choices[1]:
                        quit()

    return text
#text="any questions"
#text_to_sign(text)
