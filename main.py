# Made by Relic374
# Version 0.3

import random
import string

print("How many times should the random number be given?:")
cycle_amount = input()

cycle_amount = int(cycle_amount)


for x in range(cycle_amount):    
    characters = string.letters + string.digits + string.punctuation

    random_character = random.choice(characters)
    
    print("How many times should the random number be given?:")
    cycle_amount = input()

    cycle_amount = int(cycle_amount)
    
    random_bits = random.getrandbits(5)
    random_int = random.randrange(0, 12, 1)

    str_int = str(random_int)
    str_bits = str(random_bits)

    print("-----------------")
    print("Random Int: " + str_int)

    print("Extras:")

    print("Random Range: " + random_character)
    print("Random Bits: " + str_bits)
