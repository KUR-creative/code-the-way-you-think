from target import *
# [2] 먼저 정수 리스트를 생성해 보자.
from hypothesis import given
from hypothesis import strategies as st

# 제너레이터 자체는 "학부생 방법"으로 만든다. 뻔하니까 그래도 된다!
'''
for _ in range(25):
    #print(st.integers().example())
    print(st.lists(st.integers()).example())
    # 이렇게 계속 실행하고 확인하면서 내가 잘 짜고 있는지,
    # 피드백을 받는 것이 중요하다.
    # 아무래도 된거 같다.
'''


# 입력 값을 생성한다.
gen_lst = st.lists(st.integers())

@given(gen_lst)
def test_my_sort(in_lst):
    # 제대로 생성하는지 확인해 본다.
    #print(lst); assert False

    out_lst = my_sort(in_lst)
    #print('out', out_lst); assert False

    # 속성을 정의한다.
    # 1. 길이는 같아야 한다.
    assert len(out_lst) == len(in_lst)

    # 2. E_n < E_n+1
    for a, b in zip(out_lst[:-1], out_lst[1:]):
        #assert a < b # 앗! 스펙이 틀렸네요!
        assert a <= b # 이렇게 해야 합니다.
    #->[3]

out_lst = [1,2,3,4]
print(list(zip(out_lst[:-1], out_lst[1:])))
for a, b in zip(out_lst[:-1], out_lst[1:]):
    print(a,b)
