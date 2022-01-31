"""
connecting with functions of Controller
"""

from Controller import sign_dictionary, textTosign, audioTotext, modules, recordTotext, voice
#from Controller import convertsigntext

"""
import PySimpleGUI to build the user interface
"""
import PySimpleGUI as sg

"""
Define the main window's contents with buttons
"""
layout = [[sg.Text("Welcome to Sign Interpreter..")],
          [sg.Button("Text to sign")],
          [sg.Button("Sign to text")],
          [sg.Button("Speech to sign")],
          [sg.Button("Sign to speech")],
          [sg.Button("Recorded audio to sign")],
          [sg.Button("Sign Dictionary")],
          [sg.Button('Ok'), sg.Button('Quit')]]

""" 
Create the window of main interface
"""
window = sg.Window('Sign language interpreter', layout)

"""
Display and interact with the Window using an Event Loop
"""
while True:
    """
    read events and the values from main window
    """
    event, values = window.read()
    """
    See if user wants to quit or window was closed
    """
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
        """
            Check for user choices according to events and trigger those functions
        """



    elif event == "Text to sign":
        # textTosign.text_to_sign()
        """
            Text to sign window will appear
        """
        window2 = sg.Window("Text to sign", [[sg.Text("Input text")],
                                             [sg.Input(key=1)],
                                             [sg.Button("Interpret now"), sg.Button("Back")]])
        """
            Input field will take text input and show options either interpret now or go back
        """
        event, values = window2.read()
        # print(event)
        # print(type(event))
        # if window2.read(close=True)[0] == "Back":
        if event == "Back":
            window2.close()
        """
        for going back
        """
        if event == "Interpret now":
            #print(values)
            text = str(values[1])
            # print(text)
            textTosign.text_to_sign(text)
        """
        for interpreting text to sign
        """




    elif event == "Sign to text":
        """
        Sign to text window will appear
        """
        window2 = sg.Window("Sign to text", [[sg.Text("Input sign image directory")],
                                             [sg.Input(key=1)],
                                             [sg.Button("Interpret now"), sg.Button("Back")]])
        """
        Input field will take sign image directory and show options either interpret now or go back
        """
        event, values = window2.read()
        # print(event)
        # print(type(event))
        # if window2.read(close=True)[0] == "Back":
        if event == "Back":
            window2.close()
        """
        for going back
        """
        if event == "Interpret now":
            #print(values)
            text = str(values[1])
            # print(text)
            SignToText.sign_to_text(text)
        """
        for interpreting sign to text
        """




    elif event == "Speech to sign":
        window2 = sg.Window("Speech to sign", [[sg.Text("HELLO SAY SOMETHING TO GET YOUR SIGN LANGUAGE")],
                                             [sg.Button("Live Voice"), sg.Button("Back")]])
        """
        Audio will take using device microphone and show options either interpret now or go back
        """
        event, values = window2.read()
        # print(event)
        # print(type(event))
        # if window2.read(close=True)[0] == "Back":

        if event == "Live Voice":
            text = audioTotext.audio_to_text()
            """
            for interpreting audio to text
            """
            textTosign.text_to_sign(text)
            # print(text)
            """
            for interpreting text to sign
            """
        if event == "Back":
            window2.close()





    elif event == "Sign to speech":
        window2 = sg.Window("Sign to speech", [[sg.Text("Input sign file directory")],
                                             [sg.Input(key=1)],
                                             [sg.Button("Interpret now in male voice"), sg.Button("Interpret now in female voice"), sg.Button("Back")]])
        event, values = window2.read()
        # print(event)
        # print(type(event))
        # if window2.read(close=True)[0] == "Back":
        if event == "Back":
            window2.close()
        if event == "Interpret now in male voice":
            # print(values)
            text = str(values[1])
            print(text)

            #text2 = str(convertsigntext.convert_sign_to_text(text))
            """
            converting the sign into text
            """
            voice.change_to_male_voice(text2)
            """
            converting the text into male voice
            """
        if event == "Interpret now in female voice":
            # print(values)
            text = str(values[1])
            print(text)
            text2 = str(convertsigntext.convert_sign_to_text(text))
            """
            converting the sign into text
            """
            voice.change_to_female_voice(text2)
            """
            converting the text into female voice
            """





    elif event == "Recorded audio to sign":
        window2 = sg.Window("Recorded audio to sign", [[sg.Text("Input wav file directory")],
                                             [sg.Input(key=1)],
                                             [sg.Button("Interpret now"), sg.Button("Back")]])
        event, values = window2.read()
        # print(event)
        # print(type(event))
        # if window2.read(close=True)[0] == "Back":
        if event == "Back":
            window2.close()
        if event == "Interpret now":
            #print(values)
            text = str(values[1])
            print(text)
            text2 = str(recordTotext.record_input(text))
            """
            converting to text input record
            """
            textTosign.text_to_sign(text2)





    elif event == "Sign Dictionary":
        sign_dictionary.dictionary()





window.close()


 # print("hello")