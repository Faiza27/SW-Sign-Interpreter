import modules
import outputSign
#import audio_data



def text_to_sign(text):
    """

    :param text: text
    :return: Corresponding sign output for text input
    """
    alphabet = text
    print('You said: ' + alphabet.lower())

    my_inputs = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick',
                 'be careful',
                 'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'Hello',
                 'lets go for lunch'
                 'do you want something to drink',  'good morning',
                 'what is your name', 'flower is beautiful',
                 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything',
                 'what is your problem'
                 'there was traffic jam', 'what are you doing', 'i had to say something but I forgot',
                 'sign language interpreter'
                 'nice to meet you', 'please wait for sometime',
                 'shall I help you']


    arr_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z']

    """
    Taking input for letters
    """

    for itr in modules.string.punctuation:
        alphabet = alphabet.replace(itr, "")
        """
        For replacing string punctuation iterating through the alphabet sets
        """

        if (alphabet.lower() == 'goodbye' or alphabet.lower() == 'good bye' or alphabet.lower() == 'bye'):
            print("oops!Time To say good bye")
            break

        elif (alphabet.lower() in my_inputs):

            #print("entered into elif for gif")
            class ImageLabel(modules.tk.Label):
                """
                a label that displays images, and plays them, if they are gifs

                """

                def load(self, image):
                    if isinstance(image, str):
                        image = modules.Image.open(image)
                        """
                        load all the frames inside the images
                         """
                    self.loc = 0
                    self.frames = []
                    """
                    start the animation
                    """
                    try:
                        for i in modules.count(1):
                            self.frames.append(modules.ImageTk.PhotoImage(image.copy()))
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


            root = modules.tk.Tk()
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
            reply = modules.buttonbox(choices=choices)

            """
            buttonbox method has 3 parameter(text,title,button_list)
            """
            if reply == choices[0]:
                continue
            elif reply == choices[1]:
                quit()
        else:
            #print("takes from alphabet")
            for i in range(len(alphabet)):
                if (alphabet[i] in arr_letter):

                    ImageAddress = 'letters/' + alphabet[i] + '.jpg'
                    ImageItself = modules.Image.open(ImageAddress)
                    ImageNumpyFormat = modules.np.asarray(ImageItself)
                    modules.plt.imshow(ImageNumpyFormat)
                    modules.plt.draw()
                    modules.plt.pause(0.8)
                else:
                    continue


            choices = ["Continue watching", "Quit"]
            """
            Option 1 for continue
            Option 2 for Terminate the program    
            """
            reply = modules.buttonbox(choices=choices)

            """
            buttonbox method has 3 parameter(text,title,button_list)
            """
            if reply == choices[0]:
                continue
            elif reply == choices[1]:
                quit()


#text="be careful"
#text_to_sign(text)