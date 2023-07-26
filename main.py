from readchar import readkey, key

while True:
    k = readkey()
    match k:
        case key.UP:
            break
        case _:
            print(k)
