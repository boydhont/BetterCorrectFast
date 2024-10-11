# tests/test_create.py
import unittest
from bettercorrectfast import *
from io import StringIO
import sys

class TestCreate(unittest.TestCase):
    def test_create(self):
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the function
        debug_bcf = create()
        print(debug_bcf)
        debug_bcf.save("tests/debug.bcf")
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        
        # Assert the output
        # TODO add assert the output using self.assertEqual
       
        # Print the captured output to the console
        print(captured_output.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
