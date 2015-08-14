
##################################    Split file by query    ##############################
#coding=utf-8
import csv
qlist = {}
num = 0

f1 = open("qincommon.csv", "r")
rf1 = csv.reader(f1)
for line in rf1 :
        qlist[line[0]] = num
        print "Query list is adding... %d" %num
        num +=1
print "$$$$$$$$$$$$$    finished step one !!!    $$$$$$$$$$$$$$$$$$$$$$$"
f2 = open("fast-data-with-info.csv","r")
print "fast-data-with-info.csv is open !!"
line2 = f2.readline()

# open every file for writing
j =0
ff = []
while (j<num) :
        str1 = str(j)
        ff.append(open(str1+".csv","w"))
        j+=1
print "$$$$$$$$$$$$    every file for writing is open!!!    $$$$$$$$$$$$$$$$$$$$$$$"


linelist =[]
linecount =0
while 1 :
        if line2 :
                line2 = line2.strip()
                linelist = line2.split(',')
                query =','.join(line2.split(',')[:-4])
                print "query is : %s" % query
                if query in qlist :
                        print query
                        ff[qlist[query]].write(query+','+linelist[1]+','+linelist[2]+','+linelist[3]+','+linelist[4]+'\r\n')
                        print query+','+linelist[1]+','+linelist[2]+','+linelist[3]+','+linelist[4]+'\r\n'
        else :
                break
        line2 = f2.readline()
        linecount +=1
        print "Dealing with line: %d" %linecount

# Close every open file
f1.close()
f2.close()
j =0
while(j<num) :
        ff[j] .close()
        j+=1

###############################      calculate MAP from the split files       ##############################
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
