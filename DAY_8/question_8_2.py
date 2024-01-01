from math import gcd

# Function to calculate LCM
def lcm(x, y):
    return x * y // gcd(x, y)


def parse_file():
    with open('input.txt', 'r') as file:
        content = file.read()

    content_split = content.split()
    file_parsed = []
    for word in content_split:
        new_word = ""
        for i in range(len(word)):
            if len(word) != 0 and word[i].isalpha():
                new_word += word[i]
        if new_word:
            file_parsed.append(new_word)

    return file_parsed


def get_values_as_dict(file_parsed):
    dict_of_values = {}
    current_key = ""
    for i in range(1, len(file_parsed)):
        if i % 3 == 1:
            dict_of_values[file_parsed[i]] = []
            current_key = file_parsed[i]
        else:
            dict_of_values[current_key].append(file_parsed[i])
    return dict_of_values


def get_steps_count(left_right):
    end_values = []
    starting_values = [key for key in values_as_dict.keys() if key.endswith('A')]
    print(starting_values)
    for j in range(len(starting_values)):
        count = 0
        find_count = True
        while find_count:
            for i in range(len(left_right)):
                if left_right[i] == "L":
                    starting_values[j] = values_as_dict[starting_values[j]][0]
                    count += 1
                else:
                    starting_values[j] = values_as_dict[starting_values[j]][1]
                    count += 1
                if starting_values[j].endswith("Z"):
                    print(starting_values[j])
                    end_values.append(count)
                    find_count = False

    return end_values


file_parsed = parse_file()
values_as_dict = get_values_as_dict(file_parsed)
left_right = file_parsed[0]
numbers = get_steps_count(left_right)

result = numbers[0]
for i in range(1, len(numbers)):
    result = lcm(result, numbers[i])

print(f"The LCM of the numbers is: {result}")
