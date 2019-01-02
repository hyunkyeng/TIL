# 파일 이름 변경하기

#import os
#바꾸고 싶은 파일 위치를 복붙해오기
#os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
#위랑 같은 위치에 있으므로 "." 으로 표기
#for filename in os.listdir("."):
#    os.rename(filename, "SAMSUNG " + filename)

# samsung이 아니라 ssafy로 변경하기
import os 
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename,filename.replace("SSAFY SSAFY","SSAFY"))