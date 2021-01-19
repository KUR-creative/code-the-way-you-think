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
