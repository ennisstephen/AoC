final_output = 0

replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
with open('input.txt', 'r') as file:
    for line in file:
        new_line = line.lower()
        for word in replacements:
            if word == "eight" :
                new_line = new_line.replace(word, word + replacements[word] + "t")
            elif word == "three" or word == "five" or word == "one":
                new_line = new_line.replace(word, word + replacements[word] + "e")
            else:
                new_line = new_line.replace(word, word + replacements[word])

        parsed_value = ""
        for char in new_line:
            if char.isdigit():
                parsed_value += char

        print(parsed_value[0] + parsed_value[-1])
        final_output += int(parsed_value[0] + parsed_value[-1])

# Print or process the content as needed
print(final_output)