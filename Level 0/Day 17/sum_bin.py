'''
<프로그래머스 이진수 더하기>
이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 
두 이진수의 합을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]