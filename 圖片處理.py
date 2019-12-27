#資料夾所有照片變黑白
#os.path.join用法

from PIL import Image
import os


for file in os.listdir('orig'): #如果設('.')是指檔案位置相同，現在('origo')是目前位置裡的origo資料夾
    if file.endswith('.png'):  #找出png圖檔
        image_file = Image.open('orig/' + file) #'orig/'要注意，因為圖檔位置跟程式位置不同，會抓不到，所以這裡也要給路徑
        #上面這段也可以改成
        #image_file = Image.open(os.path.join('orig', file))
        image_file = image_file.convert('L')#1是指轉黑白，L也可以，但它畫質較好
        image_file.save('result/' + file[:-4] + '_grey.png')  #file[:-4]是要除掉最後的.png才不會重複出現 #存檔位置指定資料夾也要打上路徑'result/'
