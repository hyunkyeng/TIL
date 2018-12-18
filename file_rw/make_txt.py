# f = open("number.txt", "w", encoding = 'utf-8')
# for i in range(1,6):
#     data = f'{i}번째 줄입니다.\t'
#     f.write(data)
# f.close()

with open("number.txt", "w", encoding = 'utf-8') as f:
    for i in range(1,6):
        data = f'{i}번째 줄입니다.\t'
        f.write(data)
