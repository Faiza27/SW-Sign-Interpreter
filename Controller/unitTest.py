import unittest
import textToSpeech
class TestTextToSpeech(unittest.TestCase):


	def test_textInput(self):
		actualOutput=textToSpeech.onStart(" Fariha")
		expectedOutput="D:\TextToSpeech\scripts\converted-file.mp3"
		self.assertEqual(actualOutput, expectedOutput)



if __name__ == '__main__':
	unittest.main()
