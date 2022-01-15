import pyttsx3
"""
Text to speech conversion python library
"""

from gtts import gTTS

"""
This is a google text to speech python Library
"""

# initialisation
engine = pyttsx3.init()

"""
init() factory function to get a reference to a pyttsx3.

"""

# testing
name = input("enter a name")
"""
Taking input for name
"""
engine.say(name)
#engine.say("Fariha Akter Promi")

greetings = input("Type something like greetings")
engine.say(greetings)
engine.runAndWait()
"""
This function will make the speech audible in the system
"""


def on_start(name):
    """
        :param name:string
        :return: sends a request to the server
        """
    """
    This function will start working on load
    """

    print('starting')


def on_word(name, location, length):
    """

    :param name:string

    :param location:integer

    :param length:integer

    :return:The engine returns a voice
    """
    print('word', name, location, length)


def on_end(name, completed):
    """

    :param name:Name associated with the utterance

    :param completed:True if the utterance was output in its entirety or not

    :return:Fired when the engine finishes speaking an utterance
    
    """
    print('finishing', name, completed)


engine = pyttsx3.init()
"""
init() factory function to get a reference to a pyttsx3
"""

engine.connect('started-utterance', on_start)
"""
 Provides application access to text-to-speech synthesis.
 Registers a callback for notifications on the given topic.
"""
engine.connect('started-word', on_word)
engine.connect('finished-utterance', on_end)


question=input("enter your question")

engine.say(question)
"""
To make the text in audible format
"""


tts = gTTS(text=name, lang='en', slow=False)
"""
gTTS is a google text to speech python Library
"""
tts.save('converted-file.mp3')
"""
tts read words and convert them into audio
"""

engine.runAndWait()
"""
This function will make the speech audible in the system
"""