def parse(s: str):
  game = s.split(':')
  res = {}
  res['id'] = int(game[0].split(' ')[-1])
  res['sets'] = []
  for set in game[1].split(';'):
    cur = {}
    for cubes in set.split(','):
      cubes = cubes.strip()
      cube = cubes.split(' ')
      cur[cube[1]] = int(cube[0])
    res['sets'].append(cur)
  return res

def check_set (set: dict):
  return ('red' not in set.keys() or set['red'] <= 12) and \
         ('green' not in set.keys() or set['green'] <= 13) and \
         ('blue' not in set.keys() or set['blue'] <= 14)


def check_game (sets: list):
  return all(check_set(gameset) for gameset in sets)

# colors = ['red', 'green', 'blue']

def max_cubes (sets: list):
  res = {'red' : 0, 'green': 0, 'blue': 0}
  for set in sets:
    for color in set.keys():
      if res[color] < set[color]:
        res[color] = set[color]
  return res

import functools

sum = 0
with open('input.txt', 'r') as input:
  for line in input:
    # print(parse(line))
    game = parse(line)
    # if check_game(game['sets']):
    #   sum += game['id']
    cubes = max_cubes(game['sets'])
    power = cubes['red'] * cubes['green'] * cubes['blue']
    print(power)
    sum += power
print(sum)