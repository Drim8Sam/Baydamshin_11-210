text = input()
while text != 'quit':
    count = 1
    symbol = ''
    for i in text:
        if i == symbol:
            count += 1
        else:
            if symbol:
                print(symbol, end='')
                if count > 1:
                    print(count, end='')
            symbol = i
            count = 1
    if symbol:
        print(symbol, end='')
        if count > 1:
            print(count, end='')

    text = input()




