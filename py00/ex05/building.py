import string
import sys


def count_characters(text: str) -> None:
    """Count and display sums of upper, lower, punctuation, digits, spaces."""
    characters = len(text)
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punctuation = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {characters} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Parse sys.argv or prompt user, then display character breakdown."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1 or sys.argv[1] is None or sys.argv[1] == "":
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]
        count_characters(text)
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except (EOFError, KeyboardInterrupt):
        pass


if __name__ == "__main__":
    main()
