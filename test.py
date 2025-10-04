def print_matrix(matrix):
  for row in matrix:
    print(" ".join(f"{elem:8.2f}" for elem in row))

m = [[-2.0, 2.0, -3.0], [1.0, 0.0, 1.0], [-4.0, 3.0, -5.0]]

n = len(m)

# 확대 행렬 구하기
aug = m
for i in range(n):
  aug[i] += [0] * i + [1] + [0] * (n - 1 - i)

# 절댓값이 가장 큰 값을 피벗으로 설정
for i in range(n):
  pivot_row = i
  for k in range(i + 1, n):
    if (abs(aug[k][i]) > abs(aug[pivot_row][i])):
      pivot_row = k
  aug[i], aug[pivot_row] = aug[pivot_row], aug[i]

  pivot = aug[i][i]

  # 현재 행을 단위로 만들기
  for j in range(2 * n):
    aug[i][j] /= pivot

  # 다른 행의 해당 열을 0으로 만들기
  for j in range(n):
    if i != j:
      factor = aug[j][i]
      for k in range(2 * n):
        aug[j][k] -= factor * aug[i][k]

# 역행렬 부분만 추출
inverseWithGaussJordan = [r[n:] for r in aug]

print_matrix(inverseWithGaussJordan)