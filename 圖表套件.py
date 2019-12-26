#https://matplotlib.org/1.3.1/users/pyplot_tutorial.html

#直線圖
import matplotlib.pyplot as plt #一句套入套件並設入簡稱
plt.plot([1,2,3,4])#y值
plt.ylabel('some number')  #ylabel:Y的標示
plt.show()


#點圖
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], 'ro') #點的位置，ro是劃出紅點，沒寫就是預設藍線
plt.axis([0, 6, 0, 20]) #x軸跟y軸範圍
plt.show()


#長條圖
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
#plt.show()
plt.savefig('123.png')  #存圖，要存圖前面的plt.show()就要註解才存的下來