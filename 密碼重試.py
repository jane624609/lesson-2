#密碼輸入練習，若超過三次則強制結束
password = 'a123456' #先存正確密碼
x = 2
while True:
    pwd = input ('請輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break
    else:
        if x >= 1:
            print('密碼錯誤,還有', x,'次機會')
        else:
            print('密碼錯誤,還有', x, '次機會')
            break
        x = x - 1

#else那段可以再縮減
    #else:
        #i = i - 1
        #print('密碼錯誤,還有', x,'次機會')
        #if i == 0:
            #break
