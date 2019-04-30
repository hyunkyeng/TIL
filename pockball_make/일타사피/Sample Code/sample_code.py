import socket
import time
import math

# User and Game Server Information
NICKNAME = '파이썬'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    # stage1

    # angle = 75
    # power = 100
    # conn.send(angle, power)


    # stage2

    # angle = 75
    # power = 100
    # conn.send(angle, power)
    # angle = 248
    # power = 110
    # conn.send(angle, power)


    # stage3

    # if (gameData.balls[1][0], gameData.balls[1][1]) != (0, 0):
    #     angle = 47.5
    #     power = 100
    #     conn.send(angle, power)

    # elif (gameData.balls[1][0], gameData.balls[1][1]) == (0, 0) and (gameData.balls[2][0], gameData.balls[2][1]) != (0, 0):
    #         angle = 84
    #         power = 100
    #         conn.send(angle, power)
  
    # elif (gameData.balls[2][0], gameData.balls[2][1]) == (0, 0):
    #     # if (gameData.balls[3][0], gameData.balls[3][1]) != (0, 0):
    #     angle = 178
    #     power = 100
    #     conn.send(angle, power)


    # stage4

    # if gameData.balls[3][0] != 0:
    #     angle = 48
    #     power = 65
    #     conn.send(angle, power)
    # elif gameData.balls[3][0] == 0 and gameData.balls[4][0] != 0:
    #     angle = 173
    #     power = 90
    #     conn.send(angle, power)
    # elif gameData.balls[4][0] == 0 and gameData.balls[2][0] != 0:
    #     angle = 237
    #     power = 40
    #     conn.send(angle, power)
    # elif gameData.balls[2][0] == 0 and gameData.balls[3][0] == 0 and gameData.balls[4][0] == 0:
    #     angle = 12
    #     power = 80
    #     conn.send(angle, power)


    # stage5

    # if gameData.balls[1][0] == 195:
    #     angle = 91
    #     power = 200
    #     conn.send(angle, power)

    # else:
    #     conn.send(355, 200)


    # stage6
    
    if gameData.balls[1][0] == 195:
        angle = 91
        power = 200
        conn.send(angle, power)
    elif gameData.balls[1][0] == 248:
        angle = 355
        power = 200
        conn.send(angle, power)
    elif gameData.balls[3][0] == 199:
        angle = 277
        power = 160
        conn.send(angle, power)
    elif gameData.balls[3][0] == 0 and gameData.balls[2][0] == 234:
        angle = 112
        power = 123
        conn.send(angle, power)
    elif gameData.balls[2][0] == 0:
        angle = 18
        power = 160
        conn.send(angle, power)

    






def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        play(conn, gameData)        
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
