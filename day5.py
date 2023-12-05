seeds = []
swap = []

with open('input.txt', 'r') as input:
  for line in input:
    if line.startswith('seeds'):
      # init seeds
      nums = line.split()
      for num in nums:
        if num.strip().isnumeric():
          swap.append(int(num))
      continue
    if line == '\n':
      swap += seeds
      # reinit
      seeds = swap.copy()
      swap.clear()
      continue
    if line.endswith('map:\n'):
      continue

    # conversion
    map = line.split()
    dst = int(map[0].strip())
    src = int(map[1].strip())
    rng = int(map[2].strip())

    # move = [seed - (src - dst) for seed in seeds if seed >= src and seed < src+rng]
    # swap += move
    # seeds -= move

    tmp = seeds.copy()
    for seed in tmp:
      if seed >= src and seed < src+rng:
        swap.append(seed - (src - dst))
        seeds.remove(seed)

print(min(seeds))
# print(seeds)