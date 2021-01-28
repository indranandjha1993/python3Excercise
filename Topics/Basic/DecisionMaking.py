# Decision-making is the anticipation of conditions occurring during the execution of a program and specified actions taken according to the conditions.
#
# Decision structures evaluate multiple expressions, which produce TRUE or FALSE as the outcome.
# You need to determine which action to take and which statements to execute if the outcome is TRUE or FALSE otherwise.

class DecisionMaking:
    @staticmethod
    def is_adult_age(age: int):
        if age >= 18:
            return True
        else:
            return False
