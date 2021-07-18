#Divide int List

def get_dividers(args):
    divide = []
    for x in range(1, args+1):
        if args % x == 0:
            divide.append(x)
    return divide
print(get_dividers(12))