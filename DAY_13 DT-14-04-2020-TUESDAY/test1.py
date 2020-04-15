import main
import unittest

#print("test")

class Testmain(unittest.TestCase):
    def do_some(self):
        num = 3
        result = main.do_stuff(num)
        self.assertEqual(result,13)
        #print(result)


unittest.main()
