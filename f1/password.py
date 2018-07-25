import re
import random
p=('hayk','Adfg@)5fg','jkf90*nhj', 'hgdj68j5','hydh7#Lhf','jy4j%788','hyfd786#K')


def check():
    q = random.choice(p)


    print q
    while(True):
        if q<4 and q>10:

            print('lenght')
            break

        elif not re.search('[a-z]',q):

            print('lower case')
            break
        elif not re.search('[A-Z]',q) :

            print('upper case')
            break
        elif not re.search('[0-9]',q):

            print ('number')
            break
        else:
            print ('password ok')
            break


check()