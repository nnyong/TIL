with open('ssafy.txt','r',encoding='utf8') as f:
    lines=f.readlines() #모든 라인 가져와서 list로 반환
    #print(lines)
    for line in lines:
        print(line.strip()) #strip하면 개행문자를 없애주는 역할