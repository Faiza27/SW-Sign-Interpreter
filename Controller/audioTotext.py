from Controller import modules


def audio_to_text():
    """

    :return: return audio file into text
    """
    my_audio = modules.sr.Recognizer()
    with modules.sr.Microphone() as source:
        # For adjusting with background noise

        my_audio.adjust_for_ambient_noise(source)

        i = 0

        print("Say Something")

        audio = my_audio.listen(source)
        """this variable take input from microphone as source"""
        # recognize speech using Sphinx
        try:

            alphabet = my_audio.recognize_google(audio)
            """ recognize google voice
            """
            alphabet = alphabet.lower()
            print('Say something... ' + alphabet.lower())


        except:
            print(" ")
    # plt.close()

        return alphabet

#text=audio_to_text()
#print(text)