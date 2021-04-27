"""
Find sum of Odd number in a NxM random integer matrix with range 0 to 100 using numpy
"""
import numpy as np


def calculate_even_no(matrix, n, m):
    even_list = [j for i in matrix for j in i if j % 2 == 0]
    print(f"sum of even no is: {sum(even_list)}")


def calculate_odd_no(matrix, n, m):
    odd_list = [j for i in matrix for j in i if j % 2 != 0]
    print(f"sum of odd no is: {sum(odd_list)}")


row = int(input("Enter Number of Rows: "))
column = int(input("Enter Number of Column: "))
mat = np.random.randint(0, 100, (row, column))
print(f"Matrix is:\n{mat}")
menu = """
- 'e' for print sum of even no.
- 'o' for print sum of odd no.
- 'b' for print sum of both no respectively.
"""
b = input(menu)
if b == 'e':
    calculate_even_no(mat, row, column)
elif b == 'o':
    calculate_odd_no(mat, row, column)
elif b == 'b':
    calculate_even_no(mat, row, column)
    calculate_odd_no(mat, row, column)
else:
    print("Wrong input!!")


"""
for i in Matrix:
    for j in i:
        if j % 2 != 0:
            odd_list.append(j)
"""

