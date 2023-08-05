import random
import string as a

def generate_pass():
    c = random.randint(6, 10)
    d = a.ascii_lowercase
    e = a.ascii_uppercase
    f = a.digits
    g = random.choice(d) + random.choice(e) + random.choice(f)
    h = ''.join(random.choices(d + e + f, k=c - 3))
    i = list(g + h)
    random.shuffle(i)
    j = ''.join(i)
    return j

k = generate_pass()
print(k)
