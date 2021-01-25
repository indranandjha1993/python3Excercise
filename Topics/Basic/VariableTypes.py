# Variables are nothing but reserved memory locations to store values. It means that when you create a variable, you reserve some space in the memory.
# Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory.
# Therefore, by assigning different data types to the variables, you can store integers, decimals or characters in these variables.
class VariableTypes:
    # Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable.
    # The equal sign (=) is used to assign values to variables.
    # The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable.
    @staticmethod
    def assigned_val():
        counter = 100
        miles = 1000.0
        name = "Indra"
        return "counter: " + str(counter) + "\nmiles: " + str(miles) + "\nname:" + name

    # Here, an integer object is created with the value 1, and all the three variables are assigned to the same memory location.
    # You can also assign multiple objects to multiple variables.
    #
    # Here, two integer objects with values 1 and 2 are assigned to the variables a and b respectively, and one string object with the value "john" is assigned to the variable c.
    @staticmethod
    def multiple_assignment():
        a = b = c = 1
        # OR
        a, b, c = 1, 2, "john"
        return "a= " + str(a) + "\nb= " + str(b) + "\nc= " + str(c)

    # Number data types store numeric values. Number objects are created when you assign a value to them.
    @staticmethod
    def numbers():
        num_int = 1
        num_float = 10.2
        num_complex = 3.14j
        return num_int + num_float + num_complex

    # Strings in Python are identified as a contiguous set of characters represented in the quotation marks. Python allows either pair of single or double quotes.
    # Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 to the end.
    #
    # The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator.
    @staticmethod
    def strings():
        str1 = "Hello Worlds!"
        return str1

    # Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]).
    # To some extent, lists are similar to arrays in C. One of the differences between them is that all the items belonging to a list can be of different data type.
    #
    # The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1.
    # The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator.
    @staticmethod
    def lists():
        list1 = ['abed', 123, 2.012, 'indra', 70.2]
        return list1

    # A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however,
    # tuples are enclosed within parenthesis.
    #
    # The main difference between lists and tuples are − Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed,
    # while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists.
    @staticmethod
    def tuples():
        tuple1 = ('abed', 123, 2.012, 'indra', 70.2)
        return tuple1

    # Python's dictionaries are kind of hash-table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs.
    # A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.
    #
    # Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).
    @staticmethod
    def dictionary():
        dict1 = {'name': 'john', 'code': 6734, 'dept': 'sales'}
        return dict1

    # Sometimes, you may need to perform conversions between the built-in types. To convert between types, you simply use the type-names as a function.
    #
    # There are several built-in functions to perform conversion from one data type to another. These functions return a new object representing the converted value.
    @staticmethod
    def conversion(x, var_type = "str"):
        if var_type == "str":
            print(type(str(x)))
            print("\n")
            return str(x)
        elif var_type == "int":
            print(type(int(x)))
            print("\n")
            return int(x)
        elif var_type == "float":
            print(type(float(x)))
            print("\n")
            return float(x)
        elif var_type == "complex":
            print(type(complex(x)))
            print("\n")
            return complex(x)
        elif var_type == "repr":
            print(type(repr(x)))
            print("\n")
            return repr(x)
        elif var_type == "eval":
            print(type(eval(x)))
            print("\n")
            return eval(x)
        elif var_type == "tuple":
            print(type(tuple(x)))
            print("\n")
            return tuple(x)
        elif var_type == "list":
            print(type(list(x)))
            print("\n")
            return list(x)
        elif var_type == "set":
            print(type(set(x)))
            print("\n")
            return set(x)
        elif var_type == "dict":
            print(type(dict(x)))
            print("\n")
            return dict(x)
        elif var_type == "frozenset":
            print(type(frozenset(x)))
            print("\n")
            return frozenset(x)
        elif var_type == "chr":
            print(type(chr(x)))
            print("\n")
            return chr(x)
        elif var_type == "ord":
            print(type(ord(x)))
            print("\n")
            return ord(x)
        elif var_type == "hex":
            print(type(hex(x)))
            print("\n")
            return hex(x)
        elif var_type == "oct":
            print(type(oct(x)))
            print("\n")
            return oct(x)
        else:
            return "Nothing found here!"





