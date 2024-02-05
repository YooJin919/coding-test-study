from sys import stdin

a, b = map(int, stdin.readline().split())
A = set(map(int, stdin.readline().split()))
B = set(map(int, stdin.readline().split()))

print(len(set(A-B) | set(B-A)))