#choose to use strings because this way I could get the program to work with less lines of code
#range of 1-101 because the 101 wont be counted
for num in range(1,101):
#string is the number that the output will have in the range
    string = ""

    if num % 5 == 0:
        string = string + "Buzz"
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)