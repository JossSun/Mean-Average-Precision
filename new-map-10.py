#coding=utf-8
import csv
f1 = open("map-10.txt","a")
lcount =0
result = 0
q = 0
j =0
rel = input()
filecount = 0
while (j<12544) :
        str1 = str(j)
        ff = open(str1+".csv","r")
        reader = csv.reader(ff)
        rows = list(reader)
        rows.sort(key = lambda item:(int(item[1])))
        i = 1
        for ele in rows:
                ele[1] = i
        #       print ele
                i +=1
        print "This is file No.%d" %j
        if i < 500:
                j+=1
                continue
        filecount +=1
        rows.sort(key = lambda item: (float(item[2])) ,reverse=1)

        if rows:
                q +=1
        #       print "Dealing with file...%r" %q
        num = 1
        count = 1
        for val in rows:
                lcount +=1
                val[2] = num
                num +=1
                #print val
                if int(val[1])< rel:
                        #print str(val[1])+'/'+str(val[2])+"\r\n"
                        result += float(val[1])/float(val[2])
                        count +=1
        j+=1
print "total dealed file number is...%r" %filecount
print "q is ...%d" %q
result = result/rel/q
f1.write('rel ='+str(rel)+'\r\n')
f1.write('result is...'+str(result)+'\r\n')
print "result is...%r" %result
print "line-count is...%r" %lcount
