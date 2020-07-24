#2번 홀짝게임
import random
chance=3
a=1
com=['짝','홀']
comn = random.randint(1,100)
man=input('홀? 짝? :')
print('컴퓨터 숫자: ',comn)
if com[comn%2]==man:
    print('Win\n\n\n')
else:
    print('Lose\n\n\n')

#3번 주사위게임
print('총 합계 45 이상 Win, 27미만 Lose\n\n')
import random
chances = 5 #주사위 총 횟수
i = 1 #현재 횟수
middle_sum = 0 #중간합계
again_flag = False
while i <= chances:
    input('엔터를 눌러 주사위를 굴리세요.')
    dice1 = random.choice([1, 2, 3, 4, 5, 6])
    dice2 = random.choice([1, 2, 3, 4, 5, 6])
    middle_sum += (dice1 + dice2)
    if again_flag:
        print("더블 찬스 - 주사위 1: <<{}>>, 주사위 2: <<{}>>, 중간합계: {}\n".format(dice1, dice2, middle_sum)) 
    else:
        print("{}번째 기회 - 주사위 1: <<{}>>, 주사위 2: <<{}>>, 중간합계: {}\n".format(i, dice1, dice2, middle_sum))
    again_flag = False
    if dice1 == dice2:
        again_flag = True
    else:
        i += 1
    
if middle_sum >= 45:
    print('Win')
else:
    print('Lose')
