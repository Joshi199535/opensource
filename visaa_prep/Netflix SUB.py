def can_afford_netflix(A, B, C, X):
    if A + B >= X or B + C >= X or C + A >= X:
        return "YES"
    else:
        return "NO"
A, B, C, X = map(int, input().split())
print(can_afford_netflix(A, B, C, X))
