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
    starting_value = "AAA"
    count = 0

    while starting_value != "ZZZ":
        for i in range(len(left_right)):
            if left_right[i] == "L":
                starting_value = values_as_dict[starting_value][0]
                count += 1
            else:
                starting_value = values_as_dict[starting_value][1]
                count += 1
    print(count)


file_parsed = parse_file()
values_as_dict = get_values_as_dict(file_parsed)
left_right = file_parsed[0]
get_steps_count(left_right)
