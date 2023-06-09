'''
<알고리즘 독학하기 2단원>
~소수 구하기~
라이브러리 이용
'''

from sympy import sieve

print([i for i in sieve.primerange(1, 200)])