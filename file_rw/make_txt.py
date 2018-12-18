# f = open("number.txt", "w", encoding = 'utf-8')
# for i in range(1,6):
#     data = f'{i}번째 줄입니다.\t'
#     f.write(data)
# f.close()

# with open("new.txt", "w", encoding = 'utf-8') as f:
#     for i in range(1,11):
#         data = f'{i}번째 줄입니다.\n'
#         f.write(data)


with open("number.txt", "r", encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
