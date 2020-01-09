#class桌子範例

class Desk: #class第一個字大寫
    def __init__(self, color):
        self.color = color
        print('我被製造出來了')

    def re_color(self,new_color):
        self.color = new_color

d = Desk('Blue') #instantiation 實體化(創作出物件)
d.re_color('red')
print(d.color)