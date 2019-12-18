#1.全部寫成function
#2.調整read_file() function //把需要往外拿的東西設成參數
#3.調整user_input() function
#4.調整print_products() function
#5.調整write_file() function


#檢查要讀取的檔案是否存在
import os  #import是載入，os是operating system作業系統

#讀取檔案檢查檔案是否存在
def read_file(filename):
    products = []
    if os.path.isfile(filename):   #檔名設成參數
        print('yeha! 找到檔案了!')
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if '商品,價格' in line:
                    continue #繼續
                name, price= line.strip().split(',')
                products.append([name, price])
        print(products)
    else:
        print('找不到檔案....')
    return products
#讓使用者輸入
def user_input(pppp2):
    while  True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格')
        price = int (price)
        pppp2.append([name, price])
    print (pppp2 )
    return pppp2

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f: 
        f.write('商品,價格\n') 
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')


#使用
products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)