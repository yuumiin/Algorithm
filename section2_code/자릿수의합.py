import sys

sys.stdin = open('./section 2/6. 자릿수의 합/in1.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
print(n, a)

def digit_sum(x):
    sum = 0 # 자릿수의 합을 저장해둘 변수
    while x > 0:
        sum += x%10
        x = x // 10 

    return sum

max = -2147000000

for i in a:
    sum_res = digit_sum(i)
    if max < sum_res:
        max = sum_res
        sum_res_value = i

print(sum_res_value)


##### 최대 최소값 묻는 문제 나오면 min, max 변수를 만들어서 비교