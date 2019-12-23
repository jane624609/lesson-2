#將input檔內容改寫後再輸出output檔
#計算字數
#計算圖片數
#計算貼圖數

import os
#讀檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:   #-sig:因為記事本第一行偷偷存了編碼資料('\ufeff)，我們不要它印出
        for line in f:
            lines.append(line.strip())  #.strip()去掉/n
    return lines

#格式轉換
#判斷對話者各講幾格字
#清單的分割: n[開始值:結束值]  (開始有包含，結束不包含)
#EX:n[:3] 可以拿到前三個(開始值0可以不寫)
#EX:n[2:4] 可以一個清單裝著n[2]跟n[3]
#EX:n[-2:] 可以拿到最後兩個,(結尾值不寫表示到底)



def convert(lines):
    person = None #可以宣告預設值是0
    allen_word_cound = 0  #計算字數，0起始
    viki_word_cound = 0
    allen_sticker_cound = 0
    viki_sticker_cound = 0
    allen_image_cound = 0
    viki_image_cound = 0

    for line in lines:
        s = line.split(' ') #切割
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_cound += 1
            elif s[2] == '圖片':
                allen_image_cound += 1
            else:
                for msg in s[2:]: #不是貼圖，做文字記數
                    allen_word_cound += len(msg)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_cound += 1
            elif s[2] == '圖片':
                viki_image_cound += 1
            else:
                for msg in s[2:]:
                    viki_word_cound += len(msg)

    print('allen說了', allen_word_cound, '個字', '傳了:', allen_sticker_cound, '個貼圖', allen_image_cound, '個圖片')
    print('Viki說了', viki_word_cound, '個字', '傳了:', viki_sticker_cound, '個貼圖', viki_image_cound, '個圖片')

def write_file(filename, lines):
    with open(filename, 'w',encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')

#主要function
def main():
    lines = read_file('-LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt',lines)

#呼叫使用
main()