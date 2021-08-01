def show_total(num):
    return "The total is {}".format(num)
    
def make_path(names):
    return "/".join(names)

def find_last_three_letters(word):
    if len(word)< 3:
        print"Error"
    else:
        return word[-3:]
    
def pluralize(word):
    if(word[-1] == 's'):
        return word
    else:
        return word + 's'

def capitalize(word):
    return word.capitalize()

def remove_the_letter(letter, word):
    splitt=word.split(letter)
    return "".join(word)

def mirror(word):
    return word+word[::-1]
    
def verbing(word):
    if((len(word)>=3) and (word[-3] != "ing")):
        return word+"ing"
    elif(len(word<3)):
        return word
    elif(word[-3:] == 'ing'):
        return word+"ly"

def is_palindrome(word):
    if(word == word[::-1]):
        return true 
    else:
        return false
# retun word == word[::-1]
def test(expect, actual):
    if expect == actual:
        print("   ok")
    else:
        print("     Oops! Got: {got}, Expected: {wanted}".format(got=repr(actual),wanted=repr(expect)))
def display(testname):
    print("++ {0} ++".format(testname))

if(_name_=='_main_'):
    display("print_total")
    test('The total is 4', show_total(4))
    display("make a path")
    test("a/b/c", make_path(["a","b","c"]))
    display("find_last_three_letters")
    test('hon',find_last_three_letters('python'))

    test('ERROr', find_last_tree_letters('I'))
    display("pluralize")
    test("crates", pluralize("crate"))
    test("ladies", pluralize("ladies"))

    display("capitalize")
    test("Hello", capitalize("hello"))

    display("remove_the_letter")
    test("tomoow", remove_the_letter("r", "tomorrow"))
    display("mirror")
    test("helloolleh", mirror("hello"))

    display("verbing")
    test("it", verbing("it"))
