#讀取檔案
with open('food.txt', 'r') as f:  
#with-當你open占用了檔案，過往需要再closs，如果忘記沒做這步，中間程式有錯誤導致中斷，會導致檔案損毀，用這方式他會在離開with架構，檔案會自動關閉
#open打開某檔
#r是讀取模式，若要寫入模式為w
#as意思是當作，將此檔當作f簡稱
    for line in f:   #for迴圈讀取f檔案，每一行都取名為line
        print(line)  #一行一行印出，但印出時 會發現中間都會隔一行，因為在做txt時有打ent鍵，資料會偷偷存一個/n換行，for迴圈本身也會自動換行，所以有兩層換行


#驗證上方有雙重換行，增加一個清單列出內容
data = []#空清單
with open('food.txt', 'r') as f:
    for line in f:
        data.append(line)
print(data)


#去掉換行符號
data = []   #空清單
with open('food.txt', 'r') as f:
    for line in f:
        data.append(line.strip())  #strip可以對字串去掉換行跟空白的功能
print(data)

