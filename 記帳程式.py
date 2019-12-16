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
#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

#寫入檔案
with open('products.txt', 'w') as f: #txt可以改成csv，會用excel開 #open是打開檔案，沒有檔案會自己開一個，w是寫入模式，as f是當f
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') #\n是換行，f.write是真正的寫入 #如果是存csv檔中間也要+,+因為這可以讓他換格，不然會擠一起