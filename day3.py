map = []
area = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]
stars = []

# stars = {}

def isSymbol (c: str) -> bool:
  # return not c.isdigit() and c != '.' and c.isprintable()
  return c == '*'

def getStarById (d: tuple):
  for star in stars:
    if star['id'] == d:
      return star

def nearbyPart(i, j) -> bool:
  ans = False
  for move in area:
    x = min(max(i + move[0], 0), len(map)-1)
    y = min(max(j + move[1], 0), len(map[i])-1)
    isStar = isSymbol(map[x][y])
    ans |= isStar
    if isStar:
      star = getStarById((x,y))
      star['new'] = True
  return ans

def addNum(num: int):
  for star in stars:
    if star['new']:
      star['nums'].append(num)
    star['new'] = False

def cleanup():
  for star in stars:
    star['new'] = False

with open('input.txt', 'r') as input:
  for line in input:
    map.append(line)

for i in range(len(map)):
  for j in range(len(map[i])):
    if map[i][j] == '*':
      stars.append({'id': (i, j)})
for star in stars:
  star['new'] = False
  star['nums'] = []


number = ''
valid = False
for i in range(len(map)):
  for j in range(len(map[i])):
    char : str = map[i][j]
    if char == '.' or not char.isprintable() or isSymbol(char):
      if number != '' and valid:
        addNum(int(number))
      number = ''
      valid = False
      cleanup()
    if char.isdigit():
      number += char
      valid |= nearbyPart(i, j)


sum = 0
for star in stars:
  if len(star['nums']) == 2:
    sum += star['nums'][0] * star['nums'][1]
print (sum)