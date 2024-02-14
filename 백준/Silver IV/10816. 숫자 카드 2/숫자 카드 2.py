input()
cards = (map(int, input().split()))
input()
checks = (map(int, input().split()))

card_dict = dict()
for card in cards:
    card_dict.update({card : card_dict.get(card, 0) + 1})
    
result = []
for check in checks:
    result.append(card_dict.get(check, 0))

print(' '.join(map(str, result)))
