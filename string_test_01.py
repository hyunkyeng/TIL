# python 과거 쓰던 방식 (가로 안에 one two 만 쉽게 변경 가능)
#'일은 영어로 %s, 이는 영어로 %s' % ('one', 'two')


# pyformat
#'{} {}'.format('one','two')

#name = '이현경'
#e_name = 'hyunkyeng'
#print('안녕하세요. {}입니다. My name is {}'.format(name, e_name))
#print('안녕하세요. {1}입니다. My name is {0}'.format(e_name, name))
#print('안녕하세요. {1}입니다. My name is {1}'.format(e_name, name))

# f-string python 3.6
#print(f'안녕하세요. {name}입니다. My name is {e_name}.')

#로또
#import random
#num = list(range(1,46))
#box = random.sample(num,6)
#lotto = sorted(random.sample(num,6))
#print(box)
#print(lotto)

#로또 pyformat
import random
num = range(1,46)
box = sorted(random.sample(num,6))
print("로또번호는 {}입니다".format(box))