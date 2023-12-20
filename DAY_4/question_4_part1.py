count = 0
card_num = 0
num_of_cards = {}
card_values = {}

with open('input.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        card_num += 1
        line = line.strip()
        lotto_value = 0
        # Iterate through each character in the line
        game_name, numbers = line.split(': ')
        lotto_ticket, winning_numbers = numbers.split(' | ')
        ticket_list = [int(item) for item in lotto_ticket.split(" ") if item.isdigit()]
        winning_numbers_list = [int(item) for item in winning_numbers.split(" ") if item.isdigit()]
        ticket_value = 0

        for number in ticket_list:
            if number in winning_numbers_list:
                if ticket_value == 0:
                    ticket_value += 1
                else:
                    ticket_value *= 2
        count += ticket_value
    
print(count)
