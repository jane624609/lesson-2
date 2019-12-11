#list 清單
#清單符號是中括號
#可以混裝不同資料型別  
a = ['Toyota' , 'Honda',1122,True]  #[]內的內容叫索引index，開頭是0123順序下去
print(a)
print(a[0]) #印出a車的第0車廂
print(a[1])

a.append('Audi') #把奧迪裝入清單
print(a)

print (len(a)) #調出長度length
print('Audi' in a) #是非題 True,False,問奧迪有沒有在a裡，用in問
print('Benz' in a) #in後接清單