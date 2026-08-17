import csv

class CSVPrinter:
    def __init__(self, filename):
        self.filename = filename

    def read_lines(self):
        with open(self.filename) as file:
            reader = csv.reader(file)
            lines = list(reader)
        return lines

    def read_cols(self):
        with open(self.filename) as file:
            reader = csv.reader(file)
            cols = next(reader,[])
        return cols
