import itertools

cards = ["克拉斯", "纳贝尔", "人马", "天玑"]

hands = list(itertools.combinations(cards, 3))

for hand in hands:
    print("+".join(hand))
