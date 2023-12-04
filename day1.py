ans = 0
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for i in range(1,10):
  numbers.append(str(i))

def lmin_num (s: str):
  pos = 10**9
  ans = '-1'
  for n in numbers:
    cur = s.find(n)
    if cur > -1 and cur < pos:
      pos = cur
      ans = n
  return ans

def rmin_num (s: str):
  pos = -1
  ans = '-1'
  for n in numbers:
    cur = s.rfind(n)
    if cur > -1 and cur > pos:
      pos = cur
      ans = n
  return ans

def toint (s: str):
  if len(s) == 1:
    return int(s)
  else:
    return numbers.index(s) + 1

with open('input.txt', 'r') as input:
  for line in input:
    a = toint(lmin_num(line))
    b = toint(rmin_num(line))
    ans += a * 10 + b
print (ans)