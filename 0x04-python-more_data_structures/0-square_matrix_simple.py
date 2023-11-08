#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    result = []
    res = all(isinstance(ele, list) for ele in matrix)
    if res:
        for i in range(len(matrix)):
            result.append(list(map(lambda x: x**2, matrix[i])))
    else:
        result = list(map(lambda x: x**2, matrix))
    return result
