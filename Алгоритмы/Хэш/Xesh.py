"""import string 
import random
q = 10
def A(x):
    x = random.choices(x)
    return x

x = string.ascii_letters + string.digits
print(A(x)) 
"""

import string
import random

def CreatePassword():
    dow = []
    a1 = string.digits
    a2 = string.ascii_uppercase
    a3 = string.ascii_lowercase
    for i in range (len(a2)):
        dow.append(a3[i])
    for i in range (len(a2)):
        dow.append(a2[i])
    for i in range(len(a1)):
      dow.append(a1[i])
    return random.sample(dow, len(q))
q = "Моя имя не станет больше или меньше со временем"
new = CreatePassword()
q = q.split()
A = dict(zip(new, q))
print(A)
