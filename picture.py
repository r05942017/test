from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

data = pd.read_csv('train.csv',encoding='big5', usecols=lambda x: x not in ['日期','測站','測項'])

data=DataFrame(data)
#test=DataFrame(data[:18])
print(len(data))

datalenth=len(data)/18
AM_TEMP=data[0:18]

AM_TEMP=AM_TEMP.rename(index={0:'AMB_TEMP',1:'CH4',2:'CO',3:'NMHC',4:'NO',5:'NO2',6:'NOx',7:'O3',8:'PM10',9:'PM2.5',
						10:'RAINFALL',11:'RH',12:'SO2',13:'THC',14:'WD_HR',15:'WIND_DIREC',16:'WIND_SPEED',17:'WS_HR'})

for i in range(1,int(len(data)/18),1):      #把相同item排在同一列
	j=18*i
	buf=data[j:j+18]
	buf=buf.rename(index={j:'AMB_TEMP',j+1:'CH4',j+2:'CO',j+3:'NMHC',j+4:'NO',j+5:'NO2',j+6:'NOx',j+7:'O3',j+8:'PM10',j+9:'PM2.5',
						j+10:'RAINFALL',j+11:'RH',j+12:'SO2',j+13:'THC',j+14:'WD_HR',j+15:'WIND_DIREC',j+16:'WIND_SPEED',j+17:'WS_HR'})
	AM_TEMP = pd.concat([AM_TEMP,buf],axis=1,ignore_index=True)


AM_TEMP=AM_TEMP.T   #矩陣旋轉

for i in range(0,int(len(AM_TEMP)),1):   #change NR to 0
	if AM_TEMP['RAINFALL'][i]=='NR':
		AM_TEMP['RAINFALL'][i]=0
#------------------------------------------------------------------

num=9
n=1
#y=b+wx
AM_TEMP=AM_TEMP.apply(pd.to_numeric)    #str to float

y_correct=DataFrame()
for cor in range(12):				#get y_correct
	if cor==0:
		y_correct=AM_TEMP['PM2.5'][num:480]
		#print('che')
	else:
		y_correct=y_correct.append( AM_TEMP['PM2.5'][cor*480+num:(cor+1)*480], ignore_index=True)
#	print('ylen=',len(y_correct),'cor=',cor)
print(y_correct)	
y_test=DataFrame()
item='PM2.5'
for cor in range(12):				#get y_correct
	if cor==0:
		y_test=AM_TEMP[item][num-n:480-n]

		#print('che')
	else:
		y_test=y_test.append( AM_TEMP[item][cor*480+num-n:(cor+1)*480-n], ignore_index=True)
#	print('ylen=',len(y_correct),'cor=',cor)
print(y_test)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.scatter(y_test,y_correct)

ax.set_title('first scatter plot')
ax.set_xlabel(item)
ax.set_ylabel('PM2.5')

plt.show()