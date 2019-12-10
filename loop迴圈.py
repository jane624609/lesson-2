#loop迴圈 -while
x = 5
while x < 10:
    print ('x小於10喔!')
    print('我還困在框框裡')
    x = x + 1 #當不小於就會停止迴圈

print('我逃出迴圈了')


#break
x = 5
while True:#因為永遠是true，迴圈會無限下去
    print ('x小於10喔!')
    print('我還困在框框裡')
    break #強制跳出迴圈來終止
print('我逃出迴圈了')


#遊戲模式選擇
while True:
    mode = input('請輸入遊戲模式: ')
    if mode == 'q': #quit
        break #只有寫這才會離開
    elif mode == '1':  #因為input是字串，所以這也是用字串做比較
        print('啟動模式一')
    elif mode == '2':
        print('啟動模式二')
    else:
        print('只能輸入 1/2/q')
