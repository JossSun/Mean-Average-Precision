f1 = open("test-query.txt","r")
f2 = open("y_pred.txt","r")
f3 = open("c.txt","w")
line1 = f1.readline()
line2 = f2.readline()
num = 0
while 1:
        if line1:
                num +=1
                print "Line No.%d" %num
                line1 = line1.strip()
                line2 = line2.strip()
                f3.write(str(line1)+' ' +str(line2)+'\r\n')

        else:
                break
        line1 = f1.readline()
        line2 = f2.readline()
f1.close()
f2.close()
f3.close()
~               
