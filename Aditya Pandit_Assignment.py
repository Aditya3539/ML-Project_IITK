'''
import matplotlib.pyplot as plt
plt.plot([0,10,20,30,40,50],[0,30,60,90,120,150])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Draw a line.")
plt.show()
'''
from matplotlib.lines import lineStyles
from matplotlib.pyplot import yscale

'''
import matplotlib.pyplot as plt
plt.plot([1,2,3],[2,4,1])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sample graph!")
plt.axis([1,3,1,4])
plt.show()
'''
'''
import numpy
import matplotlib.pyplot as plt
plt.plot([1,2,3],[2,4,1])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sample graph!")
plt.axis([1,3,1,4])
plt.show()
'''
'''
import matplotlib.pyplot as plt
date= ["03", "04", "05", "06", "07"]
open= [774.25, 776.030029, 779.309998, 779, 779.659973]
high= [776.065002, 778.710022, 782.070007, 780.47998, 779.659973]
low= [769.5, 772.890015, 775.650024, 775.539978, 770.75]
close= [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
plt.plot(date, open, label='Open')
plt.plot(date, high, label='High')
plt.plot(date, low, label='Low')
plt.plot(date, close, label='Close')
plt.legend()
plt.show()
'''
'''
import matplotlib.pyplot as plt
plt.plot([10,20,30],[20,40,10],label='line 1')
plt.plot([10,20,30],[40,10,30],'g',label='line 2')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Two or more lines on same plot with suitable legends")
plt.legend()
plt.show()
'''
'''
import matplotlib.pyplot as plt
plt.plot([10,20,30],[20,40,10],label='line 1',linewidth=3)
plt.plot([10,20,30],[40,10,30],'r',label='line 2',linewidth=5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Two or more lines on same plot with suitable legends")
plt.legend()
plt.show()
'''
'''
import matplotlib.pyplot as plt
plt.plot([10,20,30],[20,40,10],'b:',label='line 1',linewidth=1)
plt.plot([10,20,30],[40,10,30],'r--',label='line 2',linewidth=2)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Two or more lines on same plot with different styles")
plt.legend()
plt.show()
'''
'''
import matplotlib.pyplot as plt
plt.plot([1,4,5,6,7],[2,6,3,6,3],marker='o',markerfacecolor='blue',markersize=10,label='line 1',linestyle='-.-',color='red')
plt.axis([1,8,1,8])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Display marker")
plt.show()
'''
'''
import matplotlib.pyplot as plt
plt.plot([0,10,20,30,40,50],[0,30,60,90,120,150])
plt.axis([0,100,0,200])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Draw a line.")
plt.show()
'''
'''
import matplotlib.pyplot as plt
x1=[2,3,5,6,8]
y1=[1,5,10,18,20]

x2=[3,4,6,7,9]
y2=[1,5,10,20,23]
plt.axis([0,10,0,30])
plt.scatter(x1,y1,marker='o',linewidth=0.5)
plt.scatter(x2,y2,marker='o',linewidth=3)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
'''
'''
import matplotlib.pyplot as plt
x1=[0,1,2,3,4,5]
y1=[1,2,3,4,5,6]

x2=[0,1,2,3,4,5]
y2=[1,2,4,6,8,10]

x3=[0,0.6,1.2,1.8,2.4,3.6,4.2,4.6,5]
y3=[1,2,15,25,35,50,65,80,110]
plt.axis([0,5,0,120])
plt.plot(x1,y1,'g--')
plt.scatter(x2,y2,marker='s')
plt.scatter(x3,y3,marker='^')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
'''
'''
import matplotlib.pyplot as plt
date=['2016-10-3','2016-10-04','2016-10-05','2016-10-06','2016-10-07']
x=[772.5,776.5,776.4,776.9,775.1]
#plt.axis([2016-10-3,2016-10-7,772.5,777.0])
plt.plot(date,x,marker='o',c='r')
plt.show()
'''
'''
import matplotlib.pyplot as plt
date=['2016-10-3','2016-10-04','2016-10-05','2016-10-06','2016-10-07']
x=[772.5,776.4,776.5,776.9,775.1]
plt.xlabel("Date")
plt.title("Closing stock value of Alphabet Inc.")
#plt.axis([date[0],date[4],772.5,777.0])
plt.plot(date,x,marker='o',c='r')
plt.grid(True,color='b')
plt.show()
'''

import matplotlib.pyplot as plt
date=['2016-10-3','2016-10-04','2016-10-05','2016-10-06','2016-10-07']
x=[772.5,776.4,776.5,776.9,775.1]
plt.xlabel("Date")
plt.title("Closing stock value of Alphabet Inc.")
#plt.axis([date[0],date[4],772.5,777.0])
plt.plot(date,x,marker='o',c='r')
yscale('log')
plt.minorticks_on()
plt.grid(True,color='r',linestyle='-',which='major')
plt.grid(True,color='r',linestyle='-',which='minor')
plt.show()