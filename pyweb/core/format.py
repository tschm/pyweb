from enum import Enum

class Format(Enum):
    HTML = "html"
    CSV = "csv"
    JSON = "json"

    @staticmethod
    def parse(format):
        small_format = format.lower().strip()
        for f in Format:
            if small_format == f.value:
                return f

        raise AssertionError


if __name__ == '__main__':
    x = "csv"
    print(Format.parse(x).value)

    y = "ccsv"
    print(Format.parse(y))
