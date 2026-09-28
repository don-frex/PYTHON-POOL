import math
from typing import Any


def NULL_not_found(object: Any) -> int:
    """Identify and print null-like values and their types, return 0 or 1."""
    if object is None:
        print(f"Nothing: None {type(object)}")
        return 0
    if isinstance(object, float) and math.isnan(object):
        print(f"Cheese: nan {type(object)}")
        return 0
    if isinstance(object, bool) and object is False:
        print(f"Fake: False {type(object)}")
        return 0
    if isinstance(object, int) and not isinstance(object, bool):
        if object == 0:
            print(f"Zero: 0 {type(object)}")
            return 0
    if isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
        return 0

    print("Type not Found")
    return 1
