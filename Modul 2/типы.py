
L = list(map(float, input().split()))
L[0], L[-1] = L[-1], L[0]

print(L)