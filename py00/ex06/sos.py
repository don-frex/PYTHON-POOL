import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def encode_morse(text: str) -> str:
    """Encode an alphanumeric and space string into Morse code."""
    morse_chars = []
    for c in text.upper():
        if c not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse_chars.append(NESTED_MORSE[c].strip())
    return " ".join(morse_chars)


def main():
    """Encode argument string into Morse code and print result."""
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        text = sys.argv[1]
        print(encode_morse(text))
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
