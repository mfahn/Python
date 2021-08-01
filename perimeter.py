import math

def rectangle(len, wide):
    return (2*len)+(2*wide)

def square(side):
    return (4*side)

def circle(diameter):
    return (math.pi*diameter)

if __name__=='__main__':
    c=circle(3)
    print(c)