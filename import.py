#產生1~100隨機數
import random #插入隨機功能
r = random.randint(1, 1) # . 是指的，randint是random跟int結合
print(r)


#猜數字遊戲
#產生一個隨機整數數字範圍給使用者設定(不要印出)
#讓使用者重複輸入數字去猜
#猜對的話 印出 "終於猜對了!"
#猜錯的話 要告訴他 比答案大/小
#印出猜了第幾次

import random
small = input('請輸入範圍開始值')
large = input('請輸入範圍結束值')
small = int(small)
large = int(large)
r = random.randint(small,large)

count = 0
while True:
    count += 1 #等於count = count + 1
    answer = input('請猜數字: ')
    answer = int(answer)
    if answer == r:
        print('終於猜對了')
        print('這是你猜的第', count, '次')
        break
    else:
        if answer > r:
            print('比答案大')
        else:
            print('比答案小')
    print('這是你猜的第', count, '次')