#!/usr/bin/env python3
import string

from random import *

chars = string.ascii_letters + string.punctuation + string.digits
passw = ''.join(choice(chars) for x in range(randint(8,16)))

print(passw)
