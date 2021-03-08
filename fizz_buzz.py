def fizz_buzz():
    numbers = ""
    for i in range(100):
        numbers += str(i+1)
        if i != 99:
            numbers +=" "
    return numbers