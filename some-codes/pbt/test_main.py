from main import *
from hypothesis import given
from hypothesis import strategies as st


register = st.dictionaries(
    keys=st.sampled_from([50000, 10000, 1000, 100, 10]),
    values=st.integers(min_value=0))

money = st.integers(min_value=1).map(lambda x: x * 10)
#for _ in range(25):
    #print(.example())
    #print(register.example())

def change_sum(dic):
    return sum(k*v for k,v in dic.items())

@given(register, money, money)
def test_change(register, product_price, paid_money):
    # 1
    ret = change(register, product_price, paid_money)
    if product_price > paid_money:
        assert change_sum(ret) == 0
    else:
        assert change_sum(ret) == paid_money - product_price
    # 2

'''
@given(st.lists(st.integers()))
def test_sort(lst):
    out = sort(lst)
    assert len(lst) == len(out)

    #for a,b in zip(lst[:-1], lst[1:]): assert a < b
    #for a,b in zip(lst[:-1]
    print(lst)
    for a,b in zip(out[:-1], out[1:]):
        assert a <= b

#out -> n, n+1
lst = [1,2,3,4,5]
print(lst[:-1])
print(lst[1:])
print(list(zip(lst[:-1], lst[1:])))
'''
