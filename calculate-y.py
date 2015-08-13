import numpy as np

f2 = open("test.txt","r")
f1 = open("coef.txt","r")
f3 = open("y_pred.txt","w")
coef = []
con = f1.readline()
while 1:
        if con:
                coef.append(float(con))
        else:
                break
        con = f1.readline()
#print coef[0]

line = f2.readline()
lnum = 0
while 1:
        if line:
                lnum +=1
                print "line No.%d" %lnum
                line = line.strip()
                #print line
                val = line.split(' ')
                y = coef[0]
                i =0
                while (i<22):
                        print "val[i] is ...%r" % float(val[i])
                        y += float(val[i]) * coef[i+1]
                        i +=1
                print "y is ...%r" %y
                f3.write(str(y)+'\r\n')
        else:
                break
        line = f2.readline()

f1.close()
f2.close()
f3.close()
