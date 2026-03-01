import csv
from typing import List, Generator


class Repository:
    def __init__(self, filename: str):
        self.filename = filename
        self._data = None

    def read(self):
        with open(self.filename, 'r', newline='', encoding='utf-8') as csv_file:
            text = csv.reader(csv_file, delimiter=',')
            next(text)
            for row in text:
                yield row

    def get_all(self) -> List[List[str]]:
        return list(self.read())

    def __call__(self, *args, **kwargs):
        return self.read()