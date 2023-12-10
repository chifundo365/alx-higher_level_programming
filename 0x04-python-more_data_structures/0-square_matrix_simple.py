def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        matric_copy = matrix.copy()
        for row in matrix_copy:
            row_index = matrix_copy.index(row)
            for digit in row:
                col_index = row.index(digit)
                matrix_copy[row_index][col_index] = digit * digit
        return matrix_copy
