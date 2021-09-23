import sys

sys.stdin = open('./section 2/5. 정다면체/in1.txt', 'rt')

n, m = map(int, input().split())

# 0으로 초기화된 리스트를 만들어 숫자가 눈의 합에 해당하는 숫자의 인덱스를 1씩 증가
# 예를 들어 눈의 합이 6이면 인덱스 6을 1씩 증가
count = [0] * (n+m+1) 

max_prob = -2147000000 # 4바이트 정수형의 최소값

# N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 구하기
for i in range(1, n+1):
    for j in range(1, m+1):
        count[i+j] += 1
print(count)

# 가장 확률이 높은 숫자 구하기
for i in range(len(count)):
    if count[i] > max_prob:
        max_prob = count[i]
        print(max_prob)

# 결과 출력
for i in range(len(count)):
    if count[i] == max_prob:
        print(i, end=' ')

##### 계수정렬 생각하면 풀 수 있는 문제!
