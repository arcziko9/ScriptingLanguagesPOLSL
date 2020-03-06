class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        length_matrix = len(self.matrix)
        add_result = [[0] * length_matrix for i in range(length_matrix)]
        if len(self.matrix) == len(other.matrix):
            for i in range(length_matrix):
                for j in range(length_matrix):
                    add_result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(add_result)

    def __sub__(self, other):
        length_matrix = len(self.matrix)
        sub_result = [[0] * length_matrix for i in range(length_matrix)]
        if len(self.matrix) == len(other.matrix):
            for i in range(length_matrix):
                for j in range(length_matrix):
                    sub_result[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(sub_result)

    def opposite2x2(self):
        if len(self.matrix) == 2 and len(self.matrix[0:2]) == 2:
            det_matrix = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
            if det_matrix == 0:
                print("Determinant equal 0")
            else:
                completion = [[self.matrix[1][1] / det_matrix, (self.matrix[0][1] * (-1)) / det_matrix],
                              [(self.matrix[1][0] * (-1)) / det_matrix, self.matrix[0][0] / det_matrix]]
        return Matrix(completion)

    def __str__(self):
        string_output = ""
        for item in self.matrix:
            string_output += str(item) + "\n"

        return string_output


matrix1 = [[2, 1], [4, 5]]
matrix2 = [[1, 3, 5], [7, 5, 1], [3, 9, 3]]

matrix_object1 = Matrix(matrix1)
matrix_object2 = Matrix(matrix2)

print(matrix_object1 + matrix_object2)
print(matrix_object1 - matrix_object2)
print(Matrix.opposite2x2(matrix_object1))
