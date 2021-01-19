# fail-test -> pass test -> refactor의 사이클을 반복한다.

# 2) try to pass
'''
def change(register, product_price, paid_money):
    pass
'''

# 4) try to pass
'''
def change(register, product_price, paid_money):
    pass
# AssertionError를 본다.
'''

# 5) try to pass
'''
def change(register, product_price, paid_money):
    return {}
'''
# 통과하는 것을 본다. 이게 바로 pass test다.

# 6) try to pass
'''
def change(register, product_price, paid_money):
    if product_price >= paid_money:
        return {}
    # 이만큼 짜고 바로 테스트해본다. 테스트 하나가 통과한 것 확인.
    return {10: 0, 100: 0, 1000: 0, 10000: 1, 50000: 2}
    # 이럼 통과하네? 다시 테스트를 짜러 간다
'''

# 8) try to pass
'''
def change(register, product_price, paid_money):
    if product_price >= paid_money:
        return {}

    # 이제 단순 코딩으로는 안되니, 생각을 좀 해야 한다.
    change_sum = paid_money - product_price
    ret = {10: 0, 100: 0, 1000: 0, 10000: 0, 50000: 0}
    # 아까처럼 해보자.

    #wons = register.keys()
    #print(wons) # 8.1) 이렇게 프린트 하면서 할 수 있다.(TDD는 아님)
    #print(sorted(wons))
    #print(sorted(wons, reverse=True))

    wons = sorted(register.keys(), reverse=True)
    print(wons) # 8.1) 이렇게 프린트 하면서 할 수 있다.(TDD는 아님)

    for won in wons:
        while register[won] > 0:
            diff = change_sum - won
            if diff >= 0:
                change_sum -= won
                register[won] -= 1
                ret[won] += 1
            else:
                break

    return ret
'''

# 9) refactor
def change(register, product_price, paid_money):
    # 테스트를 통과한 후에는, 코드를 깔끔하게 하려 한다.
    #if product_price >= paid_money:
    #    return {}
    change_sum = paid_money - product_price
    if change_sum < 0:
        return {}
    # 코드를 고친 후에는 테스트를 계속 돌린다.
    ret = {10: 0, 100: 0, 1000: 0, 10000: 0, 50000: 0}

    wons = sorted(register.keys(), reverse=True)
    for won in wons:
        while register[won] > 0:
            #diff = change_sum - won
            #if diff >= 0:
            #if change_sum > won: # 고치고 바로 확인할 수 있다.
            if change_sum >= won:
                change_sum -= won
                register[won] -= 1
                ret[won] += 1
            else:
                break

    return ret
#----------------------------------------------------------------
