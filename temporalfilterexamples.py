import lidarfilters as filters
import time
import numpy as np

# default time delay for examples
default_delay = 2


"""Temporal Filter Examples"""

# When creating a new TemporalFilter object, you must pass it a value for D.
# D represents the number of previous scans (lists), besides the current one, that  your filter
# will use to calculate a median value for a measurement found at a constant index within each scan.
# A median value, yi, is given by yi = median(ScanT[i],ScanT-1[i],...,ScanT-D[i]).

# We will do this for all measurements in our scans and get a list y where
# y = [y(i=0), ... ,y(i=N-1)] and
# N is the number of measurements included in a single scan.

# In this example we will set D to equal 3. Note D should be an int.
# If D is a float it will be automatically rounded to the nearest int.
D = 3
temporal_filter_object = filters.TemporalFilter(D)


# We can then update the TemporalFilter object with a list of numbers ie a scan.
# In this case our scan will be new_scan0
new_scan0 = [0,1,2,1,3]
# Calling .update on our TemporalFilter object returns our list of medians y
medians_list = temporal_filter_object.update(new_scan0)
# Then we can print the list of medians.
print(medians_list)

# And we can do this for as many scans as we would like so long as N remains constant.

new_scan1 = [1,5,7,1,3]
new_scan2 = [2,3,4,1,0]
new_scan3 = [3,3,3,1,3]
new_scan4 = np.array([10,2,4,0,0])  # You can update with an np.ndarray as well.

scans = [
        new_scan1, new_scan2,
        new_scan3, new_scan4
        ]

for i in range(4):
    time.sleep(default_delay)
    print(temporal_filter_object.update(scans[i]))


# Calling update on your TemporalFilter object also updates the object's _recent_scans variable
# as well as the object's _CurrentYList variable.
# Below we will demonstrate how to retrieve both variables:

# You can get the most recent and previous D scans (D+1 in total scans) by calling

recent_scans = temporal_filter_object._recent_scans
# NOTE: The leftmost list returned is the the most recent scan and
# just to the right of it is the next most recent.
# print(recent_scans)

# You can also find the current_y_list without updating the filter.
# Use ._CurrentYList on your Temporal Filter Object
current_y_list = temporal_filter_object._current_y_list
# print(current_y_list)


# A RangeFilter can be combined with a TemporalFilter as well
# For example:
range_filter = filters.RangeFilter(1.5, 6)
print("Now an example of how RangeFilter and TemporalFilter objects can be used in tandem:")
for i in range(4):
    time.sleep(default_delay)
    filtered_scan = range_filter.update(scans[i])
    print(temporal_filter_object.update(filtered_scan))


"""Some possible Mistakes"""

# Passing an argument that isn't a number during the creation of a temporal filter object.
# For example:
# new_temporal_filter_object = filters.TemporalFilter([9])
# Which causes:
# Traceback (most recent call last):
#   File "temporalfilterexamples.py", line 68, in <module>
#     new_temporal_filter_object = F.TemporalFilter([9])
#   File "/Users/*******************/lidarfilters.py", line 166, in __init__
#     raise TypeError("TemporalFilter takes a single positive int as an argument")
# TypeError: TemporalFilter takes a single positive int as an argument


# Updating with multiple arguments rather than a single list.
# For example:
# temporal_filter_object.update(9,3,4,5,5)
# Which causes:
# Traceback (most recent call last):
#   File "temporalfilterexamples.py", line 82, in <module>
#     temporal_filter_object.update(9,3,4,5,5)
# TypeError: update() takes 2 positional arguments but 6 were given


# Updating with a scan of different N (length) compared to previous scans.
# For example:
# temporal_filter_object.update([1,2,3,4,5,6])
# Which causes:
# Traceback (most recent call last):
#   File "temporalfilterexamples.py", line 92, in <module>
#     temporal_filter_object.update([1,2,3,4,5,6])
#   File "/Users/*******************/lidarfilters.py", line 220, in update
#     raise TypeError('The length of the current scan must be the same as '
#   TypeError: The length of the current scan must be the same as the length of the previous scan.
# Make a new TemporalFilter object if you wish to start filtering scans of a new length.