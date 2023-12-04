map = []
area = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]

def isSymbol (c: str) -> bool:
  return not c.isdigit() and c != '.' and c.isprintable()

def nearbyPart(i, j) -> bool:
  ans = False
  for move in area:
    x = min(max(i + move[0], 0), len(map)-1)
    y = min(max(j + move[1], 0), len(map[i])-1)
    ans = isSymbol(map[x][y]) or ans
  return ans

with open('input.txt', 'r') as input:
  for line in input:
    map.append(line)

sum = 0
number = ''
valid = False
for i in range(len(map)):
  for j in range(len(map[i])):
    char : str = map[i][j]
    if char == '.' or not char.isprintable() or isSymbol(char):
      if number != '' and valid:
        sum += int(number)
      number = ''
      valid = False
    if char.isdigit():
      number += char
      valid |= nearbyPart(i, j)
print(sum)

