# Type hints are just labels you attach to variables/parameters/return values telling anyone reading the code (including yourself, later) what kind of value is expected there. Python does not enforce them at runtime — they're purely informational, like a comment that your editor and certain tools can actually understand and check for you.

name: str = "Sky"
age: int = 18
height: float = 1.75
is_student: bool = True


print(name)


# What happens if you "break" the hint?
age: int = "eighteen"  # this runs FINE, no error
print(age)  # "eighteen"

def add_numbers(a: int, b: int) -> int:
    return a + b
# Reading this: "add_numbers expects two integers (a and b), and promises to return an integer." Again — Python won't stop you from calling add_numbers("hi", "there"), it'll just try to run it (and in this case, "hi" + "there" actually works because Python allows string concatenation with +, giving "hithere" — even though the hints said int!). The hints are guidance, not a wall.


def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)
# numbers: list[float] — "expects a list containing floats" (decimal numbers)
# -> float — "returns a single float"