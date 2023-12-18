def win (time, distance, hold) -> bool:
  if hold >= time or hold == 0:
    return False
  return (time - hold) * hold > distance

cases = []
with open ('input.txt', 'r') as input:
  times = list(map(int, input.readline().split(':')[1].split()))
  distances = list(map(int, input.readline().split(':')[1].split()))
for i in range(len(times)):
  cases.append((times[i], distances[i]))
print(cases)

sums = []
for case in cases:
  sum = 0
  for i in range(case[0]):
    if win(case[0], case[1], i):
      sum += 1
  sums.append(sum)

import functools
print(functools.reduce(lambda a,b: a*b, sums))
  