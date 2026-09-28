import sys


def whatis(number: int) -> str:
    """Return whether the number is Even or Odd."""
    return "I'm Even." if number % 2 == 0 else "I'm Odd."


def main():
    """Check sys.argv and display whether the number is Even or Odd."""
    argv = sys.argv
    if len(argv) == 1:
        return
    try:
        assert len(argv) == 2, "more than one argument is provided"
        try:
            number = int(argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        print(whatis(number))
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
