def win (time, distance, hold) -> bool:
  if hold >= time or hold == 0:
    return False
  return (time - hold) * hold > distance

cases = []
with open ('input.txt', 'r') as input:
  # times = list(map(int, input.readline().split(':')[1].split()))
  # distances = list(map(int, input.readline().split(':')[1].split()))
  time = int(input.readline().split(':')[1].replace(' ', ''))
  distance = int(input.readline().split(':')[1].replace(' ', ''))
print (time,distance)

sum = 0
for i in range(time):
  if win(time, distance, i):
    sum += 1

print(sum)