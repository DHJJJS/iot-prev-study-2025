# py11_file_inout.py - 파일 입출력

# 쓰기
# a(추가), r(읽기), w(쓰기)
f = open('./day02/textfile.txt', mode='a', encoding='utf-8')
# 아무것도 안함
f.write('저는 한국사람입니다.\n')
f.write('남자입니다.\n')
f.close()

print('텍스트파일이 생성되었습니다.')

## 읽기
f = open('./day02/textfile.txt', mode='r', encoding='utf-8')

while True: # 무한반복 
    line = f.readline() # 한줄씩 읽고
    if not line: break # 읽을 줄이 없으면 반복문 탈출

    print(line)

f.close()
