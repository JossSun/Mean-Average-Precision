#coding=utf-8
import csv
f1 = open("map-score.txt","a")

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
        rows.sort(key = lambda item:(int(item[4])))
        i = 1
        for ele in rows:
                ele[4] = i
                i +=1
                print ele
        print "Dealing with file No.%d" %j
        if i<500:
                j +=1
                continue
        rows.sort(key = lambda item: (float(item[2])) , reverse = 1)
        if rows:
                q +=1
        num = 1
        count = 1
        for val in rows:
                lcount +=1
                val[2] = num
                num +=1
                if int(val[4])<rel:
                        print str(val[4])+'/'+str(val[2])+"\r\n"
                        result += float(val[4])/float(val[2])
                        count +=1
        j+=1
print "q is ...%d" %q
result = result/rel/q
print "result is...%r" %result
f1.write('rel ='+str(rel)+'\r\n')
f1.write('result is...'+str(result)+'\r\n')
print "line-count is...%r" %lcount

f1.close()
