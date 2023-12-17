import re

symbols = []
count = 0
#  Which character is a symbol
with open('input.txt', 'r') as file:
    for line in file:
        symbols_in_line = []
        for index, char in enumerate(line):
            if not char.isdigit() and char != "." and char != "\n":
                symbols_in_line.append(True)
            elif char == "\n":
                pass
            else:
                symbols_in_line.append(False)
        symbols.append(symbols_in_line)

    file.seek(0)
    line_num = 0
    line_count = len(file.readlines()) - 1
    line_length = len(symbols[line_num])
    file.seek(0)
    for line in file:
        numbers_with_indices = [(match.group(), match.start()) for match in re.finditer(r'\d+', line)]

    # Output the numbers and their indices
        for number, index in numbers_with_indices:
            symbols_on_top = False
            symbols_on_bottom = False
            index_of_last = index + len(number)-1
            if index-1 >= 0 and symbols[line_num][index-1]:
                print(f"Number: {number}")
                count = count + int(number)
                continue
            #check right side
            if index_of_last+1 < line_length and symbols[line_num][index_of_last+1]:
                print(f"Number: {number}")
                count = count + int(number)
                continue
            #check top
            if line_num > 0:
            #top left
                if index - 1 >= 0 and symbols[line_num-1][index-1]:
                    print(f"Number: {number}")
                    count = count + int(number)
                    continue
            #top right
                if index_of_last + 1 < line_length and symbols[line_num-1][index_of_last+1]:
                    print(f"Number: {number}")
                    count = count + int(number)
                    continue
             #check directly on top
                for x in range (index, index_of_last+1):
                    if symbols[line_num-1][x]:
                        print(f"Number: {number}")
                        count = count + int(number)
                        continue

            #check bottom
            if line_num < line_count:
                # bottom left
                if index - 1 >= 0 and symbols[line_num + 1][index - 1]:
                    print(f"Number: {number}")
                    count = count + int(number)
                    continue
                # bottom right
                if index_of_last + 1 < line_length and symbols[line_num+1][index_of_last+1]:
                    print(f"Number: {number}")
                    count = count + int(number)
                    continue
                for x in range(index, index_of_last + 1):
                    if symbols[line_num + 1][x]:
                        print(f"Number: {number}")
                        count = count + int(number)
                        continue

        line_num += 1

print(count)