number = float(input())

if number == 0:
    print("zero")

if number > 0:
    if number < 1:
        print("small positive")
    elif number > 1_000_000:
        print("large positive")
    else:
        print("positive")

if number < 0:
    if abs(number) < 1:
        print("small negative")
    elif abs(number) > 1_00_000:
        print("large negative")
    else:
        print("negative")