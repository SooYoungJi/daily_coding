'''
<프로그래머스 각도기 문제>
각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 
각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(angle):
    if angle == 180:
        return 4
    elif angle > 90:
        return 3
    elif angle == 90:
        return 2
    else:
        return 1

# 다른이 풀이1

def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer
'''
아예 새로운 공식을 만들어내는 방법도 있구나...
개인적인 소견(?)으로는 그래도 다른이들이 코드를 보고 상황이해가 가야한다고 생각한다...!
짧은게 과연 무조건 좋은가? 에대한 의문이 생김...!
그래도 %90를 통해 true or false를 1과 0으로 활용한건 메모메모!
'''

# 다른이 풀이2

def solution(angle):
    angles = {180: 4, 91: 3, 90: 2, 0: 1}
    for base, result in angles.items():
        if angle >= base:
            return result

'''
변명 아닌 변명을 해보자면 이걸 생각 한해본게 아니었는데 180도랑 90도가 기준이 애매해서 포기했는데
이렇게 하도 되는구만? 그런게 90에서 91도 사이는?? 조금 모순(?)이 보인다.
일단 dict사용법만 차용해 가야겠담ㅎㅎ
'''

# 다른이 풀이 3

def solution(angle):
    if angle<=90:
        return 1 if angle<90 else 2
    else:
        return 3 if angle<180 else 4

'''
이건 내가 푼 방식을 더 짧게 쓴 방법인 것 같아서 참고하려고 가져왔음
'''