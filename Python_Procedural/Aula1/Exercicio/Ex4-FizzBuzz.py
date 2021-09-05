def fizzBuzz(numero):
    div3 = numero % 3
    div5 = numero % 5

    if div3 == 0 and div5 == 0:
        return 'FIZZ BUZZ'
    elif div3 == 0:
        return 'FIZZ'
    elif div5 == 0:
        return 'BUZZ'
    else:
        return numero

print(fizzBuzz(26))