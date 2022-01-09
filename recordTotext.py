import speech_recognition as sr
r=sr.Recognizer()
def record_input(path):
    """

    :return:recorded audio into sign
    """
    #path = input(print("Paste the audio file path on .wav format"))
    try:
        with sr.AudioFile(path) as source:
            audio = r.record(source)
            r.listen(source)
            try:
                text = r.recognize_google(audio)
                """
                converting the audio into text
                """
                # print('Working on....')
                #print(text)
            except:
                print("run again")
        return text
    except:
        print("Error with input. Please try with proper format and path location.")

#record_input('C:\\Users\\Promi\\Downloads\\iambusy.wav')