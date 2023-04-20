s = input("Input math expression: ")
while s.lower() != 'stop':
    print("Result: ", eval(s))
    s = input("Input math expression: ")
print("You've finished the program.")