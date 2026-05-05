import random

def print_matrix(matrix, title):
    print(f"\n[{title}]")
    for row in matrix:
        for val in row:
            print(f"{val:>6}", end=" ")
        print()

def generate_matrix(n):
    limit = n * n * 10
    return [[random.randint(1, limit - 1) for _ in range(n)] for _ in range(n)]

def main():
    while True:
        try:
            n = int(input("N을 입력하세요 (2~5 사이 정수): "))
            if 2 <= n <= 5: break
            else: print("2에서 5 사이의 숫자를 입력하세요.")
        except ValueError:
            print("숫자만 입력 가능합니다.")

    A, B, C = generate_matrix(n), generate_matrix(n), generate_matrix(n)
    print_matrix(A, "Matrix A"), print_matrix(B, "Matrix B"), print_matrix(C, "Matrix C")

    mul_res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mul_res[i][j] += A[i][k] * B[k][j]
                
    final_res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            final_res[i][j] = mul_res[i][j] + C[i][j]
            
    print_matrix(final_res, "Result: A * B + C")

if __name__ == "__main__":
    main()
