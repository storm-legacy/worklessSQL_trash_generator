import random
from dataHandler import *


def rand_name():
    return names[int(random.random()*len(names)-1)]

def rand_surname():
    return surnames[int(random.random()*len(surnames)-1)]

def rand_city():
    return cities[int(random.random()*len(cities)-1)]

def rand_nationality():
    return nationalities[int(random.random()*len(nationalities)-1)]

def rand_country():
    return countries[int(random.random()*len(countries)-1)]

def rand_currency():
    return currencies[int(random.random()*len(currencies)-1)]

def rand_productName():
    return products_names[int(random.random()*len(products_names)-1)]

def rand_age():
    return random.randrange(16, 110)

def rand_number ( amount ):
    number = 0
    j = 1
    for _ in range(0, amount-1):
        number = number + random.randrange(10)*j
        j *= 10
    number = number + random.randrange(1,10)*j
    return number

def rand_postCode ():
    nums = [0,0,0,0,0]
    for i in range(0, 5):
        nums[i] = str(random.randrange(10))
    return nums[0] + nums[1] + "-" + nums[2] + nums[3] + nums[4]
    

def rand_string ( amount ):
    result = ""
    for _ in range(0, amount):
        if random.randrange(0,2) == True:
            result += alphabet[int(random.random()*len(alphabet)-1)]
        else:
            result += str(random.randrange(0,10))
    return result
    
def rand_email ():
    return rand_string(random.randrange(6,15)) + "@" + domains[int(random.random()*len(domains)-1)]

