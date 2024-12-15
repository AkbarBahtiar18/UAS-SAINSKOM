import numpy as np

def main():
    matrix = np.array([
        [2, 1, 2],
        [3, 4, 1],
        [5, 2, 9]
    ])
    invers = np.linalg.inv(matrix)
    print(f"Matriks Asli:\n{matrix}")
    print(f"\nMatriks Invers:\n {invers}")
    
