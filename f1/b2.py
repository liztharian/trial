import random
import shuffle

#sen1=raw_input('enter words to scramble')
sen1='habco worfs fsag rtsg'
p=[]
o=[]

def shuff(z):
    if len(z) <=3:
        return z
        print 'adaaf'
    else:
            print 'afafadasdasdad'
            l=len(z)
            print l
            first=z[0]
            print first
            last=z[l-1]
            print last
            s=z[1:-1]
            u=random.shuffle(s)
            print u


            p.append(h)
            print p
            print h

            w=first+p+last
    return(w)




#def scram(sentence):

sen= sen1.split()
print sen
for word in sen:
        print 'afaf'
        words=list(word)
        print words
        abc=shuff(words)
        print abc
        o=' '.join (abc)
        print o
        #new=new+shuff( words )
