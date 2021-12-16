from itertools import islice
from functools import reduce

INFIX = {0: '+', 1: '*', 2: ',', 3: ',', 5: '>', 6: '<', 7: '=='}
PREFIX = {2:'min([', 3:'max(['}
SUFFIX = {2:'])', 3:'])'}

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
    if next(stream):
        return map(lambda _: packet(stream), range(fixed(stream, 11)))
    else:
        sliced = islice(stream, fixed(stream, 15))
        return map(lambda _: packet(sliced), range(1000))

def packet(stream):
    fixed(stream, 3)
    typeid = fixed(stream, 3)
    if typeid == 4: 
        return str(var(stream))
    else:
        return f"{PREFIX.get(typeid, '(')}{INFIX[typeid].join(packetlist(stream))}{SUFFIX.get(typeid, ')')}"

while True:
    try: print(packet(decode(input())))
    except EOFError: break