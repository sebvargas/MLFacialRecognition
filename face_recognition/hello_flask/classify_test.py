import unittest
from backend import login

class LoginTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def runTest(self):
        bad_uri = "garbage"
        self.assertEqual(login(bad_uri), None)

        valid_uri = "" 
        with open('valid_image_URI', 'r') as myfile:
            valid_uri=myfile.read().replace('\n', '')
        self.assertEqual(login(valid_uri), "validUser")

if __name__=='__main__':
   unittest.main()

