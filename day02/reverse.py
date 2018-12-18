with open('ssafy.txt','r',encoding='utf8') as f:
    lines=f.readlines() 

with open('ssafy_reverse.txt','w',encoding='utf8') as f:
    lines.reverse()
    f.writelines(lines)
