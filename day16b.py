from itertools import islice
from functools import reduce

TYPE = {0: int.__add__, 1: int.__mul__, 2: min, 3: max, 
        5: int.__gt__, 6: int.__lt__, 7: int.__eq__}

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

def packetlist(stream):
    if (next(stream)):
        return packets(stream, fixed(stream, 11))
    return packets(islice(stream, fixed(stream, 15)), 1000)

def packets(stream, expected):
    for packet in range(expected):
        try: fixed(stream, 3)
        except StopIteration: break   
        
        typeid = fixed(stream, 3)
        if typeid == 4: 
            yield var(stream)
        else:
            yield int(reduce(TYPE[typeid], packetlist(stream)))

while True:
    try: print(list(packets(decode(input()), 1)))
    except EOFError: break