bag = input(int("bag"))
wa = input(int("wa"))

sum = bag + wa

if sum >= 100000:
    print('total:', sum * 0.7)
    elif sum >= 50000:
    print('total:', sum * 0.8)
    else:
    print('total:', sum * 0.9)

    print("total:", sum)
