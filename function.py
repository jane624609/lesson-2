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
wash()

def say_hi():
    print('hi!')
    
say_hi()