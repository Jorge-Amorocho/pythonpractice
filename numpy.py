# -*- coding:utf-8 -*-


"""
Module docstring

square brackets: alt 5 []
curly brackets: alt 8 {}
backslash: alt shift 7 \
tilde: alt n ~
"""


import numpy as np


# #############################################################################
# # HELPERS
# #############################################################################
def print_separation(lines=10):
    """
    """
    print("\n"*lines)



# #############################################################################
# # NP ARRAYS
# #############################################################################

# the most important properties of an array are dtype and shape
arr = np.array([1, 2, 3])
print(arr, arr.dtype, arr.shape)  # lists have shape (L,)
# all elements in an array have same dtype

# matrices have shape (h, w)
i5 = np.eye(5)
print(i5, i5.dtype, i5.shape)

# different dtypes: np.uint8, np.int32, np.int64, np.float32, np.float64...
# https://numpy.org/devdocs/user/basics.types.html
z8 = np.zeros(3, dtype=np.int32)
for _ in range(260):
    print("Hola ...")
    z8[0] += 1
    print("   ", z8)


print_separation()
