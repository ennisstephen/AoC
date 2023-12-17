line_num = 0
dice_total = 0
with open('input.txt', 'r') as file:
    for line in file:
        num_of_red = 1
        num_of_green = 1
        num_of_blue = 1

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
                    if int(numeric_only) > num_of_red:
                        num_of_red = int(numeric_only)
                if "green" in string:
                    numeric_only = ''.join(char for char in string if char.isdigit())
                    if int(numeric_only) > num_of_green:
                        num_of_green = int(numeric_only)
                if "blue" in string:
                    numeric_only = ''.join(char for char in string if char.isdigit())
                    if int(numeric_only) > num_of_blue:
                        num_of_blue = int(numeric_only)
        dice_total += (num_of_red * num_of_green * num_of_blue)

print(dice_total)
