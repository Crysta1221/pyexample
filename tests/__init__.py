import unittest

from pyexample import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read_lines(self):
        printer = CSVPrinter("example.csv")
        line = printer.read_lines()
        print(line)
        self.assertEqual(len(line), 3, "Unexpected number of lines")

    def test_read_cols(self):
        printer = CSVPrinter("example.csv")
        col = printer.read_cols()
        print(col)
        self.assertEqual(len(col), 4, "Unexpected number of columns")

    def test_file_not_found(self):
        printer = CSVPrinter("example1.csv")
        with self.assertRaises(FileNotFoundError):
            printer.read_lines()