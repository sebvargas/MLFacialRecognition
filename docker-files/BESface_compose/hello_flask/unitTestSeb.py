import unittest
import backend
import os

class SomeTest(unittest.TestCase):

	def setUp(self):
		pass
	def tearDown(self):
		pass
	def runTest(self):
		#To make sure it generates the image
		
		#print("cleaned directory")
		#Image Uri
		goodImage = "data:image/jpeg;base64,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"
		self.assertEqual(backend.imgURItoFile(goodImage, "signupPic"), True)
		self.assertEqual("signupPic.png" in os.listdir("."), True)
		
		#print("cleaned directory")
		badImage = "data:image/jpeg;base64,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"
		
		self.assertEqual(backend.imgURItoFile(badImage, "signupPic"), False)
		self.assertEqual("signupPic.png" in os.listdir("."), True)

if __name__=='__main__':
	unittest.main()