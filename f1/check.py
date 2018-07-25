import random
file=open('scramble.txt','r')
fil=open('new.txt','w')
#file.write('scramling words is very intersting.Because even if they are scrambled,it dosent impact our reading')
p=[]
o=[]
sent= file.read()

new=' '

#sent=('hello how are you')



def shuff(z):
    if len(z)<=3:
        return z
    else:

        for i in z:

            first=i[0]
            last=i[len(i)-1]
            s=i[1:-1]

            h=random.shuffle(s)
            o.append(h)
            print p,h

            w=first+ p+last
            return(w)




def scram(sentence):


    sen=sentence.split()
    for word in sen:
        words=list(word)

        new=new+shuff(words)

    print new

    #return s
scram(sent)



fil.write(scram(sent))
file.close()
fil.close()
