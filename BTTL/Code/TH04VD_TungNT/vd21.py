import random

def create_random_vector(size, low, high):
    """
    Tạo vector ngẫu nhiên với các phần tử trong khoảng [low, high)
    """
    return [random.randint(low, high - 1) for _ in range(size)]

def create_random_matrix(rows, cols, low, high):
    """
    Tạo ma trận ngẫu nhiên với các phần tử trong khoảng [low, high)
    """
    return [[random.randint(low, high - 1) for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    """
    Hiển thị ma trận
    """
    for row in matrix:
        print(" ".join(map(str, row)))

# Test
if __name__ == "__main__":
    # Tạo vector
    vector = create_random_vector(5, 10, 20)
    print("Vector:", vector)

    # Tạo ma trận
    matrix = create_random_matrix(3, 4, 10, 20)
    print("Matrix:")
    print_matrix(matrix)
