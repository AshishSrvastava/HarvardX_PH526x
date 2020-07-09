import random
def password(length):
    pw=str()
    characters='abcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(length):
        pw=pw+random.choice(characters)    
    return pw