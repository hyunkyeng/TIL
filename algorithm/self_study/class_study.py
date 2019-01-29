# #클래스 Bicycle
#
# class Bicycle():
#
#     def __init__(self, wheel_size, color):
#         self.wheel_size = wheel_size
#         self.color = color
#
#     def move(self, speed):
#         print("자전거: 시속 {}킬러미터로 전진".format(speed))
#
#     def turn(self, direction):
#         print("자전거: 시속 {}킬로미터로 전진".format(direction))
#
#     def stop(self):
#         print("자전거({0}, {1}): 정지".format(self.wheel_size, self.color))
#
#
# # my_bicycle = Bicycle()
# #
# # my_bicycle.wheel_size = 26
# # my_bicycle.color = 'black'
# #
# # my_bicycle.move(30)
# # my_bicycle.turn('왼쪽')
# # my_bicycle.stop()
# #
# # bicycle1 = Bicycle()
# #
# # bicycle1.wheel_size = 27
# # bicycle1.color = 'red'
# #
# # bicycle1.move(20)
# # bicycle1.turn('오른쪽')
# # bicycle1.stop()
#
# my_bicycle = Bicycle(26, "black")
# my_bicycle.move(30)
# my_bicycle.turn('왼쪽')
# my_bicycle.stop()


# # 클래스 Car
# class Car():
#     instance_count = 0  #클래스 변수 생성 및 초기화
#
#     def __init__(self, size, color):
#         self.size = size    #인스턴스 변수 생성 및 초기화
#         self.color = color
#         Car.instance_count = Car.instance_count + 1
#         print("자동차 객체의 수: {}".format(Car.instance_count))
#
#     def move(self):
#         print("자동차({0} & {1})가 움직입니다.".format(self.size, self.color))
#
# car1 = Car('small', 'white')
# car2 = Car('big', 'black')
#
# car1.move()
# car2.move()
#
# class Car2():
#     count = 0
#
#     def __init__(self, size, num):
#         self.size = size
#         self.count = num
#         Car2.count = Car2.count + 1
#         print("자동차 객체의 수 : Car2.count = {}".format(Car2.count))
#         print("인스턴스 변수 초기화 : self.count = {}".format(Car2.count))
#
#     def move(self):
#         print("자동차 {0}&{1} 가 움직입니다.".format(self.size, self.count))
#
# car1 = Car2("big", 20)
# car2 = Car2("small", 30)