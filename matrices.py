class Matrix:
  def __init__(self, arr):
    if not (arr and all(isinstance(k, list) for k in arr)):
      raise IndexError
    self.arr = arr
    self.m = len(arr)
    self.n = len(arr[0])

  def __add__(self, other):
    if self.m != other.m or self.n != other.n:
      raise IndexError
    sum_matrix = [
      [self.arr[i][j] + other.arr[i][j] for j in range(self.n)]
      for i in range(self.m)
    ]
    return Matrix(sum_matrix)

  def __mul__(self, other):
    if self.n != other.m:
      raise IndexError
    prod = [[0] * other.n for _ in range(self.m)]
    for i in range(self.m):
      for j in range(other.n):
        for k in range(self.n):
          prod[i][j] += self.arr[i][k] * other.arr[k][j]
    return Matrix(prod)
