#dictionary 字典
#用大括號{}
#key:value配對
#都用key搜尋

#words = {'ramen': '拉麵','pasta': '義大利麵'}   可以一行式或是多行式，但要用','隔開
words = {
    'ramen': '拉麵',
    'pasta': '義大利麵'
}

words['tea'] = '茶'  #增加新的key

print(words['ramen'])
print(words['pasta'])
print(words)
#print(words['apple'])  #找不到此字典:KeyError: 'apple'


#list,dictionary混用
p0 = {
    'name': '麥香奶茶',
    'price': 10
}

p1 = {
    'name': '珍珠奶茶',
    'price': 60
}

drinks = [p0, p1]
print(drinks[0]['name'])  #查p0的name >'麥香奶茶'
print(drinks[1]['price']) #>60