import numpy as np
import numpy.typing as npt


def max_element(array: npt.NDArray[np.int_]) -> int | None:
    """
    Return max element before zero for input array.
    If appropriate elements are absent, then return None
    :param array: array,
    :return: max element value or None
    """
    # Convert the input to a NumPy array
    arr = np.asarray(array)
    # Find the index of the first occurrence of zero
    zero_index = np.where(arr == 0)[0]
    # If there are no zeros in the array, return None
    if zero_index.size == 0:
        return None
    # Get the elements before the first zero
    elements_before_zero = arr[:zero_index[0]]
    # If there are no elements before the first zero, return None
    if elements_before_zero.size == 0:
        return None
    # Return the maximum element before the first zero
    return np.max(elements_before_zero)

# Example usage
array = np.array([3, 5, 2, 0, 7, 8])
result = max_element(array)
print(result)  # Output: 5