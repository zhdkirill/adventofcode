def parse (line: str) -> tuple:
  card = line.split(':')[1].strip().replace('  ', ' ')
  left = card.split('|')[0].strip().replace('  ', ' ')
  right = card.split('|')[1].strip().replace('  ', ' ')
  # print(left, right)
  a = [int(s.strip()) for s in left.split(' ')]
  b = [int(s.strip()) for s in right.split(' ')]
  return sorted(a), b

import bisect

def exists(a: list, x: int) -> bool:
  i = bisect.bisect_left(a, x)
  return i != len(a) and a[i] == x

sum = 0
with open('input.txt', 'r') as input:
  for line in input:
    # print (parse(line))
    win, my = parse(line)
    count = 0
    for num in my:
      count += int(exists(win, num))
    sum += 1 << (count - 1) if count else 0
print(sum)