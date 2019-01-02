# for k in range(10):
#     if(k > 2):
#         break
        
#     print(k)

# for k in range(5):
#     if(k == 2):
#         continue

#     print(k)

# k = 0
# while True:
#     k = k +1

#     if k == 2:
#         print("continue next")
#         continue

#     if k > 4:
#         break

#     print(k)

# numbers = [1,2,3,4,5]
# square = []

# for i in numbers:
#     square.append(i**2)

# print(square)

numbers = [1,2,3,4,5]
square = [i**2 for i in numbers]
print(square)