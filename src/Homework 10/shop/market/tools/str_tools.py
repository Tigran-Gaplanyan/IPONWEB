#
import string
import random


#
def random_str(length, digit=True):
    if digit:
        return "".join(random.choice(string.digits) for _ in range(length))
    else:
        alphabet62 = string.digits + string.ascii_letters
        return "".join(random.choice(alphabet62) for _ in range(length))
