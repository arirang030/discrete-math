# 1. 관계 행렬 입력

# 2. 동치 관계인지 판별
# 2-1. 반사 관계인지 검사
# 2-2. 대칭 관계인지 검사
# 2-3. 추이 관계인지 검사

# 3. 동치 관계이면 동치류 출력

# 4. 폐포 구현

# 5. 추이 폐포 만들 때 와샬 알고리즘을 사용한 것과 사용하지 않은 것의 걸리는 시간 각각 계산

import timeit

# 행렬 출력
def print_matrix(m):
  for i in range(len(m)):
    for j in range(len(m)):
      print(m[i][j], end=" ")
    print()

# 관계 순서쌍 출력
def print_relation(m, a):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == 1:
        print(f"({a[i]}, {a[j]})", end=" ")

# 반사 관계인지 검사
def is_reflexive(m):
  for i in range(len(m)):
    if m[i][i] != 1:
      return False
  return True

# 대칭 관계인지 검사
def is_symmetric(m):
  for i in range(len(m)):
    for j in range(len(m)):
      if m[i][j] != m[j][i]:
        return False
  return True

# 부울 곱 계산
def matrix_mult(a, b):
  n = len(a)
  result = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        result[i][j] |= a[i][k] & b[k][j]
  return result

# 추이 관계인지 검사
def is_transitive(m):
  n = len(m)
  power = [row[:] for row in m]

  for _ in range(1, n):
    power = matrix_mult(power, m)
    for i in range(n):
      for j in range(n):
        if power[i][j] == 1 and m[i][j] == 0:
          return False
  return True

# 동치류 출력
def print_equivalence_class(m):
  print("\n이 관계는 동치 관계입니다.")
  print("\n---동치류 출력---")
  for i in range(len(m)):
    e = []
    for j in range(len(m)):
      if m[i][j] == 1:
        e.append(j)
    print(f"[{i+1}] = " + "{", end="")
    for i in range(len(e)):
      if i + 1 != len(e):
        print(f"{e[i]},", end=" ")
      else:
        print(f"{e[i]}", end="")
    print("}")
  print("-----------------")

# 반사 폐포로 만들기
def to_reflexive_closure(m):
  for i in range(len(m)):
    if m[i][i] != 1:
      m[i][i] = 1
  return m

# 대칭 폐포로 만들기
def to_symmetric_closure(m):
  for i in range(len(m)):
    for j in range(len(m)):
      if m[i][j] == 1 and m[j][i] == 0:
        m[j][i] = 1
  return m

# 추이 폐포로 만들기(와샬 알고리즘 사용)
def to_transitive_closure_by_warshall(m):
  n = len(m)
  for k in range(n): # 중간 노드
    for i in range(n): # 시작 노드
        for j in range(n): # 끝 노드
            if m[i][k] and m[k][j]:
                m[i][j] = 1
  return m

# 추이 폐포로 만들기(거듭제곱 사용)
def to_transitive_closure_by_power(m):
    n = len(m)
    combined = [row[:] for row in m]
    power = [row[:] for row in m]
    for _ in range(1, n):
        power = matrix_mult(power, m)
        for i in range(n):
            for j in range(n):
                combined[i][j] |= power[i][j]
    return combined


def main():
  a = [1, 2, 3, 4, 5]
  n = len(a)
  m = []
  print("5X5 관계 행렬을 행 단위로 입력하시오: ")

  for _ in range(n):
    row = list(map(int, input().split()))
    m.append(row)

  print("\n[관계 R에 포함된 순서쌍]")
  print_relation(m, a)
  print()

  if is_reflexive(m):
    if is_symmetric(m):
      if is_transitive(m):
          print_equivalence_class(m)
      else:
        print("\n이 관계는 추이 관계가 아닙니다.")

        # 추가 가능
        # 각각 와샬 알고리즘과 거듭 제곱을 사용해 추이 폐포로 만드는 데 걸리는 시간 확인
        t = timeit.timeit(lambda: to_transitive_closure_by_warshall(m), number=100)
        print(f"\n와샬 알고리즘을 사용해 추이 폐포를 구했을 때 소요 시간: {t}")
        t = timeit.timeit(lambda: to_transitive_closure_by_power(m), number=100)
        print(f"\n거듭 제곱을 사용해 추이 폐포를 구했을 때 소요 시간: {t}")

        transitive_m = to_transitive_closure_by_warshall(m)
        print("\n[추이 폐포가 동치 관계인지 검사]")
        print("\n폐포 변환 전: ")
        print_matrix(m)
        print("\n폐포 변환 후: ")
        print_matrix(transitive_m)
        if is_transitive(transitive_m):
          print_equivalence_class(m)
        else:
          print("\n동치 관계가 아닙니다.")

    else:
      print("\n이 관계는 대칭 관계가 아닙니다.")
      symmetric_m = to_symmetric_closure(m)
      print("\n[대칭 폐포가 동치 관계인지 검사]")
      print("\n폐포 변환 전: ")
      print_matrix(m)
      print("\n폐포 변환 후: ")
      print_matrix(symmetric_m)
      if is_symmetric(symmetric_m):
        print_equivalence_class(m)
      else:
        print("\n동치 관계가 아닙니다.")
  else:
    print("\n이 관계는 반사 관계가 아닙니다.")
    reflexive_m = to_reflexive_closure(m)
    print("\n[반사 폐포가 동치 관계인지 검사]")
    print("\n폐포 변환 전: ")
    print_matrix(m)
    print("\n폐포 변환 후: ")
    print_matrix(reflexive_m)
    if is_reflexive(reflexive_m):
      print_equivalence_class(m)
    else:
      print("\n동치 관계가 아닙니다.")

if __name__ == "__main__":
  main()