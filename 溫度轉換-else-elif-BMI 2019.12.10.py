#溫度轉換練習
c = input ('請輸入攝氏溫度: ')
c = float(c)  #溫度可能會有小數點，所以設浮點數
f = c * 9 / 5 + 32
print ('華氏溫度為: ', f, '度')


#else否則
age = input('請輸入年齡: ')
age = int(age)
if age >= 20:
    print('你可以投票')
else:
    print('你還不能投票喔!')


#else if另外如果
age = input('請輸入年齡')
age = int(age)
if age < 13:
    print('國小')
elif age >= 13 and age < 18:  #and串接，只而且
    print('國高中')
elif age >= 18 and age < 22:
    print('大學')
else:
    print('社會')


#練習計算BMI
kg = input ('請輸入體重(公斤): ')
kg = float(kg)
hight = input ('請輸入身高(公分): ')
hight = float(hight)
hight = hight /100  #換成公尺
bmi = kg / hight / hight

if bmi < 18.5:
    print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('體重正常')
elif bmi >= 24 and bmi < 27:
    print('過重')
elif bmi >= 27 and bmi < 30:
    print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('中度肥胖')
else:
    print('重度肥胖')
