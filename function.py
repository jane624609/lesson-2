#function 函式/功能
#function是用來[收納]程式碼的
#它是個功能
#語法:  def函式名稱():
#         內容
#寫程式時盡力把程式碼都收在function裡，可以讓程式碼架構清楚，對於多次使用也比較便利

def wash():  #這裡只是定義有這功能不執行，wash是我發明的功能的名稱
    print('加水')
    print('加洗衣精')
    print('旋轉')

wash()  #使用function功能，就是打出功能名稱加()
wash()

def say_hi():
    print('hi!')

say_hi()

###########################################################
#parameter(參數)像是投幣孔   def ___(參數):
#當function需要外部資料的時候，我們就設計投幣孔(參數)，把資料投進去function裡(因為讓function去拿外面東西不好)
#如果function有投幣孔，就一定要投東西(除非有預設值)
def wash(dry, water = 8):
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')

wash(True,2) 
wash(False)   #因為參數是false，代入後不會出現烘衣



def add(x =0, y=3):  #參數可以有"預設值",那就不一定要投給他
    print(x + y)

add(3, 4)  
add(123, 2323)
add(y=5)#投東西給參數的時候可以"明確指定"要投到哪一個參數
add(2)#投東西的時候自動是按照參數的順序，所以會自動對到x


#return回傳，才可以把function的執行結果存下來
def add(x, y):
    return x + y
result = add(3, 4)  #return存到result
print(result)


def average(numbers):
    avg = sum(numbers) / len(numbers)
    return avg  
a = average([1, 2, 3])   #return的存到a
print(a)
#上方濃縮寫法
def average(numbers):
    return sum(numbers) / len(numbers)  
print(average([1, 2, 3]))
print(average([23, 32, 6]))
print(average([180, 34, 92]))

#判斷是不是閏年(二月會多一天的年)
#1.公元年分除以4不可整除,為平年
#2.公元年分除以4可整除但除以100不可整除,為閏年
#3.公元年分除以100可整除但除以400不可整除,為平年
#4.公元年分除以400可整除但除以3200不可整除,為間年
def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

#寫一個function來算出清單中數字的總數
#function底該要有一個参數讓使用者投入(停遞進去)一個清單,
#function底該回停(return)清單中數字的總數・
#請把function命名為sum_of_list),這樣才可以執行測試·(PS.sum就是總數的意思)
#預期結果:
#底該要印出6
print(sum_of_list([1, 2,3]))
def sum_of_list(numbers):
    return(sum(numbers))
print(sum_of_list([1, 2, 3]))