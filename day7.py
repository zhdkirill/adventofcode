CARDS = { 'A': 20, 'K': 15, 'Q': 14, 'J': 13, 'T': 12, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

def value (hand: str):
  calc = {}
  for card in hand:
    if card in calc.keys():
      calc[card] += 1
    else:
      calc[card] = 1

  if max(calc.values()) == 5:
    # 5 of a kind
    return (100)
  if max(calc.values()) == 4:
    # 4 of a kind
    return (80)
  if max(calc.values()) == 3 and min(calc.values()) == 2:
    # full house
    return (50)
  if max(calc.values()) == 3:
    # 3 of a kind
    return 30
  if max(calc.values()) == 2 and len([calc[i] for i in calc.keys() if calc[i] == 2]) == 2:
    # two pairs
    return 25
  if max(calc.values()) == 2:
    # pair
    return 20
  return 10

hands = []
with open('input.txt', 'r') as input:
  for line in input:
    hand = {}
    hand['cards'] = line.split()[0].strip()
    hand['sort'] = line.split()[0].strip().replace('A', 'Z').replace('K', 'Y').replace('Q', 'X').replace('J', 'W').replace('T', 'V')
    hand['bid'] = int(line.split()[1])
    hand['value'] = value(hand['cards'])
    hands.append(hand)

hands.sort(key=lambda a: (a['value'], a['sort']))

answer = 0
for hand in enumerate(hands):
  answer += (hand[0] + 1) * hand[1]['bid']

print (hands)
print(answer)
  