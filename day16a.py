from itertools import chain, islice

def decode(hex):
    for b in (bin(int(x, 16))[2:].rjust(4, '0') for x in hex):
        yield from map(int, b)

def fixed(stream, count):
    answer = 0
    for i in range(count):
        answer = answer * 2 + next(stream)
    return answer

def var(stream):
    answer = 0
    while True:
        has_next = next(stream)
        answer = answer * 16 + fixed(stream, 4)
        if not has_next: return answer

def packets(stream, expected):
    answer = 0
    for packet in range(expected):
        try:
            version = fixed(stream, 3)
            typeid = fixed(stream, 3)
            answer += version

            if typeid == 4: 
                var(stream)
            elif next(stream):
                answer += packets(stream, fixed(stream, 11))
            else:
                answer += packets(islice(stream, fixed(stream, 15)), 1000)
        except StopIteration:
            break
    return answer

while True:
    try: print(packets(decode(input()), 1))
    except EOFError: break