import random
import string


for x in range(21):

    characters = string.letters + string.digits + string.punctuation

    random_character = random.choice(characters)

    random_bits = random.getrandbits(5)
    random_int = random.randrange(0, 12, 1)

    str_int = str(random_int)
    str_bits = str(random_bits)

    print("-----------------")
    print("Random Int: " + str_int)

    print("Extras:")

    print("Random Range: " + random_character)
    print("Random Bits: " + str_bits)
