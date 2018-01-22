import unittest
#login function lives here
from backend import login

class LoginTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def runTest(self):
        #malformated, nonsensical uri
        bad_uri = "garbage"
        #Should return None
        self.assertEqual(login(bad_uri), None)

        valid_uri = ""
        #retrieve a uri
        with open('valid_image_URI', 'r') as myfile:
            valid_uri=myfile.read().replace('\n', '')
        self.assertEqual(login(valid_uri), "fgf")

if __name__=='__main__':
   unittest.main()

