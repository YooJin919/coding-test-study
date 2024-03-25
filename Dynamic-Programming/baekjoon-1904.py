from sys import stdin

N = int(stdin.readline().rstrip())
seq = [0, 1, 2]

if(N == 1 or N == 2):
  print(seq[N])
else:
  for i in range(3, N+1):
    seq.append((seq[i-1] + seq[i-2])%15746)

  print(seq[N])