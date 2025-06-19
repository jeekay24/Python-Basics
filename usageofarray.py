import sys
from array import array

my_list = [1] * 1000000
my_array = array('i', [1] * 1000000)

print("List size:", sys.getsizeof(my_list))       # Memory for references
print("Array size:", sys.getsizeof(my_array))     # Much smaller
