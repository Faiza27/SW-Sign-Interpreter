"""
Important modules.
numpy
matplotlib
easygui
cv2
string
PIL  for image labeling
tkinter for GUI
itertools for iteration

"""


import speech_recognition as sr
"""
this is speech recognition module
"""
import numpy as np
"""
this is numpy module
"""
import matplotlib.pyplot as plt
"""this is matplotlib as """
import cv2
"""for image processing cv2"""
from easygui import *
"""
for GUI Programming
"""
import string
#import selecting
import os
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
# obtain audio from the microphone
"""
speechtoSign() return if matches with the input
"""


def speechtoSign():
        my_audio= sr.Recognizer()
        my_inputs=['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
                'can we meet tomorrow', 'did you book tickets', 'did you finish homework','Hello','lets go for lunch'
                'do you want something to drink', 'do you want tea or coffee', 'good morning','what is your name'
                 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything','what is your problem'
                 'there was traffic jam','what are you doing','i had to say something but I forgot','sign language interpreter'
                 'nice to meet you',  'please wait for sometime',
                'shall I help you']


        """Taking input for letters """
        arr_letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
        """taking source as audio from microphone"""

        
        with sr.Microphone() as source:
              

            #For adjusting with background noise

                my_audio.adjust_for_ambient_noise(source)


                i=0
                while True:
                        print("Say Something")

                        audio = my_audio.listen(source)
                        """this variable take input from microphone as source"""
                        # recognize speech using Sphinx
                        try:

                                alphabet= my_audio.recognize_google(audio)
                                """ recognize google voice
                                """
                                alphabet = alphabet.lower()
                                print('Say something.. ' + alphabet.lower())

                                for itr in string.punctuation:
                                    alphabet = alphabet.replace(itr, "")
                                    """For replacing string punctuation iterating through the alphabet sets"""

                                if(alphabet.lower()=='goodbye' or alphabet.lower()=='good bye' or alphabet.lower()=='bye'):
                                        print("oops!Time To say good bye")
                                        break

                                elif(alphabet.lower() in audio_data.my_inputs):

                                    class ImageLabel(tk.Label):
                                            """a label that displays images, and plays them, if they are gifs"""
                                            def load(self, image):
                                                if isinstance(image, str):
                                                    image = Image.open(image)
                                                self.loc = 0
                                                self.frames = []
                                                """
                                                load() function will return a image which  parameter has been defined
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
                                                """next_frame() function matches image with corresponding input"""
                                    root = tk.Tk()
                                    """ root is To initialize tkinter"""
                                    lbl = ImageLabel(root)
                                    """label  is for displaying tkinter image or text"""
                                    lbl.pack()
                                    """pack() method tells tk to fit the window of the given text"""
                                    lbl.load(r'Gifs/{0}.gif'.format(alphabet.lower()))
                                    """load image"""
                                    root.mainloop()
                                    """ root.mainloop() is an eventloop for appearing Tkinter window """
                                else:
                                    for i in range(len(alphabet)):
                                                    if(alphabet[i] in audio_data.arr_letter):

                                                            ImageAddress = 'letters/'+alphabet[i]+'.jpg'
                                                            ImageItself = Image.open(ImageAddress)
                                                            ImageNumpyFormat = np.asarray(ImageItself)
                                                            plt.imshow(ImageNumpyFormat)
                                                            plt.draw()
                                                            plt.pause(0.8)
                                                    else:
                                                            continue
                                    """If does not found any gif for corresponding input"""

                        except:
                               print(" ")
                        plt.close()
while 1:
  my_image   = "signlang.png"
  msg="HELLO SAY SOMETHING TO GET YOUR SIGN LANGUAGE"
  choices = ["Live Voice","All Done!"]
  """
  Option 1 for Convert microphone audio to sign
   Option 2 for Terminate the program    
   """
  reply  = buttonbox(msg,image=my_image,choices=choices)

  """
  buttonbox method has 3 parameter(text,title,button_list)
  """
  if reply ==choices[0]:
        speechtoSign()
  if reply == choices[1]:
        quit()
