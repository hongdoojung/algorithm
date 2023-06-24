import sys


sentences = ""
while True:
    sentence = sys.stdin.readline().strip()
    if sentence == "#":
        break
    else:
        num = 0
        for s in sentence:
            if s in ["a", "e", "i", "o", "u"]:
                num += 1
            elif s in ["A", "E", "I", "O", "U"]:
                num += 1
        print(num)
