import os

os.chdir(r'C:\Users\student\nnyong\day02\dummy')
#print(os.getcwd())
for filename in os.listdir('.'):
    #os.rename(filename,f'지원자_{filename}')


#합격자_0_이름.txt로 변경
    os.rename(filename,filename.replace('지원자','합격자'))
    #new_filename=filename.replace('지원자','합격자')
    #os.raname(filename,new_filename)
