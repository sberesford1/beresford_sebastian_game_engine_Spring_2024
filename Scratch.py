class Number:

    def multi (x,y) :
        return x*y
    print (multi(3,2))

    def stringify(a):
        return str(a) + "Number"

    on = True
    d=10

    while on:
        print (multi(3,2))
        print (stringify(multi(3,2)))
        d -=1
        if d == 0:
            on = False

    for i in range(10):
        print (multi(3,2))
        print (stringify(multi(3,2)))

