#coding=utf-8
import csv
f1 = open("rel.txt","w")
print "Please input relevent number..."
rel = input()
lcount =0
result = 0
q = 0
j =0
while (j<12544) :
        str1 = str(j)
        ff = open(str1+".csv","r")
        reader = csv.reader(ff)
        rows = list(reader)
        rows.sort(key = lambda item:(int(item[1])))
        i = 1
        for ele in rows:
                ele[1] = i
                print ele
                i +=1
        f1.write(str(i)+'\r\n')
        rows.sort(key = lambda item: (float(item[2])) ,reverse=1)
        print "This is file No.%d" %j
        #print rows
        if rows:
                q +=1
                print "Dealing with file...%r" %q
        num = 1
        count = 1
        for val in rows:
                lcount +=1
                val[2] = num
                num +=1
                if int(val[1])<rel:
                        #print str(val[0])+','+str(val[1])+','+str(val[2])+','+str(val[3])+','+str(val[4])+'\r\n'
                        print str(val[1])+'/'+str(val[2])+"\r\n"
                        result += float(val[1])/float(val[2])
                        #print "result mid is...%r" %result
                        count +=1
                #print str(val[0])+','+str(val[1])+','+str(val[2])+','+str(val[3])+','+str(val[4])+'\r\n'
        j+=1
print "q is ...%d" %q
result = result/rel/q
print "result is...%r" %result
print "line-count is...%r" %lcount
f1.close()



f1 = open("rel.txt","r")
rel = set([1])
line = f1.readline()
while 1:
        if line:
                line.strip()
                rel.add(int(line))
        else:
                break
        line = f1.readline()
l = list(rel)
l.sort()
print "min is...%r" %l[1]
print "max is...%r" %l[len(l)-1]
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
for val in l:
        if val<100:
                count1+=1
        elif val<200:
                count2+=1
        elif val<300:
                count3+=1
        elif val<400:
                count4+=1
        elif val<500:
                count5+=1
print "data less than 100...%r" %count1
print "data 100 < x < 200...%r" %count2
print "data 200 < x < 300...%r" %count3
print "data 300 < x < 400...%r" %count4
print "data 400 < x < 500...%r" %count5
f1.close()
