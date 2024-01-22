#!/usr/bin/python3
"""
100-matrix_mul.py
"""

def validate_matrices(m_a, m_b):
    """
    Validates two input matrices m_a and m_b
    
    Args: 
        m_a: first matrix input
        m_b: second matrix input

    Raises:
        TypeError:
            If m_a or m_b is not a list
            If m_a or m_b is not a list of lists
            If m_a or m_b is empty
            If m_a or m_b contains not float or integer values
            If rows in m_a or m_b are not equal
    Returns: None
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
       raise TypeError("m_b must be a list")
    for item in m_a:
        if not isinstance(item, list):
            raise TypeError("m_a must be a list of lists")
    for item in m_b:
        if not isinstance(item, list):
            raise TypeError("m_b is not a list of lists")
    if not m_a or not m_a[0]:
        raise TypeError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise TypeError("m_b can't be empty")
    for row in m_a:
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        
    a_row_size = len(m_a[0])
    for item in m_a:
        if len(item) != a_row_size:
            raise TypeError("each row of m_a must be of the same size")
    b_row_size = len(m_b)
    for item in m_b:
        if len(item) != b_row_size:
            raise TypeError("each row of m_b must be of the same size")
  

def matrix_mul(m_a, m_b):
    validate_matrices(m_a, m_b)
    try:
        matrix_mul_result = []
        result_row = []
        for row in range(len(m_a)):
            product = 0
            for col in range(len(m_a[row])):
                product += m_a[row][col] * m_b[col][row]
            result_row.append(product)
           # print("result row: ", result_row)
            if col == len(m_a[row]) - 1:
                matrix_mul_result.append(result_row)
        return matrix_mul_result
    except Exception as e:
        raise ValueError("m_a and m_b can't be multiplied")

