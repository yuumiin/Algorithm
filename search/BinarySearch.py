"""
이진 탐색

데이터가 정렬되어 있어야 가능!
찾으려는 데이터와 중간에 있는 데이터를 반복적으로 비교
변수 3개 필요 - 시작점, 끝점, 중간점
"""

# 반복문으로 구현
def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target :
            return mid
        
        elif array[mid] > target :
            end = mid - 1

        else: start = mid + 1

    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("찾는 값이 없음")
else:
    print(result + 1)

# 재귀함수로 구현
def binary_search_recursion(array, target, start, end) :
    if start > end :
        return None
    if array[mid] == target :
        return mid
    elif array[mid] > target :
        return binary_search_recursion(array, target, start, mid-1)
    else:
        return binary_search_recursion(array, target, mid+1, end) 

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("찾는 값이 없음")
else:
    print(result + 1)