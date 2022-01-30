
import pyttsx3
engine = pyttsx3.init()
"""
getProperty(): get the current value of an engine property
"""
voices = engine.getProperty('voices')

def change_to_male_voice(text):
   """
   This method takes a string as text parameter and
   converts it to a male speech.

   :param text:String
   :return: Play the converted audio of the text in male voice
   """


   engine.setProperty('voice', voices[0].id)
   engine.say(text)
   engine.runAndWait()


def change_to_female_voice(text):
   """
   This method takes a string as text parameter and
   converts it to a female speech.

   :param text: String
   :return: Play the converted audio of the text in female voice
   """
   engine.setProperty('voice', voices[1].id)
   engine.say(text)
   engine.runAndWait()


text = "It's very cold and I have to go out"
change_to_female_voice(text)
change_to_male_voice(text)
