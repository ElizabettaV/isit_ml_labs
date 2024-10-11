import numpy as np
import numpy.typing as npt

def add_zeros(x: npt.NDArray[np.int_]) -> npt.NDArray[np.int_]:
   x = np.asarray(x)
    return np.insert(x, slice(1, len(x)), 0) 