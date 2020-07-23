class Matrix:
    def __init__(self, arr):

        if not arr:

            raise IndexError

        if not all(isinstance(k, list) for k in arr):

            if all(isinstance(k, int) or isinstance(k, float) for k in arr):

                arr = [arr]

            else:

                raise IndexError

        self.arr = arr
        self.length = len(arr)
        self.adim = len(arr[0])


    def __add__(self, other):

        if self.length != other.length or self.adim != other.adim:

            raise IndexError

        sum_matrix = [
        [self.arr[i][j] + other.arr[i][j] for j in range(self.adim)]
        for i in range(self.length)
        ]

        return Matrix(sum_matrix)


    def __mul__(self, other):

        if isinstance(other, int) or isinstance(other, float):

            return Matrix([[other * item for item in row] for row in self.arr])

        if self.adim != other.length:

            raise IndexError

        prod = [[0] * other.adim for _ in range(self.length)]
        for i in range(self.length):

            for j in range(other.adim):

                for k in range(self.adim):

                    prod[i][j] += self.arr[i][k] * other.arr[k][j]

        return Matrix(prod)


    def __repr__(self):

        return f"Matrix({self.arr})"


    def __str__(self):

        return str(self.arr).replace(',', '')

    def __neg__(self):
        neg_matrix = [
            [-self.arr[i][j] for j in range(self.adim)]
            for i in range(self.length)
        ]

        return Matrix(neg_matrix)

    def __sub__(self,other):

        return self + -other
