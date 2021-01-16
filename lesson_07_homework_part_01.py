class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        cont = []
        for el in self.matrix:
            el = ' '.join(map(str, el))  # корректно ли использовать str внутри __str__?
            cont.append(el)
        return '\n'.join(cont)
        # мне кажется, что "развёрнутая" запись в данном случае читабельнее сокращённой
        # return '\n'.join(' '.join(map(str, el)) for el in self.matrix)

    def __add__(self, other):
        try:
            """Сложение матриц одного размера"""
            result = []
            m1 = self.matrix
            m2 = other.matrix
            for i in range(len(m1)):
                row = []
                for j in range(len(m1[i])):
                    row.append(m1[i][j] + m2[i][j])
                # row = list(m1[i][j] + m2[i][j] for j in range(len(m1[0])))
                result.append(row)
            return Matrix(result)
        except IndexError:
            """Сложение матриц разного размера"""
            # Не уверен, что правильно реализовал принцип, сделал, скорее, из "спортивного" интереса.
            result = []
            m1 = self.matrix if len(self.matrix) > len(other.matrix) else other.matrix
            m2 = other.matrix if len(self.matrix) > len(other.matrix) else self.matrix
            m1 = list(map(list, m1))
            m2 = list(map(list, m2))
            for i in range(len(m1)):
                if i < len(m2):
                    row = []
                    el1 = m1[i] if len(m1[0]) > len(m2[0]) else m2[i]
                    el2 = m2[i] if len(m1[0]) > len(m2[0]) else m1[i]
                    for j in range(len(el1)):
                        if j < len(el2):
                            row.append(el1[j] + el2[j])
                        else:
                            row.append(el1[j])
                    result.append(row)
                else:
                    result.append(m1[i])
                    if len(m1[0]) < len(m2[0]):
                        for n in range(len(m2[0]) - len(m1[0])):
                            result[i].append(0)
            return f'Предупреждение: Вы складываете матрицы разного размера!\n{Matrix(result)}'


matrix_01 = Matrix([[11, 12], [21, 22], [31, 32]])
matrix_02 = Matrix([[1100, 1200], [2100, 2200], [3100, 3200]])
matrix_03 = Matrix([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])
matrix_04 = Matrix([[1100, 1200], [2100, 2200], [3100, 3200], [4100, 4200]])
print(matrix_01)
print(matrix_01 + matrix_02)
print(matrix_03 + matrix_04)
