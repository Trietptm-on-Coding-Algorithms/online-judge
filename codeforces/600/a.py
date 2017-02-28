def is_int(x):
    if len(x) <= 0:
        return False
    return x == '0' or all(c in '0123456789' for c in x) and x[0] != '0'

def main():
    s = input()
    
    cur = []
    words = []
    for c in s:
        if c == ',' or c == ';':
            words.append(''.join(cur))
            cur = []
        else:
            cur.append(c)

    words.append(''.join(cur))

    a = []
    b = []

    for w in words:
        if is_int(w):
            a.append(w)
        else:
            b.append(w)

    if a:
        print('"{}"'.format(','.join(a)))
    else:
        print("-")

    if b:
        print('"{}"'.format(','.join(b)))
    else:
        print("-")

main()
