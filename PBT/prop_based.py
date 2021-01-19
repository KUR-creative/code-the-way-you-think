'''
def change(register, product_price, paid_money):
    return {} # [2] 작성하고 테스트 돌린다.
'''

'''
def change(register, product_price, paid_money):
#[4] 예외 케이스로 통과하게 한다
    change_sum = paid_money - product_price
    if change_sum < 0:
        return {}
    #테스트를 돌린다.
    # 그러면 통과한다. -> [5]
'''

def change(register, product_price, paid_money):
    change_sum = paid_money - product_price
    if change_sum <= 0: # [6] 기존코드에서 여길 고친다.
        return {}
    # 그리고 테스트를 돌려보면..
    '''
    Falsifying example: test_change(
        register={}, product_price=10, paid_money=20,
    )
    '''
    # 이걸 볼 수 있다! 여기서 잘 생각해야 한다!

    # 낸 돈은 20원인데, 제품은 10원이다? 그런데 금전 등록기에는 돈이 없다?
    # 잠깐, 그래도 거스름돈을 줄 수 있지 않나?

    # 이게 무슨 소리야? 함수의 스펙이 잘못 되었다는 뜻이다!
    # 그렇다. paid_money 또한 map으로 받아야 한다는 것이다!!!!

    # PBT는 이렇게 **스펙의 잘못된 부분**을 찾을 수 있게 한다.
    # 스펙의 잘못된 부분을 "체계적으로" 찾을 수 있게 한다.

    # 아무 것도 없는 것에서 자기 생각의 틀린 점을 찾아내는 게 아니라
    # 어느 정도는 자동적으로 찾아준다!
    # 이것이 바로 PBT의 가장 압도적인 장점이다.
