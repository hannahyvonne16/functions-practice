def arb_args(*pokemon):
    for i in pokemon:
        print(i)

arb_args('Pikachu', 'Bulbasaur', 'Litwick')

def inner_func(integer1, integer2):
    def minus (inner_param) :
        return inner_param - 3
    def plus (inner_param) :
        return inner_param + 5
    new_value = minus(integer1) + plus(integer2)
    return new_value

print(inner_func(9,4))

def lunch_lady(student,lunch):
        if lunch == 0:
            print(f"{student} gets Mystery Meat.")
        else:
            print(f"{student} likes to eat {lunch}.")

lunch_lady("Bobby", "Potatoes")
lunch_lady("Fearne", 0)

def sum_n_product(integer1,integer2):
    sum = integer1 + integer2
    product = integer1 * integer2
    return sum, product 

print(sum_n_product(3,4))

alias_arb_args = arb_args

def arb_mean(*numbers):
    total = 0
    for i in numbers:
        total += i
    return i/len(numbers)

print(arb_mean(1,2,5,6,7,8,3,4,2,7))

def arb_longest_string(*numbers):
    short = 0
    longest = ""
    for i in numbers:
        if len(i) > short:
            short = len(i)
            longest = i
    return longest

print(arb_longest_string([3,5,6,5],[3,4,5,8,1,5],[4,9]))