import unittest
import voice

class MyTestCase(unittest.TestCase):
    def test_male_voice_change(self):
        actualOutput = voice.change_to_male_voice("I am sleepy")
        expectedOutput = voice.change_to_male_voice("I am sleepy")
        self.assertEqual(actualOutput, expectedOutput)
    def test_female_voice_change(self):
        actualOutput = voice.change_to_female_voice("I am sleepy")
        expectedOutput = voice.change_to_female_voice("I am sleepy")
        self.assertEqual(actualOutput, expectedOutput)
if __name__ == '__main__':
    unittest.main()
