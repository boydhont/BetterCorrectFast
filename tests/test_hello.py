# tests/test_hello.py
import unittest
from better_correct_fast import say_hello
from io import StringIO
import sys

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the function
        say_hello()
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        
        # Assert the output
        # TODO add assert the output using self.assertEqual
       
        # Print the captured output to the console
        print(captured_output.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
