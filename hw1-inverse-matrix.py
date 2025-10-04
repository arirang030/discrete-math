# 행렬식 계산
def getDeterminant(m):
  if len(m) == 1:
    return m[0][0]
  if len(m) == 2:
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]
  
  determinant = 0
  for c in range(len(m)):
    determinant += ((-1) ** c) * m[0][c] * getDeterminant(getMatrixMinor(m, 0, c))

  return determinant

# 역행렬 존재 여부 판단
def has_inverse(m):
  determinant = getDeterminant(m)
  if abs(determinant) < 1e-10:
    print('행렬식이 0 이므로 역행렬 계산이 불가능합니다.')
    return False
  return True

# 소행렬 계산
def getMatrixMinor(m, i, j):
  return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]

# 전치행렬 계산
def transposeMatrix(m):
  return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

# 행렬식을 이용한 역행렬 계산
def getMatrixInverseWithDeterminant(m):
  determinant = getDeterminant(m)

  if (len(m) == 1):
    return [1.0 / determinant]
  
  if (len(m) == 2):
    adj = [[m[1][1], -1 * m[0][1]], [-1 * m[1][0], m[0][0]]]
    return [[adj[r][c] / determinant for c in range(2)] for r in range(2)]
  
  cofactors = []
  for r in range(len(m)):
    cofactorRow = []
    for c in range(len(m)):
      minor = getMatrixMinor(m, r, c)
      cofactorRow.append(((-1) ** (r + c)) * getDeterminant(minor))
    cofactors.append(cofactorRow)

  adj = transposeMatrix(cofactors)

  return [[adj[r][c] / determinant for c in range(len(adj))] for r in range(len(adj))]

# 가우스-조던 소거법을 이용한 역행렬 계산
def getMatrixInverseWithGaussJordan(m):
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

  return [r[n:] for r in aug]

# 역행렬을 이용한 연립방정식 해 구하기
def solveLinearSystem(inverse, y):
  n = len(inverse)
  x = []
  for i in range(n):
    res = 0
    for j in range(n):
      res += inverse[i][j] * y[j]
    x.append(res)
  return x

# 행렬 출력
def printMatrix(matrix):
  for row in matrix:
    print(" ".join(f"{elem:8.2f}" for elem in row))

# 메인 실행부
def main():
  k = int(input("정방 행렬의 차수 입력: "))
  if (k <= 0):
    print("차수는 양수여야 합니다.")
    return
  print(f"{k}x{k} 정방행렬을 입력하세요(각 행을 공백으로 구분하여 한 줄씩 입력):")

  m = []
  for i in range(k):
    while True:
      row_input = input(f"{i+1}행: ").strip()
      row_values = [float(x) for x in row_input.split()]
      if len(row_values) != k:
        print(f"입력 오류: 정확히 {k}개의 갑을 입력해야 합니다.")
        continue
      m.append(row_values)
      break

  while True:
    y_input = input("각 행에 대한 출력값을 입력하세요(각 출력값은 공백으로 구분): ")
    y = [float(x) for x in y_input.split()]
    if len(y) != k:
      print(f"입력 오류: 정확히 {k}개의 값을 입력해야 합니다.")
      continue
    break

  if has_inverse(m):
    # 행렬식을 이용한 역행렬 계산
    inverseWithDeterminant = getMatrixInverseWithDeterminant(m)
    print("행렬식을 이용한 역행렬")
    printMatrix(inverseWithDeterminant)

    # 가우스-조던 소거법을 이용한 역행렬 계산
    inverseWithGaussJordan = getMatrixInverseWithGaussJordan(m)
    print("가우스-조던 소거법을 이용한 역행렬")
    printMatrix(inverseWithGaussJordan)

    # 두 결과가 동일한지 비교
    isEqual = True
    for i in range(len(m)):
      for j in range(len(m)):
        if abs(inverseWithDeterminant[i][j] - inverseWithGaussJordan[i][j]) > 1e-10:
          isEqual = False
          break
    print("두 역행렬 비교 결과:")
    if isEqual:
      print("같다.")
    else:
      print("다르다.")
    
    # 역행렬을 이용한 연립방정식 해 구하기
    print(f"역행렬을 이용한 연립방정식 해: {solveLinearSystem(inverseWithDeterminant, y)}")

if __name__ == "__main__":
  main()