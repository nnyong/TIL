import csv

with open('lunch.csv','r',encoding='utf8') as f:
    #lines=f.readlines()
    items=csv.reader(f)
    for item in items:
        print(item)
        #print(line.strip().split(',')) #split 리스트형태로 나옴. strip: 개행문자 제거
        