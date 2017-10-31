class myclass:
    def __init__(self,realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = myclass(3.0, -4.5)
print (x.r, x.i)
x.j = 'I am 21 years old'
print x.j

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print "B"
    except C:
        print "C"
    except D:
        print "D"


for element in [1, 2, 3]:
    print element
for element in (1, 2, 3):
    print element
for key in {'one':1, 'two':2}:
    print key
for char in "123":
    print char

k = {'one':1, 'two':2}
print k