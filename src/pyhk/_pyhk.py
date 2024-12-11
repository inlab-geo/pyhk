import ctypes
import numpy as np
import os
import glob

# Locate the shared library in the same directory as this file
# lib_path = os.path.join(os.path.dirname(__file__), "rf_lib*.so")


# if not os.path.exists(lib_path):
#    raise FileNotFoundError(f"Shared library not found at {lib_path}")

# Load the shared library
# lib = ctypes.CDLL(lib_path)

lib = ctypes.cdll.LoadLibrary(glob.glob(os.path.dirname(__file__) + "/rf_lib*.so")[0])

# Declare the C function signature
lib.partial_modified.argtypes = [
    ctypes.c_int,  # ps
    ctypes.c_int,  # nft
    ctypes.c_int,  # m
    ctypes.POINTER(ctypes.c_float),  # thik
    ctypes.POINTER(ctypes.c_float),  # beta
    ctypes.POINTER(ctypes.c_float),  # kapa
    ctypes.c_float,  # p
    ctypes.c_float,  # dt
    ctypes.c_float,  # gauss
    ctypes.c_float,  # shft
    ctypes.c_float,  # db
    ctypes.c_float,  # dh
    ctypes.POINTER(ctypes.c_float),  # result
]
lib.partial_modified.restype = None


def rfcalc(ps, thik, beta, kapa, p, duration, dt, gauss=5.0, shft=0.0, db=0.0, dh=0.0):
    # Convert Python inputs to C-compatible types
    c_ps = ctypes.c_int(ps)
    c_m = ctypes.c_int(len(thik))
    c_p = ctypes.c_float(p)
    c_gauss = ctypes.c_float(gauss)
    c_shft = ctypes.c_float(shft)
    c_db = ctypes.c_float(db)
    c_dh = ctypes.c_float(dh)

    # Use Python float values for arithmetic
    nft_valid = int(duration / dt)
    c_nft = 1
    while c_nft < nft_valid:
        c_nft *= 2
    c_nft = ctypes.c_int(c_nft)

    # Convert NumPy arrays to ctypes pointers
    thik = np.array(thik, dtype=np.float32)
    beta = np.array(beta, dtype=np.float32)
    kapa = np.array(kapa, dtype=np.float32)
    result = np.zeros(c_nft.value, dtype=np.float32)

    c_thik_ptr = thik.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    c_beta_ptr = beta.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    c_kapa_ptr = kapa.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    c_result_ptr = result.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    # Call the C function
    lib.partial_modified(
        c_ps,
        c_nft,
        c_m,
        c_thik_ptr,
        c_beta_ptr,
        c_kapa_ptr,
        c_p,
        ctypes.c_float(dt),
        c_gauss,
        c_shft,
        c_db,
        c_dh,
        c_result_ptr,
    )

    # Return the result as a NumPy array
    return result[:nft_valid]
