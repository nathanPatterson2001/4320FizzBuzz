#choose to use strings because this way I could get the program to work with less lines of code
#range of 1-101 because the 101 wont be counted
for num in range(1,101):
#string is the number that the output will have in the range
    string = ""
#If the number can be divided by 5 print Buzz
    if num % 5 == 0:
        string = string + "Buzz"
#If the number can be divided by 3 print Fizz
    if num % 3 == 0:
        string = string + "Fizz"
#If the number can be divided by 3 and 5 FizzBuzz
#Adding the strings together to made sure that the output is FizzBuzz
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)