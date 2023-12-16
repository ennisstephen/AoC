# Day 1 Solution Analysis - Advent of Code 2023

The challenge presented a set of lines within a file, and I was to get the first and last digit of each line and merge them. Then get the sum of the numbers derived from each line. Easy Peasy right? 

> For example:
>
>1abc2
>
>pqr3stu8vwx
>
>a1b2c3d4e5f
>
>treb7uchet
>
>In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

My approach was to simply to create a new string for each line, but only save the digits, by looping through each character in each line and using the isdigit() method on each character. If the character was a digit, it got saved to my new string.

Then I used indexes to get the first and last character of my new string, merged them, and converted that to an int. Then I could add the int for each line together to get our answer.

Part 2 also seemed like a piece of cake. We now had to take into consideration if words were written.

>For example:
>
>nineninesixskjkbhx6nineoneightj
>
>would parse to 996918
>
>Then we'd take our first and last digit 98.
>
>two1nine
> 
>would parse to 219 then 29.

I initally just did a find and replace with a dictionary to replace each written number with the number character ie one would become 1. However, this didn't give me the correct answer, due to edge cases where numbers "merged" together, imagine the situation oneight, this should parse to 18. But with my solution it would become 1ight and then the eight wouldn't get parsed. I also had doubts about what was the expected behaviour when numbers "merged", but the examples didn't exactly spell it out. I thought about using dictionaries and indexes to get around this issue, because editing the line in place didn't seem to work, but I knew this would become a huge mess, and there had to be an easier solution. Eventually I came up with the solution to add an extra letter to my string in cases where another written number could use the last letter of a word which is being replaced, ie instead of replacing eight with 8, I replaced it with 8t. Therefore eightthree would become 8three and then 83, instead of 8hree. Finally got out of dodge in 34 lines of code which wasn't bad, although I'm sure there are more succinct soloutions.

# Lessons Learned
- The task underscored the significance of edge cases.

- Look closely at the example (which gives the solution), and work with that before working with main input. This will clarify some edge cases.

- I think regex will be vital going forward.😊
