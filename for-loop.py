#for loop
#意思是把清單中的東西一個一個取出
cars = ['Toyota', 'Honda']

for car in cars: #car為將取出的物都暫時取名為car，cars是指定的清單，清單有幾個東西就會走幾回
    print(car) #上面暫時取名的car印出


#練習人名
names =['Allen', 'Tom', 'Jack']
for name in names:
    print(name)


#寫一個for loop來跟student清單的每一個人名說嗨
students = ['Allen', 'Tom', 'Mayday', 'JJ', 'Jolin', 'Jay', 'Jam']
for student in students:
    print('Hi', student)


#字串可當清單
car = 'Audi'  #['A', 'u', 'd', 'i']
for  c in car:
    print(c)
print(len(car))
print('A' in car) #檢查有無在裡面
print('x' in car)
print('Au' in car)
print('Ai' in car) #false
