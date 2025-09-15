import re
user = input ("Enter any sentence:")

x = re.split (r"\s", user)

y = len(x)
print (f"you have {y} number of words")




'''user = input ("Enter any sentence:")
words = user.split()
y = (len(words))
print (f"you have {y} number of words")'''
