r1, c1, r2, c2 = map(int,input().split())

#1. generate method which gives value with input of row & column
def val_from_rc(r,c):

    boundary = max(abs(r),abs(c))
    # east side
    if c==boundary:
        if r==boundary:
            return (2*boundary+1)**2
        else:
            return (2*boundary-1)**2+(boundary-r)
    # north side
    elif r==-boundary:
        return 4*boundary**2-boundary+1-c
    # west side
    elif c==-boundary:
        return 4*boundary**2+boundary+1+r
    # south side
    else:
        return 4*boundary**2+3*boundary+1+c

#2. generate answer with given row & column
answer = []
m_length = 0

for r in range(r1, r2+1): #r1 부터 r2 까지
    row = []
    for c in range(c1, c2+1): # 
        row.append(val_from_rc(r,c))
    row = list(map(str, row))
    m_length = max((max(map(lambda val: len(val), row))), m_length)
    answer.append(row)

#3. match forms
for r in answer:
    print(' '.join(list(map(lambda val: val.rjust(m_length, " "), r))))