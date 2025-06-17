import random
def entr():
    pas=input("ENTER HERE THE PASSWORD: ")
    pas1=(encode(pas))
    return pas1
def encode(pas):
    alph="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*_"
    if len(pas) <=3:
        return pas[::-1]
    else:
        a=pas[0]
        pas=pas[1:len(pas)]
        pas= a+pas[::-1]
        b=random.choice(alph)
        return b+pas
def decode(cpas):
    if len(cpas) <=3:
        return cpas[::-1]
    else:
        cpas=cpas[1:len(cpas)]
        a=cpas[0]
        cpas=cpas[1:len(cpas)] +a
        return cpas[::-1]

