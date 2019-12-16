#range 範圍
#python內建功能:清單產生器
#通常跟for搭配
#for i in range()的寫法目的是重複執行某固定次數

range(5)  #[0,1,2,3,4,] #5是結尾值，不包含，因為沒設定初始值，所以從0開始
range(3)  #[0,1,2]
#證實range3產出
for i in range(3):
    print(i)

for i in range(3):
    print('hi')

#隨機數
import random
for i in range(3):   #因為range是從0開始排序的，所以拉出來的i就是他的排序
    r = random.randint(1,1000)
    print('這是第', i + 1, '次產生隨機數: ', r)   #因為i從0開始，所以要加1


#range的三種用法:
#range(結束值)
#range(開始值, 結束值)
#range(開始值, 結束值, 遞增值)
range(2, 5)       #[2, 3, 4]
range(8, 10)      #[8, 9]
range(2, 10, 3)   #[2, 5, 8]從開始值開始，每次增加三，但不能超過跟包含結束值
range(3, 8, 2)    #[3, 5, 7]
range(10, 3, -2)  #[10, 8, 6, 4]
