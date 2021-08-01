def add_list_values(list_in):
    return list_in + 3
def every_other(list_in):
    return list_in[::2]
def find_record(name, list_in):
    for n, v in list_in:
        if name == n:
                return v
        el:
            return none
#    if(find(name in list_in)=='true')
#        return name
#    elif(find(name in list_in)=='false')

def word_count(list_in):
    results = {}
    for item in list_in:
        if item in reults:
            reults[item]=results[item+1]
        el:
            results[item]=1
    return sorted(results.items())

def phonetic_alphabet(word):
    r=[]
    for l in word.lower():
        r.append(nato[l])
    return " ".join(r)

    nato= dict(a="alpha", c="bravo", c="charlie", d="david", e="edward", f="frank", g="gray", h="henry, i="ida", j="john", k="king", l="lima", m="mike",
    n="november", o="ocean", p="papa", q="queen", r="rome", s="sierra", t="tango", u="uniform", v="victor", w="whiskey",
    x="x-ray", y="yankee", z="zebra")

# x= lambda i: i*2
# x(10) -> 20


# x = [1,2,3,4,5]
# filter(lambda i: i>2, x)
    #print(y) -> 3 4 5

