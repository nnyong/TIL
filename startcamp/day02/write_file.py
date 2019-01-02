# f=open('ssafy.txt','w') #w: write, r: read, a: append
# f.write('This is SSAFY')
# f.close() #꼭 넣어줘야 함. 정상적으로 종료

with open('ssafy.txt','w',encoding='utf8') as f:
    f.writelines(['1\n','2\n','3\n'])
    # for i in range(10):
    #     f.write(f'This is \\ \'SSAFY\'! {i}\n')
    # #f.write('This is SSAFY!, with 이용했다.')
    # # \t: tab, \\: '\' 문자, \' & \" : 따옴표, 쌍따옴표 문자