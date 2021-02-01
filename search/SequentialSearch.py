"""
순차탐색

앞에서부터 하나씩 차례대로 확인
"""

def sequential_search(n, target, array):
    for i in range(n) :
        if array[i] == target :
            return i + 1 # 위치 반환


print ("생성할 원소 개수 입력   찾을 문자열입력")
input_data = input().split()
n = int(input_data[0])
taget = input_data[1]

print("원소개수만큼 문자열 입력")
array = input().split()

print(sequential_search(n, taget, array))