import matplotlib.pyplot as plt                   #o:Dots       ,-:Contineous Line         ,--:Dashed Line     ,s:Square Block     ,: :Dotted Line
plt.plot([1,2,3,4],[1,4,9,16],'g1:')        #g- :Green Solid Line
plt.xlabel("------Some Numbers------>")           #ro- :Red Circle Dot
plt.ylabel("------Squared Values------>")
plt.axis([-3,5,0,17])
plt.show()