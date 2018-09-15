# filters-for-LIDAR-scans

LIDAR scan filters and modules demonstrating usage.

Downloadable from:
https://github.com/darcese/filters-for-LIDAR-scans.git

The modules use numpy so make sure it's installed.
https://www.numpy.org/

* lidarfilters.py contains the classes used for filtering LIDAR scans.

* rangefilterexamples.py and temporalfilterexamples.py demonstrate how
  to incorporate the lidarfilters.py module.

* filtertests.py is just a program used to test objects created from the
  lidarfilters module.

# In order to use lidarfilters.py with Python 2:

change line 31      <br/><br/>
from: def __init__(self, range_min: float = .03, range_max: float = 50):     <br/><br/>
  to: def __init__(self, range_min = .03, range_max = 50):      <br/><br/>

change line 155     <br/><br/>
from:  def __init__(self, D: int): <br/><br/>
  to:  def __init__(self, D):      <br/><br/>
                                   <br/><br/>         
#
If you run into any issues         <br/><br/>
feel free to email me at           <br/><br/>
d.arcese@umiami.edu     

