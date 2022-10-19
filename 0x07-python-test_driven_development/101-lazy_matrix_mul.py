#!/usr/bin/python3
"""
module composed by a function that multiplies 2 matrices
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """function that multiplies 2 martices

    args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of multiplication
    """

    return (np.matmul(m_a, m_b))
