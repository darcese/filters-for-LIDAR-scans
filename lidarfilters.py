"""
Filters for LIDAR scans
"""
import numpy as np


class RangeFilter:
    """A class used to filter a scan (one-dimensional array of numbers)
    and return the filtered version of the scan with all numbers
    now residing within a specified range.

    Parameters
    ----------
    range_min : float or int, optional
        Numbers in a scan less than range_min will be set to range_min (default .03).
    range_max : float or int, optional
        Numbers in a scan greater than range_max will be set to range_max (default 50).

    Attributes
    ----------
    _min : float or int
        Equal to range_min .
    _max : float or int
        Equal to range_max .

    Note
    ----------
    If range_min is greater than range_max the two will be swapped.
    """    
    # Here we set the default range_min and range_max values if they are not passed as arguments.
    def __init__(self, range_min: float = .03, range_max: float = 50):
        """Initializes a RangeFilter object.

        Parameters
        ----------
        range_min : float or int, optional
            Numbers in a scan less than range_min will be cropped to range_min (default .03).
        range_max : float or int, optional
            Numbers in a scan greater than range_max will be cropped to range_max (default 50).
        """
        # If a range_min was passed we make sure it's a number.
        if isinstance(range_min, float) is False:
            if isinstance(range_min, int) is False:
                raise TypeError("range_min must be a float or int")

        # If a value for range_max was passed we also make sure it's a number.
        if isinstance(range_max, float) is False:
            if isinstance(range_max, int) is False:
                raise TypeError("range_max must be a float or int")

        # Store range_max and range_min
        # in the object's _min and _max attributes.
        self._min = range_min
        self._max = range_max

        # Make sure _min is smaller than _max .
        # If it isn't then switch the values.
        if self._min > self._max:
            temp_min = self._min
            temp_max = self._max
            self._min = temp_max
            self._max = temp_min
            del temp_min
            del temp_max

        # Next make sure _min and _max are not equal to each other.
        # If they are print a warning.
        if self._min == self._max:
            print("WARNING range_min is equal to range_max")
            print("All numbers in list returned by update will be equal to range_min")
            import time
            time.sleep(4)


    def update(self, scan):
        """Updates a scan and returns a modified version
        in which all numbers now lie within a specified range.

        Parameters
        ----------
        scan : One-dimensional array of numbers either as a list or np.ndarray .
            The scan to be modified.

        Returns
        ----------
        filtered_scan : list
            The modified scan.
        """
        # Check to see if the scan passed to update is a numpy array .
        # If it is we will convert it to a list.
        if isinstance(scan, np.ndarray):
            scan = scan.tolist()

        # Check to see if the scan is a list.
        if isinstance(scan, list) is False:
            raise TypeError("TemporalFilter's update method takes a list of numbers as its argument.")

        # Check that scan is just a list of numbers. It should not be a list of lists.
        for i in range(len(scan)):
            if isinstance(scan[i], float) is False:
                if isinstance(scan[i], int) is False:
                    raise TypeError('The update method takes a scan as a parameter.'
                                    ' Scan should be a list of numbers.')

        # Create a filtered_scan variable to store
        # the filtered measurements.
        filtered_scan = []

        # Loop through all the measurements (ie numbers) in a scan and
        # if a number is bigger than _max make the number
        # equal to _max and if a number is smaller than
        # _min make the number equal to _min.
        for measurement in scan:
            if measurement < self._min:
                measurement = self._min
            if measurement > self._max:
                measurement = self._max

            # Append the measurement to our filtered scan.
            filtered_scan.append(measurement)

        # Return the filtered measurements.
        return filtered_scan


class TemporalFilter:
    """A class used to find a list of median values where each median value
    is the median of values for a specific index shared between the newest scan
    and D most recent scans. I.e  median[i] = median(scanT[i], scanT-1[i], ..., scanT-D[i])
    and list of median values = (median[0], median[1], ..., median[N-1])
    where N is the length of a scan (number of values in it).

    Each scan must be a one-dimensional array of numbers as a list or np.ndarray .

    Parameters
    ----------
    D : float or int,
        Number of scans besides the current one that will be included during median value calculation.

    Attributes
    ----------
    _current_y_list : list
        The most recent list of medians returned by the object's update method.
    _D : int
        Number of scans besides the current one that will be included during median value calculation.
    _recent_scans : list
        A list of the D+1 most recent scans passed to the object's update method.

    Note
    ----------
    If a negative value is passed to D then D will become 0
    and the _current_y_list will be equal to the most recent scan.
    If a float is passed to D then D will be rounded to the nearest int.
    """
    def __init__(self, D: int):
        """Initializes a TemporalFilter object.

        Parameters
        ----------
        D : float or int
            Number of scans besides the current one that will be included during median value calculation.
        """
        # Make sure D is a number
        if isinstance(D, float) is False:
            if isinstance(D, int) is False:
                raise TypeError("TemporalFilter takes a single positive int as an argument")

        # In case D is a float ie 3.0000
        if isinstance(D, float) is True:
            D = int(np.rint(D))

        # Check the value for D.
        if D < 0:
            D = 0
            print("TemporalFilter can't take a number less than 0 as an argument")
            print("Setting D to 0")
            import time
            time.sleep(3.5)

        # Create the instance's attributes.
        self._D = D
        self._recent_scans = []
        self._current_y_list = []


    def update(self, scan):
        """Returns a list of median values where each median value
        is the median of values for a specific index shared between the newest scan
        and D most recent scans.
        I.e  median[i] = median(scanT[i], scanT-1[i], ..., scanT-D[i]).
        List of median values = (median[0] , median[1], ... median[N-1]).
        N is the length of a scan (number of values in it).

        The update method also updates the object's _current_y_list and _recent_scans attributes.

        Parameters
        ----------
        scan : One-dimensional array of numbers either as a list or np.ndarray .

        Returns
        ----------
        _current_y_list : list
            The most recent list of medians.

        Note
        ----------
        The length of scan must be equal to the length of the previous scan.
        """
        # Check to see if the scan passed to update is a numpy array.
        # If it is we will convert it to a list.
        if isinstance(scan, np.ndarray):
            scan = scan.tolist()

        # Check to see if the scan is a list.
        if isinstance(scan, list) is False:
            raise TypeError("TemporalFilter's update method takes a list of numbers as its argument.")

        # If self._recent_scans isn't empty check to see if the length of the current scan
        # matches the length of the previous scan. If the lengths don't match raise the TypeError.
        if self._recent_scans:
            if len(scan) != len(self._recent_scans[0]):
                raise TypeError('The length of the current scan must be the same as '
                                'the length of the previous scan. \n Make a new '
                                'TemporalFilter object if you wish to start '
                                'filtering scans of a new length.')

        # Check that scan is just a list of numbers. It should not be a list of lists.
        for i in range(len(scan)):
            if isinstance(scan[i], float) is False:
                if isinstance(scan[i], int) is False:
                    raise TypeError('The update method takes a scan as a parameter.'
                                    ' Scan should be a list of numbers.')

        # If the scan passes our previous checks
        # then we can put it in the first position of the _recent_scans list.
        self._recent_scans.insert(0, scan)

        # Setting D to the object's _D variable
        # and resetting the _current_y_list_
        D = self._D
        self._current_y_list = []

        # This section deletes the oldest scan once the oldest scan
        # no longer becomes necessary for calculating the _current_y_list_
        if len(self._recent_scans) > D + 1:
            del self._recent_scans[len(self._recent_scans) - 1]

        # Storing the object's _recent_scans in the variable scans
        scans = self._recent_scans

        # The next section prevents an index out of range error
        # which would happen when the number of scans we have is
        # less than D + 1 . Remember this does not affect
        # the Filter object's _D attribute
        if len(scans) < D + 1:
            D = len(scans) - 1

        # For each number in the current scan we will create
        # a new list that will store the groups that we
        # will take the medians of.
        for n in range(len(scan)):
            scan_values_at_current_index = []

            # Go through each scan ie scans[T], scans[T+1] , ..., scans[D]
            # And pick the nth element in that scan and append it to scan_values_at_current_index
            for T in range(D + 1):
                scan_values_at_current_index.append(scans[T][n])

            # Then take the median of the scan_values_at_current_index
            # and append it to the object's _current_y_list .
            median_n = np.median(scan_values_at_current_index)
            self._current_y_list.append(median_n)

        # And return the object's _current_y_list .
        return self._current_y_list
