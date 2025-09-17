import random
import string 

length = 10
chars = string.ascii_letters + string.digits + string.punctuation

randomstring = "".join(random.choice(chars) for i in range (length))
print (randomstring)
