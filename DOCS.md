# Documentation
Here's the documentation for the rest of the repository.

## Matrices Class
| Method | Description | Parameters |
|--------|-------------|------------|
| `__init__` | Initializes a matrix object with its array representation and dimensions. Raises an error if the passed array is empty or not two dimensional. | `:param arr:` The array representation of the matrix. |
| `__add__`  | Adds the matrices component-wise. Raises an error if the dimensions of the matrices don't match. | `:param other:` The matrix on the right side of the operator. </br> `:return:` Returns a matrix object of the sum. |
| `__mul__`  | Multiplies the matrices, where the ij-th entry of the product is the dot product of the i-th row of `self` and the j-th column of `other`. Raises an error if the dimensions of the matrices don't match. | `:param other:` The matrix on the right side of the operator. </br> `:return:` Returns a matrix object of the product. |
| `__repr__` | Formats the string `Matrix({self.arr})` to contain the object's array representation. | `:return:` Returns the object's `repr()` representation. |
| `__str__`  | Removes the comma's in the string representation of the object's array representation. | `:return:` Returns the object's `str()` representation. |

## Fraction Class
| Method | Description |  Parameters |
|--------|-------------|------------|
| `__init__` | Create a New Fraction object. | `param : int: `num1 and num2 can't be zero.Num1 can be defined like this: '1/3' . `:return :` return a Fraction Object. |