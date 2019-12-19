#將input檔內容改寫後再輸出output檔
#寫讀取檔案function
#寫main function
#介紹None

import os
#讀檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:   #-sig:因為記事本第一行偷偷存了編碼資料('\ufeff)，我們不要它印出
        for line in f:
            lines.append(line.strip())  #.strip()去掉/n
    return lines

#格式轉換
def convert(lines):
    new = []
    person = None #可以宣告預設值是0
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:   #意思:如果person有值，才往下執行append。 因為person初始是None，為了避免第一個開頭內容沒有人名，會使person沒有值，導致錯誤
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w',encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')


#主要function
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt',lines)


#呼叫使用
main()