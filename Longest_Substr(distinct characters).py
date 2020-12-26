def LongSubstr(st):
    if len(st)==0:
        return 0
    max_lst=[]
    s=set()
    # s={} this notation creates an empty dictionary
    # Be cautious of sets and dict
    for word in st:
        s.add(word)
    for i in  range(0,len(st)-len(s)):
        x=set()
        x.update(st[i:i+len(s)])
        max_lst.append(len(x))
    return max(max_lst)
print(LongSubstr('abcdabc'))
print(LongSubstr(''))
print(LongSubstr('aaanbfdfedd'))
# time complexity of O(n)
