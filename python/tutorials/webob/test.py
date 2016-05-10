class A(object):
    def __init__(self):
        print "class A"

    @classmethod
    def factory(cls):
        return cls()

class B(A):
    def __init__(self):
        super(B, self).__init__()
        pass

    def a():
        pass 

b = B()
print b
print type(b)
