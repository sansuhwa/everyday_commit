# 1. hello
# print hello world: hello()
from cgitb import text
import random


def hello():
    print('hello')

# 2. hello_name
# input: name
# output: hello, name


def hello_name():
    name = input('plz, name\n')
    print(f'hello, {name}')
    # return None


# 3. guess_game: 숫자 맞히기 게임
# input: 0~100 중에 입력을 받음
# output: (7) 작으면 -> '너무 작습니다',  크면 -> '너무 큽니다', 같으면 -> '정답입니다'
def guess_game():
    random_num: int = random.randint(0, 100)
    # 반복
    # 언제? 그냥 계속 반복. break 될 때까지
    while True:
        user_input: str = input('숫자를 입력: 0-100\n')
        user_num: int = int(user_input)
        if user_num == random_num:
            break
        if user_num > random_num:
            print('너무 큼')
        else:
            print('너무 작음')
    print('정답')

# 3.5. print_name
# print_name('ㅏㅣㄴㅁ우라ㅣㄴㅁㅇㄹ')


def print_name(name):
    print(name)

# 4. guess_game_limit: 숫자 맞히기 + 제한
# input: 0~100 중에 입력을 받음
# output: (7) 작으면 -> '너무 작습니다',  크면 -> '너무 큽니다', 같으면 -> '정답입니다'
# guess_game_limit():
# 인자 입력할 수 있는 기회 = limit(3)
def guess_game_limit(chance: int):
    # 수도코드
    # 랜덤으로 숫자 지정 -> 0, 100
    #실행수 = 0
    # 반복
    # 언제까지? 숫자를 맞추거나, 실행수 == 3 (change)
    # 언제까지? 쭉~
    # if chance가 count랑 같다면
    # 반복 종료

    # 사용자가 숫자를 골라

    # if 같다면
    # 반복 종료

    # 다르다면
    # 출력
    # 실행 수 +1

    # 정답 출력
    random_num: int = random.randint(0, 100)
    count: int = 0

    while True:
        if chance == count:
            print(f'{chance} 번을 다 써서 게임이 종료')
            break
        user_input: str = input('숫자를 입력: 0-100\n')
        user_num: int = int(user_input)
        if user_num == random_num:
            print('정답')
            break
        # 다르다면
        if user_num > random_num:
            print('너무 큼')
        else:
            print('너무 작음')
        count += 1  # count = count + 1


# 5. mysum
#mysum(sumlist) 만든다 인자로 sumlist
#변수 result = 0
#반복
    #for num in sumlist:
        #result = result + num
    #언제까지 sumlist의 요소가 끝날 때 까지
#return result
def mysum(sumlist: list):
    result = 0
    for num in sumlist:
        result = result + num
    return result

# 5-2. mysum_2
def mysum_2(*nums):
    print(nums)
    result = 0
    for num in nums:
        result += num
    return result

# 5-3. mysum_3
# 리스트 안에 숫자가 없을수도 있음
# mysum(list를 받음)
# 결과를 0으로 지정
# sumlist를 순회 (for) -> num
    # num이 숫자형태인지 확인
    # 맞으면 결과에 더하고
    # 아니라면 continue
# 반환
def mysum_3_2(sumlist):
    result = 0
    for num in sumlist:
        if type(num) == int or num.isnumeric():
            result += sum
        continue
    return result

def mysum_3(sumlist):
    result = 0
    for num in sumlist:
        try:
            num = int(num)
        except ValueError:
            # test를 무시하고 계속한다.
            continue
        result = result + num
    return result

# 5-4 
#run_timing() 함수생성
#runningtime_sum = 0
#check_input = 0
#계속반복
    #runningtime = input('')
    #runningtime이 숫자라면
        #runningtime_sum += runningtime
        #cheak_input += ch력ck_input
    #언제까지? runningtime_sum == ''까지
        #result = runningtime_sum / check_input
        #return 문구와 result 출력
def run_timing():
    runningtime_sum: int = 0
    check_input: int = 0
    while True:
        runningtime:str = input('Enter 10 km run time\n')
        if runningtime.isnumeric() == True:
            runningtime_sum += int(runningtime)
            check_input += 1
        elif runningtime == '':
            result = runningtime_sum / check_input
            return print(f'{check_input} 번의 10km 완주 평균기록은 {result} 입니다.')\
#5-5
#pig_latin(text):
    #text의 첫번째 글자가 aeiou 중에 있다면
        #text = text + 'way'
        #return print(text)
    #없다면
        #text = text[1:] + text[0] + 'py'
        #return print(text)
def pig_latin(text):
    if text[0] in 'aeiou':
        text = text + 'way'
        return print(text)
    else:
        text = text[1:] + text[0] + 'py'
        return print(text)

#5-6
def pl_sentence():
    sentence = input('문장을 입력해주세요.').split()
    result = []
    for word in sentence:
        if word[0] in 'aeiou':
            word = word + 'way'
            result.append(word)
        else:
            word = word[1:] + word[0] + 'py'
            result.append(word)
    return print(' '.join(result))


#5-7 ubbi_dubbi() 함수 만들기
#단어를 받아서 aeiou 앞에는 ub 붙여져서 리턴되는 함수
#word 라는 변수로 인풋을 받는다
#word를 순회 시켜서 모음을 확인한다.

def ubbi_dubbi():
    words = input('단어입력 하세여\n')
    word_list = []
    for word in words:
        if word in 'aeiou':
            word = 'ub' + word
            word_list.append(word)
        else:
            word_list.append(word)
    return print(''.join(word_list))

        

if __name__ == '__main__':
    # print(mysum(sumlist=[10, 20, 10]))
    ubbi_dubbi()
