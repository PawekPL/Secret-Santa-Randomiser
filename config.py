import time
import random


people=['p1','p2','p3','p4']
emails = {'p1':'email@adress.com','p2':'email@adress.com','p3':'email@adress.com','p4':'email@adress.com'}


abcd = ['p1','p2','p3','p4']

def name_match(people=people,emails=emails,abcd=abcd):
    random.seed(time.ctime())
    cont = True
    out = []
    for p in people:
        sender = p
        s_email = emails[sender]
        receiver = abcd[random.randint(0,len(abcd)-1)]
        now = int(time.ctime()[18])
        while sender == receiver:
            receiver = abcd[random.randint(0,len(abcd)-1)]
            if int(time.ctime()[18])-now > 3 or int(time.ctime()[18])-now < -3:
                print('InfiniteLoopError: try running your code again')
                cont = False
                out = []
                break
        abcd.remove(receiver)
        out.append([receiver,s_email,sender])
    if cont:
        print('Assigning Santas Complete')
        return out
    else:
        raise ValueError

import string

def randpass(stringLength=12):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return str(''.join(random.choice(password_characters) for i in range(stringLength)))


if __name__ == '__main__':
    print(name_match())
    print(randpass()) 
