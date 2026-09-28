import string
import sys


def filter_words(text: str, length: int) -> list:
    """Filter words from text with length greater than given integer."""
    words = text.split()
    return [word for word in words if (lambda w: len(w) > length)(word)]


def main():
    """Validate arguments and display filtered list of words."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        text = sys.argv[1]
        try:
            length = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        for c in text:
            if c in string.punctuation or not c.isprintable():
                raise AssertionError("the arguments are bad")

        print(filter_words(text, length))
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
