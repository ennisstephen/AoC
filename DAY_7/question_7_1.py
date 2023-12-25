with open('input.txt', 'r') as file:
    content = file.read()

values = content.split()

hand_list = []
values_list = []
hand_values = []
hand_as_ints = []

for value in values:
    if len(value) == 5:
        hand_list.append(value)
    else:
        values_list.append(value)

j = 0
for hand in hand_list:
    hand_values = []
    for i in range(len(hand)):
        if hand[i].isdigit():
            hand_values.append(int(hand[i]))
        elif hand[i] == 'T':
            hand_values.append(10)
        elif hand[i] == 'J':
            hand_values.append(11)
        elif hand[i] == 'Q':
            hand_values.append(12)
        elif hand[i] == 'K':
            hand_values.append(13)
        elif hand[i] == 'A':
            hand_values.append(14)
    hand_values.append(int(values_list[j]) + 100)
    hand_as_ints.append(hand_values)
    j += 1

high_card = []
pair = []
two_pair = []
trips = []
boat = []
quads = []
all_five = []

print(hand_as_ints)
hand_as_ints.sort()
print(hand_as_ints)

for hand in hand_as_ints:
    hand.sort()

    if (hand[0] == hand[1] and hand[1] == hand[2] and hand[2] == hand[3] and hand[3] == hand[4]):
        all_five.append(hand)
        continue

    if ((hand[0] == hand[1] and hand[1] == hand[2] and hand[2] == hand[3])
            or (hand[1] == hand[2] and hand[2] == hand[3] and hand[3] == hand[4])):
        quads.append(hand)
        continue

    unique_values = set(hand)

    if len(unique_values) == 3:
        boat.append(hand)
    elif ((hand[0] == hand[1] and hand[1] == hand[2])
            or (hand[1] == hand[2] and hand[2] == hand[3])
                or (hand[2] == hand[3] and hand[3] == hand[4])):
        trips.append(hand)
    elif len(unique_values) == 4:
        two_pair.append(hand)
    elif len(unique_values) == 5:
        pair.append(hand)
    else:
        high_card.append(hand)

print("high_card")
print(high_card)
print("pair")
print(pair)
print("two pair")
print(two_pair)
print("trips")
print(trips)
print("boat")
print(boat)
print("quads")
print(quads)

merged_list = high_card + pair + two_pair + trips + boat + quads + all_five
count = 0

for i in range(0, len(merged_list)):
    count += (merged_list[i][5] - 100) * (i + 1)

print(count)
print(len(merged_list))



