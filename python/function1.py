def product_of_numbers(*args):
    ans=1
    for x in args:
        ans=ans*x
    return ans
def raise_if_below_zero(num):
    if num<0:
        raise Exception("Below Zero")
    return num

def divide(n,d):
    try:
        return n/d
    except ZeroDivisionError:
        return 0

