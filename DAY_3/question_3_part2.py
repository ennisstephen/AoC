import re

symbols = []
count = 0
symbol_touches = {}
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
            #check left side
            if index-1 >= 0 and symbols[line_num][index-1]:
                if "Line: " + str(line_num) + " Index: " + str(index-1) in symbol_touches:
                    symbol_touches["Line: " + str(line_num) + " Index: " + str(index-1)].append(int(number))
                else:
                    new_list = [int(number)]
                    symbol_touches["Line: " + str(line_num) + " Index: " + str(index - 1)] = new_list
                continue
            #check right side
            if index_of_last+1 < line_length and symbols[line_num][index_of_last+1]:
                if "Line: " + str(line_num) + " Index: " + str(index_of_last+1) in symbol_touches:
                    symbol_touches["Line: " + str(line_num) + " Index: " + str(index_of_last+1)].append(int(number))
                else:
                    new_list = [int(number)]
                    symbol_touches["Line: " + str(line_num) + " Index: " + str(index_of_last + 1)] = new_list
                continue
            #check top
            if line_num > 0:
            #top left
                if index - 1 >= 0 and symbols[line_num-1][index-1]:
                    if "Line: " + str(line_num-1) + " Index: " + str(index - 1) in symbol_touches:
                        symbol_touches["Line: " + str(line_num-1) + " Index: " + str(index - 1)].append(int(number))
                    else:
                        new_list = [int(number)]
                        symbol_touches["Line: " + str(line_num - 1) + " Index: " + str(index - 1)] = new_list
                    continue
            #top right
                if index_of_last + 1 < line_length and symbols[line_num-1][index_of_last+1]:
                    if "Line: " + str(line_num - 1) + " Index: " + str(index_of_last+1) in symbol_touches:
                        symbol_touches["Line: " + str(line_num - 1) + " Index: " + str(index_of_last+1)].append(int(number))
                    else:
                        new_list = [int(number)]
                        symbol_touches["Line: " + str(line_num - 1) + " Index: " + str(index_of_last + 1)] = new_list
                    continue
             #check directly on top
                for x in range (index, index_of_last+1):
                    if symbols[line_num-1][x]:
                        if "Line: " + str(line_num - 1) + " Index: " + str(x) in symbol_touches:
                            symbol_touches["Line: " + str(line_num - 1) + " Index: " + str(x)].append(int(number))
                        else:
                            new_list = [int(number)]
                            symbol_touches["Line: " + str(line_num - 1) + " Index: " + str(x)] = new_list
                        continue

            #check bottom
            if line_num < line_count:
                # bottom left
                if index - 1 >= 0 and symbols[line_num + 1][index - 1]:
                    #symbol_touches["Line: " + str(line_num+1) + " Index: " + str(index - 1)] = int(number)
                    if "Line: " + str(line_num+1) + " Index: " + str(index - 1) in symbol_touches:
                        symbol_touches["Line: " + str(line_num+1) + " Index: " + str(index - 1)].append(int(number))
                    else:
                        new_list = [int(number)]
                        symbol_touches["Line: " + str(line_num+1) + " Index: " + str(index - 1)] = new_list
                    continue
                # bottom right
                if index_of_last + 1 < line_length and symbols[line_num+1][index_of_last+1]:
                    #symbol_touches["Line: " + str(line_num + 1) + " Index: " + str(index_of_last+1)] = int(number)
                    if "Line: " + str(line_num + 1) + " Index: " + str(index_of_last+1) in symbol_touches:
                        symbol_touches["Line: " + str(line_num + 1) + " Index: " + str(index_of_last+1)].append(number)
                    else:
                        new_list = [int(number)]
                        symbol_touches["Line: " + str(line_num + 1) + " Index: " + str(index_of_last + 1)] = new_list
                    continue
                # directly below
                for x in range(index, index_of_last + 1):
                    if symbols[line_num + 1][x]:
                        #symbol_touches["Line: " + str(line_num + 1) + " Index: " + str(x)] = int(number)
                        if "Line: " + str(line_num + 1) + " Index: " + str(x) in symbol_touches:
                            symbol_touches["Line: " + str(line_num + 1) + " Index: " + str(x)].append(number)
                        else:
                            new_list = [int(number)]
                            symbol_touches["Line: " + str(line_num + 1) + " Index: " + str(x)] = new_list
                        continue
        line_num += 1

for key, value in symbol_touches.items():
    if len(value) == 2:
        result= value[0]*value[1]
        count += result

print(count)