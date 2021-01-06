#1
def square(x):
    """
    Returns x^2.
    :param x: int.
    :return: int x raised to the second power.
    """
    return x**2

print(square(2))

#2
def print_string(word):
    """
    Prints a string passed in by user.
    :param word: str.
    """
    print(word)

print_string("This is a sentence.")

#3
def add_numbers(x, y, z, a=4, b=5):
    """
    Returns the result of the sum of 3 required parameters
    and 2 optional parameters.
    :param x: int.
    :param y: int.
    :param z: int.
    :param a: int.
    :param b: int.
    :return: int of sum of parameters.
    """
    return x + y + z + a + b

result = add_numbers(1, 2, 3)
print(result)

#4
def divide(x):
    """
    Returns the result of an integer divided by 2.
    :param x: int.
    :return: int of quotient x divided by 2.
    """
    return x / 2

def multiply(x):
    """
    Returns the result of an integer multiplied by 4.
    :param x: int.
    :return: int of product x and 4.
    """
    return x * 4

y = divide(4)
z = multiply(y)

print(z)

#5
def string_to_float(string):
    """
    Converts passed in str to float and prints the result if possible,
    otherwise it prints an error message.
    :param string: str.
    """
    try:
        print(float(string))
    except ValueError:
        print("Could not convert the string to a float.")

string_to_float("55.8")

#6
#Answer was to add docstrings to 1-5
