def fnThree():
    print("Three")

def fnTwo():
    fnThree()
    print("Two")

def fnOne():
    fnTwo()
    print("One")

 fnOne()