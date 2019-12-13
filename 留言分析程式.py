#寫程式碼來讀取留言檔
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
       #print(len(data))  一筆一筆印出目前讀到哪行
        count += 1   #每一千筆讀一次
        if count % 1000 == 0:  # %是求餘數，count除1000餘數等於0
            print(len(data))
            
print(len(data)) #問清單長度
#print(data)
print(data[0]) #印出第0個位置，就是第一個
print('----------')
print(data[1])