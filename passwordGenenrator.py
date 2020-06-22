import random

english_lower="abcdefghijkmnopqrstuvwxyz"
english_upper="ABCDEFGHIJKMNOPQRSTUVWXYZ"
number_code="0123456789"

all=english_lower+english_upper+number_code
lenght=18
password="".join(random.sample(all,lenght))

print("The new password is %x" % password)
