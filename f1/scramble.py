import random
file=open('scramble.txt','r')
fil=open('new.txt','w')
#file.write('scramling words is very intersting.Because even if they are scrambled,it dosent impact our reading')

sent= file.read()






def shuff(z):
    if len(z)<=3:
        return z
    else:

        for i in z:
            new=' '
            first=i[0]
            last=i[len(i)-1]
            for a in range(1,len(i)-2):
                index=random.randint(1,len(i)-2)
                i=i[index]
                new=new+i
            w=first+ ' '.join(new)+last
            return(w)





def scram(sentence):
    sen=sentence.split()
    for word in sen:
        ls=list(word)
        shuff(ls)
    s=' '.join(ls)

    return s

scram(sent)



fil.write(scram(sent))
file.close()
fil.close()

