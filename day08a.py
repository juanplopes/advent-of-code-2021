S = set([2, 3, 4, 7])
answer = 0
while True:
    try:
        _, data = (x.split() for x in  input().split('|'))
    except EOFError: break
    
    answer += sum(len(number) in S for number in data)
print(answer)