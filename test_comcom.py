import unittest

import comcom.procedural

class TestCopy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        comcom.procedural.init()

    @classmethod
    def tearDownClass(cls):
        comcom.procedural.destroy()

    def test_cat_short(self):
        input = b"abc"
        output = comcom.procedural.run_command(input, 'cat', ['cat'])
        self.assertEqual(input, output)

if __name__ == '__main__':
    unittest.main()
