#寫程式碼來讀取留言檔
#測試印出data清單
#只印出第0筆資料
#讀取檔案過程印出len(data)知道讀取進度
#計算留言平均長度
data = []
count = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
       #print(len(data))  一筆一筆印出目前讀到哪行
        count += 1   #每一千筆讀一次
        if count % 1000 == 0:  # %是求餘數，count除1000餘數等於0
            print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料') #問清單長度
#print(data)
print(data[0]) #印出第0個位置，就是第一個
print('----------')
print(data[1])

sum_len = 0
for d in data:     #計算留言平均長度
    sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))


#清單的篩選，找出小於100個字
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')        
print(new[0])  #印出第一筆

#清單的篩選，找出有good字的
good = []
for d in data:
    if 'good' in d:    #如果good有在裡面，裝進清單
        good.append(d)
print('一共有', len(good), '筆留言提到good')        
print(good[0])  #印出第一筆

#清單快寫法list comprehension，同等上面找good功能那四行
good = [d for d in data if 'good' in d]   #d是good.append(d)的d
good = [1 for d in data if 'good' in d]   #改成裝進去1 good.append(1)
#print(good)  這樣會出現兩萬多個1，因為只要有good就會把1放進去清單

#清單快寫，找出現bad的，用對錯方式顯示
bad = ['bad' in d for d in data]  #'bad' in d是一個運算，所以出來的只是true或是false，因此會print出一百萬筆對錯
print(bad)

#上方快寫的原始寫法
bad = []
for  d in data:
    bad.append('bad' in d)