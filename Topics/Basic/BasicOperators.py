# Operators are the constructs, which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called the operands and + is called the operator.
class ArithmeticOperators:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b

    @staticmethod
    def modulus(a, b):
        return a % b

    @staticmethod
    def exponent(a, b):
        return a ** b

    @staticmethod
    def floor_division(a, b):
        return a // b


class ComparisonOperators:
    @staticmethod
    def is_equal(a, b):
        return a == b

    @staticmethod
    def is_notequal(a, b):
        return a != b

    @staticmethod
    def is_greater(a, b):
        return a > b

    @staticmethod
    def is_less(a, b):
        return a < b

    @staticmethod
    def is_greater_or_equal(a, b):
        return a >= b

    @staticmethod
    def is_less_or_equal(a, b):
        return a <= b


class AssignmentOperators:
    @staticmethod
    def assign():
        a = 15
        return a

    @staticmethod
    def add_and_assign(a):
        b = 10
        b += a
        return b

    @staticmethod
    def subtract_and_assign(a):
        b = 10
        b -= a
        return b

    @staticmethod
    def multiply_and_assign(a):
        b = 10
        b *= a
        return b

    @staticmethod
    def division_and_assign(a):
        b = 10
        b /= a
        return b

    @staticmethod
    def modulus_and_assign(a):
        b = 10
        b %= a
        return b

    @staticmethod
    def exponent_and_assign(a):
        b = 10
        b **= a
        return b

    @staticmethod
    def floor_division_and_assign(a):
        b = 10
        b //= a
        return b
