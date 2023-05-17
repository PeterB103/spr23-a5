#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
assert run("5 * 5").output == 25
assert run("5 / 5").output == 1
assert run("5 - 5").output == 0
assert run("5 + 6").output == 11


print("All tests passed!")
