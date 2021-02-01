"""
퀵 정렬

기준데이터(pivot)를 설정하고 기준보다 큰 데이터와 작은 데이터 위치 바꿈
1. pivot 설정 (보통 index 0)
2. 왼쪽부터 pivot보다 큰 데이터 찾고 오른쪽부터 pivot보다 작은 데이터 찾음
3. 큰데이터와 작은데이터 위치 바꿈
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array) :
    if len(array) <= 1 : # 리스트 원소 개수가 1개 이하일 경우 종료
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))