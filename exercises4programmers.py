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


    # 36. 통계 계산
# 반복수 라는 변수를 만듦
#응답시간_리스트 라는 리스트 생성
# 응답시간 질문이라는 변수가 done일 때 까지
    # 응답시간이라는 변수로 인풋값을 받음
    # 만약 응답시간이 done이 아니라면
        #응답시간_리스트에 응답시간 추가하기
        #반복수 += 1
# 평균응답시간 = sum(응답시간_리스트) / 반복수
# 최소응답시간 = min(응답시간_리스트)
# 최대응답시간 = max(응답시간_리스트)
# 표준편차 = []
# for i in 응답시간_리스트:
    # 표준편차 += (i - 평균응답시간) ** 2
#표준편차 = (sum(표준편차) / len(표준편차)) ** 0.5
# return print(평균응답시간, 최소응답시간, 최대응답시간, 표준편차)


# def 통계계산():
#     반복수 = 0
#     응답시간_리스트 = []
#     while 응답시간_리스트 == 'done':
#         응답시간 = input('Enter a number: \n')
#         if 응답시간 != 'done':
#             응답시간_리스트 += 응답시간
#             반복수 += 1
#     try:
#         평균응답시간 = sum(응답시간_리스트) / 반복수
#     except ZeroDivisionError:
#             print(ZeroDivisionError)
#     최소응답시간 = min(응답시간_리스트)
#     최대응답시간 = max(응답시간_리스트)
#     표준편차 = []    
#     for i in 응답시간_리스트:
#         표준편차 += (i - 평균응답시간) ** 2
#     try:
#         표준편차 = (sum(표준편차) / len(표준편차)) ** 0.5
#     except ZeroDivisionError:
#         print(ZeroDivisionError)
        
#     return print(평균응답시간, 최소응답시간, 최대응답시간, 표준편차)


# 36. 통계 계산 다시 풀기
#응답대기시간리스트 라는 리스트를 만든다
#반복 응답대기시간 == 'done'
    #응답대기시간 이라는 변수로 인풋을 받는다
    #응답대기시간리스트 += 응답대기시간
def 통계계산():
    응답대기시간리스트 = []
    while True:
        응답대기시간 = input('Enter')
        if 응답대기시간 == 'done':
            break
        else:
            응답대기시간리스트 += 응답대기시간
    평균 = sum(응답대기시간리스트) / len(응답대기시간리스트)
    return 평균 


# 37. 암호생성기
import random
import string
def password_generator():
    # 10
    min_len = int_input("What's the minimum length? ")
    # 2
    special_len = int_input("How many special characters? ")
    # 2
    numbers_len = int_input("How many numbers? ")

    # 알파벳을 (랜덤) 6개 쓴다
    # 특수기호 = '!@#$%^&*()_'
    # 특수기호를 (랜덤) 2개 쓴다
    # 숫자를 (랜덤) 2개 쓴다
    # 다 섞는다

    # random.choice(string.ascii_lowercase)
    # 'abcdef'
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    alpha = random.choices(alphas, k=min_len)
    #~!@#$%^&*() 중에서 2개를 랜덤으로
    # ['!' ,'@']
    specials = '~!@#$%^&*()'
    special = random.choices(specials, k=special_len)
    # ['0', '6']
    numbers = '0123456789'
    number = random.choices(numbers, k=numbers_len)

    password_list = alpha + special + number
    # password_list -> string
    password_shuffle = random.shuffle(password_list)
    password = ''.join(password_list)

    print(f"Your password is {password}")


    # 38. 필터링 값
#even_filter() 라는 함수를 만듦
def even_filter():
#num_list 라는 리스트를 만듦
    num_list = []
    #num이라는 변수로 int_input을 받음
    num = int_input('Enter a list of numbers, separated by spaces: ')
    #num_list에 num을 추가하기
    num_list.append(num)
#num_list를 for문 돌리기
    for n in num_list:
    #if num / 2 != 0:
        if num / 2 != 0:
        #num_list.remove(num)
            num_list.remove(num)
#num_str = ''.join(num_list)
    num_str = ''.join(num_list)
#프린트하기
    print(f'{num_str}')

# 38. 다시풀기
#numbers라는 변수로 인풋을 받음 -> str
#공백을 기점으로 split 해서 리스트로 만듦
def even_filter2():
    numbers: str = input('Enter a list of numbers, separated by spaces: ')
    numbers_list = numbers.split(' ')
    for n in numbers_list:
        if int(n) % 2 != 0:
            numbers_list.remove(n)
    numbers_str = ' '.join(numbers_list)
    return print(f'The even numbers are {numbers_str}.')
    
if __name__ == "__main__":
    # addnum()
    # addnum_2()
    # addnum3()
    # raw_72()
    # multiply_table()
    # pulse()
    # magic_ball()
    # select_del()
    # winner_draw()
    # 통계계산()
    # password_generator()
    even_filter2()