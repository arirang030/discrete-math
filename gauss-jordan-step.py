# 행렬 출력
def printMatrix(matrix):
  for row in matrix:
    print(" ".join(f"{elem:8.2f}" for elem in row))

# 가우스-조던 소거법을 이용한 역행렬 계산
def getMatrixInverseWithGaussJordan(m):
  n = len(m)

  # 확대 행렬 구하기
  aug = m
  for i in range(n):
    aug[i] += [0] * i + [1] + [0] * (n - 1 - i)

  cnt = 1

  # 절댓값이 가장 큰 값을 피벗으로 설정
  for i in range(n):
    # 테스트용 출력문
    print(f"#{cnt}", "-" * 64)
    cnt += 1
    printMatrix(aug)

    pivot_row = i
    for k in range(i + 1, n):
      if (abs(aug[k][i]) > abs(aug[pivot_row][i])):
        pivot_row = k
    aug[i], aug[pivot_row] = aug[pivot_row], aug[i]

    # 테스트용 출력문
    print(f"#{cnt}", "-" * 64)
    cnt += 1
    printMatrix(aug)

    pivot = aug[i][i]

    # 현재 행을 단위로 만들기
    for j in range(2 * n):
      aug[i][j] /= pivot

    # 테스트용 출력문
    print(f"#{cnt}", "-" * 64)
    cnt += 1
    printMatrix(aug)

    # 다른 행의 해당 열을 0으로 만들기
    for j in range(n):
      if i != j:
        factor = aug[j][i]
        for k in range(2 * n):
          aug[j][k] -= factor * aug[i][k]

    # 테스트용 출력문
    print(f"#{cnt}", "-" * 64)
    cnt += 1
    printMatrix(aug)

  return [r[n:] for r in aug]

m = [[-2.0, 2.0, -3.0], [1.0, 0.0, 1.0], [-4.0, 3.0, -5.0]]
inverse = getMatrixInverseWithGaussJordan(m)
print("#최종", "-" * 64)
printMatrix(inverse)