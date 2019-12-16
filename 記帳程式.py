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
products[0][0]  #第一個大清單裡的第一個(name)