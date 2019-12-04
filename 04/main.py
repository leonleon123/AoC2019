def ascending_digits(a):
    return all(int(a[x])<=int(a[x+1]) for x in range(len(a)-1))
def same_digits(a):
    return any(int(a[x])==int(a[x+1]) for x in range(len(a)-1))
def larger_group(a):
    b=[""]+[a[x:x+2] for x in range(len(a)-1)]+[""]
    return any(b[x][0]==b[x][1] and b[x]!=b[x-1] and b[x]!=b[x+1] for x in range(1,len(b)-1))
print(sum(ascending_digits(str(i)) and same_digits(str(i)) for i in range(128392,643281)))
print(sum(ascending_digits(str(i)) and larger_group(str(i)) for i in range(128392,643281)))