import numpy as np
import math
import pandas as pd
from sklearn import metrics

f3 = open("fast-data-with-info.csv","r")
f2 = open("train.txt","w")
f6 = open("test.txt","w")
f7 = open("test-query.txt","w")
line = f3.readline()
linenum = 0
print "Please input the feature number..."
num = input()
while 1 :
	if line :
		linenum +=1
		print "Line No.%d" %linenum
		line = line.strip()
	        con = line.split(',')
		s = 1/float(con[4])	
		#n = pow(s,-1)-1
	        #if n<=0 :
		#	pass
		#else :
		#	m  = math.log(n)
		#	num0 = (-1/0.5) *m 
			
		num1 = float(con[2])
		num2 = 1/float(con[3])
		if linenum<1000000:
			f2.write(str(s))
		else:
			
			f7.write(con[0]+' '+str(con[4])+'\r\n')
		i =1
		while (i<=num) :
			tmp1 = pow(num1,i)
			tmp2 = pow(num2,i)
			if linenum<1000000:
				f2.write(' '+str(tmp1)+' '+str(tmp2))
			else:
				f6.write(' '+str(tmp1)+' '+str(tmp2))
			i +=1
		if linenum<1000000:
			f2.write('\r\n')
		else:
			f6.write('\r\n')
			
 
	else :
		break
	line = f3.readline()

f2.close()
f3.close()
f6.close()
f7.close()


#start to regression
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

#Load in train data
f1 = open("train.txt","r")
f4 = open("test.txt","r")
f5 = open("result.txt","w")

data = np.loadtxt(f1)
X_train = data[:,1:] #load in colomn 1 and colomn 2
y_train = data[:,0]
print "load in train data successfully!"

da = np.loadtxt(f4)
X_test = da[:,1:]
y_test = da[:,0]
print "load in test data successfully!"

#Fit in the model
linreg = LinearRegression()
linreg.fit(X_train,y_train)

print linreg.intercept_
print linreg.coef_

f1.close()
f4.close()
f5.close()
