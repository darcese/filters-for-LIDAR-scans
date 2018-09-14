# filters-for-LIDAR-scans
LIDAR scan filters and modules demonstrating usage.

lidarfilters.py contains the classes used for filtering lidar scans.

rangefilterexamples.py and temporalfilterexamples.py demonstrate how to incorporate the lidarfilters.py module.

filtertests.py is just a program used to test objects created from the lidarfilters module.

The modules use numpy so make sure you have it installed and can access it.

In order to use the lidarfilters module with Python2

change line 31 from  def __init__(self, range_min: float = .03, range_max: float = 50):
                 to  def __init__(self, range_min = .03, range_max = 50):

and

change line 155 from  def __init__(self, D: int):
                  to  def __init__(self, D):

If you run into any problems
Email me at
d.arcese@umiami.edu 
