# 1

def change(register, product_price, paid_money):
    change_sum = paid_money - product_price
    # 일단 줘야할 돈은 이렇겠지?

    ret = {50000: 0, 10000: 0, 1000: 0, 100: 0, 10: 0}
    #반환도 dict니까 이러면 될거야

    #for key in ret.keys():
        # 큰 지폐 먼저 지급
    for key in sorted(ret.keys()): #이거 오름차순이라서, 나중에 확인하고 고침
