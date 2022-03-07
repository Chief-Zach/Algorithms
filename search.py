def linear(data, term):
    for index, value in enumerate(data):
        if value == term:
            return index, value


def slicendice(lower, upper, value):
    while True:
        middle = int((upper + lower)) / 2
        if middle == value:
            return True
        elif middle < value:
            print(lower, upper)
            lower = middle
            upper = upper
        elif middle > value:
            print(lower, upper)
            lower = lower
            upper = middle