from decimal import Decimal

with open('input.txt', 'r') as file:
    content = file.read()

content_split = content.split()
times = []
distances = []

distance = False
for number in content_split:
    if number == "Distance:":
        distance = True
    if number.isdigit():
        if distance:
            distances.append(int(number))
        else:
            times.append(int(number))

print(content_split)
print(times)
print(distances)

ways_to_win_each_game = Decimal(0)

for x in range(len(times)):
    for i in range(1, times[x]):
        if i * (times[x] - i) > distances[x]:
            ways_to_win_each_game += 1

print(ways_to_win_each_game)