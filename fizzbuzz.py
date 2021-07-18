#If x % 3 or 5 == FizzBuzz  elif x not % 3 or 5 == fizz or buzz

for f in range(1, 101):
    if f % 3 == 0 and f % 5 == 0:
        print('fizzBuzz')
        continue
    elif f % 3 == 0:
        print('fizz')
        continue
    elif f % 5 == 0:
        print('buzz')
        continue
    print(f)