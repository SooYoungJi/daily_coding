'''
<2단원 이해도 check 문제 1>
1950년에서 2050년 사이의 윤년을 출력하는 프로그램을 작성하세요.
윤년은 다음 조건으로 확인할 수 있습니다.
- 4로 나누어떨어지는 해는 윤년입니다.
- 다만, 100으로 나누어떨어지고 400으로 나누어떨어지지 않는 해는 윤년이 아닙니다.
예를 들어 2019는 4로 나누어떨어지지 않으므로 윤년이 아닙니다. 2020년은 4로 나누어떨어지고 100으로 나누어 떨어지지 않으므로 윤년입니다.
2000은 4와 100, 400으로 나눌 수 있으므로 윤년입니다.
'''

yun = []

for i in range(1950, 2051):
    if i % 4 == 0:
        if (i % 100) and (i % 4 != 0):
            continue
        else:
            yun.append(i)

print(yun)