# [1] 테스트와 제품 코드의 순서는 그리 중요치 않다.
'''
def my_sort(lst):
    return lst
'''
# -> [2]
def my_sort(lst):
    return sorted(lst)
