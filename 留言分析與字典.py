#留言分析程式續集
#讓使用者輸入要查的字，並顯示此字出現幾次
data = []
count = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1   #每一千筆讀一次
        if count % 1000 == 0:  # %是求餘數，count除1000餘數等於0
            print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料') #問清單長度

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


#文字計數
wc = {} #創新字典 word_count
for d in data:
    words = d.split(' ') #split預設其實也是空字串，所以可以寫split()
        for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增key進字典

for word in wc:
    if wc[word] > 1000000:
        print(word,wc[word])

print(len(wc))
print(wc['jane'])

while True:
    w = input('請輸入查詢文字: ') 
    if w == q:
        break
    if word in wc:
        print (w, '出現過的次數為', wc[w])
    else:
        print('這個字沒有出現過喔!')
print('感謝使用查詢功能')





































