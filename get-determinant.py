# 소행렬 계산
def getMatrixMinor(m, i, j):
  return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]

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

m = [[-2, 2, -3], [1, 0, 1], [-4, 3, -5]]

print(f"determinant: {getDeterminant(m)}")