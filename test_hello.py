import io
import unittest
from contextlib import redirect_stdout

import hello


class HelloTest(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(hello.greet(), "Hello, World!")

    def test_main_prints_greeting(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            hello.main()
        self.assertEqual(buf.getvalue(), "Hello, World!\n")


if __name__ == "__main__":
    unittest.main()
