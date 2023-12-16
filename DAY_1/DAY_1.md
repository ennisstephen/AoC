# Day 1 Solution Analysis - Advent of Code 2023

The challenge presented a set of lines within a file, and I was to get the first and last digit of each line and merge them. Then get the sum of the numbers derived from each line. Easy Peasy right? 

The issue came for me when they introduced numbers AND words (one, two, three, etc.). I coverted all words to digits, but my solution still didn't produce the correct answer! Eventually, I figured out that this was because sometimes the words are "merged" together in the given input, ie. (eightwo = 82, fiveight= 58, threeight = 38 etc.). IMO, the explanation didn't make that clear enough, but I'm totally new to AoC so probably wasn't ready for a curveball like that. Using my solution eightwo would become 8wo, thus the 2 wouldn't parse. Eventually I figured out a solution (hack) - when replacing a number that could potentially clash, I also add the last letter of that number. Using this technique instead of replacing eight with 8 I would replace it with 8t, thus eightwo would become 8two and then 82. This solution got me the correct answer and 2 stars 😊

# Lessons Learned
- The task underscored the significance of edge cases.

- Look closely at the example (which gives the solution), and work with that before working with main input. This will clarify some edge cases.

- I think regex will be vital going forward.😊
