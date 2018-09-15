"""Range Filter Examples
"""

import lidarfilters as filters
import numpy as np

# Create a new RangeFilter object with default range_min set to .03 and default range max set to 50 .
range_filter_object = filters.RangeFilter()

# We can use the RangerFilter object's update method to filter a list of numbers.
# The RangeFilter object's update method must be passed a list or np.ndarray of numbers.
# In this example the list passed  to our RangeFilter object will be the list named new_scan.
new_scan = [
            0.02, 56, 24, 1.9, -1, 2, 0, 6, 34, 500, .00000002, 15, 19.99999, 70,
            1000, 51.0000, 8, .0300, .0301, .029999, -.108, 7.5, 27, 51.0001, -2.45
            ]

# The RangeFilter object's update method returns a filtered list
# where all values less than range_min are replaced with range_min
# and all values greater than range_max are replace with range_max .
# Let's store the returned filtered list in a variable named range_filtered_list .
range_filtered_list = range_filter_object.update(new_scan)

# Then print it.
print(range_filtered_list)

# We can also filter an np.ndarray
# numpy_scan = np.array([26,1.9,-1,2,0,6,34,500,.00000002,5, 19.99999,
#                        70,10000,51.0000,8, .0300,.0301, .029999,-.1, 27
#                        ])
# print(range_filter_object.update(numpy_scan))

# We can also make a new RangeFilter object with a range_min and range_max specified by the user.
# In this example our RangeFilter object will have a range_min of 2 and a range_max of 25.
# range_filter_object_with_range_specified_by_user = filters.RangeFilter(2, 25)
# We can then use this RangeFilter object's update method to return a filtered a list,
# just like in the previous example.
# range_filtered_list_with_range_defined_by_user = range_filter_object_with_range_specified_by_user.update(new_scan)
# print(range_filtered_list_with_range_defined_by_user)

# You can also find the range_min and range_max of a RangeFilter object by
# calling _min or _max on the object.
# For example:
# range_filter_object._min
# Or to find and print the _max
# print(range_filter_object._max)


"""Some possible mistakes"""

# One might accidentally pass in a list when creating a new RangeFilter object
# For example:
# range_filter_object_with_incorrect_argument_type = filters.RangeFilter([0.32,50])
# Which causes:
# Traceback (most recent call last):
#   File "rangefilterexamples.py", line 49, in <module>
#     range_filter_object_with_incorrect_argument_type = filters.RangeFilter([0.32,50])
#   File "/Users/*******************/lidarfilters.py", line 45, in __init__
#     raise TypeError("range_min must be a float or int")
# TypeError: range_min must be a float or int


# When creating a new range filter object a user might incorrectly pass in too many arguments.
# For example:
# range_filter_object_with_too_many_arguments = filters.RangeFilter(2,25,4)
# which causes:
# This results in the following error:
# Traceback (most recent call last):
# Traceback (most recent call last):
#   File "rangefilterexamples.py", line 64, in <module>
#     range_filter_object_with_too_many_arguments = filters.RangeFilter(2,25,4)
# TypeError: __init__() takes from 1 to 3 positional arguments but 4 were given


# Or after correctly making a RangeFilter object they pass a non list argument to the update method.
# For example:
# range_filter_object.update(3)
# Which causes:
# Traceback (most recent call last):
#   File "rangefilterexamples.py", line 96, in <module>
#     range_filter_object.update(3)
#   File "/Users/*******************/lidarfilters.py", line 96, in update
#     raise TypeError("TemporalFilter's update method takes a list of numbers as its argument.")
# TypeError: TemporalFilter's update method takes a list of numbers as its argument.


# Or they pass in several arguments instead of a single list.
# For example:
# range_filter_object.update(3,4,5,50.01)
# Which causes:
# Traceback (most recent call last):
#   File "rangefilterexamples.py", line 88, in <module>
#     range_filter_object.update(3,4,5,50.01)
# TypeError: update() takes 2 positional arguments but 5 were given


