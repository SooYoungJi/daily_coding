'''
<프로그래머스 영어가 싫어요>
영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 
문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
'''

# 내 풀이
def solution(numbers):
    answer = ''
    num_dict = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    num_list = list(num_dict.keys())
    
    while (len(numbers)>0):
        if ''.join(numbers[:3]) in num_list:
            temp = ''.join(numbers[:3])
            answer += str(num_dict[temp])
            numbers = numbers[3:]
        elif ''.join(numbers[:4]) in num_list:
            temp = ''.join(numbers[:4])
            answer += str(num_dict[temp])
            numbers = numbers[4:]
        elif ''.join(numbers[:5]) in num_list:
            temp = ''.join(numbers[:5])
            answer += str(num_dict[temp])
            numbers = numbers[5:]

    return int(answer)

# 다른이 풀이1
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

'''
enumerate 함수랑 replace 함수!
'''
