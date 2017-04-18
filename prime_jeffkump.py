import math
def get_primes(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append(element)

    return result_list
# or better yet...
#def get_primes(input_list):
#    return (element for element in input_list if is_prime(element))
# not germane to the example, but here's a possible implementation of
# is_prime...
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3,int(math.sqrt(number))+1,2):
            print current  
            if number % current == 0: 
                return False
        return True
    return False
l = get_primes([1,2,3,4,9])
print l 
