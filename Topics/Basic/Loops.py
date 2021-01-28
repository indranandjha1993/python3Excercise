# In general, statements are executed sequentially − The first statement in a function is executed first, followed by the second, and so on.
# There may be a situation when you need to execute a block of code several number of times.
#
# Programming languages provide various control structures that allow more complicated execution paths.
#
# A loop statement allows us to execute a statement or group of statements multiple times.

class Loop:
    @staticmethod
    def while_loop():
        count = 0
        while count < 10:
            print(count)
            count += 1

    @staticmethod
    def for_loop():
        list1 = list(range(1, 11))
        for x in list1:
            print(x)

    @staticmethod
    def nested_loop():
        for i in range(10):
            for j in range(10):
                print(i*j, " ")
        print("\n")
