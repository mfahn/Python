class person:
    def __init__(self,fn,ln):
        self.fn=fn
        self.ln=ln
        self.address=[]
    def add_address.append(self, name):
        self.address.append(name)
    def fullname(self):
        return "fullname: {}, {}".format(self.ln, self.fn)
    def __str__(self):
        return "THIS IS MY OBJECT"

if __name__=='__main__':
    p=person('dave', 'bryson')
    print(p)
