'''
<프로그래머스 서울에서 김서방 찾기>
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
'''

# 내 풀이
def solution(seoul):
    answer = ''
    for i, j in enumerate(seoul):
        if j == "Kim":
            return "김서방은 "+str(i)+"에 있다"
'''
ㅎㅎㅎ 그래도 enumerate써본게 뿌듯
'''

# 다른이 풀이1
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

'''
"{}".format()형식과 index사용 방식!
나 index알았는데 왜 생각 안났지ㅜㅜ
'''