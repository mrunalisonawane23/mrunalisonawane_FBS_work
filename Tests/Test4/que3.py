def pattern():
    for i in range(20):
        print("*", end="")
    print()

    for i in range(10):
        print(" " * (19 - i) + "*")

    for i in range(20):
        print("*", end="")
    print()

pattern()