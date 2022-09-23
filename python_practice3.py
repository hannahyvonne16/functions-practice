from math import factorial


def name_args(**kwargs):
    concatted = ""
    for i in kwargs.values():
        concatted += i
    return concatted

print(name_args(a="Am ", b="I ", c="doing ", d="this ", e="right?"))

def all_true(iterable):
    return all(iterable)

print(all_true((True,True,False)))
print(all_true((True,True,True)))

def one_true(iterable):
    return any(iterable)

print(one_true((True,True,False)))
print(one_true((True,False,False)))

def recursive_factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

print(recursive_factorial(3))

def recursive_deduplicate(string,i=0):
    if len(string) <= 1 or i == len(string)-1:
        return string
    else:
        if string[i] == string[i+1]:
            return recursive_deduplicate(string[0:i]+string[i+1:],i)
        else:
            return recursive_deduplicate(string,i+1)

print(recursive_deduplicate("book"))

def recursive_reverse(string, i=0):
  if len(string) == 0:
    return ""

  elif i == len(string)-1:
    return string[0]

  else:
    return string[-1-i] + recursive_reverse(string, i+1)

print(recursive_reverse("olleh"))