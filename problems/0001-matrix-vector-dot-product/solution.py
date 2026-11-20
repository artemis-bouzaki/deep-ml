def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:

    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    result = []
    if len(a[0]) == len(b):
        for row in a:
            dot_product= 0
            for i in range(len(row)):
                dot_product += row[i]*b[i]
            result.append(dot_product)
        return result
    else: 
        return -1
