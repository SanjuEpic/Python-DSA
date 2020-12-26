# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("************ Welcome to Sets *************")
string='hello_all'
S=set()
for word in string:
    S.add(word)
print("# for finding unique elements in a set from given string 'hello_all'")
print(S)
print('--------------------------------------------------------')
X=set(['abcd', 'efgh','ijkl','mnop','qrstuv'])
print('# update is used for adding multiple items')
print('# add for single element')
X.update(['wxyz','ab', 'cdf'])
X.add(123)
print(X)
print('\n# for discard there wont be any error thrown simply returns the same dictionary')
print(X.discard('wx'))
print('# when used remove it throws an error if no element is present')
try:
    X.remove('wxz')
except:
    print('# There was an error while using remove')
    
print('\n# Union for two sets')
s1=set([1,2, 3,45, 6978, 362])
s2=set(['str',(1,2,3), 1,3, 689, 129])
print(s1.union(s2))
print('\n# Intersection of two sets')
print('# we can use s.intersection(s1) or s & s1 too and | for union')
print(s1.intersection(s2)) 
print('# loop iteration is possible on sets too!')
for item in X:
    print(item, end='\t')
print('\n************ THE END! ************')
