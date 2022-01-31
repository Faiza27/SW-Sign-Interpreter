import unittest
import textSign
import os
class TestTextToSign(unittest.TestCase):

	"""
	  This is a  class whose instances are single test cases.It has a by default method run tests

      By default, the test code itself should be placed in a method named 'runTest'.
	"""

	def test_TextInput(self):
		"""
		This function is going to match the text input (i am sorry) with the gif (i am sorry.gif)
		and after running test case has it passed or failed , will show it.

		:param: self . This is going to create a instance of it's own and run the test case.

		:return:OK(passed) or FAILED .

        This is also going to show how many tests it ran
		"""
		s = 'E:\\signLang\\Gifs\\i am sorry.gif'
		actualOutput=textSign.text_to_sign(text="i am sorry")
		expectedOutput1=os.path.basename(s)
		#print(expectedOutput1)
		expectedOutput2=os.path.basename(s).split('.')[-1]
		#print(expectedOutput2)
		expectedOutputFinal= expectedOutput1.replace('.'+expectedOutput2, '')
		#print(expectedOutputFinal)
		self.assertEqual(actualOutput,expectedOutputFinal)



if __name__ == '__main__':
	unittest.main()