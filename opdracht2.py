import unittest
import re

class Square(object):
    def __init__(self, size = 5):
        self.size = size
    def width(self):
        return self.size
    def height(self):
        return self.size
    def toString(self):
        x=''
        for i in range(self.size):
            for j in range(self.size):
                x+='*'
            x+='\n'
        return x


class SquareTest(unittest.TestCase):
    def setUp(self):
        self.givenSize = 5
        self.square = Square( self.givenSize )

    def testWidth(self):
        expected = self.givenSize
        self.assertEqual( expected, self.square.width() )
    
    def testHeight(self):
        expected = self.givenSize
        self.assertEqual( expected, self.square.width() )

    def testPrintedChars(self):
        expectedChar = '*'
        actual = self.square.toString()
        starsRE = r'(\*{' + str(self.givenSize) + r'}\n){' + str(self.givenSize) + '}'
        regex = re.compile(starsRE, re.MULTILINE)
        self.assertTrue(regex.match(actual) != None)
        

if __name__ == '__main__':
    unittest.main()
