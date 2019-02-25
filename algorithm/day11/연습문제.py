# Q. 큐를 구현하여 다음 동작을 확인. 세 개의 데이터를 1, 2, 3을 차례로 큐에 삽입하고,
# 큐에서 세개의 데이터를 차례로 꺼내서 출력 (1, 2, 3)

size = 100
Q = [0]*size
front, rear = -1, -1

print(Q)

def isFull():
    global rear
    return rear == len(Q) -1

def isEmpty():
    global front, rear
    return front == rear

def enQueue(item):
    global rear
    if isFull():
        print("Queue Full")
    else:
        rear += 1
        Q[rear] = item


def deQueue():
    global front
    if isEmpty():
        print("Queue Empty")
    else:
        front += 1
        return Q[front]


def Qpeek():
    global front, rear
    if isEmpty():
        print("Queue Empty")
    else:
        return Q[front+1]



enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())