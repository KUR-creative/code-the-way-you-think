from prop_based import *
from hypothesis import given
from hypothesis import strategies as st

# property based testing

# 스펙을 "property"로 표현할 수 있어야 한다.
# 즉 "작동하는" 스펙을 만든다.

# 다른 방법론에 비해, 짜기 전에 생각을 많이 해야 한다.

# 입력 인자를 생성해 보자.
register = st.dictionaries(
    st.sampled_from([10, 100, 1000, 10000, 50000]),
    st.integers(min_value=0))
product_price = st.integers(min_value=1).map(lambda x: x * 10)
paid_money = st.integers(min_value=1).map(lambda x: x * 10)

'''
for _ in range(25):
    print(register.example(),
          product_price.example(), paid_money.example())
'''

def sum_change(dic):
    return sum(won * num for won, num in dic.items())
#print(sum_change({1:2, 3:4, 5:6}))
#print(sum_change({1:1, 3:3}))

'''
@given(register, product_price, paid_money)
def test_change(register, product_price, paid_money):
    #print(register)
    #assert False # 실행 해서 생성되는 값을 한번 보자.

    # 이제 함수 change가 만족해야 하는 속성을 생각해보자.
    # 1. 고객은 거스름돈을 받아야 한다.
    # 이는 거스름돈의 합계가 받은 돈 - 제품 가격 과 같아야 한다.
    ret = change(register, product_price, paid_money)
    assert sum_change(ret) == paid_money - product_price
    # [1] sum_change를 예제 기반으로 작성한 다음 코드를 만들러 간다.

    # [3]
    # 그러면... 바로 product_price < paid_money 케이스를 확인할 수 있다.
    # 생각해보자. 예제 기반에서는 생각지 못했던 케이스다.
    # 이전에는 "생각해서" 만들어낸 케이스인데, 이번에는 "자동으로" 나왔다!
    # [3.5] 스펙을 고친다.
'''

@given(register, product_price, paid_money)
def test_change(register, product_price, paid_money):
    ret = change(register, product_price, paid_money)
    # [3.5] 스펙을 고쳐서 예외적인 케이스를 추가했다.
    if paid_money < product_price:
        assert sum_change(ret) == 0
        # [5] 기존 스펙을 넣어보자.
    else:
        assert sum_change(ret) == paid_money - product_price
        # 넣고 터지는 걸 확인하고 변경한다. -> [6]






    # 2. 고객은 가능한 적은 수의 지폐와 동전을 받아야 한다.
    # 이건 어떻게 속성으로 만들까?
