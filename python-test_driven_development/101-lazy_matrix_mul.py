#!/usr/bin/python3
"""
This module contains function to multiply matrices using numpy
"""
import numpy as np
from numpy._core.fromnumeric import shape


def lazy_matrix_mul(m_a, m_b):
    """Return m_a @ m_b"""
    if type(m_a) is not list or type(m_b) is not list:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    for r1, r2 in zip(m_a, m_b):
        for e1, e2 in zip(r1, r2):
            if type(e1) is not int and type(e1) is not float:
                raise ValueError("invalid data type for einsum")
            if type(e2) is not int and type(e2) is not float:
                raise ValueError("invalid data type for einsum")
    try:
        m_a = np.array(m_a)
        m_b = np.array(m_b)
    except Exception as e:
        raise Exception("setting an array element with a sequence.")
    if m_a.ndim == 2 and m_b.ndim == 2 and m_a.shape[1] == m_b.shape[0]:
        a_col_size = len(m_a[0])
        b_col_size = len(m_b[0])
        return m_a @ m_b
    else:
        raise ValueError(
            "shapes ({},{}) and ({},{}) not aligned: {} (dim 1) != {} (dim 0)"
            .format(
                m_a.shape[0],
                m_a.shape[1],
                m_b.shape[0],
                m_b.shape[1],
                m_a.shape[1],
                m_b.shape[0],
            )
        )


if __name__ == "__main__":
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
