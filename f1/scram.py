import random

f1 = open('scramble.txt', 'r')
f2 = open('new.txt', 'a')
s = f1.read()



def scramble(k):
    #k = k.strip(".")
    #k = k.strip("?")
    #k = k.strip(".")
    #k = k.strip(":")
    #k = k.strip("!")
    k = list(k)
    li = len(k)
    init = k[0]
    proc = ""
    m = li-1
    final = k[li-1]

    if li <= 3:
        return "".join(k)
    else:
        for v in range(li - 2):
            index = random.randint(1, (m - 1))
            proc = proc + k[index]
            k.pop(index)
            m -= 1
    return str(init+proc+final)

si = s.split(" ")

l = len(si)

for x in range(0, l):
    f = scramble(si[x])
    print f
    f2.write(f)
    f2.write(" ")
print "................."
print "Scramble Complete"
print "................."

f1.close()
f2.close()
