#coding=utf-8
import csv


print "Please input relevent number..."
rel = input()
# open every file for writing
lcount =0
result = 0
q = 0
j =0
while (j<12544) :
        str1 = str(j)
        ff = open(str1+".csv","r")
        reader = csv.reader(ff)
        rows = list(reader)
        rows.sort(key = lambda item: (item[2]))
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
                if int(val[4])<rel:
                        #print str(val[0])+','+str(val[1])+','+str(val[2])+','+str(val[3])+','+str(val[4])+'\r\n'
                        #print str(val[2])+'/'+str(count)+"\r\n"
                        result += float(val[2])/float(count)
                        #print "result mid is...%r" %result
                        count +=1
                #print str(val[0])+','+str(val[1])+','+str(val[2])+','+str(val[3])+','+str(val[4])+'\r\n'
        j+=1
print "q is ...%d" %q
result = result/rel/q
print "result is...%r" %result
print "line-count is...%r" %lcount
