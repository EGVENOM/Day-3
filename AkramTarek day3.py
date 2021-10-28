x   = int(input("enter the start of range"))
y   = int(input("enter the end of range"))
zh  =   []
def PerfectSquare(zh):
    square  =   []
    for zh  in range    (x  ,y  ,1):
            if zh**2<=y:
                square.append(zh**2)
            else:
                break
    return (square)

print(PerfectSquare(zh))



