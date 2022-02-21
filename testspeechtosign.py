import unittest
from Controller import recordTotext


class TestAudioToSign(unittest.TestCase):


	def test_recordInput(self):
		actualOutput= recordTotext.record_input(path='C:\\Users\\Promi\\Downloads\\iambusy.wav')
		expectedOutput="I am busy"
		self.assertEqual(actualOutput, expectedOutput)



if __name__ == '__main__':
	unittest.main()
