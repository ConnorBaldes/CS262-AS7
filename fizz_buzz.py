def fizz_buzz():
    numbers = ""
    for i in range(100):
        if ((i+1) % 3) != 0:
            numbers += str(i+1)
        else:
            numbers += "Fizz"
        if i != 99:
            numbers +=" "
    return numbers