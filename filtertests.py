import lidarfilters as filters
import numpy as np
import time

#time delay for Temporal Filter Tests
default_delay = 2

"""Functions to help us test the filter objects"""

def get_a_really_random_number():
    x = np.random.randint(100)
    y = np.random.uniform(-x,x)

    if y == 0:
        x = np.random.randint(100)
        y = np.random.uniform(-x, x)

    z = 0.25 * y * np.random.uniform(-x,x)
    return z


def make_long_scan():
    long_scan = []
    for i in range(2000):
        long_scan.append(get_a_really_random_number())

    return long_scan


def make_random_length_scan():
    random_length = int(abs(get_a_really_random_number()))
    random_length_scan = []

    for i in range(random_length):
        random_length_scan.append(get_a_really_random_number())

    return random_length_scan


def make_empty_scan():
    empty_scan = []

    return empty_scan


"""Range Filter Tests"""

range_filter1 = filters.RangeFilter()
range_filter2 = filters.RangeFilter(1.77)
range_filter3 = filters.RangeFilter(2,4)
range_filter4 = filters.RangeFilter(3,-2)

range_filter1_dict = {
  1: range_filter1.update(make_long_scan()),
  2: range_filter1.update(make_random_length_scan()),
  3: range_filter1.update(make_empty_scan())
  }
# For range_filter1 the update should return a list of numbers
# where 0.03 <= each number in list <= 50 .
# Except on make_empty_scan()
# print(range_filter1_dict[1]) # 1 can be replaced with 2 or 3


range_filter2_dict = {
  1: range_filter2.update(make_long_scan()),
  2: range_filter2.update(make_random_length_scan()),
  3: range_filter2.update(make_empty_scan())
  }
# For range_filter2 the update should return a list of numbers
# where 1.77 <= each number in list <= 50 .
# Except on make_empty_scan() .
# print(range_filter2_dict[1]) # 1 can be replaced with 2 or 3


range_filter3_dict = {
  1: range_filter3.update(make_long_scan()),
  2: range_filter3.update(make_random_length_scan()),
  3: range_filter3.update(make_empty_scan())
  }
# For range_filter3 the update should return a list of numbers
# where 2 <= each number in list <= 4 .
# Except on make_empty_scan() .
# print(range_filter3_dict[1]) # 1 can be replaced with 2 or 3


range_filter4_dict = {
  1: range_filter4.update(make_long_scan()),
  2: range_filter4.update(make_random_length_scan()),
  3: range_filter4.update(make_empty_scan())
  }
# For range_filter4 the update should return a list of numbers
# where -2 <= each number in list <= 3 .
# Except on make_empty_scan() .
# print(range_filter4_dict[1])  # 1 can be replaced with 2 or 3


"""Temporal Filter Tests"""

D = np.random.randint(15) + 0.1234  # The TemporalFilter object will work even if it gets a float as an arg
print(" D is {}".format(D))
temporal_filter = filters.TemporalFilter(D)

# Check to see if a median value within _current_y_list is sensible
for i in range(30):
    scan = make_long_scan()
    print("Number at index 999 of current scan is {} ".format(scan[999]))
    time.sleep(default_delay)
    temporal_filter.update(scan)
    print("Current median at index 999 of _current_y_list "
          "is {} ".format(temporal_filter._current_y_list[999]))
    time.sleep(default_delay)







