import numpy as np
import numpy.typing as npt


def max_element(array: npt.NDArray[np.int_]) -> int | None:
    """
    Return max element before zero for input array.
    If appropriate elements are absent, then return None
    :param array: array,
    :return: max element value or None
    """
    arr = np.asarray(array)
    zero_index = np.where(arr == 0)[0] + 1 #индекс первого нуля
    elements_before_zero = zero_index[zero_index < len(array)] #элементы перед первым нулём
    if elements_before_zero.size == 0:
        return None
    return np.max(arr[elements_before_zero])

# Example usage
array = np.array([3, 5, 2, 0, 7, 8])
result = max_element(array)
print(result)  # Output: 5