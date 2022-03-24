import random


# 28. 숫자 추가
#숫자합 = 0
# 순회 5번
    # 숫자를 입력받음
    # 숫자합 += 숫자
    #리턴 숫자합
def addnum():
    #숫자합 = 0
    numsum:int = 0
    # 순회 5번
    for i in range(0, 5):
        # 숫자를 입력받음
        num:str = input('숫자 입력')
        # 숫자합 += 숫자
        numsum += int(num)
    print(numsum)

# 28-1. 사용자로부터 숫자로 입력받게
def addnum_2():
    repeat = input('몇번 반복하시겠습니까')
    #숫자합 = 0
    numsum:int = 0
    # 순회 5번
    for i in range(0, int(repeat)):
        # 숫자를 입력받음
        num:str = input('숫자 입력')
        # 숫자합 += 숫자
        numsum += int(num)
    print(numsum)

# 28-2. 숫자가 아닌 입력은 거부하게,
def addnum3():
    #숫자합 = 0
    numsum:int = 0
    # 순회 5번
    for i in range(0, 5):
        # 숫자를 입력받음
        num:str = input('숫자 입력')
        #만약 num이 숫자라면 
        if num.isnumeric():
        # 숫자합 += 숫자
            numsum += int(num)
        #숫자가 아니라면
        else:
            continue
        #continue 
    print(numsum)

# 29. 잘못된 입력 처리
def raw_72():
    # 반복
    while True:
        
        rate = input('rate')
        # 연이율이 0이 아닌 숫자라면
        if rate.isnumeric() and rate != '0':
            # 72/rate 반환
            print(f'it will take {round(72 / int(rate))} years')
        if rate == '0':
            print('please input valid number not 0')
        print('please input valid number over 0')


# 30. 곱셈표
def multiply_table():
    for x in range(0, 13):
        for y in range(0, 13):
            xysum = x * y
            print(f'{x} x {y} = {xysum}')


def int_input(str):
    # num = input('num')
    # while True:
    #     if num.isnumeric():
    #         return num
    #     else:
    #         num = input('num')
    while True:
        num = input(str)
        if num.isnumeric():
            return int(num)
        
# 반복
    # num이라는 변수로 인풋을 받음
    # 만약 num이 숫자면
         # int(num) 반환

#num 이라는 변수로 인풋을 받음
#반복
    # num 숫자라면 리턴
    #아니라면 num이라는 변수로 숫자를 받음


# 31. 카르보넨 심박수
def pulse():
    resting_pulse: int = (int_input('restung pulse: '))
    age: int = (int_input('Age: '))

    intensity = 55
    print(f'''
Resting Pulse: {resting_pulse} Age: {age}
Intensity   |  Rate
-----------------------''')
    while intensity <= 95:
        bpm: int = round(((220 - age - resting_pulse) * intensity/100) + resting_pulse)
        print(f'{intensity}%         |  {bpm} bpm')
        intensity += 5

#     resting_pulse = int(resting_pulse)
#     age = int(age)

#     print(f'''
# Resting Pulse: {resting_pulse} Age: {age}
# Intensity   |  Rate
# -----------------------''')
#     for intensity in range(55, 96, 5):
#         bpm: int = ((220 - age - resting_pulse) * intensity) + resting_pulse
#         print(f'{intensity}%       |  {bpm} bpm')


# 33. Magic 8 ball
def magic_ball():
    #question 이라는 변수로 질문을 받음
    question = input("What's your question? ")
    #answer 이라는 리스트에 Yes, No, Mabye, Ask Again later
    answer = ['Yes', 'No', 'Mabye', 'Ask Again later']
    return print(random.choice(answer))


# 34. 사원 명단 삭제
#사원 리스트를 만듦
# 사원리스트의 요소만큼 print('There are 5 employees:\n')
    #순회
        #for 문으로 사원리스트를 사원으로 순회시킴
        #사원이름을 출력시킴
#삭제할 사원을 인풋으로 받음
#만약 삭제할 사원이 리스트 안에 있다면 삭제
    #순회
        #for 문으로 사원리스트를 사원으로 순회시킴
        #사원이름을 출력시킴
def select_del():
    members = ['jake', 'apple', 'nana', 'simba', 'seul']
    print(f'현재 {len(members)}명의 사원은 다음과 같습니다 ')
    for member in members:
        print(member)
    del_member = input('삭제할 사원을 입력해주세요 ')
    if del_member in members:
        members.remove(del_member)
    print(f'현재 {len(members)}명의 사원은 다음과 같습니다 ')
    for member in members:
            print(member)

# 35. 승자선택
#winner_draw()
#playrs = []
#반복
    #playr 라는 변수로 인풋을 받음
    #만약 playr가 == '':
        #브레이크
    #아니라면:
        #playrs.append(playr)
#return 우승자를 랜덤으로 뽑아서 프린트
def winner_draw():
    playrs = []
    while True:
        playr = input('Enter the name: ')
        if playr == '':
            break
        else:
            playrs.append(playr)
        winner = random.choice(playrs)
    return print(f'Whe winner is ... {winner}')


    


if __name__ == "__main__":
    # addnum()
    # addnum_2()
    # addnum3()
    # raw_72()
    # multiply_table()
    # pulse()
    # magic_ball()
    # select_del()
    winner_draw()