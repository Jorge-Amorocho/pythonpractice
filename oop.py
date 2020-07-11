# -*- coding:utf-8 -*-


"""
OOP: Object-Oriented Programming/Paradigm

3 main characteristics:
  * Encapsulation: Scope of data is limited to the Object
  * Inheritance: Object fields can be implicitly used in extended classes
  * Polymorphism: Same name can have different signatures
"""

# #############################################################################
# # GLOBALS
# #############################################################################


# #############################################################################
# # CLOSURE
# #############################################################################
def increment(n):
    return lambda x: x + n

def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return lambda: inc()


# #############################################################################
# # CLASS VS INSTANCE
# #############################################################################
class Counter:
    """
    A class defines the attributes and methods (fields) of the object, and the
    instance is the actual implementation of the class.
    * Attributes are data (like a painting)
    * Methods are functions, need to be executed (like music)

    Whenever you want to put together functionality and state, a class is a
    good design.
    """

    # class attribute: identical for all instances of this class.
    # if 1 instance changes it, all change
    MODEL = "XYZ.123.BETA"

    def __init__(self, company):
        """
        This function is called when the object is created
        """
        print("created", self.__class__.__name__)
        self._count = 0  # instance attributes are declared this way
        self.company = company

    def reset(self):  # methods are declared this way
        """
        """
        self._count = 0
        return self._count

    def increment(self):
        """
        """
        # self._count = self._count + 1
        self._count += 1
        return self._count

    # "decorator"
    # static methods do NOT have a state. It is used to gather different
    # functions under same class (also more advanced uses like traits)
    @staticmethod  # no self required, this is like a "free function"
    def sum(a, b):
        """
        """
        return a + b  # no reference to self or the class


    # We require only what we need. I we don't alter the INSTANCE, we
    # don't need "self". A classmethod passes the reference to the
    # class, NOT  to the instance, and can be used to modify class
    # fields.
    @classmethod
    def change_model(cls, new_model):
        """
        """
        cls.MODEL = new_model

breakpoint()

ryanair = Counter("Ryanair")
iberia = Counter("Iberia")

Counter.sum(3, 4)




# EXAMPLE FOR SELF METHODS
for _ in range(50):
    ryanair.increment()

print("Disculpe cual es mi asiento??")
# ...

for _ in range(27):
    ryanair.increment()

print("Resultado:", ryanair._count)


# EXAMPLE FOR CLASS METHODS:
# we change the model in 1 instance, and we observe that the model has
# changed for ALL instances of the class
print(">>>", iberia.MODEL)
ryanair.change_model("XYZ.125")
print(">>>", iberia.MODEL)

breakpoint()

# #############################################################################
# # NP ARRAYS
# #############################################################################
