line_num = 0
id_total = 0
with open('input.txt', 'r') as file:
    for line in file:
        valid_line = True
        line_num += 1
        game_number, game_data = line.strip().split(': ')
        games = game_data.split('; ')
        individual_game = []
        for game in games:
            individual_game.append(game.split(", "))
        for list_of_strings in individual_game:
            for string in list_of_strings:
                if "red" in string:
                    numeric_only = ''.join(char for char in string if char.isdigit())
                    if int(numeric_only) > 12:
                        valid_line = False
                if "green" in string:
                    numeric_only = ''.join(char for char in string if char.isdigit())
                    if int(numeric_only) > 13:
                        valid_line = False
                if "blue" in string:
                    numeric_only = ''.join(char for char in string if char.isdigit())
                    if int(numeric_only) > 14:
                        valid_line = False
        if valid_line:
            id_total += line_num

print(id_total)
