#loop for the program 
for fizzbuzz in range(100):
#if the number can be divided by 3 and 5 print fizzbuzz
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
#if the number can be divided by 3 print fizz
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
#if the number can be divided by 5 print buzz
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
#commentnathan