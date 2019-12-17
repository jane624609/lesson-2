#讀取檔案(將讀到的寫入)
#用strip移除換行符號\n
#用split(',')做逗點分割
#用continue使標題(商品，價格)避開不要也匯入，意思是直接跳過到下一回圈
products = []
with open('products.csv', 'r') as f:
    for line in f:
        if '商品,價格' in line:
            continue #繼續，這次迴圈不執行，直接跳到下一回
        name, price= line.strip().split(',')
        products.append([name, price])
print(products)

#記帳程式，讓使用者多次輸入購買品項
#二維度清單(清單內再裝清單)2 dimensional
products = []

while  True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格')
    #做小清單
    p = []    #從這往下三行可縮減成 p = [name, price]
    p.append(name)
    p.append(price)

    products.append(p) #或是p直接改products.append([name, price])
print (products )
#練習存取二維清單
print (products[0][0])  #第一個大清單裡的第一個(name)

#for loop搞清楚每個東西是甚麼
for p in products:
    print(p)  #所有大清單

for p in products:
    print(p[0])  #所有大清單的[0]

for p in products:
    print(p[0], '的價格是', p[1])  #所有大清單的第一個跟小清單的第二個位置

#字串可以做加乘，但減跟除不能
#但加法只能字串跟字串或整數跟整數，不能整數跟字串
#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

#寫入檔案一
with open('products.txt', 'w') as f: #open是打開檔案，沒有檔案會自己開一個，w是寫入模式，as f是當f
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') #\n是換行，f.write是真正的寫入
        #補充:如果前面price = int(price)  改成整數
        #最後write的p[1]要改成 str(p[1]) 改回字串，因為加法需要都同類型

#寫入檔案二，excel寫入欄位名稱+處理編碼問題
with open('products.csv', 'w', encoding='utf-8') as f: #txt可以改成csv，會用excel開  #encoding='utf-8'這可以讓輸入標題的中文字不要變亂碼
    f.write('商品,價格\n') #作法:在for前加入欄位名
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')#如果是存csv檔中間也要 +,+ 因為這可以讓他換格，不然會擠一起
