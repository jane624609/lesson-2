#class 類別(種類)
#dir 屬性
#寫class是在設計藍圖

#class寫法:
#class<class名稱>:
#    def__init__(self):
#    ....
#    def 其他func(self):
#    ....

class Student:
    def __init__(self, name, score) :  #init:initialize是指初始化 #初始化參數name，設完就設定屬性
        self.name = name #增加身上屬性
        self.score = score
        self.x = '5'

        print(name, '誕生了')
        self.do_hw('英文') #self表示自己，讓他知道這些功能在自己身上，才能在其他定義中運行
        self.study()#參數在沒寫的時候系S統會自動放入self
        self.sleep()

    def do_hw(self, hw): #假設有兩個參數，對應上面 self.do_hw('英文')，輸入的參數會自動當第二個參數，因為第一個已經被自動投self了
        print('我在做作業', hw)

    def study(self):
        print('我在讀書')
        self.score += 1

    def sleep(self):
        print('I am sleeping!')

s = Student('jane', 100) #因為init是原有的功能，所以在存成s時就會自動運行 #要對應init的name參數
s1 = Student('John', 95)
s.do_hw('國文') #因為do_hw是自己寫的py不認得，所以要寫這行，s運行你的do_hw()
s.study()
s.sleep()
print(s.name, s.score)
print(s1.name, s1.score)

s1.study()
print(s1.name, s1.score)

print(dir(s)) #印出身上屬性，確認是否有增加屬性成功

#self說明:
#1.使用self來存取自身上function
#2.使用self來增加身上的屬性(attributes)
#3.典型的初始化參數設計
#4.用同一個class來創作不同的物件
#5.桌子的範例