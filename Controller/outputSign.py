
from Controller import recordTotext, audioTotext, textTosign, modules


def output_sign(inputType):
    """

    :param inputType: text, this should be a valid wav file path

    :return: display sign
    """
    while 1:
        if (inputType=="1"):
            path = input(print("Paste the audio file path on .wav format"))
            """
            only .wav formate will work 
            """
            text = recordTotext.record_input(path)
            """
            converting to text input record
            """
            textTosign.text_to_sign(text)
        else:
            my_image = "signlang.png"
            msg = "HELLO SAY SOMETHING TO GET YOUR SIGN LANGUAGE"
            choices = ["Live Voice", "All Done!"]
            """
            Option 1 for Convert microphone audio to sign
            Option 2 for Terminate the program    
            """
            reply = modules.buttonbox(msg, image=my_image, choices=choices)

            """
            buttonbox method has 3 parameter(text,title,button_list)
            """
            if reply == choices[0]:
                text = audioTotext.audio_to_text()
                textTosign.text_to_sign(text)
            if reply == choices[1]:
                quit()


output_sign('2')