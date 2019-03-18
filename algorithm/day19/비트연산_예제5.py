# 비트 연산 예제5
# 비트연산자 ^를 두 번 연산하면 처음 값을 반환한다.

def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

    
for i in range(-5, 6):
    print("%3d = " %i, end='')
    Bbit_print(i)