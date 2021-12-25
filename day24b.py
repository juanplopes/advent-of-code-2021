from collections import Counter
OP = {'add': int.__add__, 'mul': int.__mul__, 'div': int.__floordiv__, 
      'mod': int.__mod__, 'eql': int.__eq__}

def get(state, var):
    return state['wxyz'.index(var)] if var.isalpha() else int(var)

def put(state, var, value):
    idx = 'wxyz'.index(var)
    return state[:idx] + (value,) + state[idx+1:]

def exec(cmd, state, best):
    if cmd[0] == 'inp':
        for value in range(1, 10):
            yield put(state, cmd[1], value), best*10+value
    else:
        yield put(state, cmd[1], OP[cmd[0]](
            get(state, cmd[1]), get(state, cmd[2]))), best
   
MAX = 10**30
T = Counter({(0, 0, 0, 0): 0})
for i in range(10000):
    try: cmd = input().split(' ')
    except EOFError: break
    T, U = Counter(), T
    for state, best in U.items():
        for newstate, newbest in exec(cmd, state, best):
            T[newstate] = min(T.get(newstate, MAX), newbest)
    print(i, len(T))

print(min(best for (w, x, y, z), best in T.items() if z == 0))