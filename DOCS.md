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
| `__init__` | Create a New Fraction object. | `param:int: `num1 and num2 can't be zero.Num1 can be defined like this: '1/3' .  |
| `__add__` | Add Fraction Object | `param:other:`  Other is a Fraction Object too. `:return:` return a New Fraction Object |
| `__mul__` | multiply Fraction Object | `param:other` Other is a Fraction Object too. `:return:` return a new Fraction Object |

## Calculate Class
| Method | Description | Parameters |
|----------|----------|----------|
| `__init__` | Initializes a Calculate class | `param:number `The parameter like:`"5"` or `5` or `5.0`. |
| `__int__` | Return int(self.number) | `:return:` Returns int(self.number) |
| `__repr__` | Format the string `Calculate({self.number})` | </br>`:return:` Returns the object's `repr()` representation |
| `__str__` | Format the `{self.number}` | `:return:`Return str(self.number) |
| `__eq__` | Determine whether the two `Calculate object` are equal or not | `param:other`other is Calculate object too.`:return:` return True or return False |
