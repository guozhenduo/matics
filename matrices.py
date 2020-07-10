class Matrix:
    def __init__(self, arr):
        """
        Initializes a matrix object with its array representation and dimensions.
        Raises an error if the passed array is empty or not two dimensional.
    
        :param arr: The array representation of the matrix.
        """
        if not (arr and all(isinstance(k, list) for k in arr)):
            raise IndexError
        self.arr = arr
        self.length = len(arr)
        self.n = len(arr[0])



    def __add__(self, other):
        """
        Adds the matrices component-wise.
        Raises an error if the dimensions of the matrices don't match.
    
        :param other: The matrix on the right side of the operator.
        :return: Returns a matrix object of the sum.
        """
        if self.m != other.m or self.n != other.n:
            raise IndexError
        sum_matrix = [
        [self.arr[i][j] + other.arr[i][j] for j in range(self.n)]
        for i in range(self.m)
        ]
        return Matrix(sum_matrix)

    def __mul__(self, other):
        """
        Multiplies the matrices, where the ij-th entry of the product
        is the dot product of the i-th row of self and the j-th column of other.
        Raises an error if the dimensions of the matrices don't match.
    
        :param other: The matrix on the right side of the operator.
        :return: Returns a matrix object of the product.
        """
        if self.n != other.m:
            raise IndexError
        prod = [[0] * other.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(other.n):
                for k in range(self.n):
                    prod[i][j] += self.arr[i][k] * other.arr[k][j]
        return Matrix(prod)
    def __repr__(self):

        """
        >>> import matrices as m
        >>> l=m.Matrix([[1,2])
        >>> l
        Matrix([[1,2]])
        """

        return f"Matrix({self.arr})"

    def __str__(self):
        """
        >>> import matrices as m
        >>> l=m.Matrix([[1,2])
        >>> print(l)
        [[1 2]]
        """
        arr = str(self.arr)
        arr = arr.replace(",","")
        return arr
